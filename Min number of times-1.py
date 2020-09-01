"""

Louis was celebrating his 10th Birthday and his parents wished to make his birthday more special by throwing a surprise bash, inviting all their friends, relatives and neighbors. The little mathematics geek Louis has another surprise waiting for him when he had to cut his favorite Choco vanilla cake. The cake is a rectangular cake and it consists of m×n (1≤m, n≤1000) squares. His friends now called him out for a challenge. 
The challenge is that, Louis has to break the cake up into 1×1 pieces (individual squares) and find what is the minimum number of times that he breaks the choco vanilla cake, or pieces therefore, in order to achieve this? 
  
Note that he cannot stack pieces of the cake and break them, because the choco vanilla cake is thick. As an example, a 2×2 cake requires 3 breaks. First he can break it in half, then break each of the halves in half. He cannot break it in half, stack the two 1×2 pieces, and then use only one more break to achieve his goal. 
  
Input Format: 
First line of the input consists of an integer, the dimensions m of the choco vanilla cake. 
Second line of the input consists of an integer, the dimensions n of the choco vanilla cake. 
 
Output Format: 
Output the minimum number of times that he breaks the choco vanilla cake 
Refer sample input and output for formatting specifications. 
[All text in bold corresponds to input and rest corresponds to output.] 
 
Sample Input and Output 1: 
Enter m 
1 
Enter n 
2 
Minimum number of times is 1 
 
Sample Input and Output 2: 
Enter m 
2 
Enter n 
2 
Minimum number of times is 3 
 Code: 

print("Enter m") 

m=int(input()) 

print("Enter n") 

n=int(input()) 

print("Minimum number of times is",(m*n)-1) 

 """"



print('Enter m')
m=int(input())
print('Enter n')
n=int(input())
print('Minimum number of times',(m*n)-1)


