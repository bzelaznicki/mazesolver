from graphics import *


def main():
    win = Window(800, 600)
    line1 = Line(Point(100, 100), Point(200, 200))  
    line2 = Line(Point(200, 200), Point(300, 100))   

    win.draw_line(line1, "red")   
    win.draw_line(line2, "blue")
    win.wait_for_close()

main()