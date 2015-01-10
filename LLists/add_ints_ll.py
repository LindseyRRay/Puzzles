#Q: given head pointers of two linked lists where each represents an integer number backwards, add them and return the linked list
#Example ll1 = 1->4->5 = 514
#ll2 = 3->4->2 = 342
#sum = 4->8->7
import linked_list

def add_ints(head1, head2):
	output = linked_list.Node(None)
	new_head = output
	carry = 0
	while head1 != None or head2 != None or carry > 0:
		h1_val = (head1.value if head1 else 0)
		h2_val = (head2.value if head2 else 0)
		node_sum = (h1_val + h2_val + carry)%10
		carry = int((h1_val + h2_val + carry)/10)
		output.next = linked_list.Node(node_sum)
		output = output.next
		head1 = (None if head1 == None else head1.next)
		head2 = (None if head2 == None else head2.next)

	return new_head.next


def test_add():
	h1 = linked_list.create_ll(3)
	h2 = linked_list.create_ll(4)
	print("integer 1 is ")
	linked_list.print_ll(h1)
	print("Integer 2 is ")
	linked_list.print_ll(h2)
	head_sum = add_ints(h1, h2)
	print("Sum is ")
	linked_list.print_ll(head_sum)

test_add()
