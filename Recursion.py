n = int(input("Enter the number:"))
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

print("the factorial of this number s : ",factorial(n))

