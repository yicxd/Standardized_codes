while True:
    try:
        print("Enter two whole numbers")
        x1 = int(input("enter first number:"))
        x2 = int(input("enter second number:"))
        break
    except ValueError:
        print("try entering whole numbers")
        continue

if x1 == x2:
    print("Equal")
else:
    print("not equal")