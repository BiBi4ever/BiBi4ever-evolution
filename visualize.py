from tkinter import *
from grid import *

## UTILS ##
def update_label(content):
    var.set(content)
    root.update()

def create_widgets(content):
    global label, start, finish
    label = Label(root, textvariable=var)
    start = Button(root, text="Start", command=update_label(content))
    finish = Button(root, text="Finish", command=root.destroy)

def pack_widgets(*args):
    label.pack()
    start.pack()
    finish.pack()

def center_window():
    w = root.winfo_reqwidth()
    h = root.winfo_reqheight()
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('+%d+%d' % (x, y)) ## this part allows you to only change the location

## MAIN ##
root = Tk()
var = StringVar()

root.minsize(width=400, height=400)
g = Grid()
coords = [x for x in itertools.product(range(30), range(30))]
live_cells = random.sample(coords, 20)
g.populate(live_cells)

center_window()
create_widgets(g.display())
pack_widgets()
root.mainloop()
