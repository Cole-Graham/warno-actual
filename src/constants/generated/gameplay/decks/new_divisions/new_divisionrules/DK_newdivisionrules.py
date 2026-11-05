"""Division rules for LANDJUT (Danish-led NATO corps: Jutland Division + West German
6. Panzergrenadierdivision, Schleswig-Holstein).

Only two decks exist - LANDJUT Mechanized and LANDJUT Motorized, see DK_new_divs.py. Each
gets ``DK_global`` + its own Danish table + a hand-picked West German table below. A tuple is
    (unit, cards, [rookie, trained, hardened, veteran], [transports])
Each Danish unit sits in exactly one table.

Danish split, loosely following the real 1980s army:
- mechanized : Jyske Division - Leopard 1, Centurion Mk5/2, M113 family, M109, Otomatic.
- motorized  : Østre Landkommando / home defence - older Centurions, M41, reserves,
               militia, towed artillery and AA.
- global     : command, engineers, support weapons, SF, recon, helicopters, aircraft.

Danish availability and card counts mirror the WA analog of each unit (see the comments in
DK_unit_edits.py). Danish transport lists come from the vanilla DK_Jyske_multi /
DK_Ostre_Landkommando_multi division rules. Pure transports never get their own card.

West German units: a small LANDJUT-flavoured subset (not the whole RFA deck), with the
availability and transports the RFA_mechanized / RFA_motorized tables already give them,
usually one card fewer. The RFA units keep their RFA_unit_edits balance - don't edit them here.
"""

# fmt: off

DK_mechanized_newdivisionrules = {
    "logistic": [
        ("Leopard_1A3_CMD2_DK", 1, [0, 0, 2, 0]),
    ],
    "infantry": [
        ("Rifles_Mech_CMD_DK", 1, [0, 0, 5, 4], ["Bedford_MJ_4t_trans_DK", "M113A1_DK"]),
        ("Rifles_Mech_CarlG_DK", 3, [10, 7, 0, 0], ["Bedford_MJ_4t_trans_DK", "M113A1_DK"]),
        ("Engineers_CarlG_DK", 2, [0, 6, 4, 0], ["Bedford_MJ_4t_trans_DK", "M113A1_DK"]),
    ],
    "artillery": [
        ("M125_HOWZ_DK", 2, [4, 3, 0, 0]),
        ("M106A1_HOWZ_DK", 2, [4, 3, 0, 0]),
        ("M109A3_DK", 2, [3, 2, 0, 0]),
    ],
    "tank": [
        ("Leopard_1A3_CMD_DK", 1, [0, 0, 4, 0]),
        ("Leopard_1A3_DK", 3, [10, 7, 0, 0]),
        ("Leopard_1A5_DK", 2, [0, 8, 6, 0]),
        ("Centurion_Mk5_2_upgraded_CMD_DK", 1, [0, 0, 4, 0]),
        ("Centurion_Mk5_2_DK", 2, [10, 7, 0, 0]),
        ("Centurion_Mk5_2_upgraded_DK", 2, [0, 8, 6, 0]),
        ("M113A2_PNMK_DK", 2, [8, 6, 0, 0]),
        ("M113A1_TOW_DK", 2, [8, 6, 0, 0]),
    ],
    "recon": [
        ("HvyScout_DK", 2, [0, 6, 4, 0], ["Bedford_MJ_4t_trans_DK", "M113A1_reco_DK"]),
        ("Leopard_1A5_reco_DK", 1, [0, 6, 4, 0]),
    ],
    "aa": [
        ("Otomatic_DK", 2, [0, 4, 3, 0]),
    ],
}

DK_motorized_newdivisionrules = {
    "infantry": [
        ("Rifles_CMD_DK", 1, [0, 0, 7, 5], ["LandRover_DK"]),
        ("Reserve_CMD_DK", 1, [0, 7, 5, 0], ["Bedford_MJ_4t_trans_DK"]),
        ("Rifles_DK", 3, [10, 7, 0, 0], ["Bedford_MJ_4t_trans_DK"]),
        ("Rifles_LAW_DK", 2, [10, 7, 0, 0], ["Bedford_MJ_4t_trans_DK"]),
        ("Guards_DK", 1, [0, 8, 6, 0], ["Bedford_MJ_4t_trans_DK"]),
        ("Reserve_DK", 2, [10, 0, 0, 0], ["Bedford_MJ_4t_trans_DK"]),
        ("Militia_DK", 2, [12, 0, 0, 0], ["Bedford_MJ_4t_trans_DK"]),
        ("Engineers_Reserve_DK", 1, [12, 0, 0, 0], ["Bedford_MJ_4t_trans_DK"]),
        # ATteam_TOW isn't in either vanilla DK division, so there's no vanilla transport
        # pairing to copy - LandRover_DK assumed (it carries the ITOW team).
        ("ATteam_TOW_DK", 2, [9, 0, 0, 0], ["LandRover_DK"]),
        ("ATteam_RCL_M40A1_Reserve_DK", 1, [10, 0, 0, 0], ["LandRover_DK"]),
    ],
    "artillery": [
        ("Howz_M101_105mm_DK", 2, [4, 3, 0, 0], ["Bedford_MJ_4t_trans_DK"]),
        ("Howz_M114_155mm_DK", 2, [3, 2, 0, 0], ["MD_Jupiter_trans_DK"]),
        ("Howz_M114_39_155mm_DK", 1, [3, 2, 0, 0], ["MD_Jupiter_trans_DK"]),
        ("Howz_M59_LongTom_155mm_DK", 1, [3, 0, 0, 0], ["MD_Jupiter_trans_DK"]),
        ("Howz_M115_203mm_DK", 1, [2, 0, 1, 0], ["MD_Jupiter_trans_DK"]),
    ],
    "tank": [
        ("Centurion_Mk3_CMD_DK", 1, [0, 6, 0, 0]),
        ("Centurion_Mk3_DK", 2, [10, 0, 0, 0]),
        ("M41_DK1_Walker_DK", 2, [10, 7, 0, 0]),
        ("M10_Achilles_DK", 1, [10, 0, 0, 0]),
        ("LandRover_ITOW_DK", 2, [8, 6, 0, 0]),
        ("M38A1_RCL_DK", 1, [12, 0, 0, 0]),
    ],
    "recon": [
        ("Scout_Reserve_DK", 1, [8, 0, 0, 0], ["Bedford_MJ_4t_trans_DK"]),
        ("M41_DK1_Walker_reco_DK", 2, [0, 6, 4, 0]),
    ],
    "aa": [
        ("DCA_M55_DK", 1, [10, 7, 0, 0], ["LandRover_DK"]),
        ("DCA_Bofors_L60_DK", 2, [10, 7, 0, 0], ["MD_Jupiter_trans_DK"]),
        ("DCA_Bofors_upgrade_DK", 1, [10, 7, 0, 0], ["MD_Jupiter_trans_DK"]),
        ("Bedford_MJ_4t_AA_DK", 2, [8, 6, 0, 0]),
    ],
}

DK_global_newdivisionrules = {
    "logistic": [
        ("FOB_DK", 1, [2, 0, 0, 0]),
        ("Rifles_CMD2_DK", 2, [0, 2, 0, 0], ["LandRover_DK", "M113A1_DK"]),
        ("LandRover_CMD_DK", 1, [0, 4, 0, 0]),
        ("M113A1_CMD_DK", 1, [0, 3, 0, 0]),
        ("Bedford_MJ_4t_supply_DK", 2, [4, 0, 0, 0]),
        ("MD_Jupiter_supply_DK", 2, [2, 0, 0, 0]),
        ("SeaKing_S61_supply_DK", 1, [2, 0, 0, 0]),
    ],
    "infantry": [
        ("Engineers_CMD_DK", 1, [0, 0, 7, 5], ["LandRover_DK"]),
        ("Engineers_DK", 2, [0, 6, 4, 0], ["Bedford_MJ_4t_trans_DK", "M113A1_DK"]),
        ("Groupe_AT_DK", 2, [12, 9, 0, 0], ["Bedford_MJ_4t_trans_DK", "M113A1_DK"]),
        ("MP_DK", 1, [0, 12, 9, 0], ["LandRover_DK", "VW_T2b_MP_DK"]),
        ("Jaeger_DK", 1, [0, 0, 4, 3], ["LandRover_DK"]),
        ("Frogmen_DK", 1, [0, 0, 4, 3], ["LandRover_DK", "Lynx_Mk80_trans_DK"]),
        ("HMGteam_MG3_DK", 2, [12, 9, 0, 0], ["LandRover_DK"]),
        ("HMGteam_M2HB_DK", 1, [9, 7, 0, 0], ["LandRover_DK"]),
        ("ATteam_ITOW_DK", 2, [6, 4, 0, 0], ["LandRover_DK"]),
        # Same assumption as ATteam_TOW_DK: no vanilla pairing, LandRover_DK assumed.
        ("ATteam_TOW2_DK", 1, [4, 3, 0, 0], ["LandRover_DK"]),
    ],
    "artillery": [
        ("Mortier_81mm_DK", 2, [6, 5, 4, 0], ["Bedford_MJ_4t_trans_DK"]),
        ("Mortier_MO120_AM50_120mm_DK", 2, [5, 4, 3, 0], ["Bedford_MJ_4t_trans_DK"]),
    ],
    "recon": [
        ("Scout_DK", 2, [8, 6, 0, 0], ["LandRover_DK"]),
        ("Scout_AT_DK", 1, [8, 6, 0, 0], ["LandRover_DK"]),
        ("LRRP_DK", 1, [0, 0, 4, 3], ["LandRover_DK"]),
        ("SEP_DK", 1, [0, 0, 4, 3], ["LandRover_DK"]),
        ("M113_GreenArcher_DK", 1, [6, 0, 0, 0]),
        ("OH6_DK", 2, [0, 6, 0, 0]),
        ("SeaKing_S61_reco_DK", 1, [0, 4, 0, 0]),
    ],
    "aa": [
        ("MANPAD_Redeye_DK", 2, [12, 9, 0, 0], ["LandRover_DK"]),
        ("MANPAD_Stinger_C_DK", 2, [7, 5, 0, 0], ["LandRover_DK"]),
        ("DCA_I_Hawk_DK", 1, [4, 3, 0, 0], ["MD_Jupiter_trans_DK"]),
    ],
    "heli": [
        ("Ecureuil_TOW_DK", 2, [0, 4, 3, 0]),
    ],
    "planes": [
        ("F16A_AA1_DK", 1, [0, 3, 2, 0]),
        ("F16A_AA2_DK", 1, [0, 3, 2, 0]),
        ("F16A_AA3_DK", 1, [0, 2, 0, 1]),
        ("F16A_AGM_DK", 1, [0, 2, 0, 1]),
        ("F16A_HE_DK", 1, [0, 2, 0, 0]),
        ("F16A_HE_CLU_DK", 1, [0, 2, 0, 0]),
        ("F16A_CLU_DK", 1, [0, 2, 0, 0]),
        ("Saab_35F_Draken_AA_DK", 2, [0, 4, 3, 0]),
        ("Saab_35F_Draken_HE_DK", 1, [0, 4, 0, 0]),
        ("Saab_35F_Draken_HE_CLU_DK", 1, [0, 4, 0, 0]),
        ("Saab_35F_Draken_CLU_DK", 1, [0, 4, 0, 0]),
        ("Saab_35F_Draken_RKT1_DK", 1, [0, 6, 0, 0]),
    ],
}
# ---------------------------------------------------------------- West German part
# 6. Panzergrenadierdivision: PzGrenBrig 16/17 (Marder), PzBrig 18 (Leopard 2).
LANDJUT_RFA_mechanized_newdivisionrules = {
    "infantry": [
        ("Panzergrenadier_CMD_RFA", 1, [0, 0, 5, 4], ["M113A1G_RFA", "Marder_1A1_RFA", "Marder_1A3_RFA"]),
        ("Panzergrenadier_IFV_RFA", 2, [12, 9, 0, 0], ["Marder_1A1_RFA", "Marder_1A1_MILAN_RFA", "Marder_1A3_RFA", "Marder_1A3_MILAN_RFA"]),
        ("Panzergrenadier_PzF3_RFA", 1, [12, 9, 0, 0], ["Marder_1A1_RFA", "Marder_1A1_MILAN_RFA", "Marder_1A3_RFA", "Marder_1A3_MILAN_RFA"]),
    ],
    "artillery": [
        ("M110A2_Howz_RFA", 1, [2, 0, 1, 0]),
        ("Lars_2_RFA", 1, [3, 2, 0, 0]),
    ],
    "tank": [
        ("Leopard_2A1_RFA", 1, [6, 4, 0, 0]),
        ("Leopard_2A3_RFA", 1, [0, 6, 4, 0]),
        ("Jaguar_1_RFA", 1, [6, 4, 0, 0]),
    ],
    "recon": [
        ("Luchs_A1_RFA", 1, [6, 4, 0, 0]),
    ],
    "aa": [
        ("Gepard_1A2_RFA", 1, [6, 4, 0, 0]),
        ("Marder_Roland_RFA", 1, [4, 3, 0, 0]),
    ],
    "heli": [
        ("Bo_105_PAH_1_RFA", 1, [0, 6, 0, 0]),
    ],
}

# Heimatschutzbrigade 51 / Territorialkommando Schleswig-Holstein + Marineflieger.
LANDJUT_RFA_motorized_newdivisionrules = {
    "infantry": [
        ("Jager_RFA", 2, [10, 7, 0, 0], ["Unimog_trans_RFA", "TPZ_Fuchs_1_RFA"]),
        ("HeimatschutzJager_RFA", 2, [12, 0, 0, 0], ["Unimog_trans_RFA"]),
        ("Security_Marine_RFA", 1, [10, 7, 0, 0], ["MAN_630_L2AE_trans_RFA"]),
        ("ATteam_Milan_2_RFA", 1, [6, 4, 0, 0], ["Iltis_trans_RFA", "TPZ_Fuchs_MILAN_RFA", "TPZ_Fuchs_MILAN_2_RFA"]),
    ],
    "artillery": [
        ("FH70_155mm_RFA", 1, [3, 2, 0, 0], ["MAN_Kat_6x6_trans_RFA"]),
    ],
    "tank": [
        ("M48A2GA2_RFA", 2, [10, 0, 0, 0]),
        ("Leopard_1A1_RFA", 1, [10, 7, 0, 0]),
        ("Iltis_MILAN_RFA", 1, [12, 9, 0, 0]),
    ],
    "recon": [
        ("Fernspaher_RFA", 1, [0, 0, 4, 3], ["Iltis_trans_RFA", "Iltis_reco_RFA"]),
    ],
    "aa": [
        ("DCA_FK20_2_20mm_Zwillinge_RFA", 1, [10, 7, 0, 0], ["Unimog_trans_RFA"]),
    ],
    "planes": [
        ("Tornado_Marine_CLU_RFA", 1, [0, 2, 0, 0]),
    ],
}
# fmt: on
