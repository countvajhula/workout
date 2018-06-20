#!/usr/bin/env python

import os
import time

from datetime import datetime
from random import choice


WORKOUT = {
    'JUMPING JACKS': 1,
    'PUSH-UPS': 2,
    'SQUATS': 3,
    'PLANKS': 4,
    'LEFT SIDE PLANKS': 5,
    'CRUNCHES': 6,
    'CHAIR DIPS': 7,
    'BICYCLES': 8,
    'LUNGES': 9,
    'FIRE HYDRANTS': 10,
    'RIGHT SIDE PLANKS': 11,
    'WALL SITS': 12,
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
    os.system("say 'Next: {workout}.'"
              .format(workout=workout))
    time.sleep(2)
    os.system("say '3... 2... 1... GO! {workout}'"
              .format(workout=workout))
    time.sleep(duration/2.0)
    call_out = choice((False, True))
    if call_out:
        whom = choice(('Sid', 'Ariana'))
        workout_singular = workout.rstrip('Ss')
        taunt1 = ("say 'Come on {whom}! You call that a {workout_singular}?'"
                  .format(whom=whom, workout_singular=workout_singular))
        taunt2 = ("say 'My grandma does better {workout} than you two!'"
                  .format(workout=workout))
        taunt = choice((taunt1, taunt2))
        os.system(taunt)
    interval = max(0, duration/2.0 - 3)
    time.sleep(interval)
    os.system("say '3... 2... 1...'")
    time.sleep(1)
    return datetime.now()


if __name__ == '__main__':
    start_time = datetime.now()

    begin_workout()

    workout = iter(['WARM UP'] + list(WORKOUT.keys()))
    workout_time = 0

    print("workout time = {min}:{sec}".format(min=workout_time/60,
                                              sec=workout_time%60))
    n_sets = 1
    while (workout_time <= WORKOUT_DURATION):

        if n_sets % 3 == 0:
            rest(10)

        try:
            current_time = do_workout(next(workout).lower(), SET_DURATION)
        except StopIteration:
            workout = iter(WORKOUT.keys())
            current_time = do_workout(next(workout).lower(), SET_DURATION)

        workout_time = (current_time - start_time).total_seconds()

        n_sets += 1

    print("workout time = {min}:{sec}".format(min=workout_time/60,
                                              sec=workout_time%60))
    end_workout()
