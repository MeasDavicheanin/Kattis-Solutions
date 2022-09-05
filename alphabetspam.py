from string import whitespace
from symtable import Symbol
from typing import Counter


line=input()
total_space=len(line)
lowercase=0
_counter=0
uppercase=0
Symbol=0
for i in line:
    if i=="_":
        _counter+=1
    elif ord(i)>=97 and ord(i)<=122:
        lowercase+=1
    elif ord(i)>=65 and ord(i)<=90:
        uppercase+=1
    else:
        Symbol+=1


print(_counter/total_space)
print(lowercase/total_space)
print(uppercase/total_space)
print(Symbol/total_space)
