from math import atan, sqrt
import matplotlib.pyplot as plt

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        if self.b > 0:
            return f"{self.a} + {self.b}i"
        elif self.b < 0:
            return f"{self.a} - {abs(self.b)}i"
        else:
            return str(a)

    def modulus(self):
        return sqrt(self.a ** 2 + self.b ** 2)

    def argument(self):
        return atan(b/a)

    def conjugate(self):
        return ComplexNumber(self.a, -self.b)

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return ComplexNumber(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        new_a = self.a * other.a - self.b * other.b
        new_b = self.a * other.b + self.b * other.a
        return ComplexNumber(new_a, new_b)

    def __truediv__(self, other):
        new_a = (self.a * other.a + self.b * other.b) / (other.modulus() ** 2)
        new_b = (-self.a * other.b + self.b * other.a) / (other.modulus() ** 2)
        return ComplexNumber(new_a, new_b)

    def plot(self):
        range = 3
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
