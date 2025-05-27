#Write a python function to print multiplication table of a given number.def

n = int(input("Enter the  number : "))
def multiply(n):
    for i in range(1 , 11):
        print(f"{n}*{i}= {n*i}")

multiply(n)
