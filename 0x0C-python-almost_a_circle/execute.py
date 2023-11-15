#!/usr/bin/python3
""" 18-main """
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]
    
    Base.draw(list_rectangles_input, list_squares_input)