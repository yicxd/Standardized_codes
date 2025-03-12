count = 0
odds = 0
fcount = 10

while True:
    try:
        x = int(input("Enter 10 whole numbers:"))
        count = count + 1
        if x % 2 != 0:
            odds = odds + 1
        if count != fcount:
            continue
        else:
            break
    except ValueError:
        print("please enter whole numbers")

print("there are", odds, "odd numbers")