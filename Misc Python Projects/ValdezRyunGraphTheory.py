################################################################################
##                          PokePengo                                         ##
##                                                                            ##
##              Programmed by Ryun Valdez 4/23/2015                           ##
##              This program is essentially an engine for graph theory        ##
##              algorithms.                                                   ##
##                                                                            ##
################################################################################
from tkinter import *
c = Canvas(width=500, height=500)
c.pack(expand=YES, fill=BOTH)
import random

class Node():
    objectName = "Node"
    objectNum = 0
    colors = ["lightblue","lightgreen","yellow",
              "orange","red", "darkviolet", "Indigo"]
    def __init__(self, canvas, size, x, y, color, label):
        self.c = canvas
        self.size = size
        self.x = x
        self.y = y
        self.label = label
        self.color = color

        self.tag = Node.objectName + str(Node.objectNum)
        Node.objectNum += 1

        self.visited = 0
        
    def draw(self):
        c.create_oval(self.x-self.size/2,self.y-self.size/2, self.x+self.size-self.size/2,
                    self.y+self.size-self.size/2,fill=self.color,
                      tag=self.tag)
        c.create_text(self.x-(((self.x-self.x)/60)),self.y-(((self.y-self.y)/60)),
                              justify=CENTER, text=str(self.label))
    def connect(self, s2):
        for i in range(1,61):
            c.after(8)
            c.create_line(self.x,self.y, self.x-(i*((self.x-s2.x)/60)),
                          self.y-(i*((self.y-s2.y)/60)), fill="white", tag="line")
            c.update()
            
    def getColor(self):
        print(self.color)
        
    def setColor(self, color):
        self.color = color
        c.itemconfig(self.tag, fill=color)
        c.update()

    def visit(self):
        self.visited += 1
        if self.visited >= 6:
            self.setColor("Indigo")
        else:
            self.setColor(Node.colors[self.visited])
        

class Edge():
    objectName = "Edge"
    objectNum = 0
    
    def __init__(self, canvas, color, cost, width, n1, n2):
        self.c = canvas
        self.color = color
        self.cost = cost
        self.width = width
        self.n1 = n1
        self.n2 = n2

        self.tag = Edge.objectName + str(Edge.objectNum)
        self.boxTag = Edge.objectName + "Box" + str(Edge.objectNum)
        Edge.objectNum += 1

        self.traveled = 0

    def draw(self):
        count = 0
        for i in range(1,61):
            c.after(8)
            if count != 0:
                c.delete("lineSeg"+str(count-1))
            c.create_line(self.n1.x,self.n1.y, self.n1.x-(i*((self.n1.x-self.n2.x)/60)),
                          self.n1.y-(i*((self.n1.y-self.n2.y)/60)), fill=self.color,
                          tag=(self.tag,"edgeLine","lineSeg"+str(count)), width = self.width)
            if i == 30:
                c.create_rectangle(self.n1.x-(i*((self.n1.x-self.n2.x)/60))-10,
                                   self.n1.y-(i*((self.n1.y-self.n2.y)/60)-10),
                                   self.n1.x-(i*((self.n1.x-self.n2.x)/60))+10,
                                   self.n1.y-(i*((self.n1.y-self.n2.y)/60)+10),
                                   tag=(self.boxTag), fill="lightblue")
                                                
                c.create_text(self.n1.x-(i*((self.n1.x-self.n2.x)/60)),
                              self.n1.y-(i*((self.n1.y-self.n2.y)/60)),
                              justify=CENTER, text=str(self.cost), tag=self.tag)
            c.tag_lower("edgeLine")
            count += 1
            c.update()
    def travel(self, n1,n2):
        self.traveled += 1
        self.width = 2+self.traveled*2
        c.itemconfig(self.tag, width=self.width)
        n2.visit()
        c.update()
    def getColor(self):
        print(self.color)
    def setColor(self, color):
        self.color = color
        c.itemconfig(self.tag, fill=color)
        c.itemconfig(self.boxTag, outline=color)
        c.update()
    def setWidth(self, width):
        c.itemconfig(self.tag, width=width)
        c.update()
class Graph():

    def __init__(self, canvas, nodes, edges, matrix):
        self.c = canvas
        self.nodes = nodes
        self.edges = edges
        self.matrix = matrix

        subTotal=0
        for edge in self.edges:
            subTotal=subTotal+edge.cost   
        self.totalCost = subTotal

    def draw(self):
        counter = 0
        self.nodes[0].draw()
        for i in range (len(self.matrix)):
            for j in range (len(self.matrix)):
                if self.matrix[i][j] != 0:
                    edgeCost = self.matrix[i][j]
                    self.edges.append(Edge(canvas=c,color="black", cost=edgeCost,
                                           width=2, n1=self.nodes[i],n2=self.nodes[j]))
                    self.edges[counter].draw()
                    self.nodes[j].draw()
                    counter += 1
                    
    def resetFlags(self):
        for edge in self.edges:
            edge.traveled = 0
            edge.setColor("black")
        for node in self.nodes:
            node.visited = 0
            node.setColor("lightgreen")

    def randPath(self,n1,n2):
        current = n1
        target = n2
        totalCost = 0
        loop = True
        current.visit()
        while loop == True:
            random_index = random.randrange(0,len(self.edges))
            if self.edges[random_index].n1 == current:
                totalCost += self.edges[random_index].cost
                #print(totalCost)
                c.after(1000)
                self.edges[random_index].travel(self.edges[random_index].n1,
                                                self.edges[random_index].n2)
                c.update()
                if self.edges[random_index].n2 == target:
                    c.after(1000)
                    target.setColor("white")
                    c.create_text(250,250,justify=CENTER,
                                  text="Path cost: "+str(totalCost),tag="display")
                    c.update()
                    loop = False
                else:
                    current = self.edges[random_index].n2

            elif self.edges[random_index].n2 == current:
                totalCost += self.edges[random_index].cost
                #print(totalCost)
                c.after(1000)
                self.edges[random_index].travel(self.edges[random_index].n2,
                                                self.edges[random_index].n1)
                c.update()
                if self.edges[random_index].n1 == target:
                    c.after(1000)
                    target.setColor("white")
                    c.create_text(250,250,justify=CENTER,
                                  text="Path cost: "+str(totalCost),tag="display")
                    c.update()
                    loop = False
                else:
                    current = self.edges[random_index].n1                
        


n1 = Node(c,50,250,50, color="lightblue", label=1)
n2 = Node(c,50,380,120, color="lightblue", label=2)
n3 = Node(c,50,450,250, color="lightblue", label=3)
n4 = Node(c,50,380,380, color="lightblue", label=4)
n5 = Node(c,50,250,450, color="lightblue", label=5)
n6 = Node(c,50,120,380, color="lightblue", label=6)
n7 = Node(c,50,50,250, color="lightblue", label=7)
n8 = Node(c,50,120,120, color="lightblue", label=8)


nodeList= [n1,n2,n3,n4,n5,n6,n7,n8]
edgeList = []
Amatrix = [[0,1,0,0,0,0,0,0],  #n1
           [0,0,1,0,0,0,0,0],  #n2
           [0,0,0,1,0,0,0,0],  #n3
           [0,0,0,0,1,0,0,0],  #n4
           [0,0,0,0,0,1,0,0],  #n5
           [0,0,0,0,0,0,1,0],  #n6
           [0,0,0,0,0,0,0,1],  #n7
           [1,0,0,0,0,0,0,0]]  #n8

g1 = Graph(canvas=c, nodes=nodeList, edges=edgeList, matrix=Amatrix)
g1.draw()
g1.randPath(n1,n5)


