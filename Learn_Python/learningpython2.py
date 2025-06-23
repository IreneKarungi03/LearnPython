 #functions
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#lambda can take in make arguments but with an expression
x = lambda a,b,c :a+b+c
print(x(3,4,5))
#lambda functions
def myfunc(n):
    return lambda a : a*n
mydoubler = myfunc(12)
print(mydoubler(3))
 
 #class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
    