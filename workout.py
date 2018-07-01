#!/usr/bin/env python

import os
import time
from datetime import datetime
from random import choice

from routines import (
    BASIC,
    GENERAL,
    ABS,
    GLUTES,
    CORE,
    PHYSIO,
)

SET_DURATION = 30  # duration of each set in seconds


def say(text):
    os.system("say -v Anna {}".format(text))


def begin_workout(routine, total_duration=None):
    """
    Either total workout duration is a function of the selected routine
    with a default set duration ("standard" workout), or set duration
    is derived from the specified total duration ("timed" workout).

    TODO: handle rest, exercise, and warmup uniformly.
    TODO: add notion of "reps."
    """
    if total_duration:
        set_duration = float(total_duration) / len(routine)
    else:
        set_duration = SET_DURATION
        total_duration = len(routine) * set_duration

    say('Beginning {} minute workout.'.format(total_duration/60))
    return (set_duration, total_duration)


def end_workout():
    say('Workout complete! Congratulations!')


def do_exercise(exercise, duration):
    say('Next: {exercise}.'.format(exercise=exercise.name))
    time.sleep(2)
    say('3... 2... 1... GO! {exercise}'.format(exercise=exercise.name))
    time.sleep(duration/2.0)
    call_out = choice((False, False, True))
    if call_out:
        whom = choice(('Sid', 'Ariana'))
        exercise_singular = exercise.name.rstrip('Ss')
        taunt1 = ('Come on {whom}! You call that a {exercise_singular}?'
                  .format(whom=whom, exercise_singular=exercise_singular))
        taunt2 = ('My grandma does better {exercise} than you two!'
                  .format(exercise=exercise.name))
        taunt = choice((taunt1, taunt2))
        say(taunt)
    interval = max(0, duration/2.0 - 3)
    time.sleep(interval)
    say('3... 2... 1...')
    time.sleep(1)
    return datetime.now()


if __name__ == '__main__':
    start_time = datetime.now()

    routine = GENERAL
    set_duration, total_duration = begin_workout(routine)

    workout = iter(routine)
    workout_time = 0

    while True:

        try:
            current_time = do_exercise(next(workout), set_duration)
        except StopIteration:
            workout = iter(routine)
            current_time = do_exercise(next(workout), set_duration)

        workout_time = (current_time - start_time).total_seconds()

        if (workout_time > total_duration):
            break

    print("workout time = {min}:{sec}".format(min=workout_time/60,
                                              sec=workout_time%60))
    end_workout()
