t=int(input())
data = set()
count=0
for i in range(0,t):
    word=input().replace("-"," ")
    data.add(word.lower())
print(len(data))


