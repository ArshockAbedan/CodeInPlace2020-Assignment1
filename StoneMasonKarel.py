from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    while front_is_clear():
        climb_fix()
        return_to_ground()
        move_to_column()
    # Due to fencepost error issue, the last column remains unrepaired.
    climb_fix()
    return_to_ground()


def climb_fix():
    """
    This function helps Karel climb to the top of the column while repairing the column at each step.
    Pre-condition: Karel is standing at the bottom of the unrepaired column, facing east.
    Post-condition: Karel is standing at the top of the repaired column, facing north.
    """
    turn_left()
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
            move()
        else:
            move()
    """
    Due to the fencepost error, the last square remains unchecked.
    if there is no beeper at the last step i.e. the top of the column, putting the last beeper will be missed.
    so the last beeper should be put there.
    """
    if no_beepers_present():
        put_beeper()


def return_to_ground():
    """
    This function return Karel to the ground.
    Pre-condition: Karel is standing at the top of the repaired column, facing north.
    Post-condition: Karel is standing at the bottom of the repaired column, facing east.
    """
    turn_around()
    while front_is_clear():
        move()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def move_to_column():
    for j in range(4):
        move()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
