
# core, glutes, quads, calves, cardio, upper body, yoga, stretches, physio

WORKOUT = {
    'JUMPING JACKS': 1,
    'PUSH-UPS': 2,
    'SQUATS': 3,
    'PLANKS': 4,
    'LEFT SIDE PLANKS': 5,
    'RIGHT SIDE PLANKS': 6,
    'CRUNCHES': 7,
    'CHAIR DIPS': 8,
    'BICYCLES': 9,
    'LUNGES': 10,
    'FIRE HYDRANTS': 11,
    'LEFT FIRE HYDRANTS': 12,
    'RIGHT FIRE HYDRANTS': 13,
    'LEG RAISES': 14,
    'LEFT LEG RAISES': 15,
    'RIGHT LEG RAISES': 16,
    'WALL SITS': 17,
    'WALL SITS ON TOES': 18,
    'WALL SITS ON TOES HEELS IN': 19,
    'CALF RAISES': 20,
    'RIGHT CALF RAISES': 21,
    'LEFT CALF RAISES': 22,
}

WORKOUT_NAMES = {v: k for k, v in WORKOUT.items()}

FULL = WORKOUT.keys()

GENERAL = (
    WORKOUT['JUMPING JACKS'],
    WORKOUT['PUSH-UPS'],
    WORKOUT['SQUATS'],
    WORKOUT['PLANKS'],
    WORKOUT['CRUNCHES'],
    WORKOUT['CHAIR DIPS'],
    WORKOUT['BICYCLES'],
    WORKOUT['LUNGES'],
    WORKOUT['FIRE HYDRANTS'],
    WORKOUT['WALL SITS'],
    WORKOUT['LEG RAISES'],
    WORKOUT['CALF RAISES'],
)

BASIC = (
    WORKOUT['JUMPING JACKS'],
    WORKOUT['PUSH-UPS'],
    WORKOUT['SQUATS'],
    WORKOUT['PLANKS'],
    WORKOUT['CHAIR DIPS'],
    WORKOUT['BICYCLES'],
    WORKOUT['LUNGES'],
    WORKOUT['FIRE HYDRANTS'],
    WORKOUT['WALL SITS'],
    WORKOUT['CALF RAISES'],
)

ABS = (
    WORKOUT['PLANKS'],
    WORKOUT['LEFT SIDE PLANKS'],
    WORKOUT['RIGHT SIDE PLANKS'],
    WORKOUT['CRUNCHES'],
    WORKOUT['BICYCLES'],
)

GLUTES = (
    WORKOUT['SQUATS'],
    WORKOUT['LEFT FIRE HYDRANTS'],
    WORKOUT['RIGHT FIRE HYDRANTS'],
)

CORE = ABS + GLUTES

PHYSIO = (
    WORKOUT['LEFT LEG RAISES'],
    WORKOUT['RIGHT LEG RAISES'],
    WORKOUT['WALL SITS'],
    WORKOUT['WALL SITS ON TOES'],
    WORKOUT['WALL SITS ON TOES HEELS IN'],
)
