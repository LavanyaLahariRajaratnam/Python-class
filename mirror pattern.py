#reverse pattern

n=int(input())
a=(2*n)-2
for i in range(n):
    for j in range(a):
        print(end=" ")
    a=a-2
    for j in range(i+1):
        print("*",end=" ")
    print()
