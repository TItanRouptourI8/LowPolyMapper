from tkinter import *
from random import randrange


#continuer l'integration du delta.
#ajouter une mémoire  pour les events de la souris
#le draw de la map doit aller dans un thread car bcpppp trop long



class Map:

    def __init__(self, canvas, cubeX, cubeY, offset):

        self.ground = {}
        self.entities = {}
        self.start_right_click = (0,0)
        self.delta = (0,0)
        self.canvas = canvas
        self.cubeX = cubeX
        self.cubeY = cubeY
        self.offset = offset

    def init_map(self):

        margin = 0.5
        x = 0 + margin
        y = 0 + margin
        offset = self.offset
        while x < self.cubeX:

            while y < self.cubeY :
                self.ground[(x, y)] = 1
                y += 1
            x += 1
            y=0 + margin

        return self.ground

    def update_offset(self, offset):
        self.offset = int(offset)
        self.update_map()

    def create_map(self):
        margin = 0.5
        x = 0 + margin
        y = 0 + margin
        offset = self.offset
        while x < self.cubeX:

            while y < self.cubeY:
                cube_type = self.ground[(x, y)]

                if cube_type == 1:
                    self.entities[(x, y)] = self.canvas.create_rectangle(self.delta[0] + x*offset, self.delta[1] + y*offset, self.delta[0] + x * offset + offset, self.delta[1] + y*offset + offset, fill='green')
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
                    self.canvas.coords(cube_entity,  self.delta[0] + x*offset, self.delta[1] + y*offset, self.delta[0] + x * offset + offset, self.delta[1] + y*offset + offset)
                y += 1
            x += 1
            y=0 + margin



    def right_only(self, event):
        self.start_right_click = (event.x, event.y)



    def right_motion(self, event):
        self.delta = (event.x - self.start_right_click[0], event.y - self.start_right_click[1])
        self.update_map()

