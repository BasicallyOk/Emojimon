#!/usr/bin/env python
"""
Test bench is Emojimon's command line interface where one can play the game without the need for the actual front end.
This will allow the back-end and the front-end to be developed separately from one another.
The test bench will NOT be subject to our CI pipeline. This is for human testing purposes to aid development only.
"""

from components import emojimon, move

__author__ = "Khoa Nguyen" # Insert your name here if you're writing the initial code
__maintainer__ = "Khoa Nguyen" # Insert your name here if you're fixing bugs or make improvements

def main(): 
    """Main driver code"""
    generate_trainer_with_emojis()
    pass


def generate_trainer_with_emojis(id_arr1:list=[], id_arr2:list=[]):
    """
    Give players emojis to fight with, preferrably should start by generating Trainer objects
    
    Keyword arguments:
    id_arr1 -- a list of emojimon ids (integers) for your player
    id_arr2 -- a list of emojimon ids (integers) fo the opponent

    Return:
    2 Trainer objects with emojis already added
    """
    generate_trainers()
    pass


def generate_trainers():
    """
    Generate Trainer objects to play.
    These trainers should not be tracked in any way as we're simply demoing the back end, i.e., no id, no saving progress, etc.

    Return:
    2 Trainer objects
    """
    pass


if __name__ == "__main__":
    """No exports, this tool is meant to be standalone"""
    main()