t=int(input())
for i in range(0, t):
    list=[]
    n=int(input())
    data=input().split(" ")
    for i in data:
        list.append(int(i))
    diff=max(list)-min(list)
    print(diff*2)
