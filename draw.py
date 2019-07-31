
from threading import Thread
from tkinter import *
# Faut terminer l'integration du canvas
# permettre aux méthods d'acced au autre method
# supprimer les vieux scrpt dans le main
#

class canvas_adapter:

    def __init__(self, Map):
        self.canvas = Canvas(Map, bg="#4c94a1")

        self.canvas.pack(expand=1, fill=BOTH, padx=3, pady=3)
        self.painter = self.canvas.create_oval(5, 5,10, 10, fill="black")
        self.painter_size = IntVar()
        self.painter_type = None



    def change_painter_size(self, ScaleValue):
        self.canvas.coords(self.painter, 5, 5, 5 + int(ScaleValue), 5 + int(ScaleValue))

    def canvas_hover(self, event):
        offset = int(self.painter_size.get())

        self.canvas.coords(self.painter, event.x - offset / 2, event.y - offset / 2, event.x + offset - offset / 2,
                      event.y + offset - offset / 2)