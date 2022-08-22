t=int(input())
s=0
m=0
for i in range(0, t):
    data=input().split(" ")
    m+=int(data[0])
    s+=int(data[1])
total_time=s/(m*60)
if total_time<=1:
    print("measurement error")
else:
    print("{:.9f}".format(round(total_time, 9)))
