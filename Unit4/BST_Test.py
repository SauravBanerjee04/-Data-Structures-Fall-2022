import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BST_Tester(unittest.TestCase):
    def setUp(self):
        self.__string_tree = Binary_Search_Tree()

    def test_empty_tree_string(self): # Checks Empty Tree
        self.assertEqual('[ ]', str(self.__string_tree))

    def test_remove_from_empty_tree(self):
        with self.assertRaises(ValueError):
            self.__string_tree.remove_element(10)
        self.assertEqual('[ ]', str(self.__string_tree))

    def test_remove_nonexistent_element(self):
        self.__string_tree.insert_element(8)
        self.__string_tree.insert_element(9)
        self.__string_tree.insert_element(10)
        with self.assertRaises(ValueError):
            self.__string_tree.remove_element(11)
        self.assertEqual('[ 8, 9, 10 ]', str(self.__string_tree))

    def test_remove_element_twice(self):
        self.__string_tree.insert_element(8)
        self.__string_tree.insert_element(9)
        self.__string_tree.insert_element(10)
        self.__string_tree.remove_element(10)
        with self.assertRaises(ValueError):
            self.__string_tree.remove_element(10)    
        self.assertEqual('[ 8, 9 ]', str(self.__string_tree))

    def test_add_element_twice(self):
        self.__string_tree.insert_element(8)
        self.__string_tree.insert_element(9)
        self.__string_tree.insert_element(10)
        with self.assertRaises(ValueError):
            self.__string_tree.insert_element(10)    
        self.assertEqual('[ 8, 9, 10 ]', str(self.__string_tree))

    
    
    def test_empty_tree_after_removing_elements(self):
        self.__string_tree.insert_element(0)
        self.__string_tree.insert_element(10)
        self.__string_tree.insert_element(20)
        self.__string_tree.remove_element(0)
        self.__string_tree.remove_element(20)
        self.__string_tree.remove_element(10)
        self.assertEqual( '[ ]', str(self.__string_tree))

    def test_add_one_element(self):
        self.__string_tree.insert_element(0)
        self.assertEqual('[ 0 ]', str(self.__string_tree))
    
    def test_checkpreorder_add_one_element(self):
        self.__string_tree.insert_element(0)
        self.assertEqual('[ 0 ]', str(self.__string_tree.pre_order()))
    
    def test_checkpostorder_add_one_element(self):
        self.__string_tree.insert_element(0)
        self.assertEqual('[ 0 ]', str(self.__string_tree.post_order()))
    

    
    def test_add_two_descending_elements(self):
        self.__string_tree.insert_element(0)
        self.__string_tree.insert_element(-10)
        self.assertEqual('[ -10, 0 ]', str(self.__string_tree))
    
    def test_checkpreorder_add_two_descending_elements_order(self):
        self.__string_tree.insert_element(0)
        self.__string_tree.insert_element(-10)
        self.assertEqual( '[ 0, -10 ]', str(self.__string_tree.pre_order()))

    def test_checkpostorder_two_descending_elements_order(self):
        self.__string_tree.insert_element(0)
        self.__string_tree.insert_element(-10)
        self.assertEqual( '[ -10, 0 ]', str(self.__string_tree.post_order()))

    def test_add_two_increasing_elements(self):
        self.__string_tree.insert_element(0)
        self.__string_tree.insert_element(10)
        self.assertEqual('[ 0, 10 ]', str(self.__string_tree))

    def test_checkpreorder_add_two_increasing_elements(self):
        self.__string_tree.insert_element(0)
        self.__string_tree.insert_element(10)
        self.assertEqual('[ 0, 10 ]', str(self.__string_tree.pre_order()))

    def test_checkpostorder_add_two_increasing_elements(self):
        self.__string_tree.insert_element(0)
        self.__string_tree.insert_element(10)
        self.assertEqual('[ 10, 0 ]', str(self.__string_tree.post_order()))

    def test_add_ten_increasing_elements(self):
        for x in range (10):
            self.__string_tree.insert_element(x)
        self.assertEqual( '[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]', str(self.__string_tree))
    
    def test_checkpreorder_add_ten_increasing_elements(self):
        for x in range (10):
            self.__string_tree.insert_element(x)
        self.assertEqual( '[ 3, 1, 0, 2, 7, 5, 4, 6, 8, 9 ]', str(self.__string_tree.pre_order()))

    def test_add_ten_increasing_elements(self):
        for x in range (10):
            self.__string_tree.insert_element(x)
        self.assertEqual( '[ 0, 2, 1, 4, 6, 5, 9, 8, 7, 3 ]', str(self.__string_tree.post_order()))

    def test_stresstestadd_25_increasing_elements(self):
        for x in range (25):
            self.__string_tree.insert_element(x)
        self.assertEqual('[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 ]', str(self.__string_tree))
    
    


    def test_checkinorder_right_rotation_with_three_elements(self):
        self.__string_tree.insert_element(2)
        self.__string_tree.insert_element(1)
        self.__string_tree.insert_element(0)
        self.assertEqual('[ 0, 1, 2 ]' ,str(self.__string_tree.in_order()))

    def test_checkpreorder_right_rotation_with_three_elements(self):
        self.__string_tree.insert_element(2)
        self.__string_tree.insert_element(1)
        self.__string_tree.insert_element(0)
        self.assertEqual('[ 1, 0, 2 ]', str(self.__string_tree.pre_order()))
    
    def test_checkpostorder_right_rotation_with_three_elements(self):
        self.__string_tree.insert_element(2)
        self.__string_tree.insert_element(1)
        self.__string_tree.insert_element(0)
        self.assertEqual('[ 0, 2, 1 ]',str(self.__string_tree.post_order()))

    def test_checkinorder_doubleleft_rotation_with_three_elements(self):
        self.__string_tree.insert_element(0)
        self.__string_tree.insert_element(10)
        self.__string_tree.insert_element(5)
        self.assertEqual('[ 0, 5, 10 ]', str(self.__string_tree.in_order()))

    def test_checkpreorder_doubleleft_rotation_with_three_elements(self):
        self.__string_tree.insert_element(0)
        self.__string_tree.insert_element(10)
        self.__string_tree.insert_element(5)
        self.assertEqual('[ 5, 0, 10 ]', str(self.__string_tree.pre_order()))
    
    def test_postorder_doubleleft_rotation_with_three_elements(self):
        self.__string_tree.insert_element(0)
        self.__string_tree.insert_element(10)
        self.__string_tree.insert_element(5)
        self.assertEqual( '[ 0, 10, 5 ]', str(self.__string_tree.post_order()))
    

    # these next few cases check whether the double right rotation work
    def test_checkdoubleright_rotationpt1(self):
        self.__string_tree.insert_element(3)
        self.__string_tree.insert_element(1)
        self.assertEqual( '[ 1, 3 ]', str(self.__string_tree))

    def test_checkdoublerightpreorder_rotationpt1(self):
        self.__string_tree.insert_element(3)
        self.__string_tree.insert_element(1)
        self.assertEqual( '[ 3, 1 ]', str(self.__string_tree.pre_order()))

    def test_checkdoublerightpostorder_rotationpt1(self):
        self.__string_tree.insert_element(3)
        self.__string_tree.insert_element(1)
        self.assertEqual( '[ 3, 1 ]', str(self.__string_tree.pre_order()))

    #add element which causes right rotation
    def test_checkdoubleright_rotationpt2(self):
        self.__string_tree.insert_element(3)
        self.__string_tree.insert_element(1)
        self.__string_tree.insert_element(2)
        self.assertEqual( '[ 1, 2, 3 ]', str(self.__string_tree))

    def test_checkpreorder_doubleright_rotationpt2(self):
        self.__string_tree.insert_element(3)
        self.__string_tree.insert_element(1)
        self.__string_tree.insert_element(2)
        self.assertEqual( '[ 2, 1, 3 ]', str(self.__string_tree.pre_order()))

    def test_checkpostorder_doubleright_rotationpt2(self):
        self.__string_tree.insert_element(3)
        self.__string_tree.insert_element(1)
        self.__string_tree.insert_element(2)
        self.assertEqual( '[ 1, 3, 2 ]', str(self.__string_tree.post_order()))
    

    #checks  a double left after adding in 7, 20 then 9
    def test_checkinorder_doubleleft_rotationpt1(self):
        self.__string_tree.insert_element(7)
        self.__string_tree.insert_element(20)
        self.assertEqual( '[ 7, 20 ]', str(self.__string_tree))
    
    def test_checkpreorder_doubleleft_rotationpt1(self):
        self.__string_tree.insert_element(7)
        self.__string_tree.insert_element(20)
        self.assertEqual( '[ 7, 20 ]', str(self.__string_tree.pre_order()))

    def test_checkpostorder_doubleleft_rotationpt1(self):
        self.__string_tree.insert_element(7)
        self.__string_tree.insert_element(20)
        self.assertEqual( '[ 20, 7 ]', str(self.__string_tree.post_order()))

    def test_checkinorder_doubleleft_rotationpt2(self):
        self.__string_tree.insert_element(7)
        self.__string_tree.insert_element(20)
        self.__string_tree.insert_element(9)
        self.assertEqual( '[ 7, 9, 20 ]', str(self.__string_tree))

    def test_checkpreorder_doubleleft_rotationpt2(self):
        self.__string_tree.insert_element(7)
        self.__string_tree.insert_element(20)
        self.__string_tree.insert_element(9)
        self.assertEqual( '[ 9, 7, 20 ]', str(self.__string_tree.pre_order()))

    def test_checkpostorder_doubleleft_rotationpt2(self):
        self.__string_tree.insert_element(7)
        self.__string_tree.insert_element(20)
        self.__string_tree.insert_element(9)
        self.assertEqual( '[ 7, 20, 9 ]', str(self.__string_tree.post_order()))



    def test_addtree(self):
        self.__string_tree.insert_element(15)
        self.__string_tree.insert_element(9)
        self.__string_tree.insert_element(20)
        self.__string_tree.insert_element(8)
        self.__string_tree.insert_element(11)
        self.__string_tree.insert_element(10)
        self.assertEqual( '[ 8, 9, 10, 11, 15, 20 ]', str(self.__string_tree))
    
    def test_rippleeffect(self):
        self.__string_tree.insert_element(15)
        self.__string_tree.insert_element(9)
        self.__string_tree.insert_element(20)
        self.__string_tree.insert_element(8)
        self.__string_tree.insert_element(11)
        self.__string_tree.insert_element(10)
        self.__string_tree.remove_element(15) #removes root
        self.assertEqual( '[ 8, 9, 10, 11, 20 ]', str(self.__string_tree))

    def test_rippleeffect_checkpreorder(self):
        self.__string_tree.insert_element(15)
        self.__string_tree.insert_element(9)
        self.__string_tree.insert_element(20)
        self.__string_tree.insert_element(8)
        self.__string_tree.insert_element(11)
        self.__string_tree.insert_element(10)
        self.__string_tree.remove_element(15) #removes root
        self.assertEqual( '[ 11, 9, 8, 10, 20 ]', str(self.__string_tree.pre_order()))

    def test_rippleeffect_checkpostorder(self):
        self.__string_tree.insert_element(15)
        self.__string_tree.insert_element(9)
        self.__string_tree.insert_element(20)
        self.__string_tree.insert_element(8)
        self.__string_tree.insert_element(11)
        self.__string_tree.insert_element(10)
        self.__string_tree.remove_element(15) #removes root
        self.assertEqual( '[ 8, 10, 9, 20, 11 ]', str(self.__string_tree.post_order()))


    #checks ripple from adding 
    def test_rippleeffect2pt1(self): #before elements need to be shifted
        self.__string_tree.insert_element(20)
        self.__string_tree.insert_element(10)
        self.__string_tree.insert_element(40)
        self.__string_tree.insert_element(5)
        self.__string_tree.insert_element(12)
        self.assertEqual( '[ 5, 10, 12, 20, 40 ]', str(self.__string_tree))

    def test_rippleeffect2_preorderpt1(self):
        self.__string_tree.insert_element(20)
        self.__string_tree.insert_element(10)
        self.__string_tree.insert_element(40)
        self.__string_tree.insert_element(5)
        self.__string_tree.insert_element(12)
        self.assertEqual( '[ 20, 10, 5, 12, 40 ]', str(self.__string_tree.pre_order()))

    def test_rippleeffect2_postorderpt1(self):
        self.__string_tree.insert_element(20)
        self.__string_tree.insert_element(10)
        self.__string_tree.insert_element(40)
        self.__string_tree.insert_element(5)
        self.__string_tree.insert_element(12)
        self.assertEqual( '[ 5, 12, 10, 40, 20 ]', str(self.__string_tree.post_order()))

    def test_rippleeffect2_inorderpt2(self):
        self.__string_tree.insert_element(20)
        self.__string_tree.insert_element(10)
        self.__string_tree.insert_element(40)
        self.__string_tree.insert_element(5)
        self.__string_tree.insert_element(12)
        self.__string_tree.insert_element(14)
        self.assertEqual( '[ 5, 10, 12, 14, 20, 40 ]', str(self.__string_tree))

    def test_rippleeffect2_preorderpt2(self):
        self.__string_tree.insert_element(20)
        self.__string_tree.insert_element(10)
        self.__string_tree.insert_element(40)
        self.__string_tree.insert_element(5)
        self.__string_tree.insert_element(12)
        self.__string_tree.insert_element(14)
        self.assertEqual( '[ 12, 10, 5, 20, 14, 40 ]', str(self.__string_tree.pre_order()))

    def test_rippleeffect2_postorderpt2(self):
        self.__string_tree.insert_element(20)
        self.__string_tree.insert_element(10)
        self.__string_tree.insert_element(40)
        self.__string_tree.insert_element(5)
        self.__string_tree.insert_element(12)
        self.__string_tree.insert_element(14)
        self.assertEqual( '[ 5, 10, 14, 40, 20, 12 ]', str(self.__string_tree.post_order()))

    #checkinganotherexample
    def test_checktree(self):
        self.__string_tree.insert_element(29)
        self.__string_tree.insert_element(16)
        self.__string_tree.insert_element(67)
        self.__string_tree.insert_element(5)
        self.__string_tree.insert_element(21)
        self.__string_tree.insert_element(38)
        self.__string_tree.insert_element(78)
        self.__string_tree.insert_element(9)
        self.__string_tree.insert_element(51)
        self.__string_tree.insert_element(72)
        self.__string_tree.insert_element(82)
        self.__string_tree.insert_element(94)
        self.assertEqual( '[ 5, 9, 16, 21, 29, 38, 51, 67, 72, 78, 82, 94 ]', str(self.__string_tree))

    def test_checktree_preorder(self):
        self.__string_tree.insert_element(29)
        self.__string_tree.insert_element(16)
        self.__string_tree.insert_element(67)
        self.__string_tree.insert_element(5)
        self.__string_tree.insert_element(21)
        self.__string_tree.insert_element(38)
        self.__string_tree.insert_element(78)
        self.__string_tree.insert_element(9)
        self.__string_tree.insert_element(51)
        self.__string_tree.insert_element(72)
        self.__string_tree.insert_element(82)
        self.__string_tree.insert_element(94)
        self.assertEqual( '[ 29, 16, 5, 9, 21, 67, 38, 51, 78, 72, 82, 94 ]', str(self.__string_tree.pre_order()))

    def test_checktree_postorder(self):
        self.__string_tree.insert_element(29)
        self.__string_tree.insert_element(16)
        self.__string_tree.insert_element(67)
        self.__string_tree.insert_element(5)
        self.__string_tree.insert_element(21)
        self.__string_tree.insert_element(38)
        self.__string_tree.insert_element(78)
        self.__string_tree.insert_element(9)
        self.__string_tree.insert_element(51)
        self.__string_tree.insert_element(72)
        self.__string_tree.insert_element(82)
        self.__string_tree.insert_element(94)
        self.assertEqual( '[ 9, 5, 21, 16, 51, 38, 72, 94, 82, 78, 67, 29 ]', str(self.__string_tree.post_order()))

    #chechs how removing an element does

    def test_removeelement_1(self):
        self.__string_tree.insert_element(29)
        self.__string_tree.insert_element(16)
        self.__string_tree.insert_element(67)
        self.__string_tree.insert_element(5)
        self.__string_tree.insert_element(21)
        self.__string_tree.insert_element(38)
        self.__string_tree.insert_element(78)
        self.__string_tree.insert_element(9)
        self.__string_tree.insert_element(51)
        self.__string_tree.insert_element(72)
        self.__string_tree.insert_element(82)
        self.__string_tree.insert_element(94)
        self.__string_tree.remove_element(21)
        self.assertEqual( '[ 5, 9, 16, 29, 38, 51, 67, 72, 78, 82, 94 ]', str(self.__string_tree))
    
    def test_removeelement_1_preorder(self):
        self.__string_tree.insert_element(29)
        self.__string_tree.insert_element(16)
        self.__string_tree.insert_element(67)
        self.__string_tree.insert_element(5)
        self.__string_tree.insert_element(21)
        self.__string_tree.insert_element(38)
        self.__string_tree.insert_element(78)
        self.__string_tree.insert_element(9)
        self.__string_tree.insert_element(51)
        self.__string_tree.insert_element(72)
        self.__string_tree.insert_element(82)
        self.__string_tree.insert_element(94)
        self.__string_tree.remove_element(21)
        self.assertEqual( '[ 67, 29, 9, 5, 16, 38, 51, 78, 72, 82, 94 ]', str(self.__string_tree.pre_order()))
    
    def test_removeelement_1_postorder(self):
        self.__string_tree.insert_element(29)
        self.__string_tree.insert_element(16)
        self.__string_tree.insert_element(67)
        self.__string_tree.insert_element(5)
        self.__string_tree.insert_element(21)
        self.__string_tree.insert_element(38)
        self.__string_tree.insert_element(78)
        self.__string_tree.insert_element(9)
        self.__string_tree.insert_element(51)
        self.__string_tree.insert_element(72)
        self.__string_tree.insert_element(82)
        self.__string_tree.insert_element(94)
        self.__string_tree.remove_element(21)
        self.assertEqual( '[ 5, 16, 9, 51, 38, 29, 72, 94, 82, 78, 67 ]', str(self.__string_tree.post_order()))

    #checking another removal
    def test_removeelement_2(self):
        self.__string_tree.insert_element(29)
        self.__string_tree.insert_element(16)
        self.__string_tree.insert_element(67)
        self.__string_tree.insert_element(5)
        self.__string_tree.insert_element(21)
        self.__string_tree.insert_element(38)
        self.__string_tree.insert_element(78)
        self.__string_tree.insert_element(9)
        self.__string_tree.insert_element(51)
        self.__string_tree.insert_element(72)
        self.__string_tree.insert_element(82)
        self.__string_tree.insert_element(94)
        self.__string_tree.remove_element(29)
        self.assertEqual( '[ 5, 9, 16, 21, 38, 51, 67, 72, 78, 82, 94 ]', str(self.__string_tree))

    def test_removeelement_2_preorder(self):
        self.__string_tree.insert_element(29)
        self.__string_tree.insert_element(16)
        self.__string_tree.insert_element(67)
        self.__string_tree.insert_element(5)
        self.__string_tree.insert_element(21)
        self.__string_tree.insert_element(38)
        self.__string_tree.insert_element(78)
        self.__string_tree.insert_element(9)
        self.__string_tree.insert_element(51)
        self.__string_tree.insert_element(72)
        self.__string_tree.insert_element(82)
        self.__string_tree.insert_element(94)
        self.__string_tree.remove_element(29)
        self.assertEqual( '[ 38, 16, 5, 9, 21, 67, 51, 78, 72, 82, 94 ]', str(self.__string_tree.pre_order()))
    
    def test_removeelement_2_postorder(self):
        self.__string_tree.insert_element(29)
        self.__string_tree.insert_element(16)
        self.__string_tree.insert_element(67)
        self.__string_tree.insert_element(5)
        self.__string_tree.insert_element(21)
        self.__string_tree.insert_element(38)
        self.__string_tree.insert_element(78)
        self.__string_tree.insert_element(9)
        self.__string_tree.insert_element(51)
        self.__string_tree.insert_element(72)
        self.__string_tree.insert_element(82)
        self.__string_tree.insert_element(94)
        self.__string_tree.remove_element(29)
        self.assertEqual( '[ 9, 5, 21, 16, 51, 72, 94, 82, 78, 67, 38 ]', str(self.__string_tree.post_order()))

    def test_removeelement_3(self):
        self.__string_tree.insert_element(29)
        self.__string_tree.insert_element(16)
        self.__string_tree.insert_element(67)
        self.__string_tree.insert_element(5)
        self.__string_tree.insert_element(21)
        self.__string_tree.insert_element(38)
        self.__string_tree.insert_element(78)
        self.__string_tree.insert_element(9)
        self.__string_tree.insert_element(51)
        self.__string_tree.insert_element(72)
        self.__string_tree.insert_element(82)
        self.__string_tree.insert_element(94)
        self.__string_tree.remove_element(5)
        self.assertEqual( '[ 9, 16, 21, 29, 38, 51, 67, 72, 78, 82, 94 ]', str(self.__string_tree))

    def test_removeelement_3_preorder(self):
        self.__string_tree.insert_element(29)
        self.__string_tree.insert_element(16)
        self.__string_tree.insert_element(67)
        self.__string_tree.insert_element(5)
        self.__string_tree.insert_element(21)
        self.__string_tree.insert_element(38)
        self.__string_tree.insert_element(78)
        self.__string_tree.insert_element(9)
        self.__string_tree.insert_element(51)
        self.__string_tree.insert_element(72)
        self.__string_tree.insert_element(82)
        self.__string_tree.insert_element(94)
        self.__string_tree.remove_element(5)
        self.assertEqual( '[ 67, 29, 16, 9, 21, 38, 51, 78, 72, 82, 94 ]', str(self.__string_tree.pre_order()))
   
    def test_removeelement_3_postorder(self):
        self.__string_tree.insert_element(29)
        self.__string_tree.insert_element(16)
        self.__string_tree.insert_element(67)
        self.__string_tree.insert_element(5)
        self.__string_tree.insert_element(21)
        self.__string_tree.insert_element(38)
        self.__string_tree.insert_element(78)
        self.__string_tree.insert_element(9)
        self.__string_tree.insert_element(51)
        self.__string_tree.insert_element(72)
        self.__string_tree.insert_element(82)
        self.__string_tree.insert_element(94)
        self.__string_tree.remove_element(5)
        self.assertEqual( '[ 9, 21, 16, 51, 38, 29, 72, 94, 82, 78, 67 ]', str(self.__string_tree.post_order()))

    def test_removeelement_4(self):
        self.__string_tree.insert_element(29)
        self.__string_tree.insert_element(16)
        self.__string_tree.insert_element(67)
        self.__string_tree.insert_element(5)
        self.__string_tree.insert_element(21)
        self.__string_tree.insert_element(38)
        self.__string_tree.insert_element(78)
        self.__string_tree.insert_element(9)
        self.__string_tree.insert_element(51)
        self.__string_tree.insert_element(72)
        self.__string_tree.insert_element(82)
        self.__string_tree.insert_element(94)
        self.__string_tree.remove_element(72)
        self.assertEqual( '[ 5, 9, 16, 21, 29, 38, 51, 67, 78, 82, 94 ]', str(self.__string_tree))
    
    def test_removeelement_4_preorder(self):
        self.__string_tree.insert_element(29)
        self.__string_tree.insert_element(16)
        self.__string_tree.insert_element(67)
        self.__string_tree.insert_element(5)
        self.__string_tree.insert_element(21)
        self.__string_tree.insert_element(38)
        self.__string_tree.insert_element(78)
        self.__string_tree.insert_element(9)
        self.__string_tree.insert_element(51)
        self.__string_tree.insert_element(72)
        self.__string_tree.insert_element(82)
        self.__string_tree.insert_element(94)
        self.__string_tree.remove_element(72)
        self.assertEqual( '[ 29, 16, 5, 9, 21, 67, 38, 51, 82, 78, 94 ]', str(self.__string_tree.pre_order()))

    def test_removeelement_4_postorder(self):
        self.__string_tree.insert_element(29)
        self.__string_tree.insert_element(16)
        self.__string_tree.insert_element(67)
        self.__string_tree.insert_element(5)
        self.__string_tree.insert_element(21)
        self.__string_tree.insert_element(38)
        self.__string_tree.insert_element(78)
        self.__string_tree.insert_element(9)
        self.__string_tree.insert_element(51)
        self.__string_tree.insert_element(72)
        self.__string_tree.insert_element(82)
        self.__string_tree.insert_element(94)
        self.__string_tree.remove_element(72)
        self.assertEqual( '[ 9, 5, 21, 16, 51, 38, 78, 94, 82, 67, 29 ]', str(self.__string_tree.post_order()))

        
if __name__ == '__main__':
  unittest.main()
