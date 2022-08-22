t=int(input())
for i in range(0,t):
    word=input().lower().strip()
    ans=set()
    for c in word:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            ans.add(c)
    if len(ans)==26:
        print("pangram")
    else:
        missing=set("abcdefghijklmnopqrstuvwxyz")-set(word)
        missing_word=list(missing)
        missing_word.sort()
        print("missing "+"".join(missing_word))