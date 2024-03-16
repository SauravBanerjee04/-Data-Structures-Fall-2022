from Deque_Generator import get_deque

class Stack:

  def __init__(self):
    self.__dq = get_deque()

  def __str__(self):
    # TODO replace pass with your implementation.
    # Orient your string from top (left) to bottom (right).
    return self.__dq.__str__()

  def __len__(self):
    # TODO replace pass with your implementation.
    return self.__dq.__len__()

  def push(self, val):
    # TODO replace pass with your implementation.
    self.__dq.push_front(val)

  def pop(self):
    # TODO replace pass with your implementation.
    if self.__dq.__len__ == 0:
      return None
    return self.__dq.pop_front()

  def peek(self):
    # TODO replace pass with your implementation.
    if self.__dq.__len__ == 0:
      return None
    return self.__dq.peek_front()

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
