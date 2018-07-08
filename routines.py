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
    Planks(1),
    LeftSidePlanks(1),
    RightSidePlanks(1),
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

CORE = ABS + GLUTES

PHYSIO = (
    LeftLegRaises(1),
    RightLegRaises(1),
    WallSits(1),
    WallSitsOnToes(1),
    WallSitsOnToesHeelsIn(1),
)
