# LList.py
from ListNode import ListNode

class LList:

    #------------------------------------------------------------

    def __init__(self, seq=()):

        """create an LList
        post: creates a list containing items in seq"""
     
        if seq == ():
            # No items to put in, create an empty list
            self.head = None
        else:
            # Create a node for the first item
            self.head = ListNode(seq[0], None)

            # Add remaining items keeping track of last node added
            last = self.head
            for item in seq[1:]:
                last.link = ListNode(item, None)
                last = last.link

        self.size = len(seq)
   
    #------------------------------------------------------------

    def __len__(self):

        '''post: returns number of items in the list'''

        return self.size

    #------------------------------------------------------------

    def _find(self, position):

        '''private method that returns node that is at location position
        in the list (0 is first item, size-1 is last item)
        pre: 0 <= position < self.size
        post: returns the ListNode at the specified position in the
        list'''
        
        assert 0 <= position < self.size

        node = self.head
        # move forward until we reach the specified node
        for i in range(position):
            node = node.link
        return node

    #------------------------------------------------------------

    def append(self, x):

        '''appends x onto end of the list
        post: x is appended onto the end of the list'''

        # create a new node containing x
        newNode = ListNode(x)

        # link it into the end of the list
        if self.head is not None:
            # non-empty list
            node = self._find(self.size - 1)
            node.link = newNode
        else:
            # empty list
            # set self.head to new node
            self.head = newNode
        self.size += 1

    #------------------------------------------------------------

    def __getitem__(self, position):

        '''return data item at location position
        pre: 0 <= position < size
        post: returns data item at the specified position'''

        node = self._find(position)
        return node.item
    
    #------------------------------------------------------------

    def __setitem__(self, position, value):

        '''set data item at location position to value
        pre: 0 <= position < self.size
        post: sets the data item at the specified position to value'''

        node = self._find(position)
        node.item = value

    #------------------------------------------------------------

    def __delitem__(self, position):

        '''delete item at location position from the list
        pre: 0 <= position < self.size
        post: the item at the specified position is removed from 
        the list'''

        assert 0 <= position < self.size

        self._delete(position)

    #------------------------------------------------------------

    def _delete(self, position):

        #private method to delete item at location position from the list
        # pre: 0 <= position < self.size
        # post: the item at the specified position is removed from the list
        # and the item is returned (for use with pop)

        if position == 0:
            # save item from the initial node
            item = self.head.item

            # change self.head to point "over" the deleted node
            self.head = self.head.link

        else:
            # find the node immediately before the one to delete
            prev_node = self._find(position - 1)

            # save the item from node to delete
            item = prev_node.link.item

            # change predecessor to point "over" the deleted node
            prev_node.link = prev_node.link.link

        self.size -= 1
        return item

    #------------------------------------------------------------

    def pop(self, i=None):

        '''returns and removes at position i from list; the default is to
        return and remove the last item

        pre: self.size > 0 and ((i is None or (0 <= i < self.size))

        post: if i is None, the last item in the list is removed
        and returned; otherwise the item at position i is removed 
        and returned'''

        assert self.size > 0 and (i is None or (0 <= i < self.size))

        # default is to delete last item
        # i could be zero so need to compare to None
        if i is None:
            i = self.size - 1
        
        return self._delete(i)

    #------------------------------------------------------------

    def insert(self, i, x):

        '''inserts x at position i in the list
        pre: 0 <= i <= self.size
        post: x is inserted into the list at position i and 
              old elements from position i..oldsize-1 are at positions 
              i+1..newsize-1'''

        assert 0 <= i <= self.size

        if i == 0:
            # insert before position 0 requires updating self.head
            self.head = ListNode(x, self.head)
        else:
            # find item that node is to be insert after
            node = self._find(i - 1)
            node.link = ListNode(x, node.link)
        self.size += 1

    #------------------------------------------------------------

    def __copy__(self):
    
        '''post: returns a new LList object that is a shallow copy of self'''
        
        a = LList()
        node = self.head
        while node is not None:
            a.append(node.item)
            node = node.link
        return a

    #------------------------------------------------------------

    
##     def __iter__(self):

##         # generator version works in both Python2 and Python3
##         node = self.head
##         while node is not None:
##             yield node.item
##             node = node.link

    #------------------------------------------------------------

    def __iter__(self):

        return LListIterator(self.head)

    #------------------------------------------------------------

    def __max__(self):
        '''
        Loops through and keeps note of the largest variable
        in the list and stores its value to a.

        Returns max(a)
        '''
        node = self.head
        a = 0
        while node is not None:
            if a <= node.item:
                a = node.item
                node = node.link
            else:
                node = node.link
        return a

    def __min__(self):
        '''
        Loops through and keeps note of the smallest variable
        in the list and stores its value to a.

        Returns min(a)       
        '''
        node = self.head
        a = node.item
        while node is not None:
            if a >= node.item:
                a = node.item
            node = node.link
            
        return a

    def index(self, x):
        '''
        Using a for-loop,
        Loops through the LList from range 0 - (size of the list)
        while iterating through the list searching for a match with
        x. 

        Returns i       
        '''
        node = self.head
        for i in range(self.size):
            
            item = node.item
            if x == item:
                return i 
            node = node.link

    def count(self, x):
        '''
        Counts the amount occurences of x in the LList.
        Loops through and adds one(1) to the variable
        count.

        Returns count       
        '''
        node = self.head
        count = 0
        while node is not None:
            if node.item == x:
                count += 1
            node = node.link           
        return count

    def remove(self, x):
        '''       
        Removes the item x from the list.
        cycles through the list and calls
        index inside the delete function
        and breaks once found.

        returns None
        '''
        node = self.head
        while node is not None:
            if node.item == x:
                self._delete(self.index(x))
                break
            node = node.link       
    
    #------------------------------------------------------------

class LListIterator:

    #------------------------------------------------------------

    def __init__(self, head):
        self.currnode = head

    #------------------------------------------------------------
    # Python2 version
    def next(self):
        if self.currnode is None:
            raise StopIteration
        else:
            item = self.currnode.item
            self.currnode = self.currnode.link
            return item

    #------------------------------------------------------------
    # Python3 version
    def __next__(self):
        if self.currnode is None:
            raise StopIteration
        else:
            item = self.currnode.item
            self.currnode = self.currnode.link
            return item


l = LList([143, 89, 4, 4, 245, 760, 17, 45])
print('Tests of functions: max, min, index, count, and remove(Returns: None)')
print('\t[143, 89, 4, 4, 245, 760, 17, 45]\n')
print('\tTest [Max]: ', l.__max__())
print('\tTest [Min]: ', l.__min__())
print('\tTest [Index]: ', l.index(45))
print('\tTest [Count]: ', l.count(4))
l.remove(4)




