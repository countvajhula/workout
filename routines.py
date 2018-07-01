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
    WallSits,
    WallSitsOnToes,
    WallSitsOnToesHeelsIn,
    CalfRaises,
    RightCalfRaises,
    LeftCalfRaises,
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
    JumpingJacks,
    Pushups,
    Squats,
    Planks,
    Crunches,
    ChairDips,
    Bicycles,
    Lunges,
    FireHydrants,
    WallSits,
    CalfRaises,
)

ABS = (
    Planks,
    LeftSidePlanks,
    RightSidePlanks,
    Crunches,
    Bicycles,
)

GLUTES = (
    Squats,
    Lunges,
    LeftFireHydrants,
    RightFireHydrants,
)

CORE = ABS + GLUTES

PHYSIO = (
    LeftLegRaises,
    RightLegRaises,
    WallSits,
    WallSitsOnToes,
    WallSitsOnToesHeelsIn,
)
