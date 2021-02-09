import math

class Complex():
    re = 0;
    im = 0;
    
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def add(self, b):
        self.re += b.re
        self.im += b.im

    def subtract(self, b):
        self.re -= b.re
        self.im -= b.im

    def multiply(self, b):
        temp = self.re
        self.re = self.re * b.re - self.im * b.im
        self.im = temp * b.im + b.re * self.im

    def norm(self):
        return math.sqrt(self.re * self.re + self.im * self.im)

    def arg(self):
        return math.atan2(self.im, self.re)

    def pow(self, b):
        self_norm = self.norm()
        self_arg = self.arg()
        if self.norm() == 0:
            self.re = 0
            self.im = 0
            return
        constant = 0
        try:
            constant = math.pow(self_norm, b.re) * math.exp(-1 * b.im * self_arg)
        except OverflowError:
            self.re = float("inf")
            self.im = float("inf")
            return
        rad = b.re * self_arg + b.im * math.log(self_norm)
        self.re = constant * math.cos(rad)
        self.im = constant * math.sin(rad)

    
