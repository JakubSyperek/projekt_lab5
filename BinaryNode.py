from typing import Any


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'


    def __init__(self):
        self.left_child = None
        self.right_child = None
        self.value = None


    def __repr__(self):
        return f"Node {self.value}"

    def is_leaf(self):
        if self.left_child == None and self.right_child == None:
            return True
        return False


    def add_left_child(self, value):
        self.left_child == BinaryNode(value)



    def add_right_child(self,value):
        self.right_child == BinaryNode(value)

    def traverse_in_order(self):
        if self.left_child != None:
            return True
        elif self.right_child != None:
            return True


    def traverse_post_order(self):
        if self.left_child != None:
            return True
        elif self.right_child != None:
            return True


    def traverse_pre_order(self):
        if self.left_child != None:
            return True
        elif self.right_child != None:
            return True


        print("Koniec: ", end='')


