t=int(input())
for i in range(1,t+1):
    c=int(input())
    data_set=set()
    data=input().split(" ")
    for num in data:
        if num in data_set:
            data_set.remove(num)
        else:
            data_set.add(num)
    num=list(data_set)
    print("Case #"+str(i)+": "+num[0])
    


   
