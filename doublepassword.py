a=input()
b=input()
count=1
for i in range(0, len(a)):
    if a[i]!=b[i]:
        count*=2
print(count)