t=int(input())
for i in range(0,t):
    a=input().split()
    b=input().split()
    num1=int("".join(a))
    num2=int("".join(b))
    ans=list(str(num1+num2))
    out_put=""
    for i in ans:
        out_put+=i+" "
    print(out_put)