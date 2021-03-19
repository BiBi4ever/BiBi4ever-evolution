from tkinter import *
from grid import *

root = Tk()
var = StringVar()

def update_label():
    g = Grid()
    coords = [x for x in itertools.product(range(30), range(30))]
    live_cells = random.sample(coords, 20)
    g.populate(live_cells)
    var.set(g.display())
    root.update()

def create_widgets():
    label = Label(root, textvariable=var)
    start = Button(root, text="Start", command=update_label)
    finish = Button(root, text="Finish", command=root.destroy)

def pack_widgets():
    label.pack()
    start.pack()
    finish.pack()

root.minsize(width=400, height=400)
w = root.winfo_reqwidth()
h = root.winfo_reqheight()
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('+%d+%d' % (x, y)) ## this part allows you to only change the location

create_widgets()
pack_widgets()


root.mainloop()
