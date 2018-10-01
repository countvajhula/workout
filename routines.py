from activities import (
    JumpingJacks,
    Pushups,
    Squats,
    Planks,
    LeftSidePlanks,
    RightSidePlanks,
    Crunches,
    ChairDips,
    Bicycles,
    Lunges,
    FireHydrants,
    LeftFireHydrants,
    RightFireHydrants,
    LegRaises,
    LeftLegRaises,
    RightLegRaises,
    TableLeftLegRaises,
    TableRightLegRaises,
    TableLeftLegHighRaises,
    TableRightLegHighRaises,
    WallSits,
    WallSitsOnToes,
    WallSitsOnToesHeelsIn,
    CalfRaises,
    RightCalfRaises,
    LeftCalfRaises,
    SquatPulses,
    StandingObliqueCrunches,
    ClamShells,
    ToySoldiers,
    FigureFours,
    SeatedMarches,
    SitToStand,
    HamstringStretchesWithStrap,
    BandedSumoWalk,
    NeckStretch,
    HeelRaises,
    StepDowns,
    SingleLegBalance,
    LowTrapeziusRows,
    MidTrapeziusRows,
    BirdDogs,
    SupineNods,
    SegmentalThoracicFoamRoll,
    DoorwayPecStretch,
    UlnarNerveGlide,
    FounderSequences,
    SLSWobbleCushion,
    Warmup,
    Rest,
)

# core, glutes, quads, calves, cardio, upper body, yoga, stretches, physio

GENERAL = (
    Warmup(1),

    JumpingJacks(1),
    Pushups(1),
    Squats(1),

    Rest(0.3),

    Planks(1),
    Crunches(1),
    ChairDips(1),

    Rest(0.3),

    Bicycles(1),
    Lunges(1),
    FireHydrants(1),

    Rest(0.3),

    WallSits(1),
    LegRaises(1),
    CalfRaises(1),
)

BASIC = (
    JumpingJacks(1),
    Pushups(1),
    Squats(1),
    Planks(1),
    Crunches(1),
    ChairDips(1),
    Bicycles(1),
    Lunges(1),
    FireHydrants(1),
    WallSits(1),
    CalfRaises(1),
)

ABS = (
    Warmup(1),

    StandingObliqueCrunches(1.5),

    Rest(0.3),

    Planks(1),
    LeftSidePlanks(1),
    RightSidePlanks(1),

    Rest(0.3),

    Crunches(1),
    Bicycles(1),
)

GLUTES = (
    Squats(1),
    Lunges(1),
    LeftFireHydrants(1),
    RightFireHydrants(1),
    TableLeftLegRaises(1),
    TableRightLegRaises(1),
    TableLeftLegHighRaises(1),
    TableRightLegHighRaises(1),
)

# CORE = ABS + GLUTES
CORE = (
    Warmup(1),

    Squats(1),
    Lunges(1),
    StandingObliqueCrunches(1),

    Rest(0.3),

    Planks(1),
    LeftSidePlanks(1),
    RightSidePlanks(1),

    Rest(0.3),

    LeftFireHydrants(1),
    RightFireHydrants(1),
    TableLeftLegRaises(1),
    TableRightLegRaises(1),
    TableLeftLegHighRaises(1),
    TableRightLegHighRaises(1),

    Rest(0.3),

    Crunches(1),
    Bicycles(1),
)

PHYSIO_KNEES = (
    ToySoldiers(1),
    SquatPulses(1),
    ClamShells(1),
    HamstringStretchesWithStrap(1),

    Rest(0.3),

    SeatedMarches(1.5),
    LeftLegRaises(1.5),
    RightLegRaises(1.5),

    Rest(0.3),

    SitToStand(1),
    Squats(1),
    BandedSumoWalk(1),
    FigureFours(1.5),

    Rest(0.3),

    WallSits(1),
    WallSitsOnToes(1),
    WallSitsOnToesHeelsIn(1),
)

PHYSIO_BACK_AND_NECK = (
    NeckStretch(1),
    DoorwayPecStretch(1),
    UlnarNerveGlide(1),
    FounderSequences(1),

    Rest(0.3),

    BirdDogs(1.5),
    SupineNods(1),
    SegmentalThoracicFoamRoll(1),

    Rest(0.3),

    Squats(1),
    LowTrapeziusRows(1),
    MidTrapeziusRows(1),

    Rest(0.3),

)

PHYSIO_BALANCE = (
    SingleLegBalance(1.5),

    Rest(0.3),

    SLSWobbleCushion(1.5),

    Rest(0.3),

    StepDowns(1.5),

    Rest(0.3),

    HeelRaises(1.5),
)
