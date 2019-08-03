

from tkinter import *
import mapper
# Faut terminer l'integration du canvas
# permettre aux méthods d'acced au autre method
# supprimer les vieux scrpt dans le main
#

class canvas_adapter():

    def __init__(self, Map):
        self.canvas = Canvas(Map, bg="#4c94a1")
        self.canvas.pack(expand=1, fill=BOTH, padx=3, pady=3)
        self.map = mapper.Map(self.canvas, 30, 30, 30)


        #events initialisations

        self.canvas.bind('<Motion>', self.canvas_hover)
        self.canvas.bind('<B3-Motion>', self.map.right_motion)
        self.canvas.bind('<Button-3>', self.map.right_start)
        self.delta = (0,0)
        self.start_right_click = (0,0)
        #painter initialisation

        self.painter = self.canvas.create_oval(5, 5,10, 10, fill="black")
        self.painter_size = IntVar()
        self.painter_type = 0
        self.tree = 1

        #map initialisation


        self.map.init_map()
        self.map.create_map()


    def paint_tree(self):
        self.painter_type = self.tree

    def change_painter_size(self, scalevalue):
        self.canvas.coords(self.painter, 5, 5, 5 + int(scalevalue), 5 + int(scalevalue))
        self.canvas.tag_raise(self.painter)

    def canvas_hover(self, event):
        offset = int(self.painter_size.get())
        self.map.delta = (event.x - self.canvas.canvasx(event.x), event.y - self.canvas.canvasy(event.y))
        self.canvas.coords(self.painter,
                           -self.map.delta[0] + (event.x - offset / 2),
                           -self.map.delta[1] + (event.y - offset / 2),
                           -self.map.delta[0] + (event.x + offset - offset / 2),
                           -self.map.delta[1] + (event.y + offset - offset / 2))


