def Addition(p, q):
    print(p+q)
def Subtraction(p, q):
    print(p-q)
def Multiplication(p, q):
    print(p*q)
def Division(p, q):
    print(p/q)

des = input("Please select the opration by typing the sign(+,-,*,/): ")
if des == "+" or des == "-" or des == "*" or des == "/":
    num_1 = int(input("Okay now enter the first value "))
    num_2 = int(input("Now enter the second value "))
    if des == "+":
        Addition(num_1, num_2)
    elif des == "-":
        Subtraction(num_1, num_2)
    elif des == "*":
        Multiplication(num_1, num_2)
    else:
        Division(num_1, num_2)
else:
    print("I said enter one of these +,-,*,/")