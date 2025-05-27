#Write a program using functions to find greatest of three numbers.

a = int(input("Enter number : "))
b = int(input("Enter number : "))
c = int(input("Enter number : "))

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
print("greatest number is :",greatest(a,b,c))    