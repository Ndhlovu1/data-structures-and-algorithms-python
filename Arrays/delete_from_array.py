arr = [1,3,5,7,8]
length = len(arr)
print("Array Items : ",arr)
pos = int(input("Enter the Position to delete\n"))

#Perform Deletion
# while pos < length:
#     # arr[pos -1 ] = arr[pos] #Change the value in that position by moving upwards on the array
#     pos = pos +1 #Reduce the length of the array
#     arr.pop(pos)

if pos <= length:
    arr.pop(pos)

print("Array After Change : \n", arr)

