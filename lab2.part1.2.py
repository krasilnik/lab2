 # Create a class called Rational for performing arithmetic with fractions.
 # Write a program to test your class. Use integer variables to represent
 # the private data of the class – the numerator and the denominator.
 # Provide a __init__() method that enables an object of this class to be initialized when it’s declared.
 # The __init__() should contain default parameter values in case no initializers
 # are provided and should store the fraction in reduced form. For example, the fraction 2/4 would be stored
 # in the object as 1 in the numerator and 2 in the denominator. Provide public methods
 # that perform each of the following tasks:
 # - printing Rational numbers in the form a/b, where a is the numerator and b is the denominator.
 # - printing Rational numbers in floating-point format#

def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n

class Rational:

    def __init__(self, numerator, denominator):
        divisor = gcd(numerator, denominator)
        self.numerator = numerator // divisor
        self.denominator = denominator // divisor
        print(f"numerator: {self.numerator}, denominator: {self.denominator}")

    def fraction(self):
        print(f"{self.numerator}/{self.denominator}")
    def point(self):
       print(self.numerator/self.denominator)




x = Rational(2,4)
x.fraction()
x.point()