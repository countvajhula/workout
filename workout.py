#!/usr/bin/env python

import csv
import os
import platform
import re
import time
from datetime import datetime
from random import choice

from routines import (
    ABS,
    BASIC,
    BEEFCAKE,
    CORE,
    GENERAL,
    GLUTES,
    PHYSIO_KNEES,
    PHYSIO_BACK_AND_NECK,
    PHYSIO_BALANCE,
    PHYSIO_CUSTOM,
    PHYSIO_SHOULDER,
    PHYSIO_COMBINED,
    STRETCHES,
)

from constants import (WINDOWS, MAC_OS)

try:  # py3
    import configparser
except ImportError:  # py2
    import ConfigParser as configparser

SET_DURATION = 30  # duration of each set in seconds

# put a config file at this path, e.g. ~/.my_workout/config.ini
CONFIG_FILENAME = 'config.ini'
CONFIG_ROOT = os.getenv("WORKOUT_ROOT", os.path.expanduser("~/.my_workout"))
CONFIG_FILE = os.path.join(CONFIG_ROOT, CONFIG_FILENAME)


def say_mac_os(text):
    os.system("say -v Fiona {}".format(text))


def say_linux(text):
    # Linux distros come with `spd-say`.
    # Preinstalled on ubuntu, but you may need it to install
    # it on Fedora and openSUSE
    os.system("spd-say {}".format(text))


def say(text):
    sys_platform = platform.system().upper()
    if sys_platform == MAC_OS:
        say_mac_os(text)
    elif sys_platform == WINDOWS:
        # TODO
        pass
    else:
        # LINUX
        say_linux(text)


def load_workout_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    preferences = dict(config['general'])
    preferences['users'] = next(csv.reader([preferences['users']]))
    preferences['coaching'] = bool(int(preferences['coaching']))
    preferences['call_out'] = bool(int(preferences['call_out']))
    return preferences


class Workout(object):

    users = None
    coaching = False
    call_out = False
    total_duration = 0
    set_duration = 0
    routine_name = ''
    routine = None

    def __init__(self, preferences):
        self.users = preferences.get('users')
        self.coaching = preferences.get('coaching')
        self.call_out = preferences.get('call_out')
        self.routine_name = preferences.get('routine_name')
        total_duration = preferences.get('total_duration')
        self.routine = globals().get(self.routine_name)
        if total_duration:
            self.total_duration = int(total_duration)
            self.set_duration = self.total_duration / len(self.routine)
        else:
            self.set_duration = int(preferences.get('set_duration', SET_DURATION))
            self.total_duration = len(self.routine) * self.set_duration

    def begin(self):
        """
        Either total workout duration is a function of the selected routine
        with a default set duration ("standard" workout), or set duration
        is derived from the specified total duration ("timed" workout).

        TODO: add notion of "reps."
        """
        say('Beginning {} minute {} workout.'
            .format(self.total_duration/60, self.routine_name))

        start_time = datetime.now()
        workout = iter(self.routine)
        workout_time = 0

        while True:
            try:
                exercise = next(workout)
                duration = exercise.duration * self.set_duration
                current_time = self.do_exercise(exercise, duration)
            except StopIteration:
                break

            workout_time = (current_time - start_time).total_seconds()

        print("workout time = {min}:{sec}".format(min=workout_time/60,
                                                  sec=workout_time % 60))

        say('Workout complete! Congratulations!')

    def do_exercise(self, exercise, duration):
        # TODO: use threads and interrupts to time the workout more accurately,
        # and so that e.g. taunts are not unaccounted for, time wise
        say('Next: {exercise}.'.format(exercise=exercise.name))
        if self.coaching and exercise.__doc__:
            description = re.sub('[^a-zA-Z0-9 \.]', ' ', exercise.__doc__)
            say(description)
        time.sleep(2)
        say('3... 2... 1... GO! {exercise}'.format(exercise=exercise.name))
        time.sleep(duration/2.0)
        call_out = choice((False, False, True))
        call_out = False
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


# TODO: make a CLI for non-persistent config like workout type and coaching
# TODO: use a default config if config file is absent
def main():

    # add itinerary
    preferences = load_workout_config()
    workout = Workout(preferences)
    workout.begin()


if __name__ == '__main__':
    main()
