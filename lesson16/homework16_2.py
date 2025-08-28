from abc import abstractmethod, ABC
from math import pi, sqrt, sin


class Figura(ABC):

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Figura):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __setattr__(self, key, value):
        if key in ("length", "width"):
            if not isinstance(value, int):
                raise TypeError(f"{key} type must be INT only")
            else:
                if value <= 0:
                    raise ValueError(f"{key} value cannot be less than 0")

        super().__setattr__(key, value)

    def square(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"This Rectangle instance has Square = {self.square():.2f} and Perimeter = {self.perimeter()}"


class Circle(Figura):
    def __init__(self, radius):
        self.radius = radius

    def __setattr__(self, key, value):
        if key == "radius":
            if not isinstance(value, int):
                raise TypeError(f"{key} type must be INT only")
            else:
                if value <= 0:
                    raise ValueError(f"{key} value cannot be less than 0")

        super().__setattr__(key, value)

    def square(self):
        return pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * pi * self.radius

    def __str__(self):
        return f"This Circle instance has Square = {self.square():.2f} and Perimeter = {self.perimeter():.2f}"


class Rombus(Figura):
    def __init__(self, a, angle_a):
        self.a = a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == "a":
            if not isinstance(value, int):
                raise TypeError(f"{key} value should be INT")
            else:
                if value <= 0:
                    raise ValueError(f"{key} value should be > 0")

        if key == "angle_a":
            if isinstance(value, int):
                if not (0 < value < 180):
                    raise ValueError(f"{key} value should be > 0 and < 180")
            else:
                raise TypeError(f"{key} value should be INT")
        super().__setattr__(key, value)

    def square(self):
        s = self.a ** 2 * sin((self.angle_a * pi) / 180)
        return s

    def perimeter(self):
        return 4 * self.a

    def __str__(self):
        return f"This Rombus instance has Square = {self.square():.2f} and Perimeter = {self.perimeter()}"


rect = Rectangle(5, 6)
circ = Circle(7)
romb = Rombus(10,30)

figures = [rect,circ,romb]
for f in figures:
    print(f)

