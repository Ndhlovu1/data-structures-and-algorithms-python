"""
Creating a linked list with inset and delete methods for data manipulation
"""

#create a single Node
class Node:
    def __init__(self,data= None, next = None):
        self.data = data
        self.next = next

#Create a Linked Class
class LinkedList:
    def __init__(self):
        self.head = None

    #Create the method for inserting
    def put(self, data):
        new_node = Node(data)

        #Verify if the self.head has no data inside it
        if(self.head):
            current = self.head
            #Verify if there is a next pointer/node to it
            while(current.next):
                current = current.next
            #if the self.head.next has a pointer then do the below
            current.next = new_node
        #Should a self.head already exist
        else:
            self.head = new_node

    #Create the Delete from Front method
    def delFront(self):
        #verify whether self.head is empty or not
        if(self.head != None):
            temp_head_storage = self.head
            #Change the node from the head and let it point to the next value
            self.head = self.head.next
            #Delete the temporary header
            print("Previous Head Node Was :",temp_head_storage.data)
            temp_head_storage = None
            print("LIST NOW IS :",self.head.data)
        else:
            print("List is Null")

    #Create the view List methods
    def view(self):
        current = self.head
        #loop through list until empty
        while(current):
            print(current.data)
            current = current.next
        print("\n###############################")
        print("The End of Our List")
        print("_________________________________")
 


#Create some testing scenarios
#Instantiate the Linked List
instance = LinkedList()
instance.put("Hello")
instance.put("From")
instance.put("The")
instance.put("Back-End")
instance.put("Guru")
#View the created Linked List
instance.view()
#Attempt to Delete the first Element
print("\n\n###############################")
print("\nDelete the first Node\n")
print("_______________________________")
instance.delFront()
print("_______________________________")
instance.delFront()
print("_______________________________")
instance.delFront()
        

        




