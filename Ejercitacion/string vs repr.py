# import datetime
# today = datetime.datetime.now()
# print(str(today))
# print(repr(today))

class Complex:
    
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return "Rational(%s, %s)" % (self.real, self.imag)

    def __str__(self):
        return "%s + i%s" % (self.real, self.imag)

t = Complex(10, 20)

print (str(t))
print (repr(t))