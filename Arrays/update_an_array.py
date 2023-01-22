arr = [1,3,5,7,8]
length = len(arr)
print("Our Array", arr)
pos = int(input("Enter positional index you want to change\nThey start from [0]\n"))

if pos <= length:
    new_value = int(input("Enter New Element Value:\n"))
    arr.insert(pos,new_value)
    print("Updated Array :",arr)

else:
    print("Sorry Position doesnt exist\nBye for now!")






