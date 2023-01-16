#!/usr/bin/python3
""" Mdoule that contain class Rectangle,
inheritance of class Base
"""
from models.base import Base
class Rectangle(Base):
    """ initializes instances"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
        
    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area value of rectangle"""
        return self.width * self.height

    def display(self):
        """print in stdout the rectangle"""
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"
        print(rectangle, end='')

    def __str__(self):
        """str method"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width} / {self.__height}"

    def update(self, *args, **kwargs):
        """assign an argument to each attribute"""
        if args is not None and len(args) is not 0:
            list_a = ['id', 'width', 'height', 'x', 'y']
            for a in range(len(args)):
                setattr(self, list_a[a], args[a])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return the dictionary of a rectangle"""
        list_a = ['id', 'width', 'height', 'x', 'y']
        dict_a = {}

        for key in list_a:
            dict_a[key] = getattr(self, key)
            
        return dict_a
