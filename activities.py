
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
    """ Stand with your feet shoulder-width apart.  Engage your core
    muscles and gently squat down, do not allow your knees to travel
    too far forwards and keep your weight on your heels, not your
    toes.  Tense your bottom muscles at the bottom of the squat and
    keep them tense as you straighten back up to the start position.
    As you squat, bend from your hips and keep your back straight.

    **Keep knees aligned with toes. Keep knees above the ankles
      throughout**

    Recommended: 10 reps 3 sets
    """
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
    """To begin exercise, bend one knee and keep the other leg
    straight Try to engage your inner and middle thigh muscle before
    you lift the leg upward You should be lifting the leg to the
    height of the other knee, hold it then slowly lower your leg

    Recommended:  10 reps 3 sets
    Equipment: mat
    """
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
    """
    (AKA VMO Wall Circuit) Perform a wall sit with feet about hip
    width apart and toes pointing forward. Hold position for
    recommended duration. Next, bring heels together with toes
    pointing out and hold. Finally, with toes pointing outward, lift
    heels off the ground.  One repetition is holding all 3 positions
    for the recommended duration.

    Recommended: 30 seconds 3 reps 1 set
    """
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
    """ (AKA VMO Circuit) Place ball/pillow between the knees and get
    into a mini squat position. Raise up on the toes as high as you
    can and do 10 small slow pulses. Then drop into a deeper squat and
    repeat. Keep back straight and you can hold on to something stable
    for balance.

    Recommended: 30 s 1 rep 3 sets
    Equipment: wall or pole
    """
    name = "Squat pulses"


class StandingObliqueCrunches(Activity):
    name = "Standing crunches"


class ClamShells(Activity):
    """ Lie on your side and place a band above your knees,
    approximately an inch or two above the knee joint.  Bend your legs
    a little, keeping the feet in line with your back.  Use your core
    stability muscles to keep the body stable.  Keeping your feet
    together, lift the top knee up against the resistance of the band.
    Ensure you stay on your side and do not roll your hips and your
    body back with the movement.  Lower the knee back down,
    controlling the resistance.

    ***HOLD FOR 30 SECONDS***

    Recommended:  1 rep 2 sets
    Equipment: Mat, Resistance Band
    """
    name = "Clam shells"


class ToySoldiers(Activity):
    name = "Toy soldiers"


class BandedSumoWalk(Activity):
    """ Place a resistance band around the ankles or around the balls
    of your feet (between your toes and arch of the foot). Bend
    slightly at the knees and hips and stick your butt back behind
    you. Keep core engaged and lower back straight. Side step while
    keeping toes pointed forward throughout and knees pointed with
    your toes. Elevate the trailing limb and return to neutral while
    keeping tension Avoid rocking/swaying with the hips. Keep pelvis
    and shoulders facing forward.

    Recommended: 1 s 10 reps 2 sets
    Equipment: Resistance band
    """

    name = "Banded sumo walk"


class FigureFours(Activity):
    """ (AKA "Supine piriformis stretch")
    Lie on your back and bend your knees.  Place the ankle of the
    symptomatic leg over the knee of the other leg.  Interlace your
    fingers behind the thigh of the good leg.  Pull the knee towards
    the chest until you feel a stretch in your buttocks and inner
    thigh.  You can use the elbow to push the knee out further.  Hold
    this position.

    You may rest your leg against a wall for passive support

    Recommended: 30 s 1 rep 2 sets
    Equipment: Mat
    """
    name = "Figure fours"


class SeatedMarches(Activity):
    """ (AKA "Flexion of the hip in seated position") Sit on a chair.
    Raise your affected leg, making sure you keep your knee bent.
    Return back to the starting position. Optionally provide equal
    resistance from hands

    Recommended: 10 s 5 reps 2 sets
    Equipment: Chair
    """
    name = "Seated marches"


class SitToStand(Activity):
    """
    Sit in a chair with your feet flat on the floor.  Cross your arms
    in front of your chest so you are not tempted to push off of your
    thighs for momentum.  Stand up, then slowly sit back down and
    repeat a number of times.

    Recommended: 10 reps 2 sets
    Equipment: Chair
    """
    name = "Sit to stand"


class FounderSequences(Activity):
    """ Stand with your feet approximately hip width apart. Hinge at the hips
    and bend the knees as if performing a squat. Additionally, lift your arms
    up overhead as much as possible to be in plane with your body. Hold
    position for duration and repeat.
    Make sure shins are vertically upright throughout.

    **Modified version**
    Perform this exercise with arm movements, lift the arms in front of you in
    3 positions: arms in front but below shoulder level, at shoulder level,
    then up overhead. Maintain squatted position and knees directly above your
    ankles.

    Recommended: 30 s 1 rep 2 sets
    """
    name = "Founder sequences"


class StepDowns(Activity):
    name = "Step downs"


class StandingSkaters(Activity):
    """Start with a slight bend in your knees and hips with your butt
    sticking out behind you. Keep the core engaged and low back
    straight throughout. Extend one leg diagonally back and out behind
    you while keeping the rest of the body still. You should feel this
    in the glute of the stance leg. Return to neutral.

    Exercise may be performed using a resistance band around the
    ankles, using a furniture slider, or holding onto a
    doorknob/handle/counter for support.

    **Note** Be sure to keep shin as vertical as possible. Avoid hip
    rotation during movement. Do not let knee collapse inward or
    weight shift to the back leg.

    Recommended: 10 reps 2 sets
    Equipment: Resistance band
    """
    name = "Standing skaters"


class HamstringStretchesWithStrap(Activity):
    """ Lie on your back with a strap around the foot of your affected
    leg.  Pull the knee in towards your chest, then straighten the leg
    up towards the ceiling until you feel a stretch in the back of the
    thigh.  Hold this position.

    **Alternative** Lay down on your back with butt facing the
    wall. Prop up both heels on the wall and straighten your legs. You
    should feel a stretch in the back of your thigh. To feel a deeper
    stretch, scoot your buttocks closer towards the wall.

    Recommended: 30 s 1 rep 2 sets
    Equipment: Strap
    """
    name = "Hamstring stretches with strap"


class TRXSquats(Activity):
    """ Stand up straight with your feet wider than hips width apart.
    Shorten the straps and grasp the handles in each hand.  Bend your
    hips and knees, pushing your buttocks back behind you and
    counterbalancing this movement by leaning your chest forwards.
    Your arms should be taken up towards the ceiling.  Straighten back
    up, driving the movement by your buttock muscles, rather than
    pulling on the straps.

    Recommended:  10 reps 2 sets
    Equipment: TRX
    """
    name = "TRX Squats"


class HeelRaises(Activity):
    """ Stand up straight next to a wall or supporting surface.  Keep
    your knees straight, and then raise up onto your tip toes.  Slowly
    lower your heel back down.  To make this more fun you could try
    putting toys onto a high shelf, or placing stickers onto a paper
    that is taped onto the wall.

    Recommended: 1 s 10 reps 2 sets
    Equipment: Wall
    """
    name = "Heel raises"


class BirdDogs(Activity):
    """ Start with your knees and hands on the floor. Keeping our back
    straight, we are going to lift our right arm to the sky, then
    extend and straighten out our right leg behind us. Following
    around the world, we will straighten and extend our left leg
    behind us, and finish the rep by lifting up the left arm.

    Recommended: 10 reps 2 sets
    Equipment: Mat
    """
    name = "Bird dogs around the world"


class LowTrapeziusRows(Activity):
    """ Anchor an elastic band somewhere above your head (you may
    thread the band between a door jam). Stand tall and upright with
    lower back straightened and core engaged. Start with arms in front
    of you outstretched and feeling some tension. Pull downwards while
    squeezing shoulder blades together. Return to neutral without
    elastic band pulling your shoulders forward.

    Avoid lower back arching and shoulder shrugging throughout movement.

    Recommended: 1 s 10 reps 2 sets
    Equipment: Elastic Band
    """
    name = "Low trapezius rows"


class MidTrapeziusRows(Activity):
    """ With a slight bend in the knees and tight core, pull with the
    elbows and squeeze the shoulder blades together.  Do not allow
    your shoulders to shrug. Do not allow your ribs to pop out.  You
    should feel this between the shoulder blades.

    Recommended: 1 s 10 reps 2 sets
    Equipment: Elastic Band
    """
    name = "Mid trapezius rows"


class SingleLegBalance(Activity):
    """ Stand with your legs straight at shoulder width apart. Now
    lean slightly to the side and at the same time bend your opposite
    knee. You can make this more difficult by bending further but only
    within the limits of your mobility.

    ***To make more difficult, perform with leg swing or look around
    rather than at a fixed point, or raise knee to hip level and close
    eyes ***

    Recommended: 30 s 1 rep 2 sets
    Equipment: Wall
    """
    name = "Single leg balance"


class SLSWobbleCushion(Activity):
    """Place a wobble cushion on the floor near a wall, and stand in
    the middle on your affected leg.  Try and balance for as long as
    you can.

    You may use a pillow or couch cushion in place of the wobble
    cushion. Alternatively, you may also use the floor and close the
    eyes

    Recommended: 30 s 1 rep 2 sets
    Equipment: Wobble disc or pillow
    """
    name = "SLS wobble cushion"


class UlnarNerveGlide(Activity):
    """ Stand upright and make a circle between the thumb and index
    finger of your affected arm.  Hold this hand up by your ear and
    then rotate your fingers away from you towards your little finger
    ("OK sign").  Start to bring your bent elbow out to the side and
    then bring the palm of your hand towards the side of your face
    (rotating hand "backwards") until you reach the point of tension.
    Do not push any further.  At this point, tilt your head away from
    this side, whilst simultaneously moving your hand away from the
    side of your head.  As you lift and move your head back to the
    centre, bring your hand back to the side of your face.  Perform
    this exercises in one fluid movement.

    **Modified** Keep forearm is pointing vertically upwards
    throughout, no tucking underneath the cheek.  Next, turn the wrist
    outward to stretch. Next, while still facing forward and keeping
    the wrist turned outward, rotate head from shoulder to shoulder,
    to alternately release and stretch.  Additionally, if tolerable,
    plant the forearm against the wall and step forward to feel a
    stretch in the chest.

    Recommended: 20 seconds 1 rep 2 sets
    """
    name = "Ulnar nerve glide"


class SupineNods:
    """ (AKA "Supine deep neck flexor activation") Lie on your back
    with your knees bent and your feet flat on the floor.  Place a
    pillow under your head and look up towards the ceiling.  Visualise
    a pivot point going through your ears.  Gently nod your chin as
    though rotating around that pivot point without tensing your side
    neck muscles.  Use the muscles, deep at the front of your throat
    instead.  This is a very subtle exercise and will take practice to
    tuck your chin in just enough so you feel the back of your head a
    little heavy on the pillow but without the activity of your side
    neck muscles.  These deep neck muscles are important to retrain to
    help headaches and neck issues from office or computer work. Hold
    your chin downwards as advised and continue to breathe in a
    controlled manner by expanding and contracting your lower
    ribcage. Contract your lower stomach and pelvic floor muscles at
    the same time throughout the movement.

    **Place rolled up towel underneath neck instead** Place your
    finger on your nose and chin, give yourself a double chin so the
    chin moves away from the finger

    Recommended: 5 s 10 reps 2 sets
    Equipment: mat, pillow
    """
    name = "Supine nods"


class SegmentalThoracicFoamRoll(Activity):
    """ Position a foam roller horizontally and lay on it around your
    mid back region. Next, cross the arms over your chest and perform
    small pulses to arch your back. You should feel your spine
    slightly fold over the regions that the foam roller is in contact
    with. Perform a few repetitions each segment and make your way up
    the back. Each time, your back should pivot at the contact point
    while the region below it should remain motionless (e.g. lower
    back would be straight rather than arched. The point when it
    begins arching is when you should stop the arch and reverse
    direction.

    Recommended: 1 s 5 reps 2 sets
    Equipment: Mat, foam roller
    """
    name = "Segmental thoracic foam roll"


class Warmup(Activity):
    name = "Warm up"


class Rest(Activity):
    name = "Rest"
