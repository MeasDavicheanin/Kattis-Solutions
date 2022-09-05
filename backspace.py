word=list(input())
ans=[]
for i in word:
    if i!="<":
        ans.append(i)
    else:
        ans.pop()
print("".join(ans))