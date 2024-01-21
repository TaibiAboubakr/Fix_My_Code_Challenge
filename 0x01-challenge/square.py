#!/usr/bin/python3
"""width
Rectangle Class
"""


class Rectangle:
    """ class Rectangle """

    def __init__(self, width=0, height=0, **kwargs):
        """ Initialize the Rectanglewidth
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Retrieve the width (side length) of the Rectangle.

        Returns:
            int: The width of the Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width
        Set the width (side length) of the Rectangle.

        Args:
            value (int): The new width for the Rectangle.

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
        Retrieve the height (side length) of the Rectangle.

        Returns:
            int: The height of the Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """width
        Set the height (side length) of the Rectangle.

        Args:
            value (int): The new height for the Rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def area_of_my_Rectangle(self):
        """ Area of the Rectangle """
        return self.__width * self.__height

    def PermiterOfMyRectangle(self):
        """ Permiter of a Rectangle """
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ String representation of the Rectangle """
        return "{}/{}".format(self.__width, self.__height)


if __name__ == "__main__":

    s = Rectangle(12, 9)
    print(s)
    print(s.area_of_my_Rectangle())
    print(s.PermiterOfMyRectangle())
