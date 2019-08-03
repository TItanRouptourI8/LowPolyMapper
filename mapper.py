from tkinter import *
from random import randrange

#delta pour la position cu painter a integrer
#le zoom est pas encore top la c'est pas cool



class Map:

    def __init__(self, canvas, cubeX, cubeY, offset):

        self.ground = {}
        self.entities = {}
        self.canvas = canvas
        self.cubeX = cubeX
        self.cubeY = cubeY
        self.offset = offset
        self.start = (0, 0)
        self.delta = (0, 0)

    def init_map(self):

        margin = 0.5
        x = 0 + margin
        y = 0 + margin
        while x < self.cubeX:

            while y < self.cubeY :
                self.ground[(x, y)] = 1
                y += 1
            x += 1
            y=0 + margin

        return self.ground

    def update_offset(self, offset):
        self.canvas.scale("all",0,0,3, 3)
        #self.update_map()

    def create_map(self):
        margin = 0.5
        x = 0 + margin
        y = 0 + margin
        offset = self.offset
        while x < self.cubeX:

            while y < self.cubeY:
                cube_type = self.ground[(x, y)]

                if cube_type == 1:
                    self.entities[(x, y)] = self.canvas.create_rectangle(x*offset, y*offset, x * offset + offset, y*offset + offset, fill='green')
                y += 1
            x += 1
            y = 0 + margin

    def update_map(self):
        margin = 0.5
        x = 0 + margin
        y = 0 + margin
        offset = self.offset
        while x < self.cubeX:

            while y < self.cubeY:
                cube_type = self.ground[(x, y)]
                cube_entity = self.entities[(x, y)]
                if cube_type == 1:
                    self.canvas.coords(cube_entity, x*offset, y*offset, x * offset + offset, y*offset + offset)
                y += 1
            x += 1
            y=0 + margin



    def right_start(self, event):
        self.canvas.scan_mark(event.x, event.y)
        self.start = (self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))




    def right_motion(self, event):
        self.delta = (event.x - self.canvas.canvasx(event.x), event.y - self.canvas.canvasy(event.y))
        print(self.delta[0])
        self.canvas.scan_dragto(event.x, event.y, gain=1)

