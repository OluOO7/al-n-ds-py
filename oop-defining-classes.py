class Fraction:
    """Fraction Class"""
    def __init__(self, top, bottom):        #First method of any class, the Constructor that defines
        self.num = top                      #the initial internal states of a class instance/member.
        self.den = bottom
    
    def show(self):                         #show() method that prints the internal states of a class  
        print(f"{self.num}/{self.den}")     #instance. 

    def __str__(self):                      #overriding a standard Python method '__str__'
       return f"{self.num}/{self.den}"

    def __add__(self,other_fraction):
        result_num = self.num * other_fraction.den + other_fraction.num * self.den
        result_den = self.den * other_fraction.den
        result = Fraction(result_num, result_den)
        return result

a_fraction = Fraction(2,5)                  #an instance of Fraction class with states(num = 2 and den = 5)
a_fraction.show()  
print(a_fraction)     
a_fraction.__str__()
a = Fraction(1,3)
b = Fraction(1,7)
print(a + b)