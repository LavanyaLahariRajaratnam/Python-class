s=input()
U=0
L=0
D=0
S=0
for i in s:
    if i.isupper():
       U+=1
    elif i.islower():
        L+=1
    elif i.isdigit():
        D+=1
    else:
        S+=1
if (U==L==D==S):
    print("Equality For Everyone")
else:
    print("No Equality")
    
