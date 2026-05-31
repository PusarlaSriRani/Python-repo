#Find thelargest element
arr=[2,6,8,9]
max_val=arr[0]
for num in arr:
    if(num>max_val):
        max_val=num
print("Largest element is:",max_val)