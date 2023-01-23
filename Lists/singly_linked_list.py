"""
Implement a singly linked list and allow the Traversing and the adding of nodes into it.

A linked List is preferred over an array due to the simplicity of inserting and deleting from a linked ist
https://github.com/Ndhlovu1
"""

#Create a single Node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data # The data that will be added into the list
        self.next = next # Point to the next node in the potential list


#Create a Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None

    #Method to insert into the list a new node/value
    def insert(self, data):
        new_node = Node(data)
        #Verify if it is the first/head node
        if(self.head):
            current = self.head
            #Verify if there is a next pointer
            while(current.next):
                current = current.next
            #if there is another pointer already, simply add the current.next as a newnode to newnode
            current.next = new_node
        #Should there already be a head node then set this one as a normal node
        else:
            self.head = new_node

    #Create a traverse list method
    def view(self):
        #Assign a place to begin
        current = self.head
        #Loop through for as long as it is not empty
        print("BELOW IS OUR LINKED LIST - IF CREATED\n")
        print("**************************************************")
        while(current):
            
            print(current.data)
            current = current.next
        print("**************************************************")
        

"""
Test the connectivity between our Linked List and the Node
"""
#Create an instance of the linkedList
instance = LinkedList()
#Create some values with the insert()
instance.insert(12)
instance.insert(24)
instance.insert(4)
instance.insert("Ndhlovu1")
instance.insert("/")
instance.insert("github")
instance.insert(".com")
#Call the view method to traverse our newly created list
instance.view()
        






