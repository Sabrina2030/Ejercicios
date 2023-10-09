import math

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("El radio debe ser un número positivo")
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        if radius <= 0:
            raise ValueError("El radio debe ser un número positivo")
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def __mul__(self, n):
        if n <= 0:
            raise ValueError("La multiplicación debe ser por un número positivo")
        return Circle(self.radius * n)

    def __str__(self):
        return f"Círculo con radio {self.radius}"

