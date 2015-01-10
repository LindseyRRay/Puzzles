#Q: Reverse a linked list
#Show both iterative and recursive solutions

def iterative_reverse(head):
	#keep track of current pointer and previous item, 
	#set next item.next to previous item
	#special cases - list is empty
	if head == None:
		return head

	previous_item = None
	next_item = head
	while next_item != None:
		#create temp ref to next item 
		temp = next_item
		#set next to next item, could also be temp.next
		next_item = next_item.next
		#set node.next to previous node
		temp.next = previous_item 
		#update previous to current node
		previous_item = temp
	#return new head of the list
	return previous_item

def recursive_reverse(head):
	#base case
	if head == None or head.next == None:
		return head

	reversed_list = recursive_reverse(head.next)
	#set head of reversed list of pointer to current node
	head.next.next = head
	#step is not necessary for all nodes, but is important for the head
	head.next = None
	return reversed_list


