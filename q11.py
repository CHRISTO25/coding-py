word = input("Enter the string : ")
# temp =[]

# for i in range(len(word)-1,-1,-1):
#     temp.append(word[i])
  
rev = word[::-1]
# rev= "".join(temp)
print(rev)
if word == rev :
    print("Palindrome")
else:
    print("Not a palindrome")


