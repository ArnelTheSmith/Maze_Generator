from graphics import Window, Point, Line
from cell import Cell

win = Window(800, 600)
cell= Cell(win)
cell.draw(100, 100)
cell.draw_move("r")


win.wait_for_close()