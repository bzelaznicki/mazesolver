from graphics import *
from cells import *



def main():
    win = Window(800, 600)
    c1 = Cell(win) 
    c1.draw(100, 200, 100, 200)


    c2 = Cell(win)
    c2.has_bottom_wall = False
    c2.draw(200, 300, 100, 200)




    win.wait_for_close()

main()