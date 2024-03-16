from locale import currency
from tempfile import TemporaryDirectory


class Linked_List:
    
    class __Node:
        def __init__(self, v, p, n): #value,previous, next
            # Declare and initialize the public attributes for objects of the
            # Node class. TODO replace pass with your implementation
            self.val = v
            self.next = n
            self.prev = p

    

    def __init__(self):
        # Declare and initialize the private attributes for objects of the
        # sentineled Linked_List class TODO replace pass with your
        # implementation
        self.__header = self.__Node(None,None,None) # val prev next
        self.__trailer = self.__Node(None,self.__header,None)
        self.__header.next = self.__trailer
        self.__len = 0

    def __len__(self):
        # Return the number of value-containing nodes in this list. TODO replace
        # pass with your implementation
        return(self.__len)
        

    def append_element(self, val):
        # Increase the size of the list by one, and add a node containing val at
        # the new tail position. this is the only way to add items at the tail
        # position. TODO replace pass with your implementation
        tempnode = self.__Node(val,self.__trailer.prev, self.__trailer)
        self.__trailer.prev.next = tempnode
        self.__trailer.prev = tempnode
        self.__len += 1

    def insert_element_at(self, val, index):
        # Assuming the head position (not the header node) is indexed 0, add a
        # node containing val at the specified index. If the index is not a
        # valid position within the list, raise an IndexError exception. This
        # method cannot be used to add an item at the tail position. TODO
        # replace pass with your implementation
        if index >= self.__len or index < 0:
            raise IndexError
        curr = self.__header
        for x in range(index):
            curr = curr.next

        tempnode = self.__Node(val,curr, curr.next)
        curr.next =  tempnode
        curr.next.next.prev =  tempnode
        self.__len += 1
        

    def remove_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, remove
        # and return the value stored in the node at the specified index. If the
        # index is invalid, raise an IndexError exception. TODO replace pass
        # with your implementation
        if index >= self.__len or index < 0:
            raise IndexError

        if index == (self.__len - 1):
            curr = self.__trailer.prev.prev
            stored_value = curr.next.val
            curr.next = curr.next.next
            curr.next.prev = curr
            self.__len -= 1
            return stored_value

        stored_value = None
        curr = self.__header
        for x in range(index):
            curr = curr.next
        stored_value = curr.next.val
        curr.next = curr.next.next
        curr.next.prev = curr
        self.__len -= 1
        return stored_value


    def get_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, return
        # the value stored in the node at the specified index, but do not unlink
        # it from the list. If the specified index is invalid, raise an
        # IndexError exception. TODO replace pass with your implementation
        if index >= self.__len or index < 0:
            raise IndexError
        if index == (self.__len - 1):
            return self.__trailer.prev.val
        curr = self.__header
        for x in range(index):
            curr = curr.next # takes you to curr -1th index
        return curr.next.val

    def rotate_left(self):
        # Rotate the list left one position. Conceptual indices should all
        # decrease by one, except for the head, which should become the tail.
        # For example, if the list is [ 5, 7, 9, -4 ], this method should alter
        # it to [ 7, 9, -4, 5 ]. This method should modify the list in place and
        # must not return a value. TODO replace pass with your implementation.
        if self.__len == 0:
            pass
        curr = self.__header.next
        temp = curr.val
        while (curr is not self.__trailer):
            curr.val = curr.next.val
            curr = curr.next
        self.__trailer.prev.val = temp
        

        
    def __str__(self):
        # Return a string representation of the list's contents. An empty list
        # should appear as [ ]. A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ]. You may assume
        # that the values stored inside of the node objects implement the
        # __str__() method, so you call str(val_object) on them to get their
        # string representations. TODO replace pass with your implementation
        if self.__len == 0:
            return "[ ]"
        str_rep = "[ "
        curr = self.__header.next
        while curr is not self.__trailer:
            str_rep = str_rep + str(curr.val) + ", "
            curr = curr.next
        str_rep = str_rep[0:len(str_rep)-2] + " ]"
        return str_rep

    def __iter__(self):
        # Initialize a new attribute for walking through your list TODO insert
        # your initialization code before the return statement. Do not modify
        # the return statement.
        self.__currentnode = self.__header.next
        return self

    def __next__(self):
        # Using the attribute that you initialized in __iter__(), fetch the next
        # value and return it. If there are no more values to fetch, raise a
        # StopIteration exception. TODO replace pass with your implementation
        if self.__currentnode is self.__trailer:
            raise StopIteration
        temp = self.__currentnode.val
        self.__currentnode = self.__currentnode.next
        return temp

    def __reversed__(self):
        # Construct and return a new Linked_List object whose nodes alias the
        # same objects as the nodes in this list, but in reverse order. For a
        # Linked_List object ll, Python will automatically call this function
        # when it encounters a call to reversed(ll) in an application. If
        # print(ll) displays [ 1, 2, 3, 4, 5 ], then print(reversed(ll)) should
        # display [ 5, 4, 3, 2, 1 ]. This method does not change the state of
        # the object on which it is called. Calling print(ll) again will still
        # display [ 1, 2, 3, 4, 5 ], even after calling reversed(ll). This
        # method must operate in linear time.
        newlist = Linked_List()
        curr = self.__trailer.prev
        while  (curr is not self.__header):
            newlist.append_element(curr.val)
            curr = curr.prev
        return newlist
        

# if __name__ == '__main__':
#     # Your test code should go here. Be sure to look at cases when the list is
#     # empty, when it has one element, and when it has several elements. Do the
#     # indexed methods raise exceptions when given invalid indices? Do they
#     # position items correctly when given valid indices? Does the string
#     # representation of your list conform to the specified format? Does removing
#     # an element function correctly regardless of that element's location? Does
#     # a for loop iterate through your list from head to tail? Does a for loop
#     # iterate through your reversed list from tail to head? Your writeup should
#     # explain why you chose the test cases. Leave all test cases in your code
#     # when submitting. TODO replace pass with your tests
#     ll = Linked_List()
#     print(ll)
#     ll.append_element(1)
#     ll.rotate_left()
#     # print("rotated left")
#     print(ll)
#     ll.append_element(2)
#     ll.append_element(45)
#     ll.append_element(67)
#     #ll.insert_element_at(90, 95) #properly raises index error when uncommented
#     #ll.insert_element_at(99,-1) # properly raises index error for -1 index
#     #ll.get_element_at(100) # properly raises index error exception for out of bounds
#     print(ll)
#     for x in (ll):
#         print(x)
#     ll.remove_element_at(2)
#     print(ll)
#     ll.rotate_left()
#     print(ll)
#     #ll.insert_element_at(0,3) # properly raises index error since not able to append to list
#     ll.insert_element_at(0,2)
#     print(ll)
#     ll.remove_element_at(2)
#     print(ll)
#     #ll.remove_element_at(3) # properly raises index error for remove at out of bounds index
#     #ll.remove_element_at(-5) # proper raises index error for out of bounds index
#     print(reversed(ll))
#     print(ll)
