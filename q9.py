arr1=[]
arr2=[]
arr1_size = int(input("Enter the first array size : "))
for i in range(0,arr1_size,1):
    print(i+1,"). ",end="")
    arr1.append(int(input()))

arr2_size = int(input("Enter the second array size : "))
for i in range(0,arr2_size,1):
    print(i+1,"). ",end="")
    arr2.append(int(input()))

print("The arrays are : ",arr1 ,arr2)

arr3 =[]
arr3=arr1
arr1=arr2
arr2=arr3

print("The swapped array is : ",arr1, arr2)