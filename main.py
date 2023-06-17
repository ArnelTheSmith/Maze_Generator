from graphics import Window, Point, Line
from cell import Cell
from maze import Maze

win = Window(850, 750)
#cell= Cell(win)
#cell.draw(100, 100)
#cell.draw_move("r")

maze = Maze(50,50,60,win)
maze._create_cells()

win.wait_for_close()