list = [] #list of all numbers
nondupe = [] #set stores unique numbers only

for i in range(10): #ask for 10 numbers
    num = int(input("Enter a whole number: "))
    list.append(num) #puts the numbers in the list

for num in list:
    if list.count(num) == 1: #count checks how many times a number appears
        nondupe.append(num)

print(nondupe)