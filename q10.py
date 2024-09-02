arr =[]
arr_size= int(input("Enter the size of the array : "))

for i in range(0,arr_size,1):
    print(i,"). ",end="")
    arr.append(int(input(" ")))
print("The array is : ", arr)

for i in range(0,arr_size,1):
    for j in range(0,arr_size-1,1):
        if arr[j]<=arr[j+1]:
            temp= arr[j+1]
            arr[j+1]=arr[j]
            arr[j]=temp
print("The sorted array is : ",arr)