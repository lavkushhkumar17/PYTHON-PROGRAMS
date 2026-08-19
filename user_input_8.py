# taking inputs from user

"""a=input()
print("My name is ",a)"""


#a=input("Enter your name: ")

#both are correct format



"""x=input("enter first number: ")
y=input("eneter second number: ")
print(x+y) # if we put 5 and 100 they gives output 5100 because it consider as string
output after declare is 105.
# we have to declare data type of input as int or float to get the sum of two numbers"""


"""x=str(input("enter first number: "))
y=str(input("eneter your second number: "))
print(x+y)     # a and lavkush gives =alavkush """



 
# Python Program to Demonstrate for all arithmetic operators
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print(f"{a} + {b} = {a + b}")       
print(f"{a} - {b} = {a - b}")   
print(f"{a} * {b} = {a * b}")     

# Check division by zero
if b != 0:
    print(f"{a} / {b} = {a / b}")      
    print(f"{a} // {b} = {a // b}")    
    print(f"{a} % {b} = {a % b}")    
else:
    print("Division, Floor Division, and Modulus cannot be performed because the second number is 0.")

print(f"{a} ** {b} = {a ** b}") 