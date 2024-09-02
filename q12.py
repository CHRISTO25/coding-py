list1=[]
list2=[]
sum_list = []
size = int(input("Enter the size of the array : "))
for i in range(0,size,1):
    temp=[]
    for j in range(0,size,1):
        print(j+1,"). ",end="")
        temp.append(int(input('')))
    list1.append(temp)
print("The first list is : ",list1)

for i in range(0,size,1):
    temp=[]
    for j in range(0,size,1):
        print(j+1,"). ",end="")
        temp.append(int(input('')))
    list2.append(temp)
print("The second list is : ",list2)


for i in range(size):
    temp = []
    for j in range(size):
        temp.append(list1[i][j] + list2[i][j])
    sum_list.append(temp)

print("The sum of the two lists is:")
for row in sum_list:
    print(row)
