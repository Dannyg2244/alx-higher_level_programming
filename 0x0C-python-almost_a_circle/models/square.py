#!/usr/bin/python3
"""A square class module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes instances"""
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """size getter"""
        return self.__width

    @size.setter
    def size(width, value):
        """size setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be grater than 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """ update method """
        if args is not None ans len(args) is not 0:
            list_a = ['id', 'size', 'x', 'y']
            for a in range(len(args)):
                if list_a[a] == 'size':
                    setattr(self, 'width', args[a])
                    setattr(self, 'height', args[a])
                else:
                    setattr(self, list_a[a], args[a]):

        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """return the dictionary representation of a square"""
        dict_rep = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return dict_rep
