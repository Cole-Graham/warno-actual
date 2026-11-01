"""Add countries to UISpecificCountriesInfos.ndf."""

from src.constants.ui.countries import COUNTRIES_TO_ADD
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import find_obj_by_type

logger = setup_logger(__name__)


def edit_gen_ui_uispecificcountriesinfos(source_path) -> None:
    """GameData/Generated/UserInterface/UISpecificCountriesInfos.ndf

    Deck creation looks up CountryId in TUISpecificCountriesInfos. Each row in
    COUNTRIES_TO_ADD is cloned from its donor when that country key is absent.
    """
    logger.info("Adding countries to UISpecificCountriesInfos.ndf")
    # Country filter labels resolve NameToken through dico_interface_outgame.
    # DivisionName tokens such as NSWPALLNME stay in UNITS.csv (dico_units).
    write_dictionary_entries(
        [(country["name_token"], country["display"]) for country in COUNTRIES_TO_ADD],
        dictionary_type="outgame",
    )

    countries = find_obj_by_type(source_path, "TUISpecificCountriesInfos")
    texture_bank = find_obj_by_type(source_path, "TBUCKToolAdditionalTextureBank")
    if countries is None or texture_bank is None:
        logger.error("TUISpecificCountriesInfos or its texture bank was not found")
        return

    countries_map = countries.v.by_m("CountriesInfos").v
    textures = texture_bank.v.by_m("Textures").v
    text_formats = source_path.by_n("CountriesTextFormatScriptMap").v

    for country in COUNTRIES_TO_ADD:
        country_id = country["country_id"]
        donor_id = country["donor"]
        country_key = f'"{country_id}"'
        donor_key = f'"{donor_id}"'
        texture_key = f'"{country["flag_texture"]}"'

        if countries_map.by_k(country_key, False) is None:
            entry = countries_map.by_k(donor_key).copy()
            entry.k = country_key
            entry.v.by_m("FlagTexture").v = texture_key
            entry.v.by_m("Country").v = country_key
            entry.v.by_m("NameToken").v = f'"{country["name_token"]}"'
            entry.v.by_m("Coalition").v = f"TWargameCoalition/{country['coalition']}"
            countries_map.add(entry)
            logger.info(f"Added {country_id} country entry cloned from {donor_id}")
        else:
            logger.info(f"{country_id} country entry already present")

        if textures.by_k(texture_key, False) is None:
            texture = textures.by_k(
                f'"CommonTexture_MotherCountryFlag_{donor_id}"'
            ).copy()
            texture.k = texture_key
            texture.v.by_k("~/ComponentState/Normal").v.by_m("FileName").v = (
                f'"{country["flag_file"]}"'
            )
            textures.add(texture)
            logger.info(f"Registered {country_id} flag texture {country['flag_file']}")
        else:
            logger.info(f"{country_id} flag texture already present")

        if text_formats.by_k(country_key, False) is None:
            flag = text_formats.by_k(donor_key).copy()
            flag.k = country_key
            flag.v.by_m("TextureToken").v = texture_key
            text_formats.add(flag)
            logger.info(f"Added {country_id} text-format flag")
        else:
            logger.info(f"{country_id} text-format flag already present")
