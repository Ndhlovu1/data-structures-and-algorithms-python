arr = [1,3,5,7,8]
length = len(arr)
print("Array Items : ",arr)
pos = int(input("Enter the Position to delete\n"))

#Ensure the value is not out of range
if pos <= length:
    arr.pop(pos)
    print("Array After Delete : \n", arr)
else:
    print("Sorry Position is out or Bounds!")
   
    


