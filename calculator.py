def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y


print("Calculator")
x = int(input("Enter the first number"))
y = int(input("Enter the second number"))
choice = int(input("""1.Add/n
         2.Subtract/n
         3.multiply/n
         4.divide/n
         5.square of two numbers
         Enter the choice :-"""))


def squar(x, y):
    print("The square is ",x*x,y*y)


if choice == 1:
    print("The addition is",add(x,y))
elif choice == 2:
    print("The difference is:",subtract(x,y))
elif choice == 3:
    print("The product is :",multiply(x,y))
elif choice == 4:
    print("The division is:",divide(x,y))
elif choice == 5:
    squar(x,y)
else:
    print("Invalid choice try again")

