list1 = [1,2,3,4,5,6,7,9,10]

k = int(input("Enter a number: "))

start = 0
end = len(list1) - 1
ans = len(list1)

while start <= end:
    mid = (start + end) // 2
    if list1[mid] >= k:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1
print("Lower bound:", ans)

start = 0
end = len(list1) - 1
ans = len(list1)

while start <= end:
    mid = (start + end) // 2
    if list1[mid] > k:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1
print("Upper bound:", ans)