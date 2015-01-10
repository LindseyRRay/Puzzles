# The indices are the time, as a number of minutes past trade opening time, which was 9:30am local time.
# The values are the price of Apple stock at that time, in dollars.

#we could do this problem in a couple ways; find max array len recursively or use brute force
def find_lowpoint(seq, low, mid):
	left_sum = -1000000
	running_sum = 0 
	while mid >= low:
		running_sum += seq[mid]
		if running_sum > left_sum:
			left_sum = running_sum
			mid -= 1
		else:
			break
	return mid+1, running_sum


def find_highpoint(seq, high, mid):
	right_sum = -1000000
	running_sum = 0 
	while mid <= high:
		running_sum += seq[mid]
		if running_sum > right_sum:
			right_sum = running_sum
			mid += 1
		else:
			break
	return mid, running_sum

def find_mid_crossing(seq, low, mid, high):
	#note these return exclusive indices so add one to low to get inclusive
	print("original sequence")
	print(seq)
	cross_low, low_sum = find_lowpoint(seq, low, mid)
	cross_high, high_sum = find_highpoint(seq, high, mid+1)
	print(seq[cross_low:cross_high])
	return cross_low, cross_high, low_sum + high_sum


def find_max(seq, low, high):
	if low == high:
		print("base case low is %s and hgih is %s" %(low, high))
		return (low, high, seq[low])
	else:
		mid = int((low+high)/2)
		print(",id is %s"%mid)
		left_low, left_high, left_sum = find_max(seq, low, mid)
		right_low, right_high, right_sum = find_max(seq, mid+1, high)
		cross_low, cross_high, cross_sum = find_mid_crossing(seq, low, mid, high)
		if left_sum >= right_sum and left_sum >= cross_sum:
			return left_low, left_high, left_sum
		elif right_sum >= left_sum and right_sum >= cross_sum:
			return right_low, right_high, right_sum
		else:
			return cross_low, cross_high, cross_sum

if __name__ == '__main__':
	#a = [3,2,1,5,9]
	#print(find_max(a, 0, len(a)-1))
	b = [-1, 2, 4, -10, 11, 7]
	print(find_max(b, 0, len(b)-1))
	#c = [-1, 2, -1, -1, 1, 0]
	#print(find_max(c, 0, len(c)-1))

