from unit import Unit
from copy import copy

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
            raise Exception("You are trying to add different units")

    def __sub__(self, other):
        if self.unit.order(self) == self.unit.order(other):
            output = Scalar(self.value - other.value)
            return output
        else:
            raise Exception("You are trying to subtract different units")

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
