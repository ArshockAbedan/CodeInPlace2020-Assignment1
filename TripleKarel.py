from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    # the start point of the first building
    paint_first_building()
    # the start point of the second building
    paint_second_building()
    # the start point of the third building
    paint_third_building()
    # to adjust Karel in the proper direction at the final position, a turning to left is needed.
    turn_left()


def paint_first_building():
    """
    This function makes the first building painted.
    Karel should turn to the left after finishing the first wall and the second wall i.e. non-final wall,
        while Karel should turn to the right after finishing the final wall to be ready to
        paint the second building.
    Whenever there is no wall on the left side, Karel can turn left or right
        and it will not be facing the previous direction anymore.
    Pre-condition: Starting position
    Post-condition: The first building is painted.
    """
    while facing_west():
        paint_non_final_wall()
    while facing_south():
        paint_non_final_wall()
    while facing_east():
        paint_final_wall()


def paint_second_building():
    """
    This function makes the second building painted.
    Karel should turn to the left after finishing the first wall and the second wall i.e. non-final wall,
        while Karel should turn to the right after finishing the final wall to be ready to
        paint the third building.
    Whenever there is no wall on the left side, Karel can turn left or right
        and it will not be facing the previous direction anymore.
    Pre-condition: The first building is painted and Karel is at the starting point of the second building.
    Post-condition: The second building is painted and Karel is at the starting point of the third building.
    """
    while facing_south():
        paint_non_final_wall()
    while facing_east():
        paint_non_final_wall()
    while facing_north():
        paint_final_wall()


def paint_third_building():
    """
    This function makes the third building painted.
    The third building has three walls.
    Karel should turn to the left after finishing the first wall and the second wall i.e. non-final wall,
        while Karel should turn to the right after finishing the final wall to be ready to
        finish the its task.
    Whenever there is no wall on the left side, Karel can turn left or right
        and it will not be facing the previous direction anymore.
    Pre-condition: The second building is painted and Karel is at the starting point of the third building.
    Post-condition: The third building is painted
                    and Karel is at the finishing position without being in the right direction.
    """
    while facing_east():
        paint_non_final_wall()
    while facing_north():
        paint_non_final_wall()
    while facing_west():
        paint_final_wall()


def paint_non_final_wall():
    """
    This function paints a non-final wall, which is either the first wall or the second wall in a building,
        and turn left to became ready to paint the next wall.
    Pre-condition: Karel is placed at the starting point of the wall and wall is not painted yet.
    Post-condition: The wall was painted and karel is standing at the beginning of next wall
    """
    while left_is_blocked():
        put_beeper()
        move()
    turn_left()
    move()


def paint_final_wall():
    """
    This function paints a final wall, which is the third wall in a building,
        and turn right to become ready to paint the next building.
    In the third building,
        turning to the right just provides the finishing condition and there is no other building to paint
    Pre-condition: Karel is placed at the starting point of the wall and the wall is not painted yet.
    Post-condition: The wall was painted and Karel is standing at the beginning of the next wall.
                    At the third building, Karel stands at the finishing position
    """
    while left_is_blocked():
        put_beeper()
        move()
    turn_right()


def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
