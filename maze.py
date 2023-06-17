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
      num_rows=6,
      num_cols=6,
      seed=None
   ):
      if seed != None:
         random.seed(seed)
         
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
      self._break_walls_r(0,0)

   def _draw_cell(self, i, j):
      if self._win is None:
         return
      x = self._x1 + i * self._cell_size
      y = self._y1 + j * self._cell_size
      self._cells[i][j].draw(x, y, self._cell_size)
      self._animate()
   
   def _animate(self):
      self._win.redraw()
      time.sleep(0.025)
   
   def _break_walls_r(self, i,j):

      self._cells[i][j].visited = True

      exit_found = False
      while True:
         next_index_list = []

         possible_direction_indexes = 0

         #determine which cell(s) to visit next

         #left
         if i > 0 and not self._cells[i-1][j].visited:
            next_index_list.append((i-1, j))
            possible_direction_indexes += 1
         
         #right
         if i < self._num_cols -1 and not self._cells[i+1][j].visited:
            next_index_list.append((i+1, j))
            possible_direction_indexes += 1

         #top
         if j > 0 and not self._cells[i][j-1].visited:
            next_index_list.append((i, j-1))
            possible_direction_indexes += 1 
         
         #bottom
         if j < self._num_rows -1 and not self._cells[i][j+1].visited:
            next_index_list.append((i, j+1))
            possible_direction_indexes += 1
         
         #no possible moves 

         if possible_direction_indexes == 0:
            self._draw_cell(i, j)
            return   

         direction_index = random.randrange(possible_direction_indexes)
         next_index = next_index_list[direction_index]
         print([i,j] ,next_index)

         #right
         if next_index[0] == i +  1:
            self._cells[i][j].r_wall = False
            self._cells[i+1][j].l_wall = False
         #left
         if next_index[0] == i - 1:
            self._cells[i][j].l_wall = False
            self._cells[i-1][j].r_wall = False
         #top
         if next_index[1] == j - 1:
            self._cells[i][j].t_wall = False
            self._cells[i][j-1].b_wall = False
         #bottom
         if next_index[1] == j + 1:
            self._cells[i][j].b_wall = False
            self._cells[i][j+1].t_wall = False

         self._break_walls_r(next_index[0] ,next_index[1])
      

   def _break_entrance_and_exit(self):
      mtx_x=self._num_cols-1
      mtx_y=self._num_rows-1
      br_x=mtx_x * self._cell_size
      br_y=mtx_y * self._cell_size

      self._cells[0][0].t_wall = False
      self._draw_cell(0, 0)
      self._cells[mtx_x][mtx_y].b_wall= False 
      self._draw_cell(mtx_x, mtx_y)
      
      
      



