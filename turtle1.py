import turtle

class Circuito():
    corredores =[]
    posStartY = (-30 , -10 , 10, 30)
    colors = ("pink" , "red" , "green" , "gray")
    def __init__(self , width , height):
        self.width = width
        self.height = height
        
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor("lightgray")
        self.__startLine = -width/2 + 20
        self.__finishLine = width/2 - 20
        
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.colors[i])
            new_turtle.shape("turtle")
            new_turtle.penup()
            new_turtle.setpos(self.__startLine, self.posStartY[i])
            new_turtle.color(self.colors[i])
            
            self.corredores.append(new_turtle)
            
if __name__ == "__main__":
    circuito = Circuito (640, 480)