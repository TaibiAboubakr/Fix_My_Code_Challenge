#!/usr/bin/python3
"""Square Class
"""


class Square:
    
    
    def __init__(self, width=0, height=0):
        """
        Initialize the square.

        Args:
            width (int): The width of the square.
            height (int): The height of the square.
        """
        self.width = width
        self.height = height

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
        """
        Set the width (side length) of the square.

        Args:
            value (int): The new width for the square.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        self.__validate_dimension(value, "width")
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
        """
        Set the height (side length) of the square.

        Args:
            value (int): The new height for the square.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        self.__validate_dimension(value, "height")
        self.__height = value

    def __validate_dimension(self, value, dimension_name):
        """
        Validate the dimension value.

        Args:
            value: The dimension value to be validated.
            dimension_name (str): The name of the dimension being validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{dimension_name} must be an integer")
        if value < 0:
            raise ValueError(f"{dimension_name} must be >= 0")

    def area_of_my_square(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__width * self.__height

    def perimeter_of_my_square(self):
        """
        Calculate the perimeter of the square.

        Returns:
            int: The perimeter of the square.
        """
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        String representation of the square.

        Returns:
            str: A formatted string representing the square.
        """
        return f"{self.__width}/{self.__height}"


if __name__ == "__main__":
    s = Square(12, 9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
