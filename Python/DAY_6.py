# l=list(map(int,input().split()))
# d={}
# for i in l:
#     d.setdefault(i,0)
# for i in d.keys():
#     d[i]= l.count(i)
# for i,j in d.items():
#     print(i,"occured ",j, "times")
# print(min(l),"minimum number of the list ")
# print(max(l),"maximum number of the list ")

# l=list(map(int,input().split()))
# count=[]
# c=0
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         if(l[i]==l[j]):
#             c+=1
#     count[i]=c
# print(count)

# l=list(map(int,input().split()))
# n=int(input())
# for i in range(n):
#     temp=l[0]
#     for j in range(0,len(l)-1):
#         l[j]=l[j+1]
#     l[len(l)-1]=temp
# print(l)

# l=list(map(int,input().split()))
# l=[5,4,7,14,1,3,2,8]
# n1=int(input())
# n2=int(input())
# for i in range(1):
#     temp=l[n1]
#     for j in range(n2,n1,-1):
#         l[j]=l[j+1]
#     l[n2]=temp
# print(l)

#selction sort 
# l=list(map(int,input().split()))
# l=[1,5,6,8,9,4,2]
# for i in range(len(l)):
# for j in range(i+1,len(l)):
#         if(l[j]<=l[i]):
#             l[j],l[i]=l[i],l[j]
            
# print(l)


l = [1, 5, 2, 8, 9, 4, 2]

for i in range(1, len(l)):      
    temp = l[i]                
    j = i-1
    while j >= 0 and l[j] > temp:  
        l[j+1] = l[j]
        j -= 1
    l[j+1] = temp             

print(l)


