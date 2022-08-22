t=int(input())
word=input()
while(t>1):
    if t==2:
        print(str(t)+" bottles of "+word+" on the wall, " +
              str(t) + " bottles of "+word+".")
        print("Take one down, pass it around, " +
          str(t-1)+" bottle of "+word+" on the wall.")
    else:
        print(str(t)+" bottles of "+word+" on the wall, " +str(t)+ " bottles of "+word+".")
        print("Take one down, pass it around, "+str(t-1)+" bottles of "+word+" on the wall.")
    t-=1
print("1 bottle of "+word+" on the wall, 1 bottle of "+word+".")   
print("Take it down, pass it around, no more bottles of "+word+".")
