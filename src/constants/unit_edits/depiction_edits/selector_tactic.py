"""Declarations for new infantry selector tactic objects.

Each entry in ``NEW_SELECTOR_TACTIC_OBJECTS`` is a ``(unique_count, surrogates_count)``
pair that yields a new row::

    InfantrySelectorTactic_{unique_count:02}_{surrogates_count:02} is TemplateInfantrySelectorTactic(
        Surrogates = TacticDepiction_{surrogates_count:02}_Surrogates
        UniqueCount = {unique_count}
    )

The row is inserted into ``GameData/Generated/Gameplay/Gfx/Infanterie/DepictionInfantry.ndf``
by :mod:`src.gameplay_mods.generated.gameplay.gfx.depictions.depictioninfantry`.

Any ``TacticDepiction_{surrogates_count:02}_Surrogates`` row referenced above that is
missing from ``GameData/Gameplay/Gfx/Templates/TemplateDepiction.ndf`` is filled in
automatically (in numeric order so the chained ``+ [[LOD_High, 'NN']]`` references
resolve) by :mod:`src.gameplay_mods.gameplay.gfx.templates.templatedepiction`.

Example vanilla rows for reference::

    # DepictionInfantry.ndf
    InfantrySelectorTactic_00_04 is TemplateInfantrySelectorTactic( Surrogates=TacticDepiction_04_Surrogates UniqueCount=0 )
    InfantrySelectorTactic_01_04 is TemplateInfantrySelectorTactic( Surrogates=TacticDepiction_04_Surrogates UniqueCount=1 )

    # TemplateDepiction.ndf
    TacticDepiction_01_Surrogates is [[LOD_High, '01']]
    TacticDepiction_02_Surrogates is TacticDepiction_01_Surrogates + [[LOD_High, '02']]
    TacticDepiction_03_Surrogates is TacticDepiction_02_Surrogates + [[LOD_High, '03']]
"""

NEW_SELECTOR_TACTIC_OBJECTS: list[tuple[int, int]] = [
    (5, 5),
    (8, 8),
]
