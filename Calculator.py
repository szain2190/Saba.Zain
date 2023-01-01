import math
def main():
    while True:
        print("What type of calculation would you like to perfom?")
        print("1. Sum")
        print("2. Powers")
        print("3. Square root")
        print("4. Quadratic roots")
        option = input("Choose option 1, 2, 3 or 4: ")
        if option == "1":
            sum()
        elif option == "2":
            powers()
        elif option == "3":
            squareRoot()
        elif option == "4":
            quadraticRoot()
        else:
            print("Invaild input,try again")

def sum():
    calculation = input("Enter a sum: ")
    mylist = calculation.split(" ")
    op = mylist[1]
    num1 = int(mylist[0])
    num2 = int(mylist[2])
    if op == "+":
       print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    print()

def powers():
    num1 = int(input("Enter a number: "))
    power = int(input("What number would you like it to be to the power of: "))
    result = 1
    for i in range(0,power):
        result *= num1
    print(f"{num1} to the power {power} is {result}")
    print()


def squareRoot():
    num1 = int(input("Enter the number to square root: "))
    result = math.sqrt(num1)
    print(f"the square root of {num1} is {result}")

def quadraticRoot():
    print("In the format ax^2+bx+c")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    if b*b - 4*a*c < 0:
        print("No solution")
    elif b*b - 4*a*c == 0:
        formula1 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
        print(f"Double root {formula1}")
    elif b*b - 4*a*c > 0:
        formula1 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
        formula2 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
        print(f"The quadratic roots are {formula1}, {formula2}")
main()