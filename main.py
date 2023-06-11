from graphics import Window, Point, Line, Cell

cell_list= []

pos={"x1":50,"y1":50,"x2":100,"y2":100}

for n in range(6):
    n = Cell(pos["x1"]+(n*100), pos["y1"])
    cell_list.append(n)
    
win = Window(800, 600)
cell = Cell(100,100)


for n in range(6):
    win.draw_cell(cell_list[n])

win.wait_for_close()