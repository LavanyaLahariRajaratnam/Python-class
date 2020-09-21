#even positioned
s=input()
for i in range (len(s)):
    if i%2==0:
        print(s[i], end=" ")

#odd postioned

s=input()
for i in range (len(s)):
    if i%2!=0:
        print(s[i], end=" ")
