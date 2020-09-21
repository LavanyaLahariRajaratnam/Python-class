s=input()
s1=""
for i in s:
    if i.isalpha():
        s1+=i
        x=i
    else:
        d=int(i)
        ns=x*(d-1)
        s1+=ns
print(s1)
