# binary search

list1 = [1,2,3,4,5,6,7,9,10]

start = 0
end = len(list1)-1


found = False
k = int(input("Enter a number: "))

while start <= end:
    mid = (start+end)//2
    if list1[mid] == k:
        print("Key exists")
        found = True
        break
    elif list1[mid] > k:
        end = mid-1

    else:
        start = mid+1

if found == False:
    print("Key does not exist")
