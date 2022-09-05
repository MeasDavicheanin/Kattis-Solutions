away=False
ans=[]
for i in range(1,6):
    word=input()
    if "FBI" in word:
        ans.append(str(i))
        away=True
if away==False:
    print("HE GOT AWAY!")
else:
    print(" ".join(ans))
    