"""
Exercise descriptions from:
    PhysiApp (https://us.physiapp.com),
    Chiro Medical Group (https://www.chiromedicalgroup.com/),
    Greatist (https://greatist.com/fitness/perfect-plank),
    Wikipedia (https://en.wikipedia.org)
    Men's Journal (https://www.mensjournal.com/)
    BodyBuilding.com (https://www.bodybuilding.com)
    Popsugar Fitness (https://www.popsugar.com/fitness)
    Active Method Physical Therapy (https://www.activemethodpt.com/),
"""


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
    """
    1. Plant the hands directly under the shoulders (slightly wider
    than shoulder-width apart) like you’re about to do a
    push-up. Alternatively, place the forearms on the ground with the
    elbows aligned below the shoulders, and arms parallel to the body
    at about shoulder-width distance. If flat palms bother your
    wrists, clasp your hands together.

    2. Ground the toes into the floor and squeeze the glutes to
    stabilize the body. Your legs should be working in the move too;
    careful not to lock or hyperextend your knees.

    3. Neutralize the neck and spine by looking at a spot on the floor
    about a foot beyond the hands. Your head should be in line with
    your back.

    4. Hold the position for 20 seconds. As you get more comfortable
    with the move, hold your plank for as long as possible without
    compromising form or breath.
    """
    name = "Planks"


class LeftSidePlanks(Activity):
    """ This variation better engages the obliques, or the side muscles of
    the core, than a standard plank. Lie on one side with the legs
    stacked on top of one another then prop the body up on the hand or
    elbow while keeping the feet stacked. Modify the position by
    raising the opposing arm or leg (or both!) in the air to make the
    plank more difficult, or make the move easier by crossing the
    upper leg in front of the body for additional support.
    """
    name = "Left side planks"


class RightSidePlanks(Activity):
    """ This variation better engages the obliques, or the side muscles of
    the core, than a standard plank. Lie on one side with the legs
    stacked on top of one another then prop the body up on the hand or
    elbow while keeping the feet stacked. Modify the position by
    raising the opposing arm or leg (or both!) in the air to make the
    plank more difficult, or make the move easier by crossing the
    upper leg in front of the body for additional support.
    """
    name = "Right side planks"


class Crunches(Activity):
    """ A crunch begins with lying face up on the floor with knees
    bent. The movement begins by curling the shoulders towards the
    pelvis. The hands can be behind or beside the neck or crossed over
    the chest. Injury can be caused by pushing against the head or
    neck with hands.
    """
    name = "Crunches"


class ChairDips(Activity):
    """ Sit on the edge of the seat and place your palms on either side of
    your hips. Shift your weight onto your palms, lifting your butt
    forward and off the seat of the chair. With bent knees, bend your
    elbows and lower your upper body, creating 90-degree angles with
    your arms. Straighten your arms and repeat. To increase the
    difficulty, extend your legs.
    """
    name = "Chair dips"


class Bicycles(Activity):
    """ 1. Lie flat on the floor with your lower back pressed to the
    ground (pull your navel in to also target your deep abs).

    2. Put your hands behind your head, then bring your knees in
    towards your chest and lift your shoulder blades off the ground,
    but be sure not to pull on your neck.

    3. Straighten your right leg out to about a 45-degree angle to the
    ground while turning your upper body to the left, bringing your
    right elbow towards the left knee. Make sure your rib cage is
    moving and not just your elbows.

    4. Now switch sides and do the same motion on the other side to
    complete one rep.

    5. Do three sets of 20 reps.
    """
    name = "Bicycles"


class Lunges(Activity):
    name = "Lunges"


class FireHydrants(Activity):
    """
    1. Position yourself on your hands and knees on the ground. This
    will be your starting position.

    2. Keeping the knee in a bent position, abduct the femur, moving
    your knee away from the midline of the body.

    3. Pause at the top of the motion, and then slowly return to the
    starting position.

    4. Perform this slowly for a number of repetitions, and repeat on
    the other side.
    """
    name = "Fire hydrants"


class LeftFireHydrants(Activity):
    name = "Left fire hydrants"


class RightFireHydrants(Activity):
    name = "Right fire hydrants"


class LegRaises(Activity):
    """ To begin exercise, bend one knee and keep the other leg
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
    """ (AKA VMO Wall Circuit) Perform a wall sit with feet about hip
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
    """ TODO: duplicated in "heel raises" """
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
    """ Stand upright with your arms by your sides.  Raise one arm and
    move the opposite leg forward at the same time switching sides as
    you progress in a marching motion.  Start the exercise slowly then
    increase the speed of the motion as you continue.  Keep switching
    your legs, moving them out and upwards in front of you with your
    arms swinging freely.  Keep your knees straight and your feet
    Dorsi flexed, pointed to the ceiling as you raise your leg.
    Maintain good balance between both legs and keep your abdominals
    pulled in throughout.

    Recommended: 10 reps 3 sets
    """
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
    """ Sit in a chair with your feet flat on the floor.  Cross your arms
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
    """ Stand on a step with the affected leg weight bearing. The other
    leg should be off to the side and hanging. Next, bend at the hips
    and the knees to lower yourself down until the heel inches towards
    the ground.

    Do not let the hips drop or hike up during movement.

    Recommended: 1 s 10 reps 2 sets
    Equipment: Foot stool
    """
    name = "Step downs"


class StandingSkaters(Activity):
    """ Start with a slight bend in your knees and hips with your butt
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
    """ Place a wobble cushion on the floor near a wall, and stand in
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


class SupineNods(Activity):
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


class NeckStretch(Activity):
    """
    Start in a seated position.  Take your hand, place it on your head
    and gently pull your ear towards your shoulder and hold.  Then
    angle the head looking down towards the knee and gently pull the
    head with comfortable tension.

    Recommended: 30 s 1 rep 2 sets
    Equipment: Chair
    """
    name = "Two part neck stretch"


class DoorwayPecStretch(Activity):
    """
    Position arms into a shape of a "W" and plant your hands on the
    edge of the door frame. Take one step forward and lean your body weight
    forward until you feel a stretch across the chest and the front part of
    your arm. Exercise may be performed with one arm at a time if the doorway
    is too long. Place the arm lower than horizontal to emphasize the upper
    chest, place it perpendicularly to stretch the middle portion, and higher
    than parallel to stretch the lower portion.

    Recommended: 30 s 1 rep 2 sets
    """
    name = "Doorway pec stretch"


class UpperTrapeziusMFR(Activity):
    """
    Place a lacrosse ball on the top of your shoulder as shown. Hinge
    at the hips and pin the ball against the wall and roll side to
    side, up and down, or hold. Complete for recommended hold
    duration.

    Repeat to opposite side if necessary.

    Recommended: 2 m
    Equipment: Lacrosse Ball
    """
    name = "Upper trapezius myofascial release with ball"


class LevatorScapulaART(Activity):
    """
    Pin the ball on the wall with the back of your upper
    shoulder. Lean into it to adjust pressure. Next, turn your head
    towards the opposite pant pocket of the ball and repeat movement
    to release tension. Complete for recommended duration and repeat.

    Recommended: 60 s 1 rep 1 set
    Equipment: Lacrosse Ball
    """
    name = "Levator scapulae active release technique with ball"


class RhomboidMFR(Activity):
    """
    Place a lacrosse ball or tennis ball in between the shoulder blade
    and spine.  Hold the ball in place until you can lean your body
    into the wall to hold it up.  Move the ball around until you feel
    a tender spot in the Rhomboids When the tender spot has been
    found, move your arm across your body As your arm moves across the
    body, rotate the thumb downward as you finish across your body
    Bringing your arm back, rotate the thumb upward till your back at
    the starting position.

    Recommended: 1 m 1 rep 2 sets
    Equipment: Lacrosse Ball
    """
    name = "Rhomboid myofascial release with ball"


class ThoracicExtension(Activity):
    """
    Sit all the way back in a chair so that your back is leaning on the
    backrest. Put your hands on your shoulders with your elbows toward the
    ceiling. Extend over the chair and then come back to the starting position.

    Recommended: 3 s 10 rep 2 sets
    Equipment: Chair
    """
    name = "Thoracic extension"


class ExternalRotationWithBand(Activity):
    """
    Stand up with two supports (towels or balls) between the elbows and the
    torso. Keeping your shoulders retracted, externally rotate the arms against
    the resistance of the band in a controlled movement.

    Recommended: 10 rep 3 sets
    Equipment: Band
    """
    name = "External rotation with band"


class RowWithTheraband(Activity):
    """
    Stand and tie elastic in front of you at waist level and hold each end with
    your hands. With your shoulders down and back, pull your arms back as far
    as possible with your elbows bent. Slowly return to initial position and
    repeat.

    Recommended: 2 s 10 rep 3 sets
    Equipment: Band
    """
    name = "Row with theraband"


class ScapularRetraction(Activity):
    """
    Lie face down on a table with your arm hanging off the sides, thumbs up and
    shoulders back and down. Raise your arms up to shoulder level (with hands
    aligned with the shoulders) while keeping your elbows straight. Lower your
    arms and repeat. Keep your thumbs pointing up at all times.

    Recommended: 3 s 10 rep 2 sets
    Equipment: Table
    """
    name = "Scapular retraction"


class StrengtheningExternalRotation(Activity):
    """
    Stand and tie elastic on the opposite side of injured arm at elbow
    level. Hold the end of elastic and bend your elbow to 90 degrees. Tuck your
    chin in and pull the tip of your shoulder backwards while you pull the
    elastic out to the side by rotating your forearm out. Keep your elbow
    against your body and your chin tucked in at all times. Slowly return to
    initial position and repeat.

    Recommended: 15 rep 2 sets
    Equipment: Band
    """
    name = "Strengthening external rotation"


class StrengtheningInternalRotation(Activity):
    """
    Stand and tie elastic on the side of the injured arm at elbow level. Hold
    the end of elastic and bend your elbow to 90 degrees. Tuck your chin in and
    pull the tip of your shoulder backwards while you pull the elastic towards
    your belly. Keep your elbow bent and against your body and your chin tucked
    in at all times. Slowly return to initial position and repeat.

    Recommended: 15 rep 2 sets
    Equipment: Band
    """
    name = "Strengthening internal rotation"


class BandPullApartPalmsUp(Activity):
    """
    Stand straight with your arms extended in front of you at shoulder height
    and hold a band in both hands, palms up. Pull your arms apart to the
    sides. Return to the center and repeat the exercise, keeping your palms up
    at all times.

    Recommended: 10 rep 3 sets
    Equipment: Band
    """
    name = "Band pull apart palms up"


class RowWithRotation(Activity):
    """
    Stand and tie elastic in front of you at shoulder level. Hold the end of
    the band, bend your elbow to 90 degrees and lift your arm out to the side
    to 90 degrees. Pull the tip of your shoulder backwards while you rotate
    your forearm upwards keeping your elbow bent. Slowly return to initial
    position and repeat.

    Recommended: 10 rep 3 sets
    Equipment: Band
    """
    name = "Row with rotation"


class WallSlideWithFeetInFront(Activity):
    """
    Stand with your back flat against the wall, feet in front. Try to keep your
    hips/shoulders/head/elbows on the wall as you slide your arms up and down
    slowly. Keep the lower back against the wall.

    Recommended: 10 rep 2 sets
    Equipment: Band
    """
    name = "Wall slide with feet in front"


class ShoulderFlexionAbduction(Activity):
    """
    Stand up straight with an elastic strap beneath your foot and hold the ends
    of it in the opposite hand. With your palm facing the floor and your elbow
    straight, lift and turn your hand up and across your body in a diagonal
    motion so as to end up with your upper arm next to your ear. Lower your
    hand slowly back down to its original position.

    Recommended: 10 rep 2 sets
    Equipment: Band
    """
    name = "Shoulder flexion or abduction"


class ActiveShoulderProtraction(Activity):
    """
    Lie on your back with your knees bent and your back in neutral position
    (slightly arched). Engage your core by recruiting your pelvic floor and
    transverse abdominis. Maintain a steady abbdominal breathing while you
    raise one arm to 90 degrees. Once your arm is vertical, raise your shoulder
    blade off the floor and reach up to the ceiling, keeping your back flat on
    the floor. Return slowly to the initial position and repeat with the other
    arm.
    """
    name = "Active shoulder protraction"


class ScapularProtraction(Activity):
    """
    Stand facing a table and put your hands on the edge of the table with your
    elbows straight. Slowly lower into a push up. Step feet in to come back up
    to standing position.
    """
    name = "Active shoulder protraction"


class Warmup(Activity):
    name = "Warm up"


class Rest(Activity):
    name = "Rest"
