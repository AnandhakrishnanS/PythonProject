import time
import curses
import pygame
H=input("Set hour: ")
M=input("Set minute: ")
S=input("Set seconds: ")


def main(stdscr):
    while True:
        stdscr.clear()
        stdscr.addstr(0,0,time.strftime("%H:%M:%S"))
        stdscr.refresh()
        time.sleep(1)
        if time.strftime("%H:%M:%S") == f"{H:02}:{M:02}:{S:02}":
            print("its time")
            pygame.mixer.init()
            pygame.mixer.music.load("alarm.mp3")
            pygame.mixer.music.play()
            break
curses.wrapper(main)

