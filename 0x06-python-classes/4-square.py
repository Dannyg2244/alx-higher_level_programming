#!/usr/bin/python3
class Square():
    def ___init__(self, size=0):
        @property
        def size(self):
            return self.__size

        @size.setter
        def siize(self, value):
            if (type(value) is not int):
                raise TypeError("size must be an integer")
            elif (value < 0):
                raise ValueError("size must be >= 0")
            self.__size = value

        def area(self):
            return self.__size ** 2
