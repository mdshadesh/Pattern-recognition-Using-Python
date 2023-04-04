"""
indentation
1. input and output
print("Hello World")
Hello World
a=input("Enter your age")
Enter your age20
a=int(input("Enter your age = "))
Enter your age = 30
print(a)
30
2. variable declaration
year=0
year= "Enter your age  "
year= 2.5
3. Single and multiple line comment
4. for loop
for i in range(1,10,2):
    print(i)
for i in [3,4]:
    print(i)
for i in range(10):
    print(i)
4. user define function
#defination of sum function
def sum(a, b):
    s=a+b
    return s
#calling sum function
s = sum(5,5)
print(s)
5. array manipulation
6.packages: numpy, matplotlib
"""
#tutorialpoints
#geeksforgeeks
#javatpoint
#w3schools
#guru99
'''
x=5
y=6
if x>4:
    print(x)
    print(x)
print(y)
'''
def sum(a, b):
    s=a+b
    return s,s+5

s=sum(5, 10)
print(s[-1])

a = int(input("Enter interger number="))
#a=4.5555
print("value for a = {:.2f}".format(a))