#basic node class for binary trees
class Node(object):
    def __init__(self, value, l=None, r=None):
        self.value = value
        self.left = l
        self.right = r

tree1 = Node(1, 
             Node(2,
                  Node(3),
                  Node(4)),
             Node(5,
                  Node(6),
                  Node(7)))

tree2 = Node(1,
             Node(2, 
                  Node(3)),
             Node(4))


tree3 = Node(1,
             Node(2, 
                  Node(3), Node(4, Node(5), Node(6))),
             Node(8))