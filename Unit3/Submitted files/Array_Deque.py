from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    self.__len = 0
    # TODO replace pass with any additional initializations you need.
    pass
    
  def __str__(self):
    # TODO replace pass with an implementation that returns a string of
    # exactly the same format as the __str__ method in the Linked_List_Deque.
    # Orient your string from front (left) to back (right).
    if self.__len == 0:
      return "[ ]"
    else:
      st = "["
      t = 0
      while (t < self.__len):
        st = st + " " + str(self.__contents[t]) + ","
        t += 1
      st = st[:-1]
      st = st + " ]"
      return st


    
  def __len__(self): 
    # TODO replace pass with an implementation that returns the number of
    # items in the deque. This method must run in constant time.
      return self.__len

  def __grow(self):
    # TODO replace pass with an implementation that doubles the capacity
    # and positions existing items in the deque starting in cell 0 (why is
    # necessary?)
    self.__contents = self.__contents + [None] * self.__capacity
    self.__capacity = self.__capacity * 2
    
  def push_front(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if self.__len == 0:
      self.__contents[0] = val
      self.__len = 1
      
    else:
      if (self.__len + 1) > self.__capacity:
        self.__grow()
      for x in range(self.__len, 0, -1):
        self.__contents[x] = self.__contents[x-1]
      self.__contents[0] = val
      self.__len += 1

    
    
  def pop_front(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if self.__len == 0:
      return None
    temp = self.__contents[0]
    for x in range(0, self.__len-1):
      self.__contents[x] = self.__contents[x+1]
    self.__contents[self.__len - 1] = None
    self.__len -= 1
    return temp

    
  def peek_front(self):
    # TODO replace pass with your implementation.
    if self.__len == 0:
      return None
    return self.__contents[0]
    
  def push_back(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if (self.__len + 1) > self.__capacity:
      self.__grow()
    self.__contents[self.__len] = val
    self.__len += 1
  
  def pop_back(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if self.__len == 0:
      return None
    temp = self.__contents[self.__len - 1]
    self.__contents[self.__len - 1] = None
    self.__len = self.__len -1
    return temp
    pass

  def peek_back(self):
    # TODO replace pass with your implementation.
    if self.__len == 0:
      return None
    return self.__contents[self.__len -1]

# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':
#  pass
