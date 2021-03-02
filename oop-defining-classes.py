def gcd(a, b):                              #function finds the greater common divisor of two numbers.
    if a % b == 0:
        return b
    else:
       return gcd(b, a % b)
"""
def lcm(a, b):                              #function finds the least common multiple of two numbers.
    if a < b:
        if b % a == 0:
            return b
        else:
            return a * b
    else:
        if a % b == 0:
            return a
        else:
            return a * b
print(lcm(6,9))
"""

class Fraction:
    """Fraction Class"""
    def __init__(self, top, bottom):                #first method of any class, the Constructor that defines
        if top % 1 != 0 or bottom % 1 != 0:        #the initial internal states of a class instance/member.
            raise RuntimeError("Enter integer parameters") 
        else:                                               
            common_divisor = gcd(top, bottom)
            self.num = top // common_divisor
            self.den = bottom // common_divisor
    
    def show(self):                         #show() method that prints the internal states of a class. 
        print(f"{self.num}/{self.den}")     #instance. 

    def __str__(self):                      #overriding a standard Python method '__str__'.
       return f"{self.num}/{self.den}"

    def __add__(self,other_fraction):       #overriding a standard Python method '__add__'.
        result_num = self.num * other_fraction.den + \
                     other_fraction.num * self.den
        result_den = self.den * other_fraction.den
        result = Fraction(result_num, result_den)
        return result

    def __sub__(self,other_fraction):       #overriding a standard Python method '__add__'.
        result_num = self.num * other_fraction.den - \
                     other_fraction.num * self.den
        result_den = self.den * other_fraction.den
        result = Fraction(result_num, result_den)
        return result
    
    def __eq__(self, other_fraction):       #overriding a standard Python method '__eq__'.
        cross_product_1 = self.num * other_fraction.den
        cross_product_2 = self.den * other_fraction.num
        return cross_product_1 == cross_product_2
    
    def __lt__(self, other_fraction):       
        cross_product_1 = self.num * other_fraction.den
        cross_product_2 = self.den * other_fraction.num
        return cross_product_1 < cross_product_2
    
    def __gt__(self, other_fraction):       
        cross_product_1 = self.num * other_fraction.den
        cross_product_2 = self.den * other_fraction.num
        return cross_product_1 > cross_product_2

    def __mul__(self, other_fraction):      
        num_product = self.num * other_fraction.num
        den_product = self.den * other_fraction.den
        return Fraction(num_product, den_product)

    def __truediv__(self, other_fraction):      
        cross_product_1 = self.num * other_fraction.den
        cross_product_2 = self.den * other_fraction.num
        return Fraction(cross_product_1, cross_product_2)

a_fraction = Fraction(2,5)                  #an instance of Fraction class with states(num = 2 and den = 5).
a_fraction.show()  
print(a_fraction)     
a_fraction.__str__()
a = Fraction(2,8)
b = Fraction(3,12)
print(a + b)
print(a == b)
print(a * b)
print(f"{a} / {b} = {a / b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} < {b} is {a < b}")
