"""Unit edits for Denmark.

Balance pass (2026-11-04) - every value is taken from the closest unit WARNO ACTUAL already
balances (the analog is named in each comment), so Danish units cost and behave like their
West German / British / US counterparts. Availability is NOT set here: national divisions
read it from the tuples in DK_newdivisionrules.py.

Conventions copied from RFA_unit_edits.py:
- Vanilla CMD tanks / CMD infantry become leaders (LDR_TNK / LDR_Unit, no zone capture),
  priced like a regular unit + 5. Real command units are the vehicle CMDs (CMD_Unit tag,
  145-155) plus the new Rifles_CMD2_DK / Leopard_1A3_CMD2_DK in DK_new_units.py.
- Tanks with a main gun get Reload_Penalty.
- Infantry gets an infantry_equip_* specialty: light = rifles/SMGs, medium = squad MG +
  launcher (like Jager_RFA), heavy = MANPAD/ATGM carriers, veryheavy = crew-served AT.
  Speed 26 for line infantry, 20 for heavy, 14 for TOW teams, 9 for the 106mm RCL.
- Pure transports cost 15 and are refundable.

Units with an empty dict keep their vanilla values. Every unit in a DK rules table must be
a key here (or a NEW_UNITS NewName), or validate_new_divisionrules_units warns. FOB_DK is
a building, not a unit, so it has no entry (the validator skips FOB_*).
"""

# fmt: off
dk_unit_edits = {
    # ------------------------------------------------------------------ LOGISTIC / CMD
    "LandRover_CMD_DK": {  # analog LandRover_CMD_UK 145
        "CommandPoints": 145,
        "TagSet": {"add_tags": ['"CMD_Unit"']},
    },
    "M113A1_CMD_DK": {  # analog TPZ_Fuchs_CMD_RFA 155 (armored CMD carrier)
        "CommandPoints": 150,
        "TagSet": {"add_tags": ['"CMD_Unit"']},
    },
    "Bedford_MJ_4t_supply_DK": {},
    "MD_Jupiter_supply_DK": {},
    "SeaKing_S61_supply_DK": {},

    # ------------------------------------------------------------------ TRANSPORTS
    "LandRover_DK": {  # analog LandRover_UK
        "CommandPoints": 15,
        "SpecialtiesList": {"add_specs": ["'refundable_unit'",]},
    },
    "Bedford_MJ_4t_trans_DK": {  # analog Bedford_MJ_4t_trans_UK
        "CommandPoints": 15,
        "SpecialtiesList": {"add_specs": ["'refundable_unit'",]},
    },
    "MD_Jupiter_trans_DK": {  # analog MAN/Unimog trucks
        "CommandPoints": 15,
        "SpecialtiesList": {"add_specs": ["'refundable_unit'",]},
    },
    "M113A1_DK": {  # analog M113A1G_RFA
        "CommandPoints": 15,
        "orders": {"add_orders": ["EOrderType/Sell"]},
        "SpecialtiesList": {"add_specs": ["'refundable_unit'",]},
    },
    "VW_T2b_MP_DK": {
        "CommandPoints": 15,
        "SpecialtiesList": {"add_specs": ["'refundable_unit'",]},
    },
    "Lynx_Mk80_trans_DK": {  # Frogmen transport; analog Lynx_AH_Mk1_UK 50, set to 45 by hand
        "CommandPoints": 45,
        "SpecialtiesList": {"add_specs": ["'refundable_unit'",]},
    },

    # ------------------------------------------------------------------ INFANTRY LEADERS
    # Vanilla CMD infantry -> leader squads, same block as Jager_CMD_RFA.
    "Rifles_CMD_DK": {  # analog Rifles_CMD_UK 25 (4 men, SMGs + LAW)
        "CommandPoints": 25,
        "TagSet": {
            "overwrite_all": [
                "AllUnits", "LDR_Unit", "AllowedForMissileRoE", "Crew", "GroundUnits",
                "Inf_quartier_ok", "Infanterie", "UNITE_Rifles_CMD_DK", "Unite",
            ],
        },
        "TransportedTexture": "UseInGame_Transport_assault",
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "SpecialtiesList": {"overwrite_all": ["_leader", "infantry_equip_light"]},
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "max_speed": 26,
        "remove_zone_capture": None,
    },
    "Engineers_CMD_DK": {  # analog Engineers_CMD_RFA 35 - stays an engineer (role/icon/assault tag), like it
        "CommandPoints": 35,
        "TagSet": {
            "overwrite_all": [
                "AllUnits", "LDR_Unit", "AllowedForMissileRoE", "Crew", "GroundUnits",
                "Inf_quartier_ok", "Infanterie", "Infanterie_Spec_Attaque", "UNITE_Engineers_CMD_DK", "Unite",
            ],
        },
        "TransportedTexture": "UseInGame_Transport_assault",
        "IdentifiedTextures": ["Texture_RTS_H_assault", "Texture_assault"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "engineer",
        "SpecialtiesList": {"overwrite_all": ["_leader", "_choc", "infantry_equip_medium"]},
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "max_speed": 26,
        "remove_zone_capture": None,
    },
    "Reserve_CMD_DK": {  # analog Territorial_CMD_UK 20, bigger squad (12 men, MG + bazooka)
        "CommandPoints": 30,
        "TagSet": {
            "overwrite_all": [
                "AllUnits", "LDR_Unit", "AllowedForMissileRoE", "Crew", "GroundUnits",
                "Inf_quartier_ok", "Infanterie", "UNITE_Reserve_CMD_DK", "Unite",
            ],
        },
        "TransportedTexture": "UseInGame_Transport_assault",
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "SpecialtiesList": {"overwrite_all": ["_leader", "_reservist", "infantry_equip_light"]},
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "max_speed": 26,
        "remove_zone_capture": None,
    },
    "Rifles_Mech_CMD_DK": {  # analog Panzergrenadier_CMD_RFA 35 (carries a Redeye -> heavy)
        "CommandPoints": 35,
        "TagSet": {
            "overwrite_all": [
                "AllUnits", "LDR_Unit", "AllowedForMissileRoE", "Crew", "GroundUnits",
                "Inf_quartier_ok", "Infanterie", "Infanterie_IFV", "UNITE_Rifles_Mech_CMD_DK", "Unite",
            ],
        },
        "TransportedTexture": "UseInGame_Transport_assault",
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "SpecialtiesList": {"overwrite_all": ["_leader", "_ifv", "infantry_equip_heavy"]},
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "max_speed": 20,
        "remove_zone_capture": None,
    },

    # ------------------------------------------------------------------ INFANTRY
    "Rifles_DK": {  # G3/Garand + MG62 + Carl G; analog Jager_Carl_RFA 40, older rifles
        "CommandPoints": 35,
        "max_speed": 26,
        "SpecialtiesList": {"add_specs": ["'infantry_equip_medium'"]},
    },
    "Rifles_LAW_DK": {  # G3 + MG62 + LAW; analog Jager_RFA 35
        "CommandPoints": 35,
        "max_speed": 26,
        "SpecialtiesList": {"add_specs": ["'infantry_equip_medium'"]},
    },
    "Rifles_Mech_CarlG_DK": {  # G3 + MG62 + Carl G; analog Jager_Carl_RFA 40
        "CommandPoints": 40,
        "max_speed": 26,
        "SpecialtiesList": {"add_specs": ["'infantry_equip_medium'"]},
    },
    "Guards_DK": {  # 10 men, resolute, Carl G; analog Rifles_Gurkhas_UK 70 is elite - priced below
        "CommandPoints": 45,
        "max_speed": 26,
        "SpecialtiesList": {"add_specs": ["'infantry_equip_medium'"]},
    },
    "Reserve_DK": {  # 12 men, G3 + MG62 + LAW + DMR; analog HeimatschutzJager_RFA 35
        "CommandPoints": 35,
        "max_speed": 26,
        "SpecialtiesList": {"add_specs": ["'infantry_equip_medium'"]},
    },
    "Militia_DK": {  # 12 men, Garand + bazooka, militia; analog Territorial_UK 25
        "CommandPoints": 25,
        "max_speed": 26,
        "SpecialtiesList": {"add_specs": ["'infantry_equip_light'"]},
    },
    "Engineers_DK": {  # analog Engineers_RFA 50 (LAW instead of PzF)
        "CommandPoints": 45,
        "max_speed": 26,
        "SpecialtiesList": {"add_specs": ["'infantry_equip_medium'"]},
    },
    "Engineers_CarlG_DK": {  # analog Engineers_RFA 50
        "CommandPoints": 50,
        "max_speed": 26,
        "SpecialtiesList": {"add_specs": ["'infantry_equip_medium'"]},
    },
    "Engineers_Reserve_DK": {  # analog Engineers_Reserve_RFA 25
        "CommandPoints": 25,
        "max_speed": 26,
        "SpecialtiesList": {"add_specs": ["'infantry_equip_light'"]},
    },
    "Groupe_AT_DK": {  # 2x Carl G; analog Groupe_AT_RFA 30
        "CommandPoints": 30,
        "max_speed": 26,
        "SpecialtiesList": {"add_specs": ["'infantry_equip_medium'"]},
    },
    "MP_DK": {  # SMGs only; analog MP_US 30 has more men
        "CommandPoints": 20,
        "max_speed": 26,
        "SpecialtiesList": {"add_specs": ["'infantry_equip_light'"]},
    },
    "Frogmen_DK": {  # SF, MP5SD + Carl G; analog KSM_RFA 60 (fewer men here)
        "CommandPoints": 50,
        "max_speed": 26,
        "SpecialtiesList": {"add_specs": ["'infantry_equip_medium'"]},
    },
    "Jaeger_DK": {  # SF para, MG + DMR + LAW; analog Fernspaher_RFA 70 / KSM_RFA 60
        "CommandPoints": 60,
        "max_speed": 26,
        "SpecialtiesList": {"add_specs": ["'infantry_equip_medium'"]},
    },
    "HMGteam_MG3_DK": {  # same block as HMGteam_MG3_RFA
        "CommandPoints": "HMGteam_M60_US",
        "strength": "HMGteam_M60_US",
        "max_speed": "HMGteam_M60_US",
        "SpecialtiesList": {"add_specs": "HMGteam_M60_US"},
    },
    "HMGteam_M2HB_DK": {  # same block as HMGteam_M2HB_UK
        "CommandPoints": "HMGteam_M2HB_US",
        "strength": "HMGteam_M2HB_US",
        "max_speed": "HMGteam_M2HB_US",
        "SpecialtiesList": {"add_specs": "HMGteam_M2HB_US"},
    },
    "ATteam_TOW_DK": {  # analog ATteam_TOW_US 35
        "CommandPoints": 35,
        "max_speed": 14,
        "SpecialtiesList": {"add_specs": ["'infantry_equip_veryheavy'"]},
    },
    "ATteam_ITOW_DK": {  # analog ATteam_ITOW_US 50
        "CommandPoints": 50,
        "max_speed": 14,
        "SpecialtiesList": {"add_specs": ["'infantry_equip_veryheavy'"]},
    },
    "ATteam_TOW2_DK": {  # analog ATteam_TOW2_US 65
        "CommandPoints": 65,
        "max_speed": 14,
        "SpecialtiesList": {"add_specs": ["'infantry_equip_veryheavy'"]},
    },
    "ATteam_RCL_M40A1_Reserve_DK": {  # analog ATteam_RCL_M40A1_RFA 35, reservist
        "CommandPoints": 30,
        "max_speed": 9,
        "SpecialtiesList": {"add_specs": ["'infantry_equip_veryheavy'"]},
    },
    "MANPAD_Redeye_DK": {  # analog MANPAD_Redeye_RFA 20
        "CommandPoints": 20,
        "max_speed": 20,
        "SpecialtiesList": {"add_specs": ["'infantry_equip_heavy'"]},
    },
    "MANPAD_Stinger_C_DK": {  # analog MANPAD_Stinger_C_US 55
        "CommandPoints": 55,
        "max_speed": 20,
        "SpecialtiesList": {"add_specs": ["'infantry_equip_heavy'"]},
    },

    # ------------------------------------------------------------------ RECON
    "Scout_DK": {  # analog Scout_RFA 20
        "CommandPoints": 20,
        "max_speed": 26,
        "SpecialtiesList": {"add_specs": ["'infantry_equip_medium'"]},
    },
    "Scout_AT_DK": {  # Scout_DK + Carl G
        "CommandPoints": 25,
        "max_speed": 26,
        "SpecialtiesList": {"add_specs": ["'infantry_equip_medium'"]},
    },
    "Scout_Reserve_DK": {  # 6 men, reservist; analog Scout_Heimat_RFA 35 is better armed
        "CommandPoints": 25,
        "max_speed": 26,
        "SpecialtiesList": {"add_specs": ["'infantry_equip_light'"]},
    },
    "HvyScout_DK": {  # 10 men, MG + Carl G; between Scout_Heimat_RFA 35 and Fernspaher_RFA 70
        "CommandPoints": 45,
        "max_speed": 26,
        "SpecialtiesList": {"add_specs": ["'infantry_equip_medium'"]},
    },
    "LRRP_DK": {  # SMGs + LAW; analog LRRP_UK 70 (light), vanilla here was cheaper
        "CommandPoints": 60,
        "max_speed": 26,
        "SpecialtiesList": {"add_specs": ["'infantry_equip_light'"]},
    },
    "SEP_DK": {  # 4 men, 2 snipers + Redeye
        "CommandPoints": 55,
        "max_speed": 26,
        "SpecialtiesList": {"add_specs": ["'infantry_equip_medium'"]},
    },
    "M113A1_reco_DK": {  # analog M113A1G_reco_RFA 20
        "CommandPoints": 20,
        "WeaponDescriptor": {"Salves": {"HMG_12_7_mm_M2HB": 35}},  # as WA's US M113/M125/M109 family
    },
    "M113_GreenArcher_DK": {  # analog M113_GreenArcher_RFA 30
        "CommandPoints": 30,
    },
    "M41_DK1_Walker_reco_DK": {  # analog Luchs_A1_RFA 50, but a real 76mm APFSDS gun
        "CommandPoints": 75,
        "capacities": {"add_capacities": ["Reload_Penalty"]},
    },
    "OH6_DK": {  # analog Bo_105_reco_RFA 30
        "CommandPoints": 30,
    },
    "SeaKing_S61_reco_DK": {
        "CommandPoints": 45,
    },

    # ------------------------------------------------------------------ TANKS (LEADERS)
    # Vanilla CMD tanks -> leaders, same block as Leopard_1A4_CMD_RFA.
    "Leopard_1A3_CMD_DK": {  # analog Leopard_1A4_CMD_RFA 85
        "capacities": {"add_capacities": ["LDR_TNK", "Reload_Penalty"]},
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 80,
        "TagSet": {
            "overwrite_all": [
                "AllUnits", "LDR_Unit", "AllowedForMissileRoE", "Char", "GroundUnits",
                "UNITE_Leopard_1A3_CMD_DK", "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {"overwrite_all": ["_leader", "_smoke_launcher"]},
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "remove_zone_capture": None,
    },
    "Centurion_Mk3_CMD_DK": {  # analog Centurion_Mk13_CMD_UK 65
        "capacities": {"add_capacities": ["LDR_TNK", "Reload_Penalty"]},
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 65,  # leader = Centurion_Mk3_DK 60 + 5
        "TagSet": {
            "overwrite_all": [
                "AllUnits", "LDR_Unit", "AllowedForMissileRoE", "Char", "GroundUnits",
                "UNITE_Centurion_Mk3_CMD_DK", "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {"overwrite_all": ["_leader", "_smoke_launcher"]},
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "remove_zone_capture": None,
    },
    "Centurion_Mk5_2_upgraded_CMD_DK": {  # analog Leopard_1A5_CMD_RFA 100
        "capacities": {"add_capacities": ["LDR_TNK", "Reload_Penalty"]},
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 95,
        "TagSet": {
            "overwrite_all": [
                "AllUnits", "LDR_Unit", "AllowedForMissileRoE", "Char", "GroundUnits",
                "UNITE_Centurion_Mk5_2_upgraded_CMD_DK", "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {"overwrite_all": ["_leader", "_smoke_launcher"]},
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "remove_zone_capture": None,
    },

    # ------------------------------------------------------------------ TANKS
    "Leopard_1A3_DK": {  # analog Leopard_1A1A2_RFA 75 (same vanilla 95)
        "capacities": {"add_capacities": ["Reload_Penalty"]},
        "CommandPoints": 75,
    },
    "Leopard_1A5_DK": {  # analog Leopard_1A5_RFA 95
        "capacities": {"add_capacities": ["Reload_Penalty"]},
        "CommandPoints": 95,
    },
    "Centurion_Mk3_DK": {  # 20pdr; analog Centurion_Mk13_UK 65 has the 105mm -> cheaper
        "capacities": {"add_capacities": ["Reload_Penalty"]},
        "CommandPoints": 60,
    },
    "Centurion_Mk5_2_DK": {  # 105mm L7; analog Centurion_Mk13_UK 65
        "capacities": {"add_capacities": ["Reload_Penalty"]},
        "CommandPoints": 65,
    },
    "Centurion_Mk5_2_upgraded_DK": {  # late APFSDS + FCS; between Leopard 1A4 80 and 1A5 95
        "capacities": {"add_capacities": ["Reload_Penalty"]},
        "CommandPoints": 90,
    },
    "M41_DK1_Walker_DK": {  # light tank, 76mm APFSDS; analog M551A1 Sheridan 50 / Leopard 1A1 75
        "capacities": {"add_capacities": ["Reload_Penalty"]},
        "CommandPoints": 65,
    },
    "M10_Achilles_DK": {  # WW2 tank destroyer, reservist; Reload_Penalty like KanJagdPanzer_RFA
        "capacities": {"add_capacities": ["Reload_Penalty"]},
        "CommandPoints": 40,
    },
    "M113A2_PNMK_DK": {  # 25mm KBA; Marder_1A2_RFA is 45 with 20mm + more armour
        "CommandPoints": 35,
    },
    "M113A1_TOW_DK": {  # TOW-2, 8 missiles; analog M901A1_ITW_US 65
        "CommandPoints": 70,
        "WeaponDescriptor": {"Salves": {"HMG_12_7_mm_M2HB": 35}},  # as WA's US M113/M125/M109 family
    },
    "LandRover_ITOW_DK": {  # "Laro M/87"; analog LandRover_MILAN_UK 45 / M151A2_TOW_NG_US 40
        "CommandPoints": 45,
    },
    "M38A1_RCL_DK": {  # analog M151C_RCL_NG_US 25 (16 rounds)
        "CommandPoints": 25,
        "WeaponDescriptor": {"Salves": {"RocketInf_M40A1_RCL_106mm": 16}},
    },

    # ------------------------------------------------------------------ ARTILLERY
    "Mortier_81mm_DK": {  # analog Mortier_M29_81mm_US 30
        "CommandPoints": 30,
    },
    "Mortier_MO120_AM50_120mm_DK": {  # analog Mortier_Tampella_120mm_RFA 45
        "CommandPoints": 45,
    },
    "M125_HOWZ_DK": {  # analog M125_HOWZ_US 55
        "CommandPoints": 55,
        "WeaponDescriptor": {"Salves": {"HMG_12_7_mm_M2HB": 35}},  # as WA's US M113/M125/M109 family
    },
    "M106A1_HOWZ_DK": {  # analog M106A2_HOWZ_US 70
        "CommandPoints": 70,
        "ButtonTexture": "M106A2_HOWZ_US",  # vanilla DK icon is still Eugen's default.png placeholder
        "WeaponDescriptor": {"Salves": {"HMG_12_7_mm_M2HB": 35}},  # as WA's US M113/M125/M109 family
    },
    "Howz_M101_105mm_DK": {  # analog Howz_M101_105mm_RFA 55
        "CommandPoints": 55,
    },
    "Howz_M114_155mm_DK": {  # analog Howz_M198_155mm_US 110 is longer-ranged
        "CommandPoints": 85,
    },
    "Howz_M114_39_155mm_DK": {
        "CommandPoints": 105,
    },
    "Howz_M59_LongTom_155mm_DK": {  # reservist
        "CommandPoints": 95,
    },
    "Howz_M115_203mm_DK": {  # towed 203mm; M110A2_Howz_RFA is 220 self-propelled
        "CommandPoints": 125,
    },
    "M109A3_DK": {  # analog M109A2_UK 180 / M109A3G_HOWZ_RFA 190
        "CommandPoints": 180,
        "WeaponDescriptor": {"Salves": {"HMG_12_7_mm_M2HB": 35}},  # as WA's US M113/M125/M109 family
    },

    # ------------------------------------------------------------------ AA
    "DCA_M55_DK": {  # towed quad .50; same as WA DCA_M55_FR (15, 3 salvos)
        "CommandPoints": 15,
        "max_speed": 6,
        "WeaponDescriptor": {"Salves": {"DCA_4_canon_Maxson_towed_12_7mm": 3}},
    },
    "DCA_Bofors_L60_DK": {  # same as WA DCA_Bofors_L60_FR (15, 1 salvo)
        "CommandPoints": 15,
        "max_speed": 6,
        "WeaponDescriptor": {"Salves": {"DCA_1_canon_Bofors_40mm_L60": 1}},
    },
    "DCA_Bofors_upgrade_DK": {  # same as WA Bofors_40mm_RFA (30, 1 salvo)
        "CommandPoints": 30,
        "max_speed": 6,
        "WeaponDescriptor": {"Salves": {"DCA_1_canon_Bofors_40mm": 1}},
    },
    "Bedford_MJ_4t_AA_DK": {  # truck quad .50; same as WA M16_MGMC_FR (25, 3 salvos)
        "CommandPoints": 25,
        "WeaponDescriptor": {"Salves": {"DCA_4_canon_Maxson_SP_12_7mm": 3}},
    },
    "DCA_I_Hawk_DK": {  # analog DCA_I_Hawk_RFA 90
        "CommandPoints": 90,
        "SpecialtiesList": {"add_specs": ["'verygood_airoptics'"]},
    },

    # ------------------------------------------------------------------ HELICOPTERS
    "Ecureuil_TOW_DK": {  # "PVH Fennec", 4x TOW-2; analog Bo_105_PAH_1_RFA 80 (6x HOT): 6 HP vs 4, faster, but 2 missiles fewer
        "CommandPoints": 85,
    },

    # ------------------------------------------------------------------ AIR
    # F-16A: priced vs US F-16 (WA) HE 200, CBU 220, AA 180-200, AGM 275 (that one has a
    # jammer pod). Vanilla F-16A = vanilla F-16E (ECM -0.3, HighAltitude 10600); WA gives
    # every F-16 without a jammer pod ECM -0.25 + HighAltitude 13250, so the same here.
    "F16A_AA1_DK": {"CommandPoints": 170, "ECM": -0.25, "optics": {"OpticalStrengths": {"EOpticalStrength/HighAltitude": 13250}}},
    "F16A_AA2_DK": {"CommandPoints": 170, "ECM": -0.25, "optics": {"OpticalStrengths": {"EOpticalStrength/HighAltitude": 13250}}},
    "F16A_AA3_DK": {"CommandPoints": 180, "ECM": -0.25, "optics": {"OpticalStrengths": {"EOpticalStrength/HighAltitude": 13250}}},
    "F16A_AGM_DK": {"CommandPoints": 220, "ECM": -0.25, "optics": {"OpticalStrengths": {"EOpticalStrength/HighAltitude": 13250}}},
    "F16A_HE_DK": {"CommandPoints": 210, "ECM": -0.25, "optics": {"OpticalStrengths": {"EOpticalStrength/HighAltitude": 13250}}},
    "F16A_HE_CLU_DK": {"CommandPoints": 220, "ECM": -0.25, "optics": {"OpticalStrengths": {"EOpticalStrength/HighAltitude": 13250}}},
    "F16A_CLU_DK": {"CommandPoints": 210, "ECM": -0.25, "optics": {"OpticalStrengths": {"EOpticalStrength/HighAltitude": 13250}}},
    # Draken: priced vs F104G_Starfighter_RFA 110 (AA) / _HE 140. ECM: vanilla Draken has
    # -0.3 like the F-16 (F-104G only -0.1), and WA turns vanilla -0.3 into -0.25 -> -0.25.
    # The fighter gets the WA F-16/F-4F HighAltitude optics 13250 (vanilla 10600 like them);
    # the strike variants keep their own vanilla 5250.
    "Saab_35F_Draken_AA_DK": {"CommandPoints": 100, "ECM": -0.25, "optics": {"OpticalStrengths": {"EOpticalStrength/HighAltitude": 13250}}},
    "Saab_35F_Draken_HE_DK": {"CommandPoints": 170, "ECM": -0.25},
    "Saab_35F_Draken_HE_CLU_DK": {"CommandPoints": 170, "ECM": -0.25},
    "Saab_35F_Draken_CLU_DK": {"CommandPoints": 170, "ECM": -0.25},
    "Saab_35F_Draken_RKT1_DK": {"CommandPoints": 130, "ECM": -0.25},
}
# fmt: on
