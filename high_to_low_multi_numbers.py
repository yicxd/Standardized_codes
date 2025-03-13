list = []

while True:
    try:
        num = int(input("Enter a whole number: "))
        list.append(num)
        continue
    except ValueError:
        break

list.sort(reverse=True)
print(list)