# single_player.py

from random import randrange
from graphics import *
from button import Button
from dieview import DieView
from rule_display import *
from initial_dice import *

def single_player():
    # create the application window
    win = GraphWin('Bobing Game',750,750)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("orange3")

    # create a title
    titl = Text(Point(5, 9.5), "Single Player")
    titl.setFace("courier")  # type of word
    titl.setSize(30)
    titl.setStyle("bold italic")
    titl.setFill("black")
    titl.draw(win)

    # draw the interface widget
    die1 = DieView(win, Point(2,8), 1.5)
    die2 = DieView(win, Point(5,8), 1.5)
    die3 = DieView(win, Point(8,8), 1.5)
    die4 = DieView(win, Point(2,6), 1.5)
    die5 = DieView(win, Point(5,6), 1.5)
    die6 = DieView(win, Point(8,6), 1.5)
    rollButton = Button(win, Point(5,3), 6, 1, "Roll Dice")
    rollButton.activate()
    quitButton = Button(win, Point(5,1.0), 2, 1, "Quit")

    # Event loop
    pt = win.getMouse()
    try:
        #
        while not quitButton.clicked(pt):
            if rollButton.clicked(pt):
                value1 = randrange(1,7)
                die1.setValue(value1)
                value2 = randrange(1,7)
                die2.setValue(value2)
                value3 = randrange(1, 7)
                die3.setValue(value3)
                value4 = randrange(1, 7)
                die4.setValue(value4)
                value5 = randrange(1, 7)
                die5.setValue(value5)
                value6 = randrange(1, 7)
                die6.setValue(value6)
                quitButton.activate()
                # design the rectangular text tips"状元插金花"
                rule_result(value1, value2, value3, value4, value5, value6, win)
                # back to the initial dice appearance
                initial(die1, die2, die3, die4, die5, die6)

            pt = win.getMouse()

        # close up shop
        win.close()
    except GraphicsError as g:
        print(g)



