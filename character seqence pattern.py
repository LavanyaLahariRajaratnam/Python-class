'''
Pattern
A
B C
D E F
G H I J
K L M N O
'''

'''
value=65
n=int(input())
for i in range(n):
    for j in range(0,i+1):
        ch=chr(value)
        print(ch,end=' ')
        value=value+1
    print()
    
'''

value='A'
n=int(input())
for i in range(n):
    for j in range(0,i+1):
        #ch=chr(value)
        print(value,end=' ')
        value=chr(ord(value)+1)
    print()
