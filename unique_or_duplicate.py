list = []

while True: #this loop will ask the user until value is invalid
    try:
        num = int(input("Enter a whole number: "))
        list.append(num)
        continue
    except ValueError: 
        break