count = 0
fcount = 10
list = []

while True:
    try:
        num = int(input("Enter a whole number: "))
        count = count + 1
        list.append(num)
        if count != fcount: #stops after asking the 10th number
            continue
        else:
            break
    except ValueError:
        print("please enter a whole number")

print(list)