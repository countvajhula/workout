
class Activity:
    name = ''
    duration = 0
    components = None

    def __init__(self, duration=1):
        # duration is relative to parent activity
        self.duration = duration


class JumpingJacks(Activity):
    name = "Jumping jacks"

class Pushups(Activity):
    name = "Push ups"

class Squats(Activity):
    name = "Squats"

class Planks(Activity):
    name = "Planks"

class LeftSidePlanks(Activity):
    name = "Left side planks"

class RightSidePlanks(Activity):
    name = "Right side planks"

class Crunches(Activity):
    name = "Crunches"

class ChairDips(Activity):
    name = "Chair dips"

class Bicycles(Activity):
    name = "Bicycles"

class Lunges(Activity):
    name = "Lunges"

class FireHydrants(Activity):
    name = "Fire hydrants"

class LeftFireHydrants(Activity):
    name = "Left fire hydrants"

class RightFireHydrants(Activity):
    name = "Right fire hydrants"

class LegRaises(Activity):
    name = "Leg raises"

class LeftLegRaises(Activity):
    name = "Left leg raises"

class RightLegRaises(Activity):
    name = "Right leg raises"

class TableLeftLegRaises(Activity):
    name = "Table position left leg raises"

class TableRightLegRaises(Activity):
    name = "Table position right leg raises"

class TableLeftLegHighRaises(Activity):
    name = "Table position high left leg raises"

class TableRightLegHighRaises(Activity):
    name = "Table position high right leg raises"

class WallSits(Activity):
    name = "Wall sits"

class WallSitsOnToes(Activity):
    name = "Wall sits on toes"

class WallSitsOnToesHeelsIn(Activity):
    name = "Wall sits on toes with heels in"

class CalfRaises(Activity):
    name = "Calf raises"

class LeftCalfRaises(Activity):
    name = "Left calf raises"

class RightCalfRaises(Activity):
    name = "Right calf raises"

class SquatPulses(Activity):
    name = "Squat pulses"

class StandingObliqueCrunches(Activity):
    name = "Standing crunches"

class ClamShells(Activity):
    name = "Clam shells"

class ToySoldiers(Activity):
    name = "Toy soldiers"

class BandedSumoWalk(Activity):
    name = "Banded sumo walk"

class FigureFours(Activity):
    name = "Figure fours"

class SeatedMarches(Activity):
    """ With equal resistance from hands """
    name = "Seated marches"

class SitToStand(Activity):
    name = "Sit to stand"

class Warmup(Activity):
    name = "Warm up"

class Rest(Activity):
    name = "Rest"
