from cell import Cell
import math
import time, random
class Maze:
   def __init__(
      self,
      x1,
      y1,
      cell_size,
      win,
      num_rows=5,
      num_cols=5,
   ):
      self._cells= []
      self._x1 = x1
      self._y1 = y1 
      self._num_rows = num_rows
      self._num_cols = num_cols
      self._cell_size = cell_size
      self._win= win

      self._create_cells()
   
   def _create_cells(self):
      for i in range(self._num_cols):
         col_cells = []
         for j in range(self._num_rows):
               col_cells.append(Cell(self._win))
         self._cells.append(col_cells)
      for i in range(self._num_cols):
         for j in range(self._num_rows):
            self._draw_cell(i, j)

   def _draw_cell(self, i, j):
      if self._win is None:
         return
      x = self._x1 + i * self._cell_size
      y = self._y1 + j * self._cell_size
      self._cells[i][j].draw(x, y)
      self._animate()
   
   def _animate(self):
      self._win.redraw()
      time.sleep(0.2)

