#basic fibonacci with memoization

def fib(n, memo):
	#print("calculating %d"%n)
	if n in memo.keys():	
		print("using memo %d"%n)
		return memo[n]
	elif n <= 2:
			return 1
	#print("calculating for %d and %d"%(n-1, n-2))
	fib_sum = fib(n-1, memo) + fib(n-2, memo)
	memo[n] = fib_sum
	return fib_sum


if __name__ == '__main__':
	memo = dict()

	print(fib(10, memo))
	print(fib(9, memo))
