import turtle

class Koch:
    def __init__(self, startx, starty):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.penup()
        self.turtle.goto(startx, starty)
        self.turtle.pendown()


    def teken(self,orde, lengte):
        lengte = lengte/3
        if orde == 0:
            self.turtle.forward(lengte)
        elif orde > 0:
            self.teken(orde-1, lengte)
            self.turtle.left(60)
            self.teken(orde - 1, lengte)
            self.turtle.right(120)
            self.teken(orde - 1, lengte)
            self.turtle.left(60)
            self.teken(orde - 1, lengte)

