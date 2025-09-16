a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Maximum between two:",a if a>b else b)

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
print("Maximum between three:",max(a,b,c))

n=int(input("Enter a number: "))
if n>0: print("Positive")
elif n<0: print("Negative")
else: print("Zero")

n=int(input("Enter a number: "))
print("Divisible by 5 and 11" if n%5==0 and n%11==0 else "Not divisible")

n=int(input("Enter a number: "))
print("Even" if n%2==0 else "Odd")

y=int(input("Enter year: "))
print("Leap Year" if (y%4==0 and y%100!=0) or (y%400==0) else "Not Leap Year")

ch=input("Enter a character: ")
print("Alphabet" if ch.isalpha() else "Not Alphabet")

ch=input("Enter an alphabet: ")
print("Vowel" if ch.lower() in 'aeiou' else "Consonant")

ch=input("Enter any character: ")
if ch.isalpha(): print("Alphabet")
elif ch.isdigit(): print("Digit")
else: print("Special Character")

ch=input("Enter a character: ")
if ch.isupper(): print("Uppercase")
elif ch.islower(): print("Lowercase")
else: print("Not an alphabet")

week=int(input("Enter week number (1-7): "))
days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
print(days[week-1] if 1<=week<=7 else "Invalid week number")

month=int(input("Enter month number (1-12): "))
if month in [1,3,5,7,8,10,12]: print("31 days")
elif month in [4,6,9,11]: print("30 days")
elif month==2: print("28 or 29 days")
else: print("Invalid month number")
