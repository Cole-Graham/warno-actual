import unittest

from src.constants.generated.gameplay.decks import load_default_multi_decks
from src.gameplay_mods.generated.gameplay.decks.default_multi_decks import (
    MULTI_DECK_PACK_NUMBER,
    build_deck_pack_ndf,
    entry_to_pack_namespace,
    flatten_categories,
    resolve_default_deck_pack_reference,
)


class TestDefaultMultiDecks(unittest.TestCase):
    def test_entry_to_pack_namespace_simple(self):
        entry = {"Descriptor_Unit_FOB_US": {"vet": 0}}
        self.assertEqual(
            entry_to_pack_namespace(entry),
            "Descriptor_Deck_Pack_FOB_US_0_1",
        )

    def test_entry_to_pack_namespace_with_transport(self):
        entry = {
            "Descriptor_Unit_ATteam_TOW2_para_US": {
                "vet": 1,
                "transport": "Descriptor_Unit_M998_Humvee_US",
            },
        }
        self.assertEqual(
            entry_to_pack_namespace(entry),
            "Descriptor_Deck_Pack_ATteam_TOW2_para_US_M998_Humvee_US_1_1",
        )

    def test_flatten_categories_preserves_order(self):
        categories = {
            "Tanks": [{"Descriptor_Unit_T72B1_SOV": {"vet": 1}}],
            "Logistic": [{"Descriptor_Unit_FOB_SOV": {"vet": 1}}],
            "Infantry": [{"Descriptor_Unit_VDV_Metis_SOV": {"vet": 1}}],
        }
        flattened = flatten_categories(categories)
        self.assertEqual(len(flattened), 3)
        self.assertIn("FOB_SOV", next(iter(flattened[0])))
        self.assertIn("VDV_Metis_SOV", next(iter(flattened[1])))
        self.assertIn("T72B1_SOV", next(iter(flattened[2])))

    def test_flatten_categories_empty(self):
        self.assertEqual(flatten_categories({}), [])
        self.assertEqual(flatten_categories({"Logistic": []}), [])

    def test_build_deck_pack_ndf_omits_xp_at_vet_zero(self):
        ndf_str = build_deck_pack_ndf(
            "Descriptor_Deck_Pack_FOB_US_0_1",
            "FOB_US",
            0,
        )
        self.assertNotIn("Xp =", ndf_str)
        self.assertIn("Number = 1", ndf_str)

    def test_build_deck_pack_ndf_includes_transport(self):
        ndf_str = build_deck_pack_ndf(
            "Descriptor_Deck_Pack_ATteam_TOW2_para_US_M998_Humvee_US_1_1",
            "ATteam_TOW2_para_US",
            1,
            transport_name="M998_Humvee_US",
        )
        self.assertIn("Xp = 1", ndf_str)
        self.assertIn("Transport = $/GFX/Unit/Descriptor_Unit_M998_Humvee_US", ndf_str)

    def test_load_default_multi_decks_returns_two_divisions(self):
        decks = load_default_multi_decks()
        self.assertEqual(
            set(decks.keys()),
            {"US_national_airborne_armored", "SOV_national_airborne_armored"},
        )

    def test_usa_and_sov_pack_namespaces_are_unique(self):
        decks = load_default_multi_decks()
        for cfg_name, categories in decks.items():
            with self.subTest(cfg_name=cfg_name):
                namespaces = [entry_to_pack_namespace(entry) for entry in flatten_categories(categories)]
                self.assertEqual(len(namespaces), len(set(namespaces)))

    def test_resolve_default_deck_pack_reference_skips_deck_pack_modifications(self):
        namespace = "Descriptor_Deck_Pack_M1IP_Abrams_US_1_1"
        game_db = {
            "deck_pack_mappings": {
                "deck_pack_modifications": {
                    namespace: "Descriptor_Deck_Pack_M1IP_Abrams_US_3_3",
                },
                "reference_mappings": {},
            },
        }
        self.assertEqual(
            resolve_default_deck_pack_reference(namespace, game_db),
            namespace,
        )

    def test_resolve_default_deck_pack_reference_skips_command_unit_renames(self):
        namespace = "Descriptor_Deck_Pack_M1025_Humvee_CMD_US_1_1"
        renamed = "Descriptor_Deck_Pack_M1025_Humvee_CMD2_US_1_1"
        game_db = {
            "deck_pack_mappings": {
                "deck_pack_modifications": {},
                "reference_mappings": {namespace: renamed},
            },
        }
        self.assertEqual(resolve_default_deck_pack_reference(namespace, game_db), namespace)

    def test_multi_deck_pack_number_constant(self):
        self.assertEqual(MULTI_DECK_PACK_NUMBER, 1)


if __name__ == "__main__":
    unittest.main()
