from tkinter import *
from loadImg import loadimg
from draw import canvas_adapter
#load the img
loader = loadimg()


#tkinter init
window = Tk()
window.title("LowPolyMapper")
window.iconbitmap("icon.ico")
window.geometry("720x480")

root1 = PanedWindow(window, orient = HORIZONTAL)
root1.pack(fill = BOTH, expand = 1)


painter_size = IntVar()

def getwindow_width():
    window.update()
    return window.winfo_width()

def getwindow_height():
    window.update()
    return window.winfo_height()

def get_options_panel_height():
    ToolBox.update()
    return ToolBox.winfo_height()

def get_options_panel_width():
    ToolBox.update()
    return ToolBox.winfo_width()



#Creating Options window
ToolBox = Frame(window, width =(getwindow_width() / 10) * 3)
ToolBox.pack(fill=BOTH, expand=1, padx=2, pady=2)
root1.add(ToolBox)
root1.pack()
# Options handling


#Creating Map window
Map = Frame(root1, bg="white", borderwidth=2, relief=GROOVE)
Map.pack(side=RIGHT, padx=5, pady=5)
root1.add(Map)
root1.pack()
# Add Title
Label(ToolBox, text="Toolbox", anchor='n', borderwidth=2, relief=RAISED).pack(padx=2, pady=2)
Label(Map, text="Map", anchor='n').pack(padx=2, fill=X)

canvAdapter = canvas_adapter(Map)

def change_painter_size(ScaleValue):
    offset = int(painter_size.get())
    canvas.coords(painter, 5, 5, 5 + int(ScaleValue), 5 + int(ScaleValue))


def add_painters():
    PainterFrame = LabelFrame(ToolBox, text="Painters", padx = 2, pady = 2)
    PainterFrame.pack(side=TOP, expand=1, fill=BOTH)
    Tree = Button(PainterFrame, text="Tree", relief=RAISED, anchor='n').pack(side=TOP)


def add_painter_options():
    painter_options_frame = LabelFrame(ToolBox, text="Options", padx = 2, pady = 2)
    painter_options_frame.pack(side=BOTTOM, expand=1, fill=BOTH)
    Scale(painter_options_frame, orient = HORIZONTAL, variable = canvAdapter.painter_size, command= canvAdapter.change_painter_size).pack(fill=X)

def add_options():
    add_painters()
    add_painter_options()

def canvas_hover(event):
    offset = int(painter_size.get())

    canvas.coords(painter, event.x - offset/2, event.y - offset/2, event.x + offset - offset/2, event.y + offset - offset/2)
    #print(event.x + " " + event.y)




canvas = Canvas(Map, bg="#4c94a1")

canvas.pack(expand=1, fill=BOTH, padx=3, pady=3)
canvas.bind('<Motion>', canvas_hover)
painter = canvas.create_oval(5, 5,10, 10, fill="black")
add_options()

window.mainloop()