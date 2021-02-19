#! /usr/bin/env python3
# SPDX-License-Identifier: zlib-acknowledgement

import curses


# curses.init_pair(1, fg, bg)
# curses.color_pair(1)
# TODO(Ryan): Add color
def draw_ch(x, y, ch):
    clip_x = 0
    if x >= screen_width:
        clip_x = screen_width
    if x < 0:
        clip_x = 0

    clip_y = 0
    if y >= screen_width:
        clip_y = screen_width
    if y < 0:
        clip_y = 0

    curses.addch(y, x, ch)

def draw_rect(x1, y1, x2, y2, ch):
    pass

def main(curses_screen):
    if not curses.has_colors():
        return

    curses.curs_set(False)
    curses_screen.nodelay(True)

    width = curses.COLS
    height = curses.LINES 

    x = y = 0
    while True:
        # TODO(Ryan): If non-blocking, does this still call refresh()?
        input_ch = curses_screen.getch()
        if input_ch == ord("a"):
            x += 1
            y += 1

        # NOTE(Ryan): Calling clear() caused flickering
        curses_screen.erase()

        # will print and advance cursor. so if this off screen, will through exception
        # therefore have a function that clips
        # TODO(Ryan): Enable stepping into python library functions (perhaps turn off smart step?)
        curses_screen.addstr(y, x, "hi there")

        curses_screen.refresh()


# NOTE(Ryan): This will handle initialisations for us, e.g. non-buffered input, no key echo, colors, etc.
# Will also handle restoring terminal when we encounter an error.
curses.wrapper(main)
