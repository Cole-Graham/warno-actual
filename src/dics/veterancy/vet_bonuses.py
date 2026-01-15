"""Experience level data constants."""

VETERANCY_BONUSES = {
    "simple_v3": {
        "simple_v3_0": {
            "body_token": "SGZVNLTRKE",
            "body": (
                '#style1{- Accuracy: normal}'
                '\n#style1{- Aiming time: normal}'
                '\n#style1{- Reload time: normal}'
                '\n#style1{- Stress resistance: normal}'
                '\n#style1{- Stress recovery: 1.6 per second}'
                '\n(flat, multiplicative, multiplicative, percentage)'
            ),
        },
        "simple_v3_1": {
            "body_token": "UGNZEELGTC",
            "body": (
                '#style1{- Accuracy:} #moral_color_bad_2{+5%}'
                '\n#style1{- Aiming time:} #moral_color_bad_2{-4%}'
                '\n#style1{- Reload time:} #moral_color_bad_2{-10%}'
                '\n#style1{- Stress resistance:} #moral_color_bad_2{+14%}'
                '\n#style1{- Stress recovery:} #moral_color_bad_2{4.0} #style1{per second}'
                '\n(flat, multiplicative, multiplicative, percentage)'
            ),
        },
        "simple_v3_2": {
            "body_token": "KUJQCFUCWY",
            "body": (
                '#style1{- Accuracy:} #styleGreen{+10%}'
                '\n#style1{- Aiming time:} #styleGreen{-8%}'
                '\n#style1{- Reload time:} #styleGreen{-17%}'
                '\n#style1{- Stress resistance:} #styleGreen{+22%}'
                '\n#style1{- Stress recovery:} #styleGreen{4.8} #style1{per second}'
                '\n(flat, multiplicative, multiplicative, percentage)'
            ),
        },
        "simple_v3_3": {
            "body_token": "SZISEJDYHF",
            "body": (
                '#style1{- Accuracy:} #styleTurquoise{+15%}'
                '\n#style1{- Aiming time:} #styleTurquoise{-12%}'
                '\n#style1{- Reload time:} #styleTurquoise{-24%}'
                '\n#style1{- Stress resistance:} #styleTurquoise{+32%}'
                '\n#style1{- Stress recovery:} #styleTurquoise{5.4} #style1{per second}'
                '\n(flat, multiplicative, multiplicative, percentage)'
            ),
        },
    },
    "simple_v3_multiplicative": {
        "simple_v3_multiplicative_0": {
            "body_token": "YBXGZUCPGW",
            "body": (
                '#style1{- Accuracy: normal}'
                '\n#style1{- Aiming time: normal}'
                '\n#style1{- Reload time: normal}'
                '\n#style1{- Stress resistance: normal}'
                '\n#style1{- Stress recovery: 1.6 per second}'
            ),
        },
        "simple_v3_multiplicative_1": {
            "body_token": "OZELGDYCJI",
            "body": (
                '#style1{- Accuracy:} #moral_color_bad_2{+5%}'
                '\n#style1{- Aiming time:} #moral_color_bad_2{-4%}'
                '\n#style1{- Reload time:} #moral_color_bad_2{-10%}'
                '\n#style1{- Stress resistance:} #moral_color_bad_2{+14%}'
                '\n#style1{- Stress recovery:} #moral_color_bad_2{4.0} #style1{per second}'
                '\n(multiplicative, multiplicative, multiplicative, percentage)'
            ),
        },
        "simple_v3_multiplicative_2": {
            "body_token": "KODCDSFEDT",
            "body": (
                '#style1{- Accuracy:} #styleGreen{+10%}'
                '\n#style1{- Aiming time:} #styleGreen{-8%}'
                '\n#style1{- Reload time:} #styleGreen{-17%}'
                '\n#style1{- Stress resistance:} #styleGreen{+22%}'
                '\n#style1{- Stress recovery:} #styleGreen{4.8} #style1{per second}'
                '\n(multiplicative, multiplicative, multiplicative, percentage)'
            ),
        },
        "simple_v3_multiplicative_3": {
            "body_token": "GQBPUEGUYF",
            "body": (
                '#style1{- Accuracy:} #styleTurquoise{+15%}'
                '\n#style1{- Aiming time:} #styleTurquoise{-12%}'
                '\n#style1{- Reload time:} #styleTurquoise{-24%}'
                '\n#style1{- Stress resistance:} #styleTurquoise{+32%}'
                '\n#style1{- Stress recovery:} #styleTurquoise{5.4} #style1{per second}'
                '\n(multiplicative, multiplicative, multiplicative, percentage)'
            ),
        },
    },
    "SF_v2": {
        "SF_v2_0": {
            "body_token": "FSDWIVSTQO",
            "body": (
                '#style1{- Movement speed: normal}'
                '\n#style1{- Accuracy: normal}'
                '\n#style1{- Aiming time: normal}'
                '\n#style1{- Reload Time: normal}'
                '\n#style1{- Stress resistance: normal}'
                '\n#style1{- Stress recovery: 2.0 per second}'
            ),
        },
        "SF_v2_1": {
            "body_token": "BTMBWVRSDH",
            "body": (
                '#style1{- Movement speed:} #styleGreen{+10%}'
                '\n#style1{- Accuracy:} #moral_color_bad_2{+8%}'
                '\n#style1{- Aiming time:} #moral_color_bad_2{-10%}'
                '\n#style1{- Reload time:} #moral_color_bad_2{-10%}'
                '\n#style1{- Stress resistance:} #moral_color_bad_2{+20%}'
                '\n#style1{- Stress recovery:} #moral_color_bad_2{4.8} #style1{per second}'
                '\n(percentage, flat, multiplicative, multiplicative, percentage)'
            ),
        },
        "SF_v2_2": {
            "body_token": "JHQIIEVPZF",
            "body": (
                '#style1{- Movement speed:} #styleGreen{+20%}'
                '\n#style1{- Accuracy:} #styleGreen{+12%}'
                '\n#style1{- Aiming time:} #styleGreen{-20%}'
                '\n#style1{- Reload time:} #styleGreen{-20%}'
                '\n#style1{- Stress resistance:} #styleGreen{+30%}'
                '\n#style1{- Stress recovery:} #styleGreen{6.0} #style1{per second}'
                '\n(percentage, flat, multiplicative, multiplicative, percentage)'
            ),
        },
        "SF_v2_3": {
            "body_token": "ZIUCSNONPU",
            "body": (
                '#style1{- Movement speed:} #styleTurquoise{+30%}'
                '\n#style1{- Accuracy:} #styleTurquoise{+16%}'
                '\n#style1{- Aiming time:} #styleTurquoise{-30%}'
                '\n#style1{- Reload time:} #styleTurquoise{-30%}'
                '\n#style1{- Stress resistance:} #styleTurquoise{+40%}'
                '\n#style1{- Stress recovery:} #styleTurquoise{7.8} #style1{per second}'
                '\n(percentage, flat, multiplicative, multiplicative, percentage)'
            ),
        },
    },
    "SF_v2_multiplicative": {
        "SF_v2_multiplicative_0": {
            "body_token": "OIKXZUZCBK",
            "body": (
                '#style1{- Movement speed: normal}'
                '\n#style1{- Accuracy: normal}'
                '\n#style1{- Aiming time: normal}'
                '\n#style1{- Reload Time: normal}'
                '\n#style1{- Stress resistance: normal}'
                '\n#style1{- Stress recovery: 2.0 per second}'
            ),
        },
        "SF_v2_multiplicative_1": {
            "body_token": "OPCTRVJHFT",
            "body": (
                '#style1{- Movement speed:} #styleGreen{+10%}'
                '\n#style1{- Accuracy:} #moral_color_bad_2{+8%}'
                '\n#style1{- Aiming time:} #moral_color_bad_2{-10%}'
                '\n#style1{- Reload time:} #moral_color_bad_2{-10%}'
                '\n#style1{- Stress resistance:} #moral_color_bad_2{+20%}'
                '\n#style1{- Stress recovery:} #moral_color_bad_2{4.8} #style1{per second}'
                '\n(percentage, multiplicative, multiplicative, multiplicative, percentage)'
            ),
        },
        "SF_v2_multiplicative_2": {
            "body_token": "KMDMZPBWMO",
            "body": (
                '#style1{- Movement speed:} #styleGreen{+20%}'
                '\n#style1{- Accuracy:} #styleGreen{+12%}'
                '\n#style1{- Aiming time:} #styleGreen{-20%}'
                '\n#style1{- Reload time:} #styleGreen{-20%}'
                '\n#style1{- Stress resistance:} #styleGreen{+30%}'
                '\n#style1{- Stress recovery:} #styleGreen{6.0} #style1{per second}'
                '\n(percentage, multiplicative, multiplicative, multiplicative, percentage)'
            ),
        },
        "SF_v2_multiplicative_3": {
            "body_token": "UOHDGZDXIE",
            "body": (
                '#style1{- Movement speed:} #styleTurquoise{+30%}'
                '\n#style1{- Accuracy:} #styleTurquoise{+16%}'
                '\n#style1{- Aiming time:} #styleTurquoise{-30%}'
                '\n#style1{- Reload time:} #styleTurquoise{-30%}'
                '\n#style1{- Stress resistance:} #styleTurquoise{+40%}'
                '\n#style1{- Stress recovery:} #styleTurquoise{7.8} #style1{per second}'
                '\n(percentage, multiplicative, multiplicative, multiplicative, percentage)'
            ),
        },
    },
    "artillery": {
        "artillery_0": {
            "body_token": "NWAXFLCAIU",
            "body": (
                '#style1{- Accuracy: normal}'
                '\n#style1{- Aiming time: normal}'
                '\n#style1{- Reload time: normal}'
                '\n#style1{- Stress resistance: normal}'
                '\n#style1{- Stress recovery: 1.6 per second}'
            ),
        },
        "artillery_1": {
            "body_token": "SZTBFODBVW",
            "body": (
                '#style1{- Accuracy:} #moral_color_bad_2{+6%}'
                '\n#style1{- Aiming time:} #moral_color_bad_2{-15%}'
                '\n#style1{- Reload time:} #moral_color_bad_2{-20%}'
                '\n#style1{- Stress resistance:} #moral_color_bad_2{+6%}'
                '\n#style1{- Stress recovery:} #moral_color_bad_2{3.0} #style1{per second}'
                '\n(flat, multiplicative, multiplicative, percentage)'
            ),
        },
        "artillery_2": {
            "body_token": "YZGZLNRVWU",
            "body": (
                '#style1{- Accuracy:} #styleGreen{+12%}'
                '\n#style1{- Aiming time:} #styleGreen{-30%}'
                '\n#style1{- Reload time:} #styleGreen{-40%}'
                '\n#style1{- Stress resistance:} #styleGreen{+12%}'
                '\n#style1{- Stress recovery:} #styleGreen{3.8} #style1{per second}'
                '\n(flat, multiplicative, multiplicative, percentage)'
            ),
        },
        "artillery_3": {
            "body_token": "UQNUCMTWOZ",
            "body": (
                '#style1{- Accuracy:} #styleTurquoise{+16%}'
                '\n#style1{- Aiming time:} #styleTurquoise{-45%}'
                '\n#style1{- Reload time:} #styleTurquoise{-60%}'
                '\n#style1{- Stress resistance:} #styleTurquoise{+24%}'
                '\n#style1{- Stress recovery:} #styleTurquoise{4.6} #style1{per second}'
                '\n(flat, multiplicative, multiplicative, percentage)'
            ),
        },
    },
    "helico": {
        "helico_0": {
            "body_token": "CCPVCWPZKZ",
            "body": (
                '#style1{- Precision: normal}'
                '\n#style1{- Aiming time: normal}'
                '\n#style1{- Stress resistance: normal}'
                '\n#style1{- Stress recovery: 1.6 per second}'
            ),
        },
        "helico_1": {
            "body_token": "NSWPFSVOYP",
            "body": (
                '#style1{- Precision: normal}'
                '\n#style1{- Aiming time:} #moral_color_bad_2{-20%}'
                '\n#style1{- Stress resistance: normal}'
                '\n#style1{- Stress recovery:} #moral_color_bad_2{4.2} #style1{per second}'
                '\n(multiplicative)'
            ),
        },
        "helico_2": {
            "body_token": "ETUVQWYSIR",
            "body": (
                '#style1{- Precision:} #styleGreen{+8%}'
                '\n#style1{- Aiming time:} #styleGreen{-40%}'
                '\n#style1{- Stress resistance:} #styleGreen{+25%}'
                '\n#style1{- Stress recovery:} #styleGreen{6.2} #style1{per second}'
                '\n(flat, multiplicative, percentage)'
            ),
        },
        "helico_3": {
            "body_token": "BQBYGPLFJC",
            "body": (
                '#style1{- Precision:} #styleTurquoise{+16%}'
                '\n#style1{- Aiming time:} #styleTurquoise{-60%}'
                '\n#style1{- Stress resistance:} #styleTurquoise{+45%}'
                '\n#style1{- Stress recovery:} #styleTurquoise{8.4} #style1{per second}'
                '\n#style1{- Evasion:} #styleTurquoise{+5%}'
                '\n(flat, multiplicative, percentage)'
            ),
        },
    },
    "avion": {
        "avion_0": {
            "body_token": "LNZBFCYAIE",
            "body": (
                '#style1{- Accuracy: normal}'
                '\n#style1{- Aiming time: normal}'
                '\n#style1{- Stress resistance: normal}'
                '\n#style1{- Stress recovery: normal}'
                '\n#style1{- Evasive maneuvers: normal}'
            ),
        },
        "avion_1": {
            "body_token": "NMDXSJVEMU",
            "body": (
                '#style1{- Accuracy: normal}'
                '\n#style1{- Aiming time: normal}'
                '\n#style1{- Stress resistance: normal}'
                '\n#style1{- Stress recovery:} #moral_color_bad_2{2.2} #style1{per second}'
                '\n#style1{- Evasive maneuvers: normal}'
            ),
        },
        "avion_2": {
            "body_token": "ZCKHBWOUCJ",
            "body": (
                '#style1{- Accuracy:} #styleGreen{+4%}'
                '\n#style1{- Aiming time:} #styleGreen{-10%}'
                '\n#style1{- Stress resistance:} #styleGreen{+20%}'
                '\n#style1{- Stress recovery:} #styleGreen{4.2} #style1{per second}'
                '\n#style1{- Evasive maneuvers:} #styleGreen{+4%}'
                '\n(flat, multiplicative, percentage, flat)'
            ),
        },
        "avion_3": {
            "body_token": "KRMIXGZVQU",
            "body": (
                '#style1{- Accuracy:} #styleTurquoise{+8%}'
                '\n#style1{- Aiming time:} #styleTurquoise{-20%}'
                '\n#style1{- Stress resistance:} #styleTurquoise{+40%}'
                '\n#style1{- Stress recovery:} #styleTurquoise{6.2} #style1{per second}'
                '\n#style1{- Evasive maneuvers:} #styleTurquoise{+8%}'
                '\n(flat, multiplicative, percentage, flat)'
            ),
        },
    },
}
