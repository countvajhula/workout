#!/usr/bin/env python

import os
import time

from datetime import datetime


WORKOUT = {
    'JUMPING JACKS': 1,
    'PUSH-UPS': 2,
    'SQUATS': 3,
    'PLANKS': 4,
    'SIDE PLANKS': 5,
    'CRUNCHES': 6,
    'CHAIR DIPS': 7,
    'BICYCLES': 8,
    'LUNGES': 9,
    'FIRE HYDRANTS': 10,
}

WORKOUT_DURATION = 7 * 60  # 7 minutes
SET_DURATION = 30  # duration of each set in seconds


def rest(duration):
    os.system("say 'Rest!'")
    time.sleep(duration)


def begin_workout():
    os.system("say 'Beginning {} minute workout.'".format(WORKOUT_DURATION/60))


def end_workout():
    os.system("say 'Workout complete! Congratulations!'")


def do_workout(workout, duration):
    os.system("say 'Next: {workout}. 3... 2... 1... GO! {workout}'"
              .format(workout=workout))
    time.sleep(duration - 3)
    os.system("say '3... 2... 1...'")
    time.sleep(1)
    return datetime.now()


if __name__ == '__main__':
    start_time = datetime.now()

    begin_workout()

    workout = WORKOUT.iterkeys()
    workout_time = 0

    print "workout time = {min}:{sec}".format(min=workout_time/60,
                                              sec=workout_time%60)
    n_sets = 1
    while (workout_time <= WORKOUT_DURATION):

        if n_sets % 3 == 0:
            rest(10)

        try:
            current_time = do_workout(workout.next().lower(), SET_DURATION)
        except StopIteration:
            workout = WORKOUT.iterkeys()
            current_time = do_workout(workout.next().lower(), SET_DURATION)

        workout_time = (current_time - start_time).total_seconds()

        n_sets += 1

    print "workout time = {min}:{sec}".format(min=workout_time/60,
                                              sec=workout_time%60)
    end_workout()
