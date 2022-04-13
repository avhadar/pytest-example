import math

class ComplexNum:

    def __init__(self, x = 0, y = 0):
        self.x = x # real part
        self.y = y # imaginary part


    def __repr__(self):
        return f'{self.x!r} + i * {self.y!r}'


    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)


    def __abs__(self):
        return math.hypot(self.x, self.y)


    def __add__(self, other):
        # check argument type: scalar or complex number
        if not isinstance(other, ComplexNum):
            # addition of scalar
            x = self.x + other
            y = self.y + other
        else:
            # complex addition
            x = self.x + other.x
            y = self.y + other.y

        return ComplexNum(x, y)


    def __sub__(self, other):
        # check argument type: scalar or complex number
        if not isinstance(other, ComplexNum):
            # subtraction of scalar
            x = self.x - other
            y = self.y - other
        else:
            # complex subtraction
            x = self.x - other.x
            y = self.y - other.y

        return ComplexNum(x, y)


    def __mul__(self, other):
        # check argument type: scalar or complex number
        if not isinstance(other, ComplexNum):
            # multiplication with scalar
            x = self.x * other
            y = self.y * other
        else:
            # complex multiplication
            x = self.x * other.x - self.y * other.y
            y = self.y * other.x + self.x * other.y

        return ComplexNum(x, y)


    def __truediv__(self, other):
        # check argument type: scalar or complex number
        if not isinstance(other, ComplexNum):
            # division with scalar
            if other != 0:
                x = self.x / other
                y = self.y / other
            else:
                raise ZeroDivisionError
        
        else:
            # complex division
            denom = other.x * other.x + other.y * other.y
            x = (self.x * other.x + self.y * other.y) / denom
            y = (self.y * other.x - self.x * other.y) / denom

        return ComplexNum(x, y)


    def real(self):
        return self.x


    def img(self):
        return self.y


    def conj(self):
        return ComplexNum(self.x, -self.y)


    def polar(self):
        r = abs(self)
        theta = math.atan2(self.y, self.x)
        return r, theta
    
    
    def is_real(self):
        return self.y == 0
    
    
    def is_img(self):
        return self.x == 0


if __name__ == '__main__':
    mynum = ComplexNum(3, 4)
    print(f"This a complex number: {mynum}")

