import sys

x = 1000000

sys.setrecursionlimit(x)

x = 1

def recursor():
    global x
    print(x)
    x += 1
    recursor()

recursor()
