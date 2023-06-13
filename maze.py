from cell import Cell
import math
import time, random
class Maze:
   def __init__(
      self,
      x1,
      y1,
      cell_size,
      win=None,
      num_rows=4,
      num_cols=4,
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
      self._break_entrance_and_exit()

   def _draw_cell(self, i, j):
      if self._win is None:
         return
      x = self._x1 + i * self._cell_size
      y = self._y1 + j * self._cell_size
      self._cells[i][j].draw(x, y, self._cell_size)
      self._animate()
   
   def _animate(self):
      self._win.redraw()
      time.sleep(0.15)
   def _break_entrance_and_exit(self):
      mtx_x=self._num_cols-1
      mtx_y=self._num_rows-1
      br_x=mtx_x * self._cell_size
      br_y=mtx_y * self._cell_size

      self._cells[0][0] = Cell(self._win, l_wall=False, t_wall=False) 
      self._cells[mtx_x][mtx_y] = Cell(self._win, r_wall=False, b_wall=False) 
      
      self._draw_cell(0, 0)
      self._draw_cell(mtx_x, mtx_y)
      
      
      



