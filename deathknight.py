t=int(input())
ans=0
for i in range(0,t):
    word=input()
    if "CD" in word:
        ans+=1
print(t-ans)