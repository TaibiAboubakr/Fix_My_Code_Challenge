#!/usr/bin/python3
"""Square Class
"""


class square:
    """ Class square """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initialize the squarewidth
        Args:
            width (int): The width of the new square.
            height (int): The height of the new square.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def width(self):
        """
        Retrieve the width (side length) of the square.

        Returns:
            int: The width of the square.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width
        Set the width (side length) of the square.

        Args:
            value (int): The new width for the square.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height (side length) of the square.

        Returns:
            int: The height of the square.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """width
        Set the height (side length) of the square.

        Args:
            value (int): The new height for the square.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def area_of_my_square(self):
        """ Area of the square """
        return self.__width * self.__height

    def PermiterOfMySquare(self):
        """ Permiter of a Square """
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ String representation of the square """
        return "{}/{}".format(self.__width, self.__height)


if __name__ == "__main__":

    s = Square(12, 9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
