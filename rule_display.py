# rule_display.py

from random import randrange
from graphics import *
from button import Button
from dieview import DieView
import time


def rule_result(val_1, val_2, val_3, val_4, val_5, val_6, window):

    val = [val_1, val_2, val_3, val_4, val_5, val_6]
    # set 6 number_counters to count the concrete dice appearance
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0

    for i in val:
        if i == 1:
            count1 += 1
        elif i == 2:
            count2 += 1
        elif i == 3:
            count3 += 1
        elif i ==4:
            count4 += 1
        elif i == 5:
            count5 += 1
        elif i == 6:
            count6 += 1

    # according to the rule of the Bobing, we distinguish the result and display it
    if count4 == 1:
        reslt = Text(Point(5, 4), "一秀")
        reslt.setSize(30)
        reslt.setFill("black")
        reslt.draw(window)
        time.sleep(3)
        reslt.undraw()

    elif count4 == 2:
        reslt = Text(Point(5, 4), "二举")
        reslt.setSize(30)
        reslt.setFill("black")
        reslt.draw(window)
        time.sleep(3)
        reslt.undraw()

    elif count2 == 4:
        reslt = Text(Point(5, 4), "四进")
        reslt.setSize(30)
        reslt.setFill("black")
        reslt.draw(window)
        time.sleep(3)
        reslt.undraw()

    elif count4 == 3:
        reslt = Text(Point(5, 4), "三红")
        reslt.setSize(30)
        reslt.setFill("black")
        reslt.draw(window)
        time.sleep(3)
        reslt.undraw()

    elif count1 == 1 and count2 == 1 and count3 == 1 and count4 == 1 and count5 == 1 and count6 == 1:
        reslt = Text(Point(5, 4), "对堂")
        reslt.setSize(30)
        reslt.setFill("black")
        reslt.draw(window)
        time.sleep(3)
        reslt.undraw()

    elif count4 == 4:
        reslt = Text(Point(5, 4), "四点红")
        reslt.setSize(30)
        reslt.setFill("red")
        reslt.draw(window)
        time.sleep(3)
        reslt.undraw()

    elif count2 == 5:
        reslt = Text(Point(5, 4), "五子登科")
        reslt.setSize(30)
        reslt.setFill("red")
        reslt.draw(window)
        time.sleep(3)
        reslt.undraw()

    elif count4 == 5 and count1 == 1:
        reslt = Text(Point(5, 4), "五红")
        reslt.setSize(30)
        reslt.setFill("red")
        reslt.draw(window)
        time.sleep(3)
        reslt.undraw()

    elif count1 == 6:
        reslt = Text(Point(5, 4), "遍地锦")
        reslt.setSize(30)
        reslt.setFill("red")
        reslt.draw(window)
        time.sleep(3)
        reslt.undraw()

    elif count4 == 6:
        reslt = Text(Point(5, 4), "六杯红")
        reslt.setSize(30)
        reslt.setFill("red")
        reslt.draw(window)
        time.sleep(3)
        reslt.undraw()

    elif count4 == 4 and count1 == 2:
        reslt = Text(Point(5, 4), "状元插金花")
        reslt.setSize(30)
        reslt.setFill("red")
        reslt.draw(window)
        time.sleep(3)
        reslt.undraw()

    else:
        reslt = Text(Point(5, 4), "无！")
        reslt.setSize(36)
        reslt.setFill("black")
        reslt.draw(window)
        time.sleep(3)
        reslt.undraw()
