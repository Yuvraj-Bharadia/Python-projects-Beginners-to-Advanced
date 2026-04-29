import curses
from curses import wrapper
import time
import random

texty = ["The job of a site connectivity checker is to visit a URL and display the status of that URL, that is, whether or not it is a live URL. Usually, site connectivity checkers visit URLs at regular intervals and return the results each time. This project will work on the same lines . it will check the live status of URLs. Site connectivity checker is one of the interesting python projects for beginners.", "Post-it notes are an excellent way to note down trivial chores so that you don’t forget to do them. In this project, we’ll make a virtual version of the physical, adhesive post-it notes. The main goal of building this application is to allow users to carry their post-it notes wherever they go (since it is on a digital platform).", "The design of this application will be straightforward – the main focus should be the primary function, that is, converting currency units from one to another. You can use Tkinter, the standard Python interface to the Tk GUI toolkit shipped along with Python."]

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the speed typing test!")
    stdscr.addstr("\nPlease enter a key to Begin!")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(5, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)

        stdscr.addstr(0, i, char, color)

def wpm_test(stdscr):
    target_text = random.choice(texty)
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()

        elif len(current_text) < len(target_text):
            current_text.append(key)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)

        stdscr.addstr(2, 0, "You have completed the text! Press any key to continue....")
        key = stdscr.getkey()
        if ord(key) == 27:
            break

wrapper(main)
