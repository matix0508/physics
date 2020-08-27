from copy import copy

class Unit:
    units_to_short = {
        "metr": "m",
        "second": "s",
        "kilogram": "kg",
        "newton": "(kg * m)/(s^2)"
    }

    def __init__(self, name=None):
        self.numerator = []
        self.denominator = []
        self.short = None
        if name:
            self.numerator.append(self.units_to_short[name])

    def reduce(self):
        to_kill = []
        for item in self.numerator:
            if item in self.denominator:
                to_kill.append(item)
                # print(f"[DEBUG1]:: {to_kill}")
                self.denominator.remove(item)
                # print(f"[DEBUG2]:: {to_kill}")
        # print(f"[DEBUG3]:: {to_kill}")
        for item in to_kill:
            self.numerator.remove(item)

    def __repr__(self):
        self.reduce()
        output = ""

        if len(self.numerator) == 0 and len(self.denominator) != 0:
            output += "1"

        if len(self.numerator) > 1 and len(self.denominator) > 0:
            output = "("
        lst = []
        for unit in self.numerator:
            if unit not in lst:
                count = self.numerator.count(unit)
                lst.append(unit)
                if count > 1:
                    output += f"{unit}^{count} "
                else:
                    output += unit + " "
        if output[-1] == " ":
            output = output[:-1]
        if len(self.numerator) > 1 and len(self.denominator) > 0:
            output += ")"


        if self.denominator:
            output += "/"

        if len(self.denominator) > 1:
            output += "("

        lst = []
        for unit in self.denominator:
            if unit not in lst:
                count = self.denominator.count(unit)
                lst.append(unit)
                if count > 1:
                    output += f"{unit}^{count} "
                else:
                    output += unit

        if len(self.denominator) > 1:
            output += ")"

        return output



    def __add__(self, other):
        if self.name != other.name:
            raise Exception("You are trying to add different units")
        else:
            return self

    def __sub__(self, other):
        if self.name != other.name:
            raise Exception("You are trying to subtract different units")
        else:
            return self

    def __mul__(self, other):
        output = Unit()
        output.numerator = self.numerator + other.numerator
        output.denominator = self.denominator + other.denominator
        output.reduce()
        return output

    def __truediv__(self, other):
        output = Unit()
        output.numerator = self.numerator + other.denominator
        output.denominator = self.denominator + other.numerator
        output.reduce()
        return output


class Scalar:
    def __init__(self, val, name=None):
        self.value = val
        self.unit = Unit()
        self.name = name

    def __repr__(self):
        return f"{self.name}: {self.value}{self.unit}"

class Vector:
    def __init__(self, x, y, name="Vector"):
        self.x = x
        self.y = y
        self.initial = (x, y)
        self.unit = Unit()
        self.name = name

    def __repr__(self):
        return f"{self.name}: [{self.x};{self.y}]{self.unit}"


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
            raise Exception(f"You are trying to add different vectors( {type(self)} and {type(other)})")

    def __sub__(self, other):
        if self.same_type(other):
            obj = copy(self)
            obj.x = self.x - other.x
            obj.y = self.y - other.y
            return obj
        else:
            raise Exception(f"You are trying to subtract different vectors( {type(self)} and {type(other)})")

    def __mul__(self, other):
        if type(self) == type(other):
            output = 0
            output += self.x * other.x
            output += self.y * other.y
            return obj

    def __rtruediv__(self, other):
        v = Vector(self.x / other.value, self.y / other.value)
        v.unit = self.unit / other.unit
        return v

    def same_type(self, other):
        if type(self) == type(other):
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



r1 = Vector(3, 4, "position")
r2 = Vector(5, 6, "position")
t = Scalar(1, "time")
v = (r1 - r2) / t
