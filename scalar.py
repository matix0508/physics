from unit import Unit
from copy import copy

class Scalar:
    def __init__(self, val=0, name=None):
        self.value = val
        self.unit = Unit()
        self.name = name

    def __repr__(self):
        return f"{self.name}: {self.value}{self.unit}"

    def __add__(self, other):
        if self.unit.order(self) == self.unit.order(other):
            output = Scalar(self.value + other.value)
            return output

    def __sub__(self, other):
        if self.unit.order(self) == self.unit.order(other):
            output = Scalar(self.value - other.value)
            return output

    def __mul__(self, other):
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
        output = Scalar(self)
        output.value = self.value / other.value
        output.unit = self.unit / other.unit
        return output
