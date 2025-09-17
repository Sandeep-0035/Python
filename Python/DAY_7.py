#              SLIDING WINDOW

# l=list(map(int,input().split()))
# k=int(input())
# s=[]
# for i in range (0,len(l)-k+1):
#     sum=0
#     for j in range(i,i+k):
#         sum+=l[j]
#     s.append(sum)
# print(s)


# l = list(map(int, input().split()))
# k = int(input())
# s = []
# for i in range(0, len(l) - k + 1):
#     sum = 0
#     for j in range(i, len(l)):
#         sum += l[j]
#         if (j - i + 1 == k):
#             print(sum)
#             s.append(sum)   
#             break  
# print(s)         

# s="abcacdfac"
# k=4
# l=list(s)
# for i in range(0, len(l) - k + 1):
#     ans=[]
#     for j in range(i, i+k):
#         ans.append(l[j])
#     if(len(ans)==len(set(ans))):
#         print("".join(ans)) 
    
# s="abacddcbkbb"
# k=4
# l=list(s)                                                               
# for i in range(0, len(l) - k + 1):
#     ans={}
#     for j in range(i, i+k):
#         ans.setdefault(l[j],1)
#     if(len(ans)==j-i+1):
#         print("".join(ans.keys()))
#     ans.pop(s[i])

#              GEEKS OF GEEKS

#Sum of min and max of all subarrays of size k.
# arr=list(map(int,input().split(" ")))
# k=int(input())
# res=[]
# for i in range(0,len(arr)-k+1):
#     ans=[]
#     for j in range(i,i+k):
#         ans.append(arr[j])
#     res.append(len(set(ans)))
# print(res)

#Count Distinct Elements In Every Window of Size K
# arr=list(map(int,input().split(" ")))
# k=int(input())
# res=[]
# for i in range(0,len(arr)-k+1):
#     ans=[]
#     for j in range(i,i+k):
#         ans.append(arr[j])
#     res.append(len(set(ans)))
# print(res)

#Sum of min and max of all subarrays of size k.
# arr=list(map(int,input().split(" ")))
# k=int(input())
# res=[]
# for i in range(0,len(arr)-k+1):
#     ans=[]
#     mn=0
#     mx=0
#     sum=0
#     for j in range(i,i+k):
#         ans.append(arr[j])
#         mn=min(ans)
#         mx=max(ans)
#         sum=mx+mn
#     res.append(sum)
# print(res)

#First negative integer in every window of size k
# arr=list(map(int,input().split(" ")))
# k=int(input())
# res=[]
# for i in range(0,len(arr)-k+1):
#     s=0
#     for j in range(i,i+k):
#         if(arr[j]<0):
#             s=arr[j]
#             break
#     res.append(s)
# print(res)

#Sum of all subarrays of size K
# arr=list(map(int,input().split(" ")))
# k=int(input())
# res=[]
# for i in range(0,len(arr)-k+1):
#     mx=0
#     ans=[]
#     for j in range(i,i+k):
#         ans.append(arr[j])
#         mx=max(ans)
#     res.append(mx)
# print(res)


# Maximum MEX from all subarrays of length K
arr=list(map(int,input().split(" ")))
k=int(input())
res=[]
for i in range(0,len(arr)-k+1):
    ans=[]
    n=0
    mx=0
    arr_set=()
    for j in range(i,i+k):
        ans.append(arr[j])
    n =len(ans)
    arr_set = set(ans)
    for l in range(1, n + 2):
        if l not in arr_set:
            res.append(l)
            break
    mx=max(res)
print(mx)

