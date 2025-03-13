list = [] #list of all numbers
dupes = set() #changed this to a set from previous code
nondupe = set() #set stores unique numbers only

for i in range(10): #ask for 10 numbers
    num = int(input("Enter a whole number: "))
    list.append(num) #puts the numbers in the list

for n in list:
    if n in nondupe:
        dupes.add(n)
    else:
        nondupe.add(n)

print(dupes)