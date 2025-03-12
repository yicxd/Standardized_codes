list = [] #list of all numbers
dupes = [] #list of all duplicates
nondupe = set() #set stores unique numbers only

for i in range(10): #ask for 10 numbers
    num = int(input("Enter a whole number: "))
    list.append(num) #puts the numbers in the list

for num in list:
    if num in nondupe:
        dupes.append(num)
    else:
        nondupe.add(num)

print(nondupe)