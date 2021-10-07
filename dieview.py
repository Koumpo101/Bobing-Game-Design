# 骰子（die）类
from graphics import *

class DieView:
    '''Dieview is a widget that display a graphical representation of a standard six-sided die '''

    def __init__(self, win, center, size):
        """Create a view of a die ,e.g:
        d1 = DieView(myWin, Point(40,50), 20)
        create a die centered at ()"""

        # first define some standard values
        self.win = win
        self.background = 'white'
        self.foreground = 'black'
        self.foreground_2='red'
        self.psize = 0.1 * size
        hsize = size / 2.0
        offset = 0.6 * hsize

        # create a square for the face
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx-hsize, cy-hsize)
        p2 = Point(cx+hsize, cy+hsize)
        rect = Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)

        # create 7 circle for standard pip locations
        self.pip1 = self.__makePip(cx-offset, cy-offset)
        self.pip2 = self.__makePip(cx-offset, cy)
        self.pip3 = self.__makePip(cx-offset, cy+offset)
        self.pip4 = self.__makePip(cx, cy)
        self.pip5 = self.__makePip(cx+offset, cy-offset)
        self.pip6 = self.__makePip(cx+offset, cy)
        self.pip7 = self.__makePip(cx+offset, cy+offset)

        # draw an initial value
        self.setValue(4)

    def __makePip(self,x,y):
        "Internal helper method to draw a pip at (x,y)"
        pip = Circle(Point(x,y),self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self, value):
        "set this die to display value"

        # turn all pips off
        self.pip1.setFill(self.background)
        self.pip2.setFill(self.background)
        self.pip3.setFill(self.background)
        self.pip4.setFill(self.background)
        self.pip5.setFill(self.background)
        self.pip6.setFill(self.background)
        self.pip7.setFill(self.background)

        # turn correct pips on
        if value == 1:
            self.pip4.setFill(self.foreground_2)
        elif value == 2:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 3:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
        elif value == 4:
            self.pip1.setFill(self.foreground_2)
            self.pip3.setFill(self.foreground_2)
            self.pip5.setFill(self.foreground_2)
            self.pip7.setFill(self.foreground_2)
        elif value == 5:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        else:
            self.pip1.setFill(self.foreground)
            self.pip2.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip6.setFill(self.foreground)



