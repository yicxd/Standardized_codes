count = 0
sum = 0
fcount = 10

while True:
    try:
        x = int(input("Enter 10 whole numbers:"))
        sum = sum + x
        count = count + 1
        if count != fcount:
            continue
        else:
            break
    except ValueError:
        print("please enter whole numbers")

print(sum)