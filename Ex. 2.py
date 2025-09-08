import math
import unittest


class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_angle(self):
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0]**2 +sides[1]**2, sides[2]**2, rel_tol=1e-9)


def calculate_area(shape: Shape):
    return shape.area()


class TestShapes(unittest.TestCase):

    def test_circle_area(self):
        c = Circle(3)
        expected = math.pi * 9
        self.assertAlmostEqual(c.area(), expected)

    def test_triangle_area(self):
        t = Triangle(3, 4, 5)
        self.assertAlmostEqual(t.area(), 6)

    def test_triangle_iaa_angle(self):
        t = Triangle(3, 4, 5)
        self.assertTrue(t.is_right_angle())
        t2 = Triangle(4, 4, 5)
        self.assertFalse(t2.is_right_angle())

    def test_calculate_area_function(self):
        c = Circle(2)
        t = Triangle(3, 4, 5)
        self.assertAlmostEqual(calculate_area(c), math.pi * 4)
        self.assertAlmostEqual(calculate_area(t), 6)


if __name__ == "__main__":
    unittest.main()