from cells import *
from graphics import *
import time



class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        self._create_cells()
        self._break_enterance_and_exit()
        self._mark_entrance_and_exit()

    def _create_cells(self):
        for i in range(self._num_rows):
            row = []
            for j in range(self._num_cols):
                cell = Cell(self._win)
                row.append(cell)
            self._cells.append(row)
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        x1 = self._x1 + j * self._cell_size_x
        y1 = self._y1 + i * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, x2, y1, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
    
    def _break_enterance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False

    def _mark_entrance_and_exit(self):
        if self._win is None:
            return
        
    # Draw entrance marker (top of first cell)
        entrance_line = Line(
            Point(self._x1, self._y1),
            Point(self._x1 + self._cell_size_x, self._y1)
        )
        self._win.draw_line(entrance_line, "green")
    
    # Draw exit marker (bottom of last cell)
        exit_x = self._x1 + (self._num_cols - 1) * self._cell_size_x
        exit_y = self._y1 + self._num_rows * self._cell_size_y
        exit_line = Line(
            Point(exit_x, exit_y),
            Point(exit_x + self._cell_size_x, exit_y)
        )
        self._win.draw_line(exit_line, "red")