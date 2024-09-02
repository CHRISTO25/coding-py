mark = float(input("Enter the mark : "))

if mark>90 and mark<=100:
    print("A Grade")
elif mark>=80 and mark <90:
    print("B Grade")
elif mark>=70 and mark <80:
    print("C Grade")
elif mark>=60 and mark <70:
    print("D Grade")
elif mark>=50 and mark <60:
    print("E Grade")
elif mark >=0 and mark <50:
    print("Failed")
else:print ("Enter a valid number")