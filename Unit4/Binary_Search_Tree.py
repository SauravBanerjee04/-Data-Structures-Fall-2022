import copy
class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the the methods.

    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None
      self.height = 1
    
      # TODO complete Node initialization

    def getbalance(self):
      if self.left == None:
        if self.right == None:
          return 0
        else:
          return self.right.height
      elif self.right == None:
        if self.left == None:
          return 0
        return 0 - self.left.height
      return self.right.height - self.left.height

    def updateheight(self):
      newheight = 1
      if self.left == None and self.right == None:
        self.height = 1
        return 1
      (lh,rh) = (0,0)
      if not (self.left == None):
        if self.left.value == None:
          self.left = None
        else:
          lh = self.left.updateheight()
      if not (self.right == None):
        if self.right.value == None:
          self.right = None
        else:
          rh = self.right.updateheight()
      self.height = 1 + max(lh,rh)
      return self.height
      


  def __init__(self):
    self.__root = None
    # TODO complete initialization

  def __rotate_left(self,root):
    newvalue = root.right.value #stores value for a new left node
    newleftvalue = root.value
    newleftsleft = root.left
    newleftsright = root.right.left

    newleftnode = self.__BST_Node(newleftvalue) #puts new left node in
    newleftnode.left = newleftsleft
    newleftnode.right = newleftsright

    root.right = root.right.right # fixes root
    root.value = newvalue
    root.left = newleftnode

    # newroot = copy.deepcopy(root.right)
    # root.right = newroot.left
    # newroot.left = root
    # newrootcopy = copy.deepcopy(root)
    # root.left = newrootcopy.left
    # root.right = newrootcopy.right
    # root.value = newrootcopy.value


    # newnode = self.__BST_Node(node.right.value)
    # newnode.left = node.right.left
    # newnode.right = node.right.right
    # node.right = newnode.left
    # newnode.left = self.__BST_Node(node.value)
    # newnode.left = node.left
    # newnode.right = node.right
    # (node.value, node.left, node.right) = (newnode.value,newnode.left,newnode.right)

    # temp = node.left
    # node.left = self.__BST_Node(node.value)
    # node.left.left = temp
    # node.value = node.right.value
    # node.right = node.right.right

  def __rotate_right(self,root):
    newvalue = root.left.value # takes the values for the new root's right node
    newrightvalue = root.value
    newrightsright = root.right
    newrightsleft = root.left.right

    newrightnode = self.__BST_Node(newrightvalue) # makes a new node
    newrightnode.left = newrightsleft
    newrightnode.right = newrightsright

    root.left = root.left.left #sets the new values for the new root
    root.value = newvalue
    root.right = newrightnode
    
    # newroot = copy.depcopy(root.left)
    # root.left = newroot.right
    # newroot.right = root
    # newrootcopy = copy.deepcopy(newroot)
    # root.left = newrootcopy.left
    # root.right = newrootcopy.right
    # root.value = newrootcopy.value

    # newnode = self.__BST_Node(node.left.value)
    # newnode.left = node.left.left
    # newnode.right = node.left.right
    # node.left = newnode.right
    # newnode.right = self.__BST_Node(node.value)
    # newnode.left = node.left
    # newnode.right = node.right

    # (node.value, node.left, node.right) = (newnode.value,newnode.left,newnode.right)
    # temp = node.right
    # node.right = self.__BST_Node(node.value)
    # node.right.right = temp
    # node.value = node.left.value
    # node.left = node.left.left



  def __balance(self, t):
    if t == None:
      pass
    else:
      balance = t.getbalance()
      if (balance == 2):
        if t.right.getbalance() == -1:
          self.__rotate_right(t.right)
          self.__rotate_left(t)
        else:
          self.__rotate_left(t)

      elif (balance == -2):
        if t.left.getbalance() == 1:
          self.__rotate_left(t.left)
          self.__rotate_right(t)
        else:
          self.__rotate_right(t)

  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    if self.__root == None:
      self.__root = self.__BST_Node(value)
    else:
      self.__insert_helper(self.__root,value)
    self.__root.updateheight()

  def __insert_helper(self, node, val):
    if val == node.value:
      raise ValueError()
    else:
      if val < node.value:
        if node.left == None:
          node.left = self.__BST_Node(val)
        else:
          self.__insert_helper(node.left, val)
      if val > node.value:
        if node.right == None:
          node.right = self.__BST_Node(val)
        else:
          self.__insert_helper(node.right, val)
      node.updateheight()
      self.__balance(node)
      
    

  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    if self.__root == None:
      raise ValueError
    self.__remove_helper(self.__root,value)
    self.__root.updateheight()
    if self.__root.value == None:
      self.__root = None

  def __remove_helper(self, node, val):
    if node == None:
      raise ValueError
    if val < node.value:
      self.__remove_helper(node.left,val)
    elif val > node.value:
      self.__remove_helper(node.right,val)
    else:
      self.__remove_node(node)
    if not node.value == None:
      node.updateheight()
    self.__balance(node)
    
  def __remove_node(self, node):
    if node.left == None and node.right == None: #if leaf
      node.value = None
    elif (node.left == None and not(node.right == None)) or (node.right == None and not(node.left == None)): #if has one child
      if node.left == None:
        node.value = node.right.value
        node.left = node.right.left
        node.right = node.right.right
      else:
        node.value = node.left.value
        node.right = node.left.right
        node.left = node.left.left
    else: #if has two children
      temp = node.right
      while not (temp.left == None): 
        temp = temp.left #finds inorder sucessor
      node.value = temp.value
      self.__remove_node(temp)


    
  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root == None:
      return "[ ]"
    return("[ " + str(self.__inorder_helper(self.__root))[1:-1] +" ]")

  def __inorder_helper(self, node):
    l = [node.value]
    if (node.left == None and node.right == None):
      return l
    if not node.left == None:
      l = self.__inorder_helper(node.left) + l
    if not node.right == None:
      l = l + self.__inorder_helper(node.right)
    return l

  def to_list(self):
    return self.__inorder_helper(self.__root)

  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root == None:
      return "[ ]"
    return("[ " + str(self.__preorder_helper(self.__root))[1:-1] +" ]")
  
  def __preorder_helper(self, node):
    l = [node.value]
    if (node.left == None and node.right == None):
      return l
    if not node.left == None:
      l = l + self.__preorder_helper(node.left) 
    if not node.right == None:
      l = l + self.__preorder_helper(node.right)
    return l


  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root == None:
      return "[ ]"
    return("[ " + str(self.__postorder_helper(self.__root))[1:-1] +" ]")
  
  def __postorder_helper(self, node):
    l = [node.value]
    if (node.left == None and node.right == None):
      return l
    if not node.right == None:
      l = self.__postorder_helper(node.right) + l
    if not node.left == None:
      l = self.__postorder_helper(node.left) + l
    return l

  
  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    if self.__root == None:
      return 0
    return self.__root.height

  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
  pass #unit tests make the main section unnecessary.
  bst = Binary_Search_Tree()
  # bst.insert_element(20)
  # bst.insert_element(30)
  # bst.insert_element(40)
  # bst.insert_element(50)
  # bst.insert_element(60)
  # bst.insert_element(70)
  # bst.insert_element(80)
  # bst.insert_element(90)
  # bst.insert_element(100)
  # bst.insert_element(110)
  # bst.insert_element(120)
  # bst.insert_element(130)
  # bst.insert_element(140)
  # bst.insert_element(150)
  # bst.insert_element(160)
  

  # bst.insert_element(60)
  # bst.insert_element(50)
  # bst.insert_element(70)
  # bst.insert_element(30)
  # bst.insert_element(55)
  # bst.insert_element(80)
  # bst.remove_element(60)
  # bst.remove_element(70)
  
  # print(bst)
  # print(bst.get_height())
