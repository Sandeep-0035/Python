i=int(input("Enter an integer: "))
f=float(input("Enter a float: "))
c=input("Enter a character: ")
s=input("Enter a string: ")
print("Integer:",i,"Float:",f,"Character:",c,"String:",s)

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Sum:",a+b)

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Addition:",a+b)
print("Subtraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b if b!=0 else "Undefined")
print("Modulus:",a%b if b!=0 else "Undefined")

l=float(input("Enter length: "))
w=float(input("Enter breadth: "))
print("Perimeter of rectangle:",2*(l+w))

l=float(input("Enter length: "))
w=float(input("Enter breadth: "))
print("Area of rectangle:",l*w)

r=float(input("Enter radius: "))
print("Diameter:",2*r)
print("Circumference:",2*3.14159*r)
print("Area:",3.14159*r*r)

cm=float(input("Enter length in cm: "))
print("Meters:",cm/100)
print("Kilometers:",cm/100000)

c=float(input("Enter Celsius: "))
print("Fahrenheit:",(c*9/5)+32)

f=float(input("Enter Fahrenheit: "))
print("Celsius:",(f-32)*5/9)

days=int(input("Enter days: "))
years=days//365
weeks=(days%365)//7
d=(days%365)%7
print("Years:",years,"Weeks:",weeks,"Days:",d)

x=float(input("Enter base: "))
y=float(input("Enter exponent: "))
print("Power:",x**y)

n=float(input("Enter number: "))
print("Square root:",n**0.5)

a1=float(input("Enter first angle: "))
a2=float(input("Enter second angle: "))
print("Third angle:",180-(a1+a2))

b=float(input("Enter base: "))
h=float(input("Enter height: "))
print("Area of triangle:",0.5*b*h)

s=float(input("Enter side of equilateral triangle: "))
print("Area:",(3**0.5/4)*(s**2))

marks=[]
for i in range(5):
    marks.append(float(input(f"Enter mark {i+1}: ")))
total=sum(marks)
avg=total/5
percent=(total/500)*100
print("Total:",total,"Average:",avg,"Percentage:",percent)

p=float(input("Enter Principal: "))
t=float(input("Enter Time: "))
r=float(input("Enter Rate: "))
print("Simple Interest:",(p*t*r)/100)

p=float(input("Enter Principal: "))
t=float(input("Enter Time: "))
r=float(input("Enter Rate: "))
print("Compound Interest:",p*((1+r/100)**t -1))
