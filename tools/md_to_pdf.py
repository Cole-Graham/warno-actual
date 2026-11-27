"""Convert a Markdown report into a PDF with a title page, table of contents and PDF bookmarks.

Usage::

    python tools/md_to_pdf.py docs/easyndf_limitations_report.md
    python tools/md_to_pdf.py report.md -o out/report.pdf --page-size a4 --toc-depth 3

The Markdown may start with front matter: ``key: value`` lines between two ``---`` lines.
``title``, ``subtitle`` and ``kicker`` (a small label above the title) go on the title page,
``short_title`` replaces the title in page headers, and every other key is listed on the title
page as a labelled row (``prepared_for`` is shown as "Prepared for"). Without a ``title``, the
first level-1 heading is used. A level-1 heading that repeats the title is not printed again.

The top heading level (``##`` when the document has a single ``#`` title) starts a new page and
is level 1 of the table of contents. Supported Markdown: headings, paragraphs, bold, italic,
strikethrough, inline code, links, bullet and numbered lists (nested), tables, fenced code,
block quotes, horizontal rules and local images.

Needs reportlab and mistune (both in the ``optional`` extra: ``pip install -e ".[optional]"``).
"""

from __future__ import annotations

import argparse
import os
import textwrap
from pathlib import Path
from xml.sax.saxutils import escape

import mistune
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import A4, LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    CondPageBreak,
    Flowable,
    Frame,
    Image,
    ListFlowable,
    ListItem,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    XPreformatted,
)
from reportlab.platypus.flowables import HRFlowable
from reportlab.platypus.tableofcontents import TableOfContents

NAVY = colors.HexColor("#1F3A5F")
ACCENT = colors.HexColor("#2E75B6")
GOLD = colors.HexColor("#C9A227")
TEXT = colors.HexColor("#222222")
MUTED = colors.HexColor("#6B7280")
RULE = colors.HexColor("#C9D3E0")
ROW_ALT = colors.HexColor("#F3F6FA")
CODE_BG = colors.HexColor("#F5F7FA")
CODE_BORDER = colors.HexColor("#D8DEE8")

TITLE_PAGE_KEYS = {"title", "subtitle", "kicker", "short_title"}

# (family name, regular, bold, italic, bold italic); the first family whose files all exist wins.
SANS_CANDIDATES = (
    ("ReportSans", "segoeui.ttf", "segoeuib.ttf", "segoeuii.ttf", "segoeuiz.ttf"),
    ("ReportSans", "arial.ttf", "arialbd.ttf", "ariali.ttf", "arialbi.ttf"),
    ("ReportSans", "DejaVuSans.ttf", "DejaVuSans-Bold.ttf", "DejaVuSans-Oblique.ttf", "DejaVuSans-BoldOblique.ttf"),
)
MONO_CANDIDATES = (
    ("ReportMono", "consola.ttf", "consolab.ttf", "consolai.ttf", "consolaz.ttf"),
    ("ReportMono", "DejaVuSansMono.ttf", "DejaVuSansMono-Bold.ttf", "DejaVuSansMono-Oblique.ttf",
     "DejaVuSansMono-BoldOblique.ttf"),
)
FONT_DIRS = (
    Path(os.environ.get("WINDIR", r"C:\Windows")) / "Fonts",
    Path.home() / "AppData" / "Local" / "Microsoft" / "Windows" / "Fonts",
    Path("/usr/share/fonts/truetype/dejavu"),
    Path("/usr/share/fonts/TTF"),
    Path("/Library/Fonts"),
)


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    """Split ``---`` front matter (``key: value`` lines) from the Markdown body."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text
    for end in range(1, len(lines)):
        if lines[end].strip() == "---":
            meta = {}
            for line in lines[1:end]:
                key, sep, value = line.partition(":")
                if sep and key.strip():
                    meta[key.strip()] = value.strip().strip('"').strip("'")
            return meta, "\n".join(lines[end + 1:])
    return {}, text


def register_fonts() -> dict[str, str]:
    """Register a TrueType sans and mono family when available; fall back to the built-in PDF fonts."""
    fonts = {
        "regular": "Helvetica",
        "bold": "Helvetica-Bold",
        "italic": "Helvetica-Oblique",
        "mono": "Courier",
    }

    def find(file_name: str) -> Path | None:
        return next((d / file_name for d in FONT_DIRS if (d / file_name).is_file()), None)

    for role, candidates in (("sans", SANS_CANDIDATES), ("mono", MONO_CANDIDATES)):
        for family, *files in candidates:
            paths = [find(name) for name in files]
            if not all(paths):
                continue
            faces = [family, f"{family}-Bold", f"{family}-Italic", f"{family}-BoldItalic"]
            for face, path in zip(faces, paths):
                pdfmetrics.registerFont(TTFont(face, str(path)))
            pdfmetrics.registerFontFamily(family, normal=faces[0], bold=faces[1], italic=faces[2], boldItalic=faces[3])
            if role == "sans":
                fonts.update(regular=faces[0], bold=faces[1], italic=faces[2])
            else:
                fonts["mono"] = faces[0]
            break
    return fonts


def make_styles(fonts: dict[str, str]) -> dict[str, ParagraphStyle]:
    regular, bold = fonts["regular"], fonts["bold"]
    body = ParagraphStyle("body", fontName=regular, fontSize=10, leading=14.5, textColor=TEXT, spaceAfter=7)
    return {
        "body": body,
        "list": ParagraphStyle("list", parent=body, spaceAfter=3),
        "quote": ParagraphStyle("quote", parent=body, textColor=colors.HexColor("#3F4A5A")),
        "h1": ParagraphStyle("h1", parent=body, fontName=bold, fontSize=22, leading=27, textColor=NAVY,
                             spaceBefore=0, spaceAfter=12, keepWithNext=1),
        "h2": ParagraphStyle("h2", parent=body, fontName=bold, fontSize=17, leading=22, textColor=NAVY,
                             spaceBefore=4, spaceAfter=4, keepWithNext=1),
        "h3": ParagraphStyle("h3", parent=body, fontName=bold, fontSize=13, leading=17, textColor=ACCENT,
                             spaceBefore=12, spaceAfter=5, keepWithNext=1),
        "h4": ParagraphStyle("h4", parent=body, fontName=bold, fontSize=11, leading=15,
                             textColor=colors.HexColor("#33415C"), spaceBefore=9, spaceAfter=4, keepWithNext=1),
        "h5": ParagraphStyle("h5", parent=body, fontName=fonts["italic"], fontSize=10, leading=14,
                             textColor=colors.HexColor("#33415C"), spaceBefore=7, spaceAfter=3, keepWithNext=1),
        "cell": ParagraphStyle("cell", parent=body, fontSize=8.5, leading=11.5, spaceAfter=0),
        "cell_head": ParagraphStyle("cell_head", parent=body, fontName=bold, fontSize=8.5, leading=11.5,
                                    spaceAfter=0, textColor=colors.white),
        "code": ParagraphStyle("code", fontName=fonts["mono"], fontSize=8, leading=10.5, textColor=TEXT,
                               backColor=CODE_BG, borderColor=CODE_BORDER, borderWidth=0.5, borderPadding=6,
                               leftIndent=6, rightIndent=6, spaceBefore=6, spaceAfter=12),
        "toc_title": ParagraphStyle("toc_title", parent=body, fontName=bold, fontSize=20, leading=25,
                                    textColor=NAVY, spaceAfter=16),
        "title": ParagraphStyle("title", fontName=bold, fontSize=28, leading=34, textColor=colors.white),
        "subtitle": ParagraphStyle("subtitle", fontName=regular, fontSize=13.5, leading=18,
                                   textColor=colors.HexColor("#D6E2F0")),
        "kicker": ParagraphStyle("kicker", fontName=bold, fontSize=10, leading=13, textColor=GOLD),
        "meta_label": ParagraphStyle("meta_label", fontName=bold, fontSize=9.5, leading=13, textColor=MUTED),
        "meta_value": ParagraphStyle("meta_value", fontName=regular, fontSize=10.5, leading=14, textColor=TEXT),
    }


def inline_markup(children: list[dict], fonts: dict[str, str], code_size: float) -> str:
    """Render mistune inline tokens as reportlab paragraph markup."""
    out = []
    for node in children:
        kind = node["type"]
        if kind == "text":
            out.append(escape(node["raw"]))
        elif kind == "codespan":
            out.append(f'<font face="{fonts["mono"]}" size="{code_size}" backColor="#EEF1F5">'
                       f'{escape(node["raw"])}</font>')
        elif kind == "strong":
            out.append(f"<b>{inline_markup(node['children'], fonts, code_size)}</b>")
        elif kind == "emphasis":
            out.append(f"<i>{inline_markup(node['children'], fonts, code_size)}</i>")
        elif kind == "strikethrough":
            out.append(f"<strike>{inline_markup(node['children'], fonts, code_size)}</strike>")
        elif kind == "link":
            url = escape(node["attrs"]["url"], {'"': "&quot;"})
            out.append(f'<a href="{url}" color="#1F5FA8">{inline_markup(node["children"], fonts, code_size)}</a>')
        elif kind == "linebreak":
            out.append("<br/>")
        elif kind == "softbreak":
            out.append(" ")
        elif "children" in node:
            out.append(inline_markup(node["children"], fonts, code_size))
        else:
            out.append(escape(node.get("raw", "")))
    return "".join(out)


def plain_text(children: list[dict]) -> str:
    return "".join(plain_text(n["children"]) if "children" in n else n.get("raw", " ") for n in children)


class BodyStart(Flowable):
    """Zero-size marker: the page it lands on is page 1 of the body."""

    def wrap(self, *_args):
        return 0, 0

    def draw(self):
        pass


class Heading(Paragraph):
    """A heading that leaves a PDF bookmark at its own position and feeds the table of contents."""

    def __init__(self, markup: str, style: ParagraphStyle, level: int, text: str, key: str):
        super().__init__(markup, style)
        self.toc_level = level
        self.plain = text
        self.bookmark = key

    def draw(self):
        self.canv.bookmarkHorizontal(self.bookmark, 0, self.height + self.style.leading)
        super().draw()


class ReportTemplate(BaseDocTemplate):
    def __init__(self, filename: str, meta: dict[str, str], styles: dict, fonts: dict, toc_depth: int, **kwargs):
        super().__init__(filename, **kwargs)
        self.meta = meta
        self.styles = styles
        self.fonts = fonts
        self.toc_depth = toc_depth
        self.source_name = kwargs.get("subject", "")
        self.body_start_page = None
        self.outline_level = -1
        body_frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="body",
                           leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        title_frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="title")
        self.addPageTemplates([
            PageTemplate("title", [title_frame], onPage=self._draw_title_page),
            PageTemplate("body", [body_frame], onPageEnd=self._draw_header_footer),
        ])

    def beforeDocument(self):
        self.body_start_page = None
        self.outline_level = -1

    def page_label(self, page: int) -> str:
        if self.body_start_page and page >= self.body_start_page:
            return str(page - self.body_start_page + 1)
        roman = ("", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x")
        return roman[page] if page < len(roman) else str(page)

    def afterFlowable(self, flowable):
        if isinstance(flowable, BodyStart):
            self.body_start_page = self.page
            return
        if not isinstance(flowable, Heading):
            return
        level = min(flowable.toc_level, self.outline_level + 1)
        self.outline_level = level
        self.canv.addOutlineEntry(flowable.plain, flowable.bookmark, level=level, closed=level > 0)
        if level < self.toc_depth:
            page = self.page - self.body_start_page + 1 if self.body_start_page else self.page
            self.notify("TOCEntry", (level, escape(flowable.plain), page, flowable.bookmark))

    def _draw_title_page(self, canv, doc):
        width, height = doc.pagesize
        band = height * 0.46
        canv.saveState()
        canv.setFillColor(NAVY)
        canv.rect(0, height - band, width, band, stroke=0, fill=1)
        canv.setFillColor(GOLD)
        canv.rect(0, height - band - 5, width, 5, stroke=0, fill=1)

        y = height - 1.45 * inch
        blocks = []
        if self.meta.get("kicker"):
            blocks.append((Paragraph(escape(self.meta["kicker"].upper()), self.styles["kicker"]), 14))
        blocks.append((Paragraph(escape(self.meta.get("title", "")), self.styles["title"]), 16))
        if self.meta.get("subtitle"):
            blocks.append((Paragraph(escape(self.meta["subtitle"]), self.styles["subtitle"]), 0))
        for paragraph, gap in blocks:
            _, h = paragraph.wrapOn(canv, doc.width, band)
            paragraph.drawOn(canv, doc.leftMargin, y - h)
            y -= h + gap

        rows = [
            [Paragraph(escape(key.replace("_", " ").capitalize()), self.styles["meta_label"]),
             Paragraph(escape(value), self.styles["meta_value"])]
            for key, value in self.meta.items()
            if key not in TITLE_PAGE_KEYS and value
        ]
        if rows:
            table = Table(rows, colWidths=[1.6 * inch, doc.width - 1.6 * inch], hAlign="LEFT")
            table.setStyle(TableStyle([
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
                ("LINEBELOW", (0, 0), (-1, -2), 0.5, RULE),
                ("TOPPADDING", (0, 1), (-1, -1), 9),
            ]))
            _, h = table.wrapOn(canv, doc.width, height)
            table.drawOn(canv, doc.leftMargin, height - band - 0.75 * inch - h)

        canv.setStrokeColor(RULE)
        canv.setLineWidth(0.5)
        canv.line(doc.leftMargin, 0.9 * inch, width - doc.rightMargin, 0.9 * inch)
        canv.setFont(self.fonts["regular"], 8)
        canv.setFillColor(MUTED)
        if self.source_name:
            canv.drawString(doc.leftMargin, 0.7 * inch, f"Source: {self.source_name}")
        canv.restoreState()

    def _draw_header_footer(self, canv, doc):
        width, _ = doc.pagesize
        top = doc.bottomMargin + doc.height + 0.3 * inch
        bottom = doc.bottomMargin - 0.35 * inch
        canv.saveState()
        canv.setStrokeColor(RULE)
        canv.setLineWidth(0.5)
        canv.setFillColor(MUTED)
        canv.setFont(self.fonts["regular"], 8)
        in_body = self.body_start_page is not None and doc.page >= self.body_start_page
        if in_body:
            canv.drawString(doc.leftMargin, top + 4, self.meta.get("short_title") or self.meta.get("title", ""))
            if self.meta.get("date"):
                canv.drawRightString(width - doc.rightMargin, top + 4, self.meta["date"])
            canv.line(doc.leftMargin, top, width - doc.rightMargin, top)
        canv.line(doc.leftMargin, bottom + 12, width - doc.rightMargin, bottom + 12)
        canv.drawCentredString(width / 2, bottom, self.page_label(doc.page))
        canv.restoreState()


class StoryBuilder:
    """Turns mistune block tokens into reportlab flowables."""

    def __init__(self, styles, fonts, width: float, base_dir: Path, title: str, top_level: int, section_breaks: bool):
        self.styles = styles
        self.fonts = fonts
        self.width = width
        self.base_dir = base_dir
        self.title = title
        self.top_level = top_level
        self.section_breaks = section_breaks
        self.headings = 0
        self.chapters = 0
        self.title_skipped = False
        self._aligned: dict[tuple[str, str], ParagraphStyle] = {}

    def blocks(self, tokens: list[dict], width: float) -> list[Flowable]:
        story: list[Flowable] = []
        for token in tokens:
            kind = token["type"]
            if kind == "heading":
                story.extend(self.heading(token))
            elif kind in ("paragraph", "block_text"):
                style = self.styles["list"] if kind == "block_text" else self.styles["body"]
                story.extend(self.paragraph(token["children"], style, width))
            elif kind == "list":
                story.append(self.bullets(token, width))
                story.append(Spacer(1, 5))
            elif kind == "table":
                story.append(self.table(token, width))
                story.append(Spacer(1, 10))
            elif kind == "block_code":
                story.append(self.code(token["raw"], width))
            elif kind == "block_quote":
                story.append(self.quote(token, width))
            elif kind == "thematic_break":
                story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceBefore=6, spaceAfter=10))
        return story

    def heading(self, token: dict) -> list[Flowable]:
        level = token["attrs"]["level"]
        text = plain_text(token["children"]).strip()
        if level == 1 and not self.title_skipped and text == self.title:
            self.title_skipped = True
            return []
        out: list[Flowable] = []
        if level <= self.top_level:
            if self.chapters:
                out.append(PageBreak() if self.section_breaks else CondPageBreak(2.5 * inch))
            self.chapters += 1
        self.headings += 1
        style = self.styles[f"h{min(max(level, 1), 5)}"]
        markup = inline_markup(token["children"], self.fonts, style.fontSize - 1)
        out.append(Heading(markup, style, max(level - self.top_level, 0), text, f"h{self.headings}"))
        if level <= self.top_level:
            rule = HRFlowable(width="100%", thickness=1.4, color=ACCENT, spaceBefore=2, spaceAfter=10)
            rule.keepWithNext = True
            out.append(rule)
        return out

    def paragraph(self, children: list[dict], style: ParagraphStyle, width: float) -> list[Flowable]:
        images = [n for n in children if n["type"] == "image"]
        if images and len(images) == len([n for n in children if n["type"] != "softbreak"]):
            return [flowable for node in images for flowable in self.image(node, width)]
        return [Paragraph(inline_markup(children, self.fonts, style.fontSize - 1), style)]

    def image(self, node: dict, width: float) -> list[Flowable]:
        path = (self.base_dir / node["attrs"]["url"]).resolve()
        if not path.is_file():
            return [Paragraph(f"<i>[missing image: {escape(node['attrs']['url'])}]</i>", self.styles["body"])]
        image_w, image_h = ImageReader(str(path)).getSize()
        scale = min(1.0, width / image_w)
        return [Image(str(path), width=image_w * scale, height=image_h * scale, hAlign="CENTER"), Spacer(1, 8)]

    def bullets(self, token: dict, width: float) -> ListFlowable:
        ordered = token["attrs"].get("ordered", False)
        depth = token["attrs"].get("depth", 0)
        indent = 16
        items = [ListItem(self.blocks(item["children"], width - indent)) for item in token["children"]]
        if ordered:
            return ListFlowable(items, bulletType="1", start=token["attrs"].get("start", 1), bulletFormat="%s.",
                                leftIndent=indent, bulletFontName=self.fonts["regular"], bulletFontSize=10,
                                bulletColor=TEXT)
        return ListFlowable(items, bulletType="bullet", start="\u2022" if depth % 2 == 0 else "\u2013",
                            leftIndent=indent, bulletFontName=self.fonts["regular"], bulletFontSize=10,
                            bulletColor=ACCENT, bulletOffsetY=0)

    def table(self, token: dict, width: float) -> Table:
        head = token["children"][0]["children"]
        body = token["children"][1]["children"] if len(token["children"]) > 1 else []
        rows = [head] + [row["children"] for row in body]
        aligns = [cell["attrs"].get("align") for cell in head]
        texts = [[plain_text(cell["children"]) for cell in row] for row in rows]

        columns = len(head)
        weights = []
        for col in range(columns):
            lengths = [len(row[col]) for row in texts if col < len(row)]
            weights.append(max(6.0, (min(max(lengths), 60) + sum(lengths) / len(lengths)) / 2))
        floor = min(width / columns, 0.9 * inch)
        widths = [max(floor, width * w / sum(weights)) for w in weights]
        widths = [w * width / sum(widths) for w in widths]

        data = []
        for r, row in enumerate(rows):
            base = self.styles["cell_head" if r == 0 else "cell"]
            data.append([
                Paragraph(inline_markup(cell["children"], self.fonts, base.fontSize - 0.5),
                          self._align(base, aligns[c] if c < len(aligns) else None))
                for c, cell in enumerate(row)
            ])
        commands = [
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("GRID", (0, 0), (-1, -1), 0.4, RULE),
            ("LINEBELOW", (0, 0), (-1, 0), 1.0, NAVY),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("LEFTPADDING", (0, 0), (-1, -1), 5),
            ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ]
        commands += [("BACKGROUND", (0, r), (-1, r), ROW_ALT) for r in range(2, len(data), 2)]
        table = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
        table.setStyle(TableStyle(commands))
        return table

    def _align(self, style: ParagraphStyle, align: str | None) -> ParagraphStyle:
        if align not in ("center", "right"):
            return style
        key = (style.name, align)
        if key not in self._aligned:
            self._aligned[key] = ParagraphStyle(f"{style.name}_{align}", parent=style,
                                                alignment=TA_CENTER if align == "center" else TA_RIGHT)
        return self._aligned[key]

    def code(self, raw: str, width: float) -> XPreformatted:
        style = self.styles["code"]
        usable = width - style.leftIndent - style.rightIndent - 2 * style.borderPadding
        columns = max(20, int(usable / pdfmetrics.stringWidth("M", style.fontName, style.fontSize)))
        lines = []
        for line in raw.rstrip("\n").expandtabs(4).splitlines():
            if len(line) <= columns:
                lines.append(line)
                continue
            indent = " " * (len(line) - len(line.lstrip()) + 4)
            lines.extend(textwrap.wrap(line, columns, subsequent_indent=indent, break_long_words=True,
                                       break_on_hyphens=False))
        return XPreformatted(escape("\n".join(lines)), style)

    def quote(self, token: dict, width: float) -> Table:
        inner: list[Flowable] = []
        for child in token["children"]:
            if child["type"] == "paragraph":
                inner.extend(self.paragraph(child["children"], self.styles["quote"], width - 18))
            else:
                inner.extend(self.blocks([child], width - 18))
        table = Table([[inner]], colWidths=[width], hAlign="LEFT")
        table.setStyle(TableStyle([
            ("LINEBEFORE", (0, 0), (0, -1), 2.5, ACCENT),
            ("BACKGROUND", (0, 0), (-1, -1), ROW_ALT),
            ("LEFTPADDING", (0, 0), (-1, -1), 12),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ]))
        return table


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Convert a Markdown report to a PDF with a title page and contents.")
    parser.add_argument("markdown", type=Path, help="Markdown file to convert")
    parser.add_argument("-o", "--output", type=Path, help="PDF to write (default: next to the Markdown file)")
    parser.add_argument("--page-size", choices=("letter", "a4"), default="letter")
    parser.add_argument("--toc-depth", type=int, default=2, help="heading levels listed in the contents (default 2)")
    parser.add_argument("--no-section-breaks", action="store_true",
                        help="do not start each top-level section on a new page")
    args = parser.parse_args(argv)

    source = args.markdown.read_text(encoding="utf-8")
    meta, body = parse_front_matter(source)
    tokens = mistune.create_markdown(renderer=None, plugins=["table", "strikethrough", "url"])(body)
    h1s = [plain_text(t["children"]).strip() for t in tokens if t["type"] == "heading" and t["attrs"]["level"] == 1]
    meta.setdefault("title", h1s[0] if h1s else args.markdown.stem.replace("_", " "))
    top_level = 2 if len(h1s) <= 1 else 1

    fonts = register_fonts()
    styles = make_styles(fonts)
    output = args.output or args.markdown.with_suffix(".pdf")
    output.parent.mkdir(parents=True, exist_ok=True)
    doc = ReportTemplate(
        str(output),
        meta,
        styles,
        fonts,
        args.toc_depth,
        pagesize=A4 if args.page_size == "a4" else LETTER,
        leftMargin=0.95 * inch,
        rightMargin=0.95 * inch,
        topMargin=1.0 * inch,
        bottomMargin=0.95 * inch,
        title=meta["title"],
        author=meta.get("prepared_by", ""),
        subject=args.markdown.name,
    )

    toc = TableOfContents(dotsMinLevel=0)
    toc.levelStyles = [
        ParagraphStyle("toc0", fontName=fonts["bold"], fontSize=10.5, leading=15, spaceBefore=7, textColor=NAVY),
        ParagraphStyle("toc1", fontName=fonts["regular"], fontSize=9.5, leading=13, leftIndent=18, textColor=TEXT),
        ParagraphStyle("toc2", fontName=fonts["regular"], fontSize=9, leading=12, leftIndent=36, textColor=MUTED),
        ParagraphStyle("toc3", fontName=fonts["regular"], fontSize=8.5, leading=11.5, leftIndent=54, textColor=MUTED),
    ]
    builder = StoryBuilder(styles, fonts, doc.width, args.markdown.parent, meta["title"], top_level,
                           not args.no_section_breaks)
    story: list[Flowable] = [
        Spacer(1, 1),
        NextPageTemplate("body"),
        PageBreak(),
        Paragraph("Contents", styles["toc_title"]),
        toc,
        PageBreak(),
        BodyStart(),
        *builder.blocks(tokens, doc.width),
    ]
    doc.multiBuild(story)
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
