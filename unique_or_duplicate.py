list = []
og = set()

while True: #this loop will ask the user until value is invalid
    try:
        num = int(input("Enter a whole number: "))
        list.append(num)
        if num not in og: #if number is new adds it to the og set
            print("unique")
            og.add(num)
        else: #if number is found in og set its a duplicate
            print("duplicate")
        continue
    except ValueError: 
        break