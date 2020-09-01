from copy import copy
from unit import Unit
from errors import WrongDimensionsError, WrongUnitsError

class Scalar:
    """
    class for Scalar instances
    """
    def __init__(self, val=0, name="Scalar"):
        self.value = val
        self.unit = Unit()
        self.name = name

    def __repr__(self):
        """
        how the object is represented
        """
        return f"{self.name}: {self.value} {self.unit}"

    def __add__(self, other):
        "handles addition"
        if self.unit.order(self) == self.unit.order(other):
            output = Scalar(self.value + other.value)
            return output
        else:
            raise WrongUnitsError("You are trying to add different units")

    def __sub__(self, other):
        if self.unit.order(self) == self.unit.order(other):
            output = Scalar(self.value - other.value)
            return output
        else:
            raise WrongUnitsError("You are trying to subtract different units")

    def __mul__(self, other):
        """
        handles dot product
        """
        if type(other) != type(self):
            obj = copy(other)
            obj.x *= self.value
            obj.y *= self.value
            obj.unit *= self.unit
            return obj
        else:
            obj = Scalar(self.value, other.value)
            obj.unit = self.unit * other.unit


    def __truediv__(self, other):
        if type(other) == type(Scalar()):
            output = Scalar()
            output.value = self.value / other.value
            output.unit = self.unit / other.unit
            return output
        else:
            output = Scalar()
            output.value = self.value / other
            output.unit = self.unit
            return output

    def __rtruediv__(self, other):
        output = Scalar()
        output.value = other / self.value
        output.unit = Unit() / self.unit
        return output


class Vector:
    def __init__(self, x=0, y=0, z=0, name="Vector"):
        self.x = x
        self.y = y
        self.z = z
        self.initial = (x, y)
        self.unit = Unit()
        self.name = name

    def __repr__(self):
        return f"{self.name}: [{self.x}, {self.y}, {self.z}]{self.unit}"


    def reset(self, x=True, y=True):
        if x:
            self.x, _ = self.initial
        if y:
            _, self.y = self.initial

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __add__(self, other):
        if self.same_type(other):
            obj = copy(self)
            obj.x = self.x + other.x
            obj.y = self.y + other.y
            return obj
        else:
            raise WrongDimensionsError("you are trying to add two different-sized vectors")

    def __sub__(self, other):
        if self.same_type(other):
            obj = copy(self)
            obj.x = self.x - other.x
            obj.y = self.y - other.y
            return obj
        else:
            raise WrongDimensionsError("you are trying to subtract two different-sized vectors")

    def __mul__(self, other):
        if type(other) == type(Vector()):
            output = 0
            output += self.x * other.x
            output += self.y * other.y
            return output

        if type(other) == type(Scalar()):
            obj = copy(self)
            obj.x *= other.value
            obj.y *= other.value
            return obj

    def __truediv__(self, other):
        if type(other) == type(Scalar()):
            v = Vector(self.x / other.value, self.y / other.value)
            v.unit = self.unit / other.unit
        else:
            v = Vector(self.x / other, self.y / other)
            v.unit = self.unit
        return v

    def cross(self, other):
        if type(other) == type(Vector()):
            output = Vector()
            output.x = self.y * other.z - self.z * other.y
            output.y = other.x * self.z - self.x * other.z
            output.z = self.x * other.y - other.x * self.y
            output.unit = self.unit * other.unit
            return output
        else:
            raise Exception("Invalid Operation")

    def same_type(self, other):
        if type(self) == type(other) and self.unit.order() == other.unit.order():
            return True
        else:
            return False

# class Velocity(Vector):
#     def __init__(self, x, y):
#         super().__init__(x, y)
#         self.name = "Velocity"
#         self.unit = Unit()
#         self.unit.numerator.append("m")
#         self.unit.denominator.append("s")
#
# class Position(Vector):
#     def __init__(self, x, y):
#         super().__init__(x, y)
#         self.name = "Position"
#         self.unit = Unit("m")


#
# r1 = Vector(3, 4)
# r2 = Vector(5, 6)
# r3 = Vector(7, 2)
# t = Scalar(1)
# t.unit.add("s")
# t.name = "Time"
# for vec in [r1, r2, r3]:
#     vec.unit.add("m")
#     vec.name = "Position"
#
# m = Scalar(3)
# m.name = "mass"
# m.unit.add("kg")
#
# v2 = (r3 - r2) / t
# v1 = (r2 - r1) / t
# p1 = m * v1
# p2 = m * v2
#
# a = (v2 - v1) / t
#
# F = m * a
#
# a.name = "Acceleration"
#
# F.name = "Force"
#
# for vec in [v1, v2]:
#     vec.name = "Velocity"
#
# for vec in [p1, p2]:
#     vec.name = "Momentum"
