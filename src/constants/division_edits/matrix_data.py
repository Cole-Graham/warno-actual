"""Division matrix constants for DivisionCostMatrix.ndf"""

# In order to optimize for balance in veterancy choices, the "length" and "height" of
# categories has been adjusted. The length being the number of cards in each category,
# and the height being the base availability of each card in that category. 
#
# Example 1: In order to increase the accessibiltiy and availability of "line" infantry
# in WARNO, the average number of cards in the infantry category has been increased 
# along with the base availability of each card. This also achieves the goal of
# increasing the variety of infantry units you can take in a deck at one time.
#
# Example 2: On the other hand, the Tank tab has less cards on average, while increasing
# base availability. The overally quantity of tanks in vanilla WARNO is about right,
# but the base availability was so low that it didn't leave any room to balance the
# veterancy choices in terms of the # of tanks you get when upvetting.
#
# The rate at which the cost of each card increases also varies, depending on the
# category. For example, each additional card of planes tends to increase the overall
# viability of heavy air play, and thus plane cards become expensive faster than 
# other categories. In contrast, each additional card of tanks only adds value in terms
# of flexibility for the player because its rare to see a player consume an entire tab
# of tanks in a single match. 

# NEW MATRICES DIC IS WIP (we need an actual python dictionary for validation purposes)
DIVISION_MATRICES_NEW = {
    "US_3rd_Arm_multi": {
        "EFactory/Art": [2, 3, 4, 5, 6],
        "EFactory/DCA": [2, 2, 4, 4, 4],
        "EFactory/Defense": [],
        "EFactory/Helis": [2, 2, 3, 4, 5],
        "EFactory/Infantry": [2, 2, 2, 2, 2, 3, 4, 5],
        "EFactory/Logistic": [2, 2, 2, 2, 2, 2, 2, 3, 3],
        "EFactory/Planes": [2, 2, 4, 5, 6, 8],
        "EFactory/Recons": [2, 2, 2, 2, 3, 3, 4],
        "EFactory/Tanks": [2, 2, 2, 2, 2, 2, 3, 3],
    },
}

DIVISION_MATRICES = {
    "MatrixCostName_US_3rd_Arm_multi": (
        'MatrixCostName_US_3rd_Arm_multi is MAP'
        '['
        '    (EFactory/Art, [2, 3, 4, 5, 6]),'
        '    (EFactory/DCA, [2, 2, 4, 4, 4]),'
        '    (EFactory/Defense, []),'
        '    (EFactory/Helis, [2, 2, 3, 4, 5]),'
        '    (EFactory/Infantry, [2, 2, 2, 2, 2, 3, 4, 5]),'
        '    (EFactory/Logistic, [2, 2, 2, 2, 2, 2, 2, 3, 3]),'
        '    (EFactory/Planes, [2, 2, 4, 5, 6, 8]),'
        '    (EFactory/Recons, [2, 2, 2, 2, 3, 3, 4]),'
        '    (EFactory/Tanks, [2, 2, 2, 2, 2, 2, 3, 3]),'
        ']'
    ),

    "MatrixCostName_US_8th_Inf_multi": (
        'MatrixCostName_US_8th_Inf_multi is MAP'
        '['
        '    (EFactory/Art, [2, 2, 4, 4, 6]),'
        '    (EFactory/DCA, [2, 2, 4, 4, 4]),'
        '    (EFactory/Defense, []),'
        '    (EFactory/Helis, [2, 2, 4, 4]),'
        '    (EFactory/Infantry, [2, 2, 2, 2, 2, 2, 3, 4, 4, 4, 5]),'
        '    (EFactory/Logistic, [2, 2, 2, 2, 2, 2, 3, 3, 3]),'
        '    (EFactory/Planes, [2, 2, 4, 5, 6, 8]),'
        '    (EFactory/Recons, [2, 2, 2, 3, 3, 3]),'
        '    (EFactory/Tanks, [2, 2, 2, 3, 3]),'
        ']'
    ),

    "MatrixCostName_US_82nd_Airborne_multi": (
        'MatrixCostName_US_82nd_Airborne_multi is MAP'
        '['
        '    (EFactory/Art, [2, 2, 4, 4]),'
        '    (EFactory/DCA, [2, 2, 3, 4, 4]),'
        '    (EFactory/Defense, []),'
        '    (EFactory/Helis, [2, 2, 3, 4, 4, 4]),'
        '    (EFactory/Infantry, [2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4]),'
        '    (EFactory/Logistic, [2, 2, 2, 2, 2, 2, 3, 3]),'
        '    (EFactory/Planes, [2, 2, 3, 3, 4, 6, 8]),'
        '    (EFactory/Recons, [2, 2, 2, 3, 3, 3, 3]),'
        '    (EFactory/Tanks, [2, 2, 3, 3]),'
        ']'
    ),

    "MatrixCostName_UK_2nd_Infantry_multi": (
        'MatrixCostName_UK_2nd_Infantry_multi is MAP'
        '['
        '    (EFactory/Art, [2, 2, 4, 4, 6]),'
        '    (EFactory/DCA, [2, 2, 3, 4, 4]),'
        '    (EFactory/Defense, []),'
        '    (EFactory/Helis, [2, 2, 3, 3, 4]),'
        '    (EFactory/Infantry, [2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4]),'
        '    (EFactory/Logistic, [2, 2, 2, 2, 2, 3, 3]),'
        '    (EFactory/Planes, [2, 2, 3, 5, 5, 7]),'
        '    (EFactory/Recons, [2, 2, 2, 2, 2, 2, 2]),'
        '    (EFactory/Tanks, [2, 2, 3, 3, 3]),'
        ']'
    ),

    "MatrixCostName_US_101st_Airmobile_multi": (
        'MatrixCostName_US_101st_Airmobile_multi is MAP'
        '['
        '    (EFactory/Art, [2, 2, 2, 2, 4, 4]),'
        '    (EFactory/DCA, [2, 3, 5, 5, 5]),'
        '    (EFactory/Defense, []),'
        '    (EFactory/Helis, [2, 2, 2, 3, 3, 4, 4, 4]),'
        '    (EFactory/Infantry, [2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4]),'
        '    (EFactory/Logistic, [2, 2, 2, 2, 2, 2, 3]),'
        '    (EFactory/Planes, [2, 2, 4, 5, 6, 6]),'
        '    (EFactory/Recons, [2, 2, 2, 3, 3, 3, 3]),'
        '    (EFactory/Tanks, [4, 4, 6, 6]),'
        ']'
    ),
    
    "MatrixCostName_RFA_TerrKo_Sud_multi": (
        'MatrixCostName_RFA_TerrKo_Sud_multi is MAP'
        '['
        '    (EFactory/Art, [2, 2, 4, 4, 5, 6]),'
        '    (EFactory/DCA, [2, 2, 3, 4, 5]),'
        '    (EFactory/Defense, []),'
        '    (EFactory/Helis, [2, 2, 3, 3, 4]),'
        '    (EFactory/Infantry, [2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4]),'
        '    (EFactory/Logistic, [2, 2, 2, 2, 2, 2, 2, 2, 3]),'
        '    (EFactory/Planes, [2, 2, 2, 4, 4, 5, 7]),'
        '    (EFactory/Recons, [2, 2, 2, 2, 3, 4]),'
        '    (EFactory/Tanks, [2, 2, 2, 3, 3]),'
        ']'
    ),

    "MatrixCostName_SOV_119IndTkBrig_multi": (                           
        'MatrixCostName_SOV_119IndTkBrig_multi is MAP'
        '['
        '    (EFactory/Art, [2, 2, 4, 4, 6]),'
        '    (EFactory/DCA, [2, 2, 4, 4]),'
        '    (EFactory/Defense, []),'
        '    (EFactory/Helis, [2, 2, 3, 4, 4, 4]),'
        '    (EFactory/Infantry, [2, 2, 2, 2, 3, 4, 4, 5]),'
        '    (EFactory/Logistic, [2, 2, 2, 2, 2, 2, 3, 3]),'
        '    (EFactory/Planes, [2, 2, 3, 4, 5, 5, 7, 7]),'
        '    (EFactory/Recons, [2, 2, 2, 2, 3, 3, 3, 3]),'
        '    (EFactory/Tanks, [2, 2, 2, 2, 2, 3, 3, 3]),'
        ']'
    ),

    "MatrixCostName_SOV_27_Gds_Rifle_multi": (
        'MatrixCostName_SOV_27_Gds_Rifle_multi is MAP'
        '['
        '    (EFactory/Art, [2, 2, 4, 4, 5, 6]),'
        '    (EFactory/DCA, [2, 2, 3, 3, 4, 4]),'
        '    (EFactory/Defense, []),'
        '    (EFactory/Helis, [2, 3, 4]),'
        '    (EFactory/Infantry, [2, 2, 2, 2, 2, 2, 2, 3, 4, 5]),'
        '    (EFactory/Logistic, [2, 2, 2, 2, 2, 2, 2, 3, 3, 3]),'
        '    (EFactory/Planes, [2, 2, 4, 5, 5, 7]),'
        '    (EFactory/Recons, [2, 2, 2, 4, 4, 4]),'
        '    (EFactory/Tanks, [2, 2, 3, 3, 3]),'
        ']'
    ),

    "MatrixCostName_SOV_76_VDV_multi": (
        'MatrixCostName_SOV_76_VDV_multi is MAP'
        '['
        '    (EFactory/Art, [2, 2, 4, 4, 6]),'
        '    (EFactory/DCA, [2, 2, 3, 4, 4]),'
        '    (EFactory/Defense, []),'
        '    (EFactory/Helis, []),'
        '    (EFactory/Infantry, [2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4]),'
        '    (EFactory/Logistic, [2, 2, 2, 2, 2, 2, 3, 3]),'
        '    (EFactory/Planes, [2, 2, 3, 3, 4, 5, 7, 8]),'
        '    (EFactory/Recons, [2, 2, 2, 2, 2, 2, 2, 2, 2]),'
        '    (EFactory/Tanks, [2, 2, 3, 3, 3, 3]),'
        ']'
    ),

    "MatrixCostName_RDA_7_Panzer_multi": (
        'MatrixCostName_RDA_7_Panzer_multi is MAP'
        '['
        '    (EFactory/Art, [2, 2, 4, 4, 5, 6]),'
        '    (EFactory/DCA, [2, 2, 4, 4, 6]),'
        '    (EFactory/Defense, []),'
        '    (EFactory/Helis, [2, 2, 3, 4]),'
        '    (EFactory/Infantry, [2, 2, 2, 2, 2, 3, 4, 5]),'
        '    (EFactory/Logistic, [2, 2, 2, 2, 2, 2, 2, 3, 3]),'
        '    (EFactory/Planes, [2, 2, 4, 4, 5, 7]),'
        '    (EFactory/Recons, [2, 2, 2, 2, 2, 2, 2]),'
        '    (EFactory/Tanks, [2, 2, 2, 2, 2, 2, 2, 3]),'
        ']'
    ),
    
    "MatrixCostName_RDA_KdA_Bezirk_Erfurt_multi": (
        'MatrixCostName_RDA_KdA_Bezirk_Erfurt_multi is MAP'
        '['
        '    (EFactory/Art, [2, 2, 2, 4, 6, 6, 6]),'
        '    (EFactory/DCA, [2, 2, 3, 4, 5]),'
        '    (EFactory/Defense, []),'
        '    (EFactory/Helis, [2, 2, 3, 3, 4]),'
        '    (EFactory/Infantry, [2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4]),'
        '    (EFactory/Logistic, [2, 2, 2, 2, 2, 2, 2, 2, 3, 3]),'
        '    (EFactory/Planes, [2, 2, 2, 4, 4, 5, 7]),'
        '    (EFactory/Recons, [2, 2, 2, 2, 3]),'
        '    (EFactory/Tanks, [2, 2, 2, 2, 3, 3]),'
        ']'
    ),

    "MatrixCostName_POL_20_Pancerna_multi": (
        'MatrixCostName_POL_20_Pancerna_multi is MAP'
        '['
        '    (EFactory/Art, [2, 2, 4, 4, 5, 6]),'
        '    (EFactory/DCA, [2, 2, 4, 4, 4]),'
        '    (EFactory/Defense, []),'
        '    (EFactory/Helis, [2, 4, 4]),'
        '    (EFactory/Infantry, [2, 2, 2, 2, 2, 3, 4, 5]),'
        '    (EFactory/Logistic, [2, 2, 2, 2, 2, 2, 2, 2, 3, 3]),'
        '    (EFactory/Planes, [2, 2, 4, 4, 5, 7]),'
        '    (EFactory/Recons, [2, 2, 2, 2, 2, 2, 3]),'
        '    (EFactory/Tanks, [2, 2, 2, 2, 2, 3, 3, 3]),'
        ']'
    ),
    
    "MatrixCostName_POL_4_Zmechanizowana_multi": (
        'MatrixCostName_POL_4_Zmechanizowana_multi is MAP'
        '['
        '    (EFactory/Art, [2, 3, 4, 4, 6]),'
        '    (EFactory/DCA, [2, 2, 4, 4, 4]),'
        '    (EFactory/Defense, []),'
        '    (EFactory/Helis, [2, 2, 3, 4, 5, 5]),'
        '    (EFactory/Infantry, [2, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5]),'
        '    (EFactory/Logistic, [2, 2, 2, 2, 2, 2, 2, 3, 3, 3]),'
        '    (EFactory/Planes, [2, 2, 3, 4, 5, 6]),'
        '    (EFactory/Recons, [2, 2, 2, 2, 2, 2, 2]),'
        '    (EFactory/Tanks, [2, 2, 2, 3, 3, 3]),'
        ']'
    ),
    
    "MatrixCostName_US_11ACR_multi": (
        'MatrixCostName_US_11ACR_multi is MAP'
        '['
        '    (EFactory/Art, [2, 3, 4, 6, 6]),'
        '    (EFactory/DCA, [2, 2, 3, 4, 5]),'
        '    (EFactory/Defense, []),'
        '    (EFactory/Helis, [2, 2, 2, 2, 3, 4]),'
        '    (EFactory/Infantry, [2, 2, 2, 2, 3, 4, 4, 5]),'
        '    (EFactory/Logistic, [2, 2, 2, 2, 2, 3, 3]),'
        '    (EFactory/Planes, [2, 2, 3, 4, 5, 6, 8]),'
        '    (EFactory/Recons, [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),'
        '    (EFactory/Tanks, [2, 2, 2, 2, 3, 3, 3, 3]),'
        ']'
    ),
    
    "MatrixCostName_FR_5e_Blindee_multi": (
        'MatrixCostName_FR_5e_Blindee_multi is MAP'
        '['
        '    (EFactory/Art, [2, 2, 4, 4, 4, 5]),'
        '    (EFactory/DCA, [2, 2, 3, 4, 4, 5]),'
        '    (EFactory/Defense, []),'
        '    (EFactory/Helis, [2, 3, 3, 3]),'
        '    (EFactory/Infantry, [2, 2, 2, 2, 3, 4, 4, 5]),'
        '    (EFactory/Logistic, [2, 2, 2, 2, 2, 2, 3, 3]),'
        '    (EFactory/Planes, [2, 2, 3, 5, 6, 6, 8]),'
        '    (EFactory/Recons, [2, 2, 2, 2, 3, 3, 4]),'
        '    (EFactory/Tanks, [2, 2, 2, 2, 2, 2, 3, 3]),'
        ']'
    ),
}
