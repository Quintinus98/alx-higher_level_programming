#!/usr/bin/python3
"""Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """Represents a Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes class Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves and sets width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves and sets height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves and sets x"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves and sets y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return (self.__height * self.__width)

    def display(self):
        """prints the Rectangle instance with the character #"""
        if self.__y != 0:
            print("\n" * self.__y, end="")
        for i in range(0, self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width, end="\n")

    def __str__(self):
        """String documentation for rectangle"""
        doc = "[{}] ({}) ".format(self.__class__.__name__, self.id)
        xy = "{}/{} ".format(self.x, self.y)
        return (doc + xy + "- {}/{}".format(self.width, self.height))

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args is not None and len(args) != 0:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle"""
        attrs = ['id', 'width', 'height', 'x', 'y']
        dict_attrs = {}
        for k in attrs:
            dict_attrs[k] = getattr(self, k)
        return dict_attrs
