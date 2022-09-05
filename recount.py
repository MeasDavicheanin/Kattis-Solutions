freq={}
while True:
    word=input()
    if word=="***":
        break
    data=[]
    data.append(word)
    for i in data:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
print(freq)

largest_key=max(freq.items(), key=lambda x: x[1])[0]
win=True
for key,value in freq.items():
    if key!=largest_key:
        if freq[largest_key]<=value:
            win=False
if win:
    print(largest_key)
else:
    print("Runoff!")
