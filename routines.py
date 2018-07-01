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
    Warmup,

    JumpingJacks,
    Pushups,
    Squats,

    Rest,

    Planks,
    Crunches,
    ChairDips,

    Rest,

    Bicycles,
    Lunges,
    FireHydrants,

    Rest,

    WallSits,
    LegRaises,
    CalfRaises,
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
