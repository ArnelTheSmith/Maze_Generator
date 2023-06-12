from graphics import Window, Point, Line
from cell import Cell
from maze import Maze

win = Window(800, 600)
#cell= Cell(win)
#cell.draw(100, 100)
#cell.draw_move("r")

maze = Maze(40,40,80,win)
maze._create_cells()

win.wait_for_close()