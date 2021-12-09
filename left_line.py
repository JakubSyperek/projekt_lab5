##zadanie jest niedokończone, mam nieznane problemy związane z BinaryTree, przez które funkcja left_line nie może zadziałać.

from typing import Any, List
from BinaryNode import BinaryNode
from BinaryTree import BinaryTree


def left_line(tree: BinaryTree) -> List[BinaryNode]:
    lista = [tree.root.value]
    wezel = tree.root

    while wezel.left_child is not None:
        lista.append(wezel.left_child.value)
        wezel = wezel.left_child
    return lista


tree_pd = BinaryTree(1)
tree_pd.root.add_left_child(2)
tree_pd.root.add_right_child(3)
tree_pd.root.left_child.add_left_child(4)
tree_pd.root.left_child.add_right_child(5)
tree_pd.root.right_child.add_right_child(7)
tree_pd.root.left_child.left_child.add_left_child(8)
tree_pd.root.left_child.left_child.add_right_child(9)


print("Koniec: ", end='')
print(left_line(tree_pd))
