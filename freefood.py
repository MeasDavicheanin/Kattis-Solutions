t=int(input())
ans=set()
for i in range(0,t):
    data=input().split()
    a=int(data[0])
    b=int(data[1])
    for i in range(a, b+1):
        ans.add(i)
print(len(ans))  