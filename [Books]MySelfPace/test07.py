# Test Window

import curses

curses.initscr()
curses.cbreak()


height = 3
width = 10
starty = 25
startx = 2

curses.start_color()
curses.init_color(1,curses.COLOR_RED,curses.COLOR_BLACK,curses.COLOR_BLUE)

win = curses.newwin(height,width,starty,startx)
win.attron(COLOR_PAIR(1))
win.keypad(1)
print("Press F1 to exit")
win.attroff(COLOR_PAIR(1))

curses.endwin()
