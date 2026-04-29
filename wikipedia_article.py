import ctypes
import wikipedia as wiki
word = input("What is your topic(be specific): ")
info = wiki.summary(word)
ctypes.windll.user32.MessageBoxW(
    0, info[:400], word, 0
)