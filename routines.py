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
    LeftCalfRaises,
    RightCalfRaises,
    SquatPulses,
    StandingObliqueCrunches,
    ClamShells,
    ToySoldiers,
    BandedSumoWalk,
    FigureFours,
    SeatedMarches,
    SitToStand,
    FounderSequences,
    StepDowns,
    StandingSkaters,
    HamstringStretchesWithStrap,
    TRXSquats,
    HeelRaises,
    BirdDogs,
    LowTrapeziusRows,
    MidTrapeziusRows,
    SingleLegBalance,
    SLSWobbleCushion,
    UlnarNerveGlide,
    SupineNods,
    SegmentalThoracicFoamRoll,
    NeckStretch,
    DoorwayPecStretch,
    UpperTrapeziusMFR,
    LevatorScapulaART,
    RhomboidMFR,
    ThoracicExtension,
    ExternalRotationWithBand,
    RowWithTheraband,
    ScapularRetraction,
    StrengtheningExternalRotation,
    StrengtheningInternalRotation,
    BandPullApartPalmsUp,
    RowWithRotation,
    ShoulderStabilizationAbduction,
    ShoulderFlexionAbduction,
    ActiveShoulderProtraction,
    ScapularProtraction,
    ChinTuck,
    SnowAngels,
    StretchingSideBending,
    KneelingLatPullDownWithBand,
    LatPullDownWithBand,
    AnkleDorsiflexionWithBand,
    DorsiflexionWithBand,
    EversionWithBand,
    ResistedEversion,
    HamstringAndCalfStretch,
    LongSittingGastrocStretch,
    Bookends,
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
    ClamShells(1),
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

    UpperTrapeziusMFR(1),
    LevatorScapulaART(1),
    RhomboidMFR(1),
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

PHYSIO_CUSTOM = (

    Warmup(0.5),

    Squats(1.0),
    FounderSequences(1.0),
    BandedSumoWalk(1.5),

    Rest(0.3),

    LeftCalfRaises(1.0),
    RightCalfRaises(1.0),
    FigureFours(1.0),

    Rest(0.3),

    ToySoldiers(1.0),
    SeatedMarches(1.5),

    Rest(0.3),

    HamstringStretchesWithStrap(1.5),
    SegmentalThoracicFoamRoll(2.0),
    SLSWobbleCushion(2.0),
)

PHYSIO_SHOULDER = (
    DoorwayPecStretch(1.0),
    ThoracicExtension(1.0),
    ExternalRotationWithBand(1.0),
    RowWithTheraband(1.0),

    Rest(0.3),

    ScapularRetraction(1.0),
    StrengtheningExternalRotation(1.0),
    StrengtheningInternalRotation(1.0),

    Rest(0.3),

    BandPullApartPalmsUp(1.0),
    RowWithRotation(1.0),
    ShoulderStabilizationAbduction(1.0),

    Rest(0.3),

    ShoulderFlexionAbduction(1.0),
    ActiveShoulderProtraction(1.0),
    ScapularProtraction(1.0),

    Rest(0.3),

    ChinTuck(1.0),
    SnowAngels(1.0),
)

PHYSIO_COMBINED = (

    Warmup(0.5),

    SingleLegBalance(1.5),
    Squats(1.0),
    FounderSequences(1.0),
    BandedSumoWalk(1.5),

    Rest(0.3),

    FigureFours(1.0),
    SupineNods(1.0),
    ClamShells(1.0),

    Rest(0.3),

    ToySoldiers(1.0),
    SeatedMarches(1.5),
    WallSits(1.0),
    WallSitsOnToes(1.0),
    WallSitsOnToesHeelsIn(1.0),

    Rest(0.3),

    HamstringStretchesWithStrap(1.5),
    BirdDogs(1.5),
    SegmentalThoracicFoamRoll(2.0),
    SLSWobbleCushion(2.0),
)

PHYSIO_NECK = (

    Warmup(0.5),

    StretchingSideBending(1),
    ChinTuck(1.0),
    SupineNods(1),
    Bookends(1),

    Rest(0.3),

    ExternalRotationWithBand(1.0),
    BandPullApartPalmsUp(1.0),
    RowWithTheraband(1.0),

    Rest(0.3),

    KneelingLatPullDownWithBand(1),
    LatPullDownWithBand(1),
)

PHYSIO_ANKLE = (

    Warmup(0.5),

    HamstringAndCalfStretch(1),
    LongSittingGastrocStretch(1),

    Rest(0.3),

    AnkleDorsiflexionWithBand(1),
    DorsiflexionWithBand(1),

    Rest(0.3),

    EversionWithBand(1),
    ResistedEversion(1),
)

STRETCHES = (
    Warmup(0.5),
    # TODO: put some good/the right stretches in here
    FigureFours(1.0),
    HamstringStretchesWithStrap(1.5),
    DoorwayPecStretch(1.0),
    NeckStretch(1.0),
)

BEEFCAKE = (
    Warmup(1),

    JumpingJacks(1),
    Pushups(1),
    ChairDips(1),

    Rest(0.3),

    FigureFours(1.0),
    LegRaises(1),
    CalfRaises(1),

    Rest(0.3),

    WallSits(1.0),
    WallSitsOnToes(1.0),
    WallSitsOnToesHeelsIn(1.0),

    Rest(0.3),

    Squats(1),
    Lunges(1),
    ClamShells(1),

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
