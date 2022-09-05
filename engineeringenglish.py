import sys
data_set = set()
for sentence in sys.stdin:
    ans=[]
    sentence_list=sentence.split()
    for word in sentence_list:
        w=word.lower()
        if w not in data_set:
            data_set.add(w)
            ans.append(word)
        else:
            ans.append(". ")
    print(" ".join(ans))
         



