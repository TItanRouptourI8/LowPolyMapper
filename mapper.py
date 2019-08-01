from tkinter import *
from random import randrange

class Map:

    def __init__(self, canvas, cubeX, cubeY, offset):

        self.ground = {}
        self.canvas = canvas
        self.cubeX = cubeX
        self.cubeY = cubeY
        self.offset = offset

    def create_map(self):

        margin = 0.5
        x = 0 + margin
        y = 0 + margin
        offset = self.offset
        while x < self.cubeX:

            while y < self.cubeY :
                self.ground[(x * offset, y * offset)] = 1
                y += 1
            x += 1
            y=0 + margin

        return self.ground

    def read_map(self):
        margin = 0.5
        x = 0 + margin
        y = 0 + margin
        offset = self.offset
        while x < self.cubeX:

            while y < self.cubeY:
                cube_type = self.ground[(x * offset, y * offset)]

                if cube_type == 1:
                    self.canvas.create_rectangle(x*offset, y*offset, x * offset + offset, y*offset + offset, fill='green')
                y += 1
            x += 1
            y=0 + margin

class MapReader:

    def __init__(self, canvas, map):
        self.canvas = canvas
        self.map = map
        self.offset = 10

    def print_map(self, width, height):
        offset = self.offset
        x = 0
        y = 0

        while x < width:

            while y < height:
                painter_type = self.map[(x, y)]
                if painter_type == 1:
                    self.canvas.create_rectangle(x, y, x + offset, y + offset, fill="green")
                y += self.offset
            x += self.offset
            painter_type = self.map[(x, y)]
            if painter_type == 1:
                self.canvas.create_rectangle(x, y, x + offset,y + offset, fill="green")
