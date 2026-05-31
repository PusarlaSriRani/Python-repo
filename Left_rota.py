#Left rotate array by 1
arr=[3,8,9,6]
n=len(arr)
sri=arr[0]
for i in range(1,n):
    arr[i-1]=arr[i]
arr[n-1]=sri
print(arr)