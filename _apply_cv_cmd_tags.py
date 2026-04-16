"""Add CMD_Unit via add_tags to all vanilla CV unit_edits entries."""

import os
import re

# All vanilla CV entries identified (CMD units without LDR_Unit/LDR_SOV_Unit).
VANILLA_CVS = {
    "src/constants/unit_edits/UK_unit_edits.py": [
        "LandRover_CMD_nonBerlin_UK",
        "LandRover_CMD_UK",
        "Saxon_CMD_UK",
        "FV1612_Humber_CMD_UK",
        "MCV_80_Warrior_CMD_UK",
        "Gazelle_CMD_UK",
    ],
    "src/constants/unit_edits/FR_unit_edits.py": [
        "M201_CMD_FR",
        "VAB_CMD_FR",
        "AMX_13_mod56_CMD_FR",
        "AMX_10_PC_CMD_FR",
        "Alouette_II_CMD_FR",
        "Gazelle_CMD_FR",
    ],
    "src/constants/unit_edits/RFA_unit_edits.py": [
        "Iltis_para_CMD_RFA",
        "Faun_Kraka_CMD_RFA",
        "TPZ_Fuchs_CMD_RFA",
        "Bo_105_CMD_RFA",
        "Alouette_II_CMD_RFA",
    ],
    "src/constants/unit_edits/USA_unit_edits.py": [
        "OH58C_CMD_US",
        "M151_MUTT_CMD_US",
        "M1025_Humvee_CMD_para_US",
        "M1025_Humvee_CMD_US",
        "NatGuard_CMD_US",
    ],
    "src/constants/unit_edits/SOV_unit_edits.py": [
        "UAZ_469_CMD_SOV",
        "UAZ_469_CMD_Naval_SOV",
        "BMP_1_CMD_POTOK2_SOV",
        "BMD_1_CMD_SOV",
        "BMD_1K_CMD_SOV",
        "BMP_1_CMD_SOV",
        "BMD_2_CMD_SOV",
        "LUAZ_967M_CMD_VDV_SOV",
        "UAZ_469_CMD_VDV_SOV",
        "BMP_2_CMD_SOV",
        "BRDM_2_CMD_SOV",
        "BTR_60_CMD_SOV",
        "BTR_80_CMD_SOV",
        "Mi_8K_CMD_SOV",
        "Naval_Rifle_CMD_SOV",
        "Naval_VDV_CMD_SOV",
        "Engineers_CMD_Naval_SOV",
        # T55AM_CMD_SOV excluded: has remove_zone_capture (not a CV)
    ],
    "src/constants/unit_edits/RDA_unit_edits.py": [
        "UAZ_469_CMD_DDR",
        "PT76B_CMD_DDR",
        "MTLB_CMD_DDR",
        "BMP_1_CMD_DDR",
        "BRDM_2_CMD_DDR",
        "BTR_60_CMD_DDR",
        "BTR_60_CHAIKA_CMD_DDR",
        "Mi_2_CMD_DDR",
    ],
    "src/constants/unit_edits/POL_unit_edits.py": [
        "UAZ_469_CMD_POL",
        "UAZ_469_CMD_Para_POL",
        "BMP_1_CMD_POL",
        "BRDM_2_CMD_POL",
        "BRDM_2_CMD_R5_POL",
        "OT_64_SKOT_CMD_POL",
        "Mi_2_CMD_POL",
    ],
}


def process_file(filepath, unit_keys):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    added = 0
    inserted = 0

    for unit_key in unit_keys:
        pattern = f'"{unit_key}":'
        key_idx = None
        for i in range(len(lines)):
            if pattern in lines[i] and not lines[i].lstrip().startswith("#"):
                key_idx = i + inserted
                break

        if key_idx is None:
            print(f"    WARNING: key {unit_key} not found in {os.path.basename(filepath)}")
            continue

        # Check if this unit block has remove_zone_capture (skip if so)
        key_indent = len(lines[key_idx]) - len(lines[key_idx].rstrip("\n").lstrip())
        block_end = len(lines) - 1
        has_remove_zone = False
        has_tagset = False

        for j in range(key_idx + 1, min(key_idx + 80, len(lines))):
            line = lines[j]
            indent = len(line) - len(line.rstrip("\n").lstrip())
            stripped = line.strip()

            if stripped and indent <= key_indent and j > key_idx:
                block_end = j
                break

            if "remove_zone_capture" in line and not stripped.startswith("#"):
                has_remove_zone = True
            if '"TagSet"' in line and not stripped.startswith("#"):
                has_tagset = True

        if has_remove_zone:
            print(f"    SKIP {unit_key}: has remove_zone_capture")
            continue

        if has_tagset:
            print(f"    SKIP {unit_key}: already has TagSet")
            continue

        # Find the closing }, of this unit's dict — it's the line just before block_end
        # that looks like "    }," at key_indent + 4 or key_indent
        insert_before = block_end
        for j in range(block_end - 1, key_idx, -1):
            stripped = lines[j].strip()
            if stripped == "},":
                insert_before = j
                break

        inner_indent = " " * (key_indent + 4)
        insert_line = f'{inner_indent}"TagSet": {{"add_tags": [\'\"CMD_Unit\"\']}},\n'
        lines.insert(insert_before, insert_line)
        inserted += 1
        added += 1

    print(f"  {added} CMD_Unit tags added to {os.path.basename(filepath)}")

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(lines)


if __name__ == "__main__":
    print("=== Adding CMD_Unit to vanilla CV unit_edits ===")
    for filepath, keys in VANILLA_CVS.items():
        process_file(filepath, keys)
    print("\nDone.")
