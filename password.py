import string
up=string.ascii_uppercase
h,m=map(int,input().split(':'))
s=h
for i in range(m):
    h=2*h-1
    s+=h
password=""
for i in str(s):
    password+=up[int(i)]
print(password)
