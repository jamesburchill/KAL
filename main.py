import pyautogui as pag
import random
import time
import sys


def main():
    """
    Running this script with no parameter will cause the program to
    execute the loop 1000 times - approx an hour or so of mouse moving.
    If you pass a number, it will run the loop that many times ...
    Rough rule of thumb: 1000 = 1H of KAL activity.
    :return: 0
    """
    scrn_width, scrn_height = pag.size()
    shrink_to = .8  # 80%
    random.seed()
    until = 1000  # the number of times the mouse loop runs (a little over an hour)
    if len(sys.argv) > 1:
        until = int(sys.argv[1])

    # eg 1000 * .8 = 800
    new_width = scrn_width * shrink_to
    new_height = scrn_height * shrink_to

    # eg 100 = (1000 - 800) / 2
    x_offset = (scrn_width - new_width) / 2
    y_offset = scrn_height - new_height

    TL = (x_offset, y_offset)
    TR = (scrn_width-x_offset, y_offset)
    BR = (scrn_width-x_offset, scrn_height-y_offset)
    BL = (x_offset, scrn_height-y_offset)

    LOCS = [TL, TR, BR, BL]

    for ii in range(until):
        my_move(*LOCS[random.randint(0, 3)])
        time.sleep(random.randint(0, 3))

    return 0


def my_move(x, y, d=3):
    """
    This is a convenience wrapper function that moves the mouse to x,y
    taking d seconds to execute the move (in a 'natural' fashion.)

    :param x: co-ord
    :param y: co-ord
    :param d: uration it takes to move to x,y
    :return: 0
    """
    pag.moveTo(x, y, duration=random.randint(1, d), tween=pag.easeInOutQuad)

    return 0


if __name__ == '__main__':
    main()
