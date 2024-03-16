import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    self.__deque = get_deque()
    self.__stack = Stack()
    self.__queue = Queue()

  # TODO add your test methods here. Like Linked_List_Test.py,
  # each test should me in a method whose name begins with test_

if __name__ == '__main__':
  # unittest.main()
  p = Stack()
  print("Stack Testing: ")
  for x in range(10):
    print("Pushing: " + str(x))
    p.push(x)
    print("Size: " + str(len(p)) + " Array: " + str(p))
    print()
  print()
  for x in range(12):
    print("Calling Pop: ")
    print("Value of Peek: " + str(p.peek()))
    print("Value Returned from Pop: " + str(p.pop()))
    print("Length: " + str(len(p)))
    print("String Representation: " + str(p))
    print()
  
  p = Queue()
  print("Queue")
  for x in range(5):
    print("Queueing :" + str(x))
    p.enqueue(x)
    print("Size :" + str(len(p)) + " Array: " + str(p))
    print()
  print()
  for x in range(6):
    print("Calling Dequeue: ")
    print("Value of Peek: " + str(p.peek()))
    print("Value Returned from Dequeue: " + str(p.dequeue()))
    print("Length: " + str(len(p)))
    print("String Representation: " + str(p))
    print()