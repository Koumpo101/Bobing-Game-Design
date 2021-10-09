# invitation_readyRoom

from graphics import *
from button import Button
from dieview import DieView
from multi_player import *
from rule_display import *


def ready_room():
    # create the application window
    win = GraphWin('Bobing Game',750,750)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("orange3")

    # create a title
    title = Text(Point(5, 9), "Invitation Room" )
    title.setFace("courier")  # type of word
    title.setSize(36)
    title.setStyle("bold italic")
    title.setFill("black")
    title.draw(win)

    # ROOM Label
    room_num = Text(Point(1.7,7.5), "Room ID:")
    room_pin = Text(Point(1.7,5.5), "Room PIN:")
    name = Text(Point(1.7,6.5), "Player name:")
    room_num.setFace("courier")  # type of word
    room_num.setSize(17)
    room_num.setStyle("bold")
    room_pin.setFace("courier")  # type of word
    room_pin.setSize(17)
    room_pin.setStyle("bold")
    name.setFace("courier")  # type of word
    name.setSize(13)
    name.setStyle("bold")
    room_num.draw(win)
    room_pin.draw(win)
    name.draw(win)

    # Entry object: let users input the information
    num_input = Entry(Point(5, 7.5), 40)
    pin_input = Entry(Point(5, 5.5), 40)
    name_input = Entry(Point(5, 6.5), 40)
    num_input.draw(win)
    pin_input.draw(win)
    name_input.draw(win)

    dieA = DieView(win, Point(1, 9), 1)
    dieB = DieView(win, Point(9, 9), 1)
    dieC = DieView(win, Point(9, 1), 1)
    dieD = DieView(win, Point(1, 1), 1)

    # Button Initialization
    quitButton = Button(win, Point(5, 1), 4, 1, "Quit")
    quitButton.activate()

    conButton = Button(win, Point(5, 4),4, 1, "Confirm")
    conButton.activate()

    beginButton = Button(win, Point(5,2.5), 4, 1, "Go ahead")


    # Event
    pt = win.getMouse()
    try:
        #
        while not quitButton.clicked(pt):
            # get the text information from the user
            name_str = name_input.getText()
            num_str = num_input.getText()
            pin_str = pin_input.getText()   # for case of the game needing PIN

            if conButton.clicked(pt):
                beginButton.activate()

            pt = win.getMouse()  # track the mouse action
            if beginButton.clicked(pt):
                # whether the beginButton is clicked
                multi_player(name_str, num_str)
        # close up shop
        win.close()
    except GraphicsError as g:
        print(g)