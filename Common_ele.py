#Find common elements
arr1 = [1,2,3,4]
arr2 = [2,3,5]
i = 0
j = 0
sri = []
while i < len(arr1) and j < len(arr2):
    if arr1[i] == arr2[j]:
        sri.append(arr1[i])
        i += 1
        j += 1
    elif arr1[i] < arr2[j]:
        i += 1
    else:
        j += 1
print(sri)