"""LANDJUT divisions (Danish-led NATO corps in Jutland / Schleswig-Holstein).

Three decks: LANDJUT (universal: every table below), LANDJUT Mechanized and LANDJUT
Motorized. There is no standalone Danish division. Each kind deck = DK_global + its Danish
kind table + a hand-picked West German table (LANDJUT_RFA_*), all in
new_divisionrules/DK_newdivisionrules.py.

Keys keep the "DK_" prefix on purpose: divisions.py picks the donor division (country/flag)
from the key prefix, and the matrix code takes the kind from the part after the first "_"
("DK_mechanized" -> "mechanized"). Players only see the LANDJUT names below.

The vanilla Danish divisions DK_Jyske_multi and DK_Ostre_Landkommando_multi are Eugen's own
(LANDJUT DLC) and are hidden via hide_divs; reusing their cfg_name collides ("Namespace
opened twice") - so don't. All three decks reuse the DK_Jyske emblem (the emblem loader skips creating a
texture that already exists); swap in real emblems under
assets/gameplaymod/2d/interface/useoutgame/division/emblem/ and drop the "emblem" keys.

Activation points as RFA: universal 75, mechanized 100, motorized 105.
"""

from .new_divisionrules import (
    DK_global_newdivisionrules,
    DK_mechanized_newdivisionrules,
    DK_motorized_newdivisionrules,
    LANDJUT_RFA_mechanized_newdivisionrules,
    LANDJUT_RFA_motorized_newdivisionrules,
)

dk_new_divs = {
    "DK_general": {
        "division_id": 6211,
        "interface_order": 2311,
        "guid": "8fbac795-0572-4695-8be2-6d8e47210657",
        "cfg_name": "LANDJUT_national_general",
        "emblem": "DK_Jyske",
        "div_name": ("LANDJUT", "DKGENNAME"),
        "div_power": "DC_PWR1",
        "description_title": ("LANDJUT", "DKGENTITL"),
        "standout_units": ["Leopard_1A5_DK", "Otomatic_DK", "Leopard_2A3_RFA"],
        "summary_text": ("Danish-led NATO corps in Jutland and Schleswig-Holstein.", "DKGENSUMM"),
        "history_text": ("LANDJUT combined arms division.", "DKGENHIST"),
        "activation_points": 75,
        "type_texture": "infantryReg",
        "division_rules": [
            DK_global_newdivisionrules,
            DK_mechanized_newdivisionrules,
            DK_motorized_newdivisionrules,
            LANDJUT_RFA_mechanized_newdivisionrules,
            LANDJUT_RFA_motorized_newdivisionrules,
        ],
    },
    "DK_mechanized": {
        "division_id": 6215,
        "interface_order": 2315,
        "guid": "990156b6-7b50-4d70-93b3-4e1935e09740",
        "cfg_name": "LANDJUT_national_mechanized",
        "emblem": "DK_Jyske",
        "div_name": ("LANDJUT Mechanized", "DKMECNAME"),
        "div_power": "DC_PWR1",
        "description_title": ("LANDJUT Mechanized", "DKMECTITL"),
        "standout_units": ["Leopard_1A5_DK", "Otomatic_DK", "Leopard_2A3_RFA"],
        "summary_text": ("Danish Jutland Division and West German 6th Panzergrenadier Division.", "DKMECSUMM"),
        "history_text": ("LANDJUT mechanized division.", "DKMECHIST"),
        "activation_points": 100,
        "type_texture": "infantryReg",
        "division_rules": [
            DK_global_newdivisionrules,
            DK_mechanized_newdivisionrules,
            LANDJUT_RFA_mechanized_newdivisionrules,
        ],
    },
    "DK_motorized": {
        "division_id": 6217,
        "interface_order": 2317,
        "guid": "a54641e5-8a2a-4122-81e6-82f22b2f1ee4",
        "cfg_name": "LANDJUT_national_motorized",
        "emblem": "DK_Jyske",
        "div_name": ("LANDJUT Motorized", "DKMOTNAME"),
        "div_power": "DC_PWR1",
        "description_title": ("LANDJUT Motorized", "DKMOTTITL"),
        "standout_units": ["Guards_DK", "LandRover_ITOW_DK", "Tornado_Marine_CLU_RFA"],
        "summary_text": ("Danish home defence and West German territorial forces.", "DKMOTSUMM"),
        "history_text": ("LANDJUT motorized division.", "DKMOTHIST"),
        "activation_points": 105,
        "type_texture": "infantryReg",
        "division_rules": [
            DK_global_newdivisionrules,
            DK_motorized_newdivisionrules,
            LANDJUT_RFA_motorized_newdivisionrules,
        ],
    },
}
