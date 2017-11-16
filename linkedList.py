#ARRAY/list VS LINKED list

list1 =["one","two","three","four","five"]

class node:
    def __init__(self, data=None):
        #contains the data of the node
        self.data = data
        #contains the pointer to the next element on the linked list. at fist it is almwasy none
        self.next = None

class linked_list:
    def __init__(self):
        #the head node never contains actual data, also not indexable, user not accessable, used as a place holder to point to th frst one. not a data node
        self.head = node()
    #append function to add new data ppoint to the current list. in the beginng this is used to add the first element to the list.
    def append(self,data):
        #first create a new node
        new_node = node(data)
        #stores the node that were currently working on, starts at the left most point
        current_node = self.head
#starts atthe left most point, then interates over all of the node, and once the next node of the current node is none, we know that that is the last and then can insert
        while current_node.next!= None:
            current_node = current_node.next
        #once we know we're at the last element of the list, we set the next node to the new node
        current_node.next = new_node
    #length to figure out how many nodes are in the list itslef
    def length(self):
        #points to current node as the head
        current_node = self.head
        #current number of nodes seen so far
        total = 0

        #interation. exits once at the last node
        while current_node.next != None:
            #increments total
            total+=1
            #goes to the next node and starts the process again
            current_node = current_node.next
        return total
    #helper function to display contents of list
    def display(self):
        #creates a list of elements seen
        elems =[]
        current_node = self.head
        #while theres still more nodes to traverse
        while current_node.next != None:
            current_node = current_node.next
            #adds nodes data to display to elements
            elems.append(current_node.data)
        #prints elements
        print(elems)

    #passes in the index of the data to search for
    def get(self,index):
        #make sure you cant go past the last node
        if index >= self.length():
            print("GET index out of range")
            return None
        #contains the current index that were looking at
        current_index = 0
        #the current node that were looking at, starts off at head
        current_node = self.head
        while True:
            #increments the current node( at the beginning it will be the head node)
            current_node= current_node.next
            #if the current index is equal to the one passed in
            if current_index ==  index:
                #return the data of that node
                 return current_node.data
             #otherwise, increment the current index and keep going
            current_index +=1



my_list = linked_list()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.display()
print(my_list.get(2))
