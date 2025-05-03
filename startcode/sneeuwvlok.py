import turtle
from koch import Koch




class Sneeuwvlok:


    def teken(self, orde, grootte):
        for i in range(3):
            koch1 = Koch(-250, 0)
            koch1.teken(3, 500)

            koch2 = Koch(-125, -250)
            koch2.teken(3, 300)


turtle.hideturtle()
turtle.exitonclick()