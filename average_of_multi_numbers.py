list = []

while True:
    try:
        num = int(input("Enter a whole number: "))
        list.append(num)
        continue
    except ValueError:
        break

#sum() is the sum of all in the list and len() is the count of elements
print(sum(list) / len(list))