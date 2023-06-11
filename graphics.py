from tkinter import Tk, BOTH, Canvas
class Window:

    def __init__(self,width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white",  width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False
        
    def draw_line(self,line, fill_color="black"):
        line.draw(self.__canvas,fill_color)

    def draw_cell(self,cell, fill_color="black"):
        cell.draw(self.__canvas,fill_color)
    



class Point:
        def __init__(self,x,y):
            self.x = x
            self.y = y
class Line:
        def __init__(self,p1,p2):
            self.p1 = p1
            self.p2 = p2
        def draw(self,canvas,fill_color="black"):
            canvas.create_line( self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
            canvas.pack(fill=BOTH, expand=1)
class Cell:
        def __init__(self,_x,_y,l_wall=True,r_wall=True,t_wall=True,b_wall=True,_win=False):
            self.l_wall = l_wall
            self.r_wall = r_wall
            self.t_wall = t_wall
            self.b_wall = b_wall
            self._x = _x
            self._x2 = _x + 100
            self._y= _y
            self._y2 = _y + 100 
            self._win= _win

        def draw(self,canvas, fill_color="black"):
            if self.l_wall:
                wall=Line(Point(self._x,self._y),Point(self._x,self._y+100))
                wall.draw(canvas)
            if self.r_wall:
                wall=Line(Point(self._x+100,self._y),Point(self._x+100,self._y+100))
                wall.draw(canvas)
            if self.t_wall:
                wall=Line(Point(self._x,self._y),Point(self._x+100,self._y))
                wall.draw(canvas)
            if self.b_wall:
                wall=Line(Point(self._x,self._y+100),Point(self._x+100,self._y+100))
                wall.draw(canvas)





        
        
        
        
