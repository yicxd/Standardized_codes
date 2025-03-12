#i looped and added value error to all programs to make it easier for me to test (i misclick alot) :3
#it still works without them, remove while true, try, line 9-12

while True:
    try:
        print("Enter two whole numbers")
        x1 = int(input("enter first number: "))
        x2 = int(input("enter second number: "))
        break
    except ValueError:
        print("try entering whole numbers")
        continue

if x1 < x2:
    print(x2)
else:
    print(x1)