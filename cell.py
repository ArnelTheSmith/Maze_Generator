from graphics import Point, Line
class Cell:
        def __init__(self,win,l_wall=True,r_wall=True,t_wall=True,b_wall=True):
            self.size = None
            self._visited = False
            self.l_wall = l_wall
            self.r_wall = r_wall
            self.t_wall = t_wall
            self.b_wall = b_wall
            self._x = None
            self._x2 = None
            self._y= None
            self._y2 = None
            self._win= win
                

        def draw(self,x,y, size):
            self.size =  size
            self._x = x
            self._x2 = x + self.size
            self._y= y
            self._y2 = y + self.size

            #Draw existing walls
            if self.l_wall:
                wall=Line(Point(x,y),Point(x,y+self.size))
                self._win.draw_line(wall)
            else:
                wall=Line(Point(x,y),Point(x,y+self.size))
                self._win.draw_line(wall,"white")

            if self.r_wall:
                wall=Line(Point(x+self.size,y),Point(x+self.size,y+self.size))
                self._win.draw_line(wall)
            else:
                wall=Line(Point(x+self.size,y),Point(x+self.size,y+self.size))
                self._win.draw_line(wall,"white")
            
            if self.t_wall:
                wall=Line(Point(x,y),Point(x+self.size,y))
                self._win.draw_line(wall)
            else:
                wall=Line(Point(x,y),Point(x+self.size,y))
                self._win.draw_line(wall,"white")
            
            if self.b_wall:
                wall=Line(Point(x,y+self.size),Point(x+self.size,y+self.size))
                self._win.draw_line(wall)
            else:
                wall=Line(Point(x,y+self.size),Point(x+self.size,y+self.size))
                self._win.draw_line(wall,"white")
        
        def draw_move(self,to_cell):
            mid_p = Point(((self._x * 2) + self.size)/2, ((self._y * 2) + self.size)/2)
            if to_cell == "l":
                line = Line(mid_p, mid_p.translateX(-self.size))
                self._win.draw_line(line)
            if to_cell == "r":
                line = Line(mid_p,mid_p.translateX(self.size))
                self._win.draw_line(line)
            if to_cell == "t":
                line = Line(mid_p,mid_p.translateY(-self.size))
                self._win.draw_line(line)
            if to_cell == "b":
                line = Line(mid_p,mid_p.translateY(self.size))
                self._win.draw_line(line)