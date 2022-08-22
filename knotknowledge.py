t=input()
a=input().split(" ")
b=input().split(" ")
ans=set()
for i in a:
   ans.add(i)

for i in b:
    ans.remove(i)

for i in ans:
    print(i)