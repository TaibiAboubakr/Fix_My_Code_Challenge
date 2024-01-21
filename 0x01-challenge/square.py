#!/usr/bin/python3
"""size
Square Class
"""


class Square:
    """ class square """

    def __init__(self, size=0, **kwargs):
        """ Initialize the squaresize
        Args:
            size (int): The size of the new square.
            height (int): The height of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieve the size (side length) of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size
        Set the size (side length) of the square.

        Args:
            value (int): The new size for the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be > 0")
        self.__size = value

    def area_of_my_square(self):
        """ Area of the square """
        return self.__size * self.__size

    def PermiterOfMySquare(self):
        """ Permiter of a Square """
        return (self.__size * 4)

    def __str__(self):
        """ String representation of the square """
        return "{}/{}".format(self.__size, self.__size)


if __name__ == "__main__":

    s = Square(12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
