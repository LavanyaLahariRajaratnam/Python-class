'''
The prime functionality of an Event Management System is budgeting. An Event Management System should estimate the total expenses incurred by an event and the percentage rate of each of the expenses involved in planning and executing an event. Nikhil, the founder of "Pine Tree" wanted to include this functionality in his company’s Amphi Event Management System and requested your help in writing a program for the same. 
  
The program should get the branding expenses, travel expenses, food expenses and logistics expenses as input from the user and calculate the total expenses for an event and the percentage rate of each of these expenses. 
  
Input Format: 
First input is a int value that corresponds to the branding expenses. 
Second input is a int value that corresponds to the travel expenses. 
Third input is a int value that corresponds to the food expenses. 
Fourth input is a int value that corresponds to the logistics expenses. 
  
Output Format: 
First line of the output should display the int value that corresponds to the total expenses for the Event. 
Next four lines should display the percentage rate of each of the expenses. 
Refer sample input and output for formatting specifications. 
[All text in bold corresponds to input and rest corresponds to output.] 
 
Sample Input and Output: 
Enter branding expenses 
20000 
Enter travel expenses 
40000 
Enter food expenses 
15000 
Enter logistics expenses 
25000 
Total expenses : Rs.100000.00 
Branding expenses percentage : 20.00% 
Travel expenses percentage : 40.00% 
Food expenses percentage : 15.00% 
Logistics expenses percentage : 25.00% 
'''


br=int(input("Enter branding expenses\n"))
tr=int(input("Enter travel expenses\n"))
fd=int(input("enter food expenses\n"))
lg=int(input("Enter logistic expenses\n"))
tot=br+tr+fd+lg
print("Total expenses : Rs. {:.2f}%".format(float(tot)))
print("Branding expenses percentage: {:.2f}%".format((br/tot)*100))
print("travel expenses percentage:{:.2f}%".format((tr/tot)*100))
print("food expenses percentage:{:.2f}%".format((fd/tot)*100))
print("logistic expenses percentage:{:.2f}%".format((lg/tot)*100))
