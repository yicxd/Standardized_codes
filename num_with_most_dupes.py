list = []

while True:
    try:
        num = int(input("Enter a whole number: "))
        list.append(num)
        continue
    except ValueError:
        break

#prevented myself from importing and using the counter()
#counts each elements first then max returns the frequent one
most = max(set(list), key = list.count)
print(most)