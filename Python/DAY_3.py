# n=int(input())
# x=2
# for i in range(n):
#     print(x,end=" ")
#     x*=2

# n=int(input())
# x=5
# for i in range(n):
#     print(x,end=" ")
#     x+=2

# n=int(input())
# x=65
# for i in range(n):
#     print(x,end=" ")
#     x+=1

# n=int(input())
# for i in range(n):
#     print("* $ @")

# n=int(input())
# for i in range(n):
#     print(f"{chr(65+i)} {chr(90-i)}")
#     x+=1

# n=int(input())
# for i in range(n):
#     print(f"{chr(97+i)} {chr(65+i)}")
#     x+=1

# n=int(input("enter no.of rows: "))
# m=int(input("enter no.of columns: "))

# for i in range(n):
#     for j in range(m):
#         print("*",end=" ")
#     print()

# n=int(input("enter no.of rows: "))
# m=int(input("enter no.of columns: "))

# x="$@"

# for i in range(n):
#     for j in range(m):
#         print(x,end=" ")
#     print()
#     for l in range(m):
#         print(f"*{l+1}",end=" ")
#     print("\n")


# n=int(input("enter no.of rows: "))
# m=int(input("enter no.of columns: "))
# l=1
# for i in range(n):
#     for j in range(m):
#         print(l,end=" ")
#         l+=1
#     print()

# n=int(input("enter no.of rows: "))
# x=n-1
# for i in range(n):
#     for j in range(n+1):
#         if(j<=x):
#             print("*",end=" ")
#         else:
#             print("@",end=" ")
#     print()
#     x-=1

# n=int(input())
# for i in range(n):
#     for j in range(i+1):
#         print(f"{j+1}",end=" ")
#     print()

# n=int(input())
# x=n
# for i in range(n*2-1):
#     for j in range(n+1):
#         if(j<x):
#             print("*",end=" ")
#         else:
#             print("@",end=" ")
#     if(i>=n-1):
#         x+=1
#     else:
#         x-=1
#     print()

# n=int(input())
# x=1
# for i in range(n*2-1):
#     for j in range(n+1):
#         if(j<x):
#             print("*",end=" ")
#         else:
#             print("@",end=" ")
#     if(i>=n-1):
#          x-=1
#     else:
#         x+=1
#     print()


# n=int(input())
# x=n
# y=n
# for i in range(1,n*2):
#     for j in range(1,n*2):
#         if(j>=x and j<=y):
#             print("*",end=" ")
#         else:
#             print(" ", end=" ")
#     if(i>=n):
#         x+=1
#         y-=1
#     else:
#         y+=1
#         x-=1
#     print()

# n=int(input())
# x=n+1
# y=n+1
# for i in range(1,n*2+2):
#     t=1
#     for j in range(1,n*2+2):
#         if(j>=x and j<=y):
#             if(t==1):
#                 print("*",end="")
#                 t=0
#             else:
#                 print(" ",end="")
#                 t=1
#         else:
#             print(" ",end="")
#     if(i>=n):
#         x+=1
#         y-=1
#     else:
#         y+=1
#         x-=1
#     print()
            
# n=int(input() )
# x=1
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(f"{x}",end=" ")
#         if(x==1):
#             x=0
#         else:
#             x=1
#     print()


# n=int(input())
# x=1
# for i in range(1,n+2):
#      for j in range(n+1):
#         if(i%2==1):
#             if(j==n+1):
#                 print(x+1,end=" ")
#             else:
#                 print(x,end=" ")
#         else:
#             if(j==0):
#                 print(x,end=" ")
#             else:
#                 print(x,end=" ")
#      x+=1
#      print()

# n=int(input())

# while(n!=0):
#     print(n%10,end=", ")
#     n=n//10
# print()

# while(n>=10):
#     print(n%100,end=", ")
#     n=n//10

# count how many even digits are there in a number
# reverse a number and check if it is palindrome or not
# 

# n=int(input())
# c=0
# p=1
# while(n!=0):
#     if((n%10)%2==p%2):
#         c+=1
#     n=n//10
#     p+=1
# print(c)

# reversing a number
rev=0
n=int(input())
temp=n
while(n!=0):
    rev=rev*10+n%10
    n=n//10

print(f"reverse the given number is {rev}")

if(rev==temp):
    print("Palindrome")
else:
    print("Not a palindrome")


          
