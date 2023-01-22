arr = [1,3,5,7,8]
choice = int(input("Enter [1] for Value Search or Enter [2] for Positional Search\n"))

if choice == 1:
    value = int(input("Enter Value\n"))
    #Verify Value in Array
    if value in arr:
        print("Value "+str(value)+" Found at position : "+str(arr.index(value)))
    else:
        print("not found")

if choice == 2:
    pos = int(input("Enter Position\n"))
    #Verify Value in Array
    if pos <= len(arr):
        print("Value "+str(arr[pos])+" Found at position : "+str(pos))
    else:
        print("not found")

else:
    print("PLEASE CHOOSE VALID OPTION")


