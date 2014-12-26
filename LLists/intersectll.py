# Definition for singly-linked list.
from random import randint 

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#runs in O(n) time with O(1) memory
class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    @staticmethod 
    def getIntersectionNode(headA, headB):
    	#create pointers to top of both linked lists
    	#uses a hash table to keep track of visited addresses
    	pointer1, pointer2 = headA, headB
    	if pointer2 == None or pointer1 == None:
    		return None

    	id_list = list()	
    	while pointer1 != None and pointer2 != None:
    		id_list.append(id(pointer1))
    		if id(pointer2) in id_list:
    			return pointer2.val
    		pointer2 = pointer2.next
    		pointer1 = pointer1.next
    	return None

    def getIntersectionNode2(headA, headB):
    	#create pointers to top of both linked lists
    	pointer1, pointer2 = headA, headB
    	if 	

    	while pointer1 != None and pointer2 != None:
    		if pointer1 == pointer2:
    			return pointer1

    		pointer2 = pointer2.next
    		pointer1 = pointer1.next
    	return None

    @staticmethod
    def setupLinkedList(length):
    	i=0
    	node = ListNode(randint(0,10000))
    	while i < length:
    		new = ListNode(randint(0,10000))
    		new.next = node
    		node = new
    		i += 1
    	return node


if __name__ == '__main__':

	linkA = Solution.setupLinkedList(5)
	linkB = Solution.setupLinkedList(4)

	print(Solution.getIntersectionNode(linkA, linkB))

	linkB.next.next = linkA.next.next

	print(Solution.getIntersectionNode(linkA, linkB))
	linkA = None
	linkB = None 
	print(Solution.getIntersectionNode(linkA, linkB))
