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
        if output:
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
        if output:
            if output[-1] == " ":
                output = output[:-1]

        if len(self.denominator) > 1:
            output += ")"

        return output

    def add(self, short, denominator=False):
        if not denominator:
            self.numerator.append(short)
        else:
            self.denominator.append(short)



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

    def order(self):
        return sorted(self.numerator + self.denominator)
