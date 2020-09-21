s=input("enter a string")
a="aeiouAEIOU"
count=0
'''
for i in s:
    if i in a:
        count+=1'''
#with index value
for i in range(len(s)):
    if s[i] in a:
        count+=1
print("count of vowels is",count)
