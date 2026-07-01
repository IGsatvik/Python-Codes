print("Welcome to Python calculator")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice=int(input("Enter your choice : "))
x=float(input("Enter first variable : "))
y=float(input("Enter second variable : "))
if choice == 1 :
    print(f"Your answer is {x+y}")
elif choice == 2 :
    print(f"Your answer is {x-y}")
elif choice == 3 :
    print(f"Your answer is {x*y}")
elif choice == 4 :
    if y != 0 :
        print(f"Your answer is {round(x/y,3)}")
    else :
        print("Division not possible")
#use pass to skip code block

if choice !=0 :
    pass
