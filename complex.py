from math import atan, sqrt, log
import matplotlib.pyplot as plt

def factorial(num):
    output = 1
    for i in range(1, num+1):
        output *= i
    return output

def exp(x):
    output = 1
    for i in range(1, 9):
        # print(type(x))
        output += x ** i / factorial(i)
        print(x ** i / factorial(i))
    return output


class ComplexNumber:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def __repr__(self):
        if self.a ==0:
            return f"{self.b}i"
        if self.b > 0:
            return f"{self.a:.2f} + {self.b:.2f}i"
        elif self.b < 0:
            return f"{self.a:.2f} - {abs(self.b):.2f}i"
        else:
            return str(self.a)

    def __eq__(self, other):
        if (self.a == other.a and self.b == other.b):
            return True
        else:
            return False

    def __abs__(self):
        return sqrt(self.a ** 2 + self.b ** 2)

    def argument(self):
        return atan(b/a)

    def conjugate(self):
        return ComplexNumber(self.a, -self.b)

    def __add__(self, other):
        if type(other) == type(self):
            return ComplexNumber(self.a + other.a, self.b + other.b)
        else:
            return ComplexNumber(self.a + other, self.b)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if type(other) == type(ComplexNumber()):
            return ComplexNumber(self.a - other.a, self.b - other.b)
        else:
            return ComplexNumber(self.a - other, self.b)

    def __rsub__(self, other):
        return ComplexNumber(-self.a + other, self.b)

    def __mul__(self, other):
        if type(other) == type(ComplexNumber()):
            new_a = self.a * other.a - self.b * other.b
            new_b = self.a * other.b + self.b * other.a
            return ComplexNumber(new_a, new_b)
        else:
            return ComplexNumber(other * self.a, other * self.b)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __pow__(self, other):
        # if type(other) == type(int):
        output = self
        for i in range(1, other):
            output *= output
        return output

    def __truediv__(self, other):
        if type(other) == type(self):
            new_a = (self.a * other.a + self.b * other.b) / (abs(other) ** 2)
            new_b = (-self.a * other.b + self.b * other.a) / (abs(other) ** 2)
            return ComplexNumber(new_a, new_b)
        else:
            return ComplexNumber(self.a / other, self.b / other)

    def __rtruediv__(self, other):
        return ComplexNumber(other / self.a, other / self.b)

    def plot(self):
        range = 2
        plt.scatter(self.a, self.b, label=str(self), marker="*", color="green", s=30)
        plt.xlabel("Real part")
        plt.ylabel("Imaginary part")
        plt.title("ComplexNumber")

        plt.ylim(ymin=-self.b * range, ymax=self.b * range)
        plt.xlim(xmin=-self.a * range, xmax=self.a * range)

        plt.axhline(y=0, color="black")
        plt.axvline(x=0, color="black")

        plt.legend()
        plt.show()
