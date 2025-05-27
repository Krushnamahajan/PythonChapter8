#Write a python program using function to convert Celsius to Fahrenheit.

celsius = int(input("Enter the value in Celsius : "))

def c_to_f(celsius):
    return (celsius * 9/5) + 32

print(f"convert Celsius to Fahrenheit is :{c_to_f(celsius)}°F ")