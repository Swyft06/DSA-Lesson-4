#linear search

list1 = [1,2,3,4,5,6,7,8,9,10]

print(list1)
a = int(input("Enter a number:  "))

found = False
for num in range(0,len(list1)):
    if list1[num] == a:
        print("Key exists")
        found = True
        break

if found == False:
    print("Key does not exist")
