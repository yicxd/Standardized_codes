list = [] #list of all numbers
n1 = set() #set only stores unique numbers

for i in range(10): #ask for 10 numbers
    num = int(input("Enter a whole number: "))
    list.append(num) #puts the numbers in the list

for num in list:
    n1.add(num)

print(n1)