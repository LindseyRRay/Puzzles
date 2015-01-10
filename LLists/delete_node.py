#Q: delete the node of a linked list
import linked_list

def delete_node(head, key):
	#special case if head == key
	if head == key:
		return head.next

	#otherwise keep track of pointer to previous item
	previous = None
	current = head
	while current != None:
		if current.value == key:
			previous.next = current.next
		previous = current
		current = current.next

	return head


def test_delete():
	test_ll = linked_list.create_ll(10)
	temp = test_ll.next
	test_ll.next = linked_list.Node(100, temp)
	linked_list.print_ll(test_ll)
	print("deleted ll")
	new_head = delete_node(test_ll, 100)
	linked_list.print_ll(test_ll)

test_delete()
