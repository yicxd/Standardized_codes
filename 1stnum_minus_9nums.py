count = 0
sum = 0
fcount = 9

x1 = int(input("Enter 10 whole numbers:"))

while True:
    try:
        x2 = int(input("Enter 10 whole numbers:"))
        sum = sum + x2
        count = count + 1
        if count != fcount:
            continue
        else:
            break
    except ValueError:
        print("please enter whole numbers")

print(x1 - sum)