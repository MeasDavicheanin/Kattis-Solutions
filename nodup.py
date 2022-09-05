word=input().split(" ")
data=set()
for i in word:
    data.add(i)
if len(data)==len(word):
    print("yes")
else:
    print("no")
    
    