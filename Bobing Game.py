# main page for the user

from graphics import *
from button import Button
from dieview import DieView
from single_player import single_player
from Multi_readyRoom import ready_room


def menu_page():
    # create the application window
    win = GraphWin('Bobing Game',750,750)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("orange3")

    # create a title
    title = Text(Point(5, 9), "Bobing Game" )
    title.setFace("courier")  # type of word
    title.setSize(36)
    title.setStyle("bold italic")
    title.setFill("black")
    title.draw(win)

    # WELCOME WORD
    wel = Text(Point(5, 1), "Welcome to play our game!\nCreated by ZHI LING & WEN QI")
    wel.setFace("times roman")  # type of word
    wel.setSize(22)
    wel.setStyle("bold italic")
    wel.setFill("black")
    wel.draw(win)

    # button initialization
    singleButton = Button(win, Point(5, 7), 4, 1, "Single Player" )
    singleButton.activate()

    quitButton = Button(win, Point(5, 3), 4, 1, "Quit")
    quitButton.activate()

    multiButton = Button(win, Point(5, 5 ), 4, 1, "Multi Player" )
    multiButton.activate()

    dieA = DieView(win, Point(1, 9), 1)
    dieB = DieView(win, Point(9, 9), 1)
    dieC = DieView(win, Point(9, 1), 1)
    dieD = DieView(win, Point(1, 1), 1)

    # Event
    pt = win.getMouse()
    try:
        #
        while not quitButton.clicked(pt):

            pt = win.getMouse()   # track the mouse action

            # check if single_player is clicked
            if singleButton.clicked(pt):
                single_player()

            # check if multi_player is clicked
            elif multiButton.clicked(pt) :
                ready_room()

        # close up shop
        win.close()
    except GraphicsError as g:
        print(g)

menu_page()