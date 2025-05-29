#variables in python
x=5
y="karungi irene"
print(x)
print(y)
# allowed variable names
myvar = 7
_my_var=23
MyVar = 78
my_var =90
print(myvar)
print(my_var)
print(_my_var)
print(MyVar)
#allows to assign values to variables multiple and you can also use the plus operator
x, y, z, = "irene", "karungi", "Fredrick"
print(x)
print(y+z)
#python allows you to assign values from a list or tuple and also use the print function to output multiple variables separated by a comma
fruits =("orange", "purple")
x, y = fruits
print(y,x)
#global variables are variables used out of the function like the ones above
#creating a variable outside a function and using it inside a function
x = "easiest"
def myfunc():
   print("Python is " + x)
myfunc()

#If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#how to print the data type
x = 5
print(type(x))
y = ("cow", "dog", "animal")
print(type(y))
z = ["mwebaze", "Fred"]
print(type(z))
h = {"mariam", "wambui"}
print(type(h))
m = ({"mariam", "wambui"})
print(type(m))

#type casting.
x = int(65.99)
y = int(23.33333)
z = float(23)
print(x)
print(y)
print(z)

#Slicing strings
a = "karungi"
print(a[2:5]) #it prints fron index 2 to 5
b = "Hello, World!"
print(b[2:]) #from index 2 upto the end
b = "Hello, World!"
print(b[:5]) #from the start
c = "Karungi"
print(c[-5:-2])

#modify strings
a = "Mukaddenefu"
print(a.upper())
b = "KARUNGI"
print(b.lower())
c = "   Karungi  irene    "
print(c.strip()) #removes white space from begginig or the end
d = "Lone"
print(d.replace("n", "v"))
e = "karungi irene"
print(e.split())

#format strings
age = 22
txt = f"My name is karungi, l am {age}" # you just put age without curly brackets, it brings an error
print(txt)
txt = f"the sum of 2 multiplied by 4 is {2*4}"
print(txt)

#booleans
a=200
b=56
if b>a:
 print("a is the number is the greatest")
else:
 print("b is the number is lower")
 print(b>a)
 
 #lists
 thislist = ["louis", "walter", "mariam"]
 print(thislist)
 print(len(thislist))
 #using list() constructor
 this = list(["karungi", "irene"])
 print(this)
 #change lists
 thislist=["blue", "yellow", "red", "black"]
 thislist[3] ="purple"
 print(thislist)
 #add lists
 thislist.append("green")
 print(thislist)
 #extend() lists
 thislist.extend(this)
 print(thislist)
 #remove lists
 thislist=["purple", "yellow", "grey"]
 thislist.remove("grey")
 print(thislist)
 #loop
 animal = ["cow", "dog", "cat"]
 for x in animal:
   print(x)
#using while loop
 animal = ["cow", "dog", "cat"]
 i = 0
 while i < len(animal):
     print(animal[i])
     i = i+1
 #adding new items to a list with a specified number
 fruits = ["mango", "orange", "yellow", "apple"]
 newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
        print(newlist)
#sorting lists
colour = ["yellow", "blue", "green", "black", "purple"]
colour.sort()
print(colour)
colour.sort(reverse = True)
print(colour)
#make a copy
animal = colour.copy()
print(animal)

 
 
 
 
 
 
 
 
