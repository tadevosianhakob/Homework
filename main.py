class Calculator:
    def __init__(self, x):
        if isinstance(x, (int, tuple)):
            self.__x = x
        else:
            raise Exception("error")

    @property
    def getter(self):
        return self.__x

    def __add__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__x + other.__x)
        else:
            raise Exception("Error")

    def __sub__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__x - other.__x)
        else:
            raise Exception("Error")

    def __mul__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__x * other.__x)
        else:
            raise Exception("Error")

    def __truediv__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__x / other.__x)
        else:
            raise Exception("Error")

    def __floordiv__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__x // other.__x)
        else:
            raise Exception("Error")

    def __mod__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__x % other.__x)
        else:
            raise Exception("Error")

    def __pow__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__x ** other.__x)
        else:
            raise Exception("Error")

    def __str__(self):
        other = Calculator(10)
        return f"{self.__x}, {self.__add__(other).__x}, {self.__sub__(other).__x}, {self.__mul__(other).__x}, {self.__truediv__(other).__x},{self.__floordiv__(other).__x}, {self.__mod__(other).__x}, {self.__pow__(other).__x}"

t1 = Calculator(10)

print(t1.__str__())
