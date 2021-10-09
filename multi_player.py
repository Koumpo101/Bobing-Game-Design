# multiple_player.py


from random import randrange
from graphics import *
from button import Button
from dieview import DieView
from rule_display import *
from initial_dice import *
import time


def multi_player(name, num):
    # create the application window
    win = GraphWin('Bobing Game', 750, 750)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("orange3")

    # create a title
    title = Text(Point(5, 9.5), "Multiple Player")
    title.setFace("courier")  # type of word
    title.setSize(30)
    title.setStyle("bold italic")
    title.setFill("black")
    title.draw(win)

    # create the initial message (room ID & user name)
    name_message = Text(Point(1,2), "User Name: " + name)
    name_message.draw(win)

    room_message = Text(Point(1,9), "Room ID:" + num)
    room_message.draw(win)

    # create 3 "virtual friends"  <Kounmpo> <Kritio> <Karl>
    mine = Button(win, Point(9, 4.0), 2, 1, name)
    mine.activate()
    fri_1 = Button(win, Point(9, 3.0), 2, 1, "Kounmpo")
    fri_2 = Button(win, Point(9, 2.0), 2, 1, "Kirito")
    fri_3 = Button(win, Point(9, 1.0), 2, 1, "Karl")


    # draw the interface widget
    die1 = DieView(win, Point(2, 8), 1.5)
    die2 = DieView(win, Point(5, 8), 1.5)
    die3 = DieView(win, Point(8, 8), 1.5)
    die4 = DieView(win, Point(2, 6), 1.5)
    die5 = DieView(win, Point(5, 6), 1.5)
    die6 = DieView(win, Point(8, 6), 1.5)
    rollButton = Button(win, Point(5, 3), 5, 1, "Roll Dice")
    rollButton.activate()
    quitButton = Button(win, Point(5, 1.0), 2, 1, "Quit")

    # Event loop
    pt = win.getMouse()
    try:
        #
        while not quitButton.clicked(pt):
            while rollButton.clicked(pt):
                value1 = randrange(1, 7)
                die1.setValue(value1)
                value2 = randrange(1, 7)
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

                # your turn is over
                rollButton.deactivate()
                time.sleep(2)   # reaction time
                mine.deactivate()

                # fri_1 turn
                fri_1.activate()
                time.sleep(2)
                value1 = randrange(1, 7)
                die1.setValue(value1)
                value2 = randrange(1, 7)
                die2.setValue(value2)
                value3 = randrange(1, 7)
                die3.setValue(value3)
                value4 = randrange(1, 7)
                die4.setValue(value4)
                value5 = randrange(1, 7)
                die5.setValue(value5)
                value6 = randrange(1, 7)
                die6.setValue(value6)
                # design the rectangular text tips"状元插金花"
                rule_result(value1, value2, value3, value4, value5, value6, win)
                # back to the initial dice appearance
                initial(die1, die2, die3, die4, die5, die6)

                # fri_1 turn is over
                time.sleep(2)  # reaction time
                fri_1.deactivate()

                # fri_2 turn
                fri_2.activate()
                time.sleep(2)
                value1 = randrange(1, 7)
                die1.setValue(value1)
                value2 = randrange(1, 7)
                die2.setValue(value2)
                value3 = randrange(1, 7)
                die3.setValue(value3)
                value4 = randrange(1, 7)
                die4.setValue(value4)
                value5 = randrange(1, 7)
                die5.setValue(value5)
                value6 = randrange(1, 7)
                die6.setValue(value6)
                # design the rectangular text tips"状元插金花"
                rule_result(value1, value2, value3, value4, value5, value6, win)
                # back to the initial dice appearance
                initial(die1, die2, die3, die4, die5, die6)

                # fri_2 turn is over
                time.sleep(2)  # reaction time
                fri_2.deactivate()

                # fri_3 turn
                fri_3.activate()
                time.sleep(2)
                value1 = randrange(1, 7)
                die1.setValue(value1)
                value2 = randrange(1, 7)
                die2.setValue(value2)
                value3 = randrange(1, 7)
                die3.setValue(value3)
                value4 = randrange(1, 7)
                die4.setValue(value4)
                value5 = randrange(1, 7)
                die5.setValue(value5)
                value6 = randrange(1, 7)
                die6.setValue(value6)
                # design the rectangular text tips"状元插金花"
                rule_result(value1, value2, value3, value4, value5, value6, win)
                # back to the initial dice appearance
                initial(die1, die2, die3, die4, die5, die6)

                # fri_3 turn is over
                time.sleep(2)  # reaction time
                fri_3.deactivate()

                # activate the rollButton and check if player click this Button
                mine.activate()
                rollButton.activate()
                pt = win.getMouse()

            pt = win.getMouse()

        # close up shop
        win.close()
    except GraphicsError as g:
        print(g)
