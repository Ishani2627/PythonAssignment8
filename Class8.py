#Que1
print("create a class and calculate area and circumference of circle")
PI = 3.14
class Circle:
    def __init__(self,r):
        self.radius = r
    def getArea(self):
        return PI*self.radius*self.radius
    def getCircumference(self):
        return 2*PI*self.radius

radius = float(input("enter the value of radius of circle : "))
C = Circle(radius)
print("area of the circle : ",C.getArea())
print("circumference of the circle : ",C.getCircumference())
print("\n")

#Que2
print("create a student class and display its name ,rollno, age and marks")
class student:
    def __init__(self, rollno, name):
        self.roll_no = rollno
        self.Name = name
        
    def display(self):
        return self.roll_no
        return self.Name
    def setAge(self,age):
        print("age of the student : ",age)
        
    def setMarks(self,science,maths):
        print("marks in science : ",science)
        print("marks in maths : ",maths)
roll_no = input("enter the rollno : ")
Name = input("enter the name : ")

obj = student(roll_no,Name)
obj.display()
obj.setAge(20)
obj.setMarks(78,80)
print("\n")

#Que3
print("conversion of temperature")
class temperature:
    def ConvertFahrenheit(self,c):
        f = c*(9/5)+32
        return f
    def ConvertCelcius(self,f):
        c = (f-32)*(5/9)
        return c

convertor = temperature()
c = float(input("enter temperature in celcius : "))
print(convertor.ConvertFahrenheit(c))
f = float(input("enter temperature in fahrenheit : "))
print(convertor.ConvertCelcius(f))
print("\n")

#Que4
class MovieDetails:
    def __init__(self, artistName, year_of_release, ratings):
        self.artistname = artistName
        self.year = year_of_release
        self.rating = ratings

    def display(self):
        return self.artistname
        return self.year
        return self.rating      

    def add(self,add):
        return add
       
artistname = input("enter the artist name : ")
year = int(input("year of release is : "))
rating = int(input("ratings of the movie are : "))
add = input("other details are : ")

movie = MovieDetails(artistname, year, rating)
movie.display()
movie.add(add)
print("\n")

#Que5
print("accessing a base class method")
class Animal:
    def animal_attribute(self):
        print("This is the Base class Animal with a method animal_attribute")

class tiger(Animal):
    def do_fast(self):
        print("This is another class Tiger inheriting the base class Animal  ")

obj = tiger()
obj.animal_attribute()
print("\r")
obj.do_fast()
print("\n")

#Que6
print("output of the code given ")
class A:
    def f(self):
        return self.g()
    def g(self):
        return 'A'
class B(A):
    def g(self):
        return 'B'
a = A()
b = B()
print (a.f(), b.f()) 
print (a.g(), b.g())
#A B
#A B
print("\n")

#Que7
print("inheritance with shapes")
class Shape:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b
    def area(self):
        print(self.length*self.breadth)

class rectangle(Shape):
    def rec_area(self):
        print("area of rectangle  : ")
class square(rectangle):
    def sq_area(self):
        print("area of square : ")

length = int(input("enter the length : "))
breadth = int(input("enter the breadth : "))
obj = square(length,breadth)
obj.rec_area()
obj.area()
obj.sq_area()
obj.area()