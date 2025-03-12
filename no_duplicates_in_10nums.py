count = 0
fcount = 10

while True:
    try:
        num = int(input("Enter a whole number: ")).split
        count = count + 1
        if count != fcount: #stops after asking the 10th number
            continue
        else:
            break
    except ValueError:
        print("please enter a whole number")

print(num)