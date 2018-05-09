import turtle
import time
from collections import deque
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("maze")
wn.setup(700,700)

#creat pen
class Pen (turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Exp (turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("grey")
        self.penup()
        self.speed(0)

#creat player
class Player (turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

    def go(self,xx,yy):
        if(xx,yy) not in walls:
            self.goto(xx,yy)
        self.stamp()


    def go_up(self):
        mx=player.xcor()
        my=player.ycor()+24
        if(mx,my) not in walls:
            self.goto(self.xcor(),self.ycor()+24)
        self.stamp()

    def go_down(self):
        mx = player.xcor()
        my = player.ycor() - 24
        if (mx, my) not in walls:
            self.goto(self.xcor(), self.ycor() - 24)
        self.stamp()

    def go_left(self):
        mx = player.xcor() -24
        my = player.ycor()
        if (mx, my) not in walls:
            self.goto(self.xcor() -24, self.ycor())
        self.stamp()

    def go_right(self):
        mx = player.xcor() +24
        my = player.ycor()
        if (mx, my) not in walls:
            self.goto(self.xcor()+24, self.ycor())
        self.stamp()

    def is_goal(self,other):
        a=self.xcor()-other.xcor()
        b=self.ycor()-other.ycor()

        if a==0 and b==0:
            return True
        else:
            return False


class Goal(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

#Define first level
map=[
"xxxxxxxxxxxxxxxxxxxxxxxxx",
"x          xx ttttttttttx",
"x          xx tttttt    x",
"x          xx tttttt    x",
"x          xx tttttt    x",
"x          xx           x",
"x     xxxxxxx           x",
"x     xxxxxxx      g    x",
"x                       x",
"x ttttt        xx       x",
"x              xx       x",
"x       p      xx       x",
"x         tttttxx       x",
"x        ttttttxx       x",
"xxxxxxxxxxxxxxxxxxxxxxxxx",
]



#level setup function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screenx=-288+(x*24)
            screeny=288-(y*24)

            if character=="x":
                pen.goto(screenx,screeny)
                pen.stamp()
                walls.append((screenx,screeny))
            else:
                if level[y][x+1]==" ":
                    graphR[(screenx,screeny)]=(screenx+24,screeny)
                if level[y+1][x]==" ":
                    graphU[(screenx,screeny)]=(screenx,screeny+24)
                if level[y][x-1]==" ":
                    graphL[(screenx,screeny)]=(screenx-24,screeny)
                if level[y-1][x]==" ":
                    graphD[(screenx,screeny)]=(screenx,screeny-24)

            if character == "p":
                start=(screenx,screeny)
                player.goto(screenx,screeny)
                player.stamp()

            if character=="g":
                end=(screenx,screeny)
                goal.goto(screenx,screeny)

            if character=="t":
                exp.goto(screenx,screeny)
                exp.stamp()


    ############## algorithm #################
    """"
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            player.go(node[0],node[1])
            time.sleep(1 / 20)

            if node == end:
                return
            if node in graphR and graphR[node] not in visited:
                stack.append(graphR[node])

            if node in graphU and graphU[node] not in visited:
                stack.append(graphU[node])

            if node in graphL and graphL[node] not in visited:
                stack.append(graphL[node])

            if node in graphD and graphD[node] not in visited:
                stack.append(graphD[node])"""

    visited = set()
    queue = [start]
    print(start)
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            print(node)
            player.go(node[0], node[1])
            time.sleep(1 / 20)

            if node == end:
                return
            if node in graphR and graphR[node] not in visited:
                queue.append(graphR[node])

            if node in graphU and graphU[node] not in visited:
                queue.append(graphU[node])

            if node in graphL and graphL[node] not in visited:
                queue.append(graphL[node])

            if node in graphD and graphD[node] not in visited:
                queue.append(graphD[node])




    #########################################
exp=Exp()
pen = Pen()
player=Player()
goal = Goal()
walls=[]
graphR= dict(name='value')
graphU= dict(name='value')
graphL= dict(name='value')
graphD= dict(name='value')


setup_maze(map)

print(graphD)
print(graphL)
print(graphR)
print(graphU)

wn.tracer(0)

while True:
    pass

