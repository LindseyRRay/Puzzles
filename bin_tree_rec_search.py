#binary tree searching with recursion
#Write a recursive function to compute the sum of a binary tree of numbers. Here's an example of a tree:
import pdb 
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

def depth_search(node):
    #pdb.set_trace()
    if node.left == None and node.right == None:
        print("base %d"%node.value)
        return node.value
    else:
        try:
            depth_search(node.left)
        except:
            pass
        try:
            depth_search(node.right)
        except:
            pass
        print("Non base %d"%node.value)
        return node.value

if __name__ == '__main__':
    depth_search(tree1)
    print("tree 2")
    depth_search(tree2)