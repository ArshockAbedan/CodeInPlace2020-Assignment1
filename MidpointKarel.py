from karel.stanfordkarel import *

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    At the first step, Karel has to lay down a line of beepers in the first row i.e. a painted line, But without
    the first and last squares.
    """
    if front_is_clear():
        # if moving forward is possible and it is not 1X1 world, then Karel can move.
        move()
    while front_is_clear():
        put_beeper()
        move()
    turn_around()
    if front_is_clear():
        move()
    else:
        turn_around()
    """
    Karel has to take one side of the painted line at each step 
    and repeat it each time to reach the center of the world. 
    """
    while beepers_present():
        cut_the_edge()
    """
    If the width of the world is even and Karel is facing the east when it cleans the painted line, 
    so Karel should put the beeper on either of the two center squares i.e. current square and the previous one. 
    In 1x! world, there is no painted line and at the final step Karel is facing the west, so front is not clear 
    and putting just one beeper would be enough.
    Else means Karel is facing the east when it cleans the painted line and the width of the world is odd 
    ( except 1X1 world ). Therefore, Karel must put the beeper in the center square, 
    and it should be noted that Karel has gone one step further regarding the fencepost issue.
    """
    if facing_east():
        turn_around()
        if front_is_clear():
            move()
        put_beeper()
    else:
        put_beeper()
        turn_around()
        if front_is_clear():
            move()
        put_beeper()


def cut_the_edge():
    """
    This function helps Karel to reach one edge of the painted line and cut that edge.
    And then Karel will turn around.
    Pre-condition: Karel is Standing at the inner border of the one side of the painted line, facing inside.
    Post-condition: Karel cuts the edge of other side of the painted line, facing inside.
    """
    while beepers_present():
        move()
    turn_around()
    if front_is_clear():
        move()
    pick_beeper()
    move()


def turn_around():
    turn_left()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
