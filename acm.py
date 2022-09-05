right=[]
wrong=[]
count=0
time=0
while True:
    word=input()
    if word=="-1":
        break
    data=word.split(" ")
    for item in data:
        if item=="right":
            count+=1
            right.append([data[1],data[0]])
        if item=="wrong":
            wrong.append([data[1], data[0]])
for i in right:
    for j in wrong:
     if i[0] in j[0]:
        time+=20
for i in right:
    time+=int(i[1])
print(count,time)