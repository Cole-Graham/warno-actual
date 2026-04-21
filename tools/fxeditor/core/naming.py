"""Render output filenames from a template + source stem."""

from __future__ import annotations

import re
from typing import Tuple

STEM_TRAILING_INDEX_RE = re.compile(r"_(\d+)$")

DEFAULT_TEMPLATE = "{rootname}_{radiusinmeters}m_{n}.ndf"


def extract_trailing_index(stem: str) -> Tuple[str, str, str]:
    """Split *stem* into ``(base, suffix_with_underscore, number_only)``.

    If no trailing ``_digits``, suffix and number are empty strings.
    """
    m = STEM_TRAILING_INDEX_RE.search(stem)
    if not m:
        return stem, "", ""
    return stem[: m.start()], m.group(0), m.group(1)


def format_radius_for_name(radius_m: float) -> str:
    if abs(radius_m - round(radius_m)) < 1e-9:
        return str(int(round(radius_m)))
    return str(radius_m)


def render_filename(
    template: str,
    rootname: str,
    radius_m: float,
    source_stem: str,
) -> str:
    _, suffix, n = extract_trailing_index(source_stem)
    r_str = format_radius_for_name(radius_m)
    result = template
    result = result.replace("{rootname}", rootname)
    result = result.replace("{radiusinmeters}", r_str)
    result = result.replace("{suffix}", suffix)
    result = result.replace("{n}", n)
    return result
