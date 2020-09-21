s=input()
se=""
so=""
for i in range(len(s)):
    if i%2==0:
        se+=s[i]
    else:
        so+=s[i]
print("even string",se)
print("odd string",so)
        
