list = []

while True:
    try:
        num = int(input("Enter a whole number: "))
        list.append(num)
        continue
    except ValueError:
        break

print(min(list)) #min finds the smallest value in the list