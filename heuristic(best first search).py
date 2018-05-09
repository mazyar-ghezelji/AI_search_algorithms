import turtle
import time
from collections import deque
import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]




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
                graph_cost[(screenx,screeny)]=1
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
                graph_cost[(screenx,screeny)]=3


    ############## algorithm #################
    """""
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
                stack.append(graphD[node])
"""""

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    print(graph_cost)

    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = dict(name='value')
    cost_so_far = dict(name='value')
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()
        player.go(current[0],current[1])
        time.sleep(1 / 20)

        if current == end:
            break




        if current in graphD and graphD[current] in graph_cost:
            if current in cost_so_far:
                new_cost = cost_so_far[current] + graph_cost[graphD[current]]
            else:
                new_cost=graph_cost[graphD[current]]
            if graphD[current] not in cost_so_far or new_cost < cost_so_far[graphD[current]]:
                cost_so_far[graphD[current]] = new_cost
                priority = heuristic(end,graphD[current])
                frontier.put(graphD[current], priority)
                came_from[graphD[current]] = current





        if current in graphL and graphL[current] in graph_cost:
            if current in cost_so_far:
                new_cost = cost_so_far[current] + graph_cost[graphL[current]]
            else:
                new_cost=graph_cost[graphL[current]]
            if graphL[current] not in cost_so_far or new_cost < cost_so_far[graphL[current]]:
                cost_so_far[graphL[current]] = new_cost
                priority =  heuristic(end,graphL[current])
                frontier.put(graphL[current], priority)
                came_from[graphL[current]] = current




        if current in graphU and graphU[current] in graph_cost:
            if current in cost_so_far:
                new_cost = cost_so_far[current] + graph_cost[graphU[current]]
            else:
                new_cost=graph_cost[graphU[current]]
            if graphU[current] not in cost_so_far or new_cost < cost_so_far[graphU[current]]:
                cost_so_far[graphU[current]] = new_cost
                priority = heuristic(end,graphU[current])
                frontier.put(graphU[current], priority)
                came_from[graphU[current]] = current





        if current in graphR and graphR[current] in graph_cost:
            if current in cost_so_far:
                new_cost = cost_so_far[current] + graph_cost[graphR[current]]
            else:
                new_cost=graph_cost[graphR[current]]
            if graphR[current] not in cost_so_far or new_cost < cost_so_far[graphR[current]]:
                cost_so_far[graphR[current]] = new_cost
                priority =  heuristic(end,graphR[current])
                frontier.put(graphR[current], priority)
                came_from[graphR[current]] = current
    #########################################

pen = Pen()
exp=Exp()
player=Player()
goal = Goal()
walls=[]
graphR= dict(name='value')
graphU= dict(name='value')
graphL= dict(name='value')
graphD= dict(name='value')

graph_cost= dict(name='value')


setup_maze(map)
''''
print(graphD)
print(graphL)
print(graphR)
print(graphU)
'''
print(graph_cost)
wn.tracer(0)

while True:
    pass

