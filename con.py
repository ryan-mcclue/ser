#! /usr/bin/env python3
# SPDX-License-Identifier: zlib-acknowledgement

import curses

def main(curses_sceen):
    curses.curs_set(False)
    curses.nodelay(True)

    width = curses.COLS
    height = curses.LINES 
    have_colors = curses.has_colors()

    while True:
        input_ch = curses_screen.getch()
        if input_ch == ord("a"):
            pass

        curses_sceen.clear()

        # addch()
        curses_sceen.addstr(y, x, "", curses.A_UNDERLINE)

        curses_sceen.refresh()


# NOTE(Ryan): This will handle initialisations for us, e.g. non-buffered input, no key echo, colors, etc.
# Will also handle restoring terminal when we encounter an error.
curses.wrapper(main)
