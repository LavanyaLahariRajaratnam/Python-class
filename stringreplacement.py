s=input()
res=""
for i in s:
    if i.isalpha():
        res+=i
        x=i
    else:
        d=chr((ord(x)-ord('a')+ord(i)-ord('0'))%26+97)
        res+=d
print(res)
