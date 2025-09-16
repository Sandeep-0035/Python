# n=int(input())
# print("1",end=" ")
# for i in range(2,n//2+1):
#     if(n % i==0):
#         print(i,end=" ")
# print(n)

# n=int(input())
# print(f"(1,{n})")
# c=2
# for i in range(2,int(n**(1/2))+1):
#     if(n % i == 0):
#         if(i==n//i):
#             c+=1
#             print(f"({i})")
#         else:
#             c=c+2
#             print(f"({i},{n//i})")
# print(c)
# if(c%2==0):
#     print(f"{n} is not perfect square")
# else:
#     print(f"{n} is perfect square")

# nums=list(map(int,input().split( )))
# cp=0
# cnp=0
# for n in nums:
#     c=2
#     for i in range(2,int(n**(1/2))+1):
#         if(n % i == 0):
#             if(i==n//i):
#                 c+=1
#             else:
#                 c=c+2        
#     if(c==2):
#         print(f"{n} is prime")
#     else:
#         print(f"{n} is not a prime")

# n=int(input())
# e=int(input())
# pc=0
# npc=0
# for i in range(n,e+1):
#     c=2
#     for j in range(2,int(i**(1/2))+1):
#         if(i % j == 0):
#             c=40
#             break       
#     if(c==2):
#         pc+=1
#         print(i,end=" ")
#     else:
#         npc+=1
# print()
# print(f"prime count={pc} and non prime count={npc}")


# n=int(input())
# a=0
# b=1
# c=2
# sum=0
# print(a,b,c,end=" ")
# for i in range(1,n+1):
#     sum=a+b+c
#     print(sum,end=" ")
#     a=b
#     b=c
#     c=sum

# a,b=map(int,input().split( ))
# while(a!=b):
#     r= b % a
#     if(r==0):
#         break
#     b=a
#     a=r
    
# print(a)/

a,b=map(int,input().split( ))
n1=a
n2=b
while(a!=b):
    r= b % a
    if(r==0):
        break
    b=a
    a=r
print("gcd:",a)
Lcm=(n1*n2)//a
print("lcm:",Lcm)
