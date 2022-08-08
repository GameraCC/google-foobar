from cgitb import small
from tkinter import Y


def solution (x, y):
    smaller_list = y if len(x) > len(y) else x
    bigger_list = x if len(x) > len(y) else y

    for id in bigger_list:
        if id not in smaller_list:
            return id

def main():
    print(solution([13, 5, 6, 2, 5], [5, 2, 5, 13]))

main()