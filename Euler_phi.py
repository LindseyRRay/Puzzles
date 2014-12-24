#Calculate Euler's totient function phi(m)
#phi(m) is number of integers 1<=r<m that are coprime to m
#number of positive integers that are coprime to m
#implement the sieve of Atkins to calculate prime numbers
#phi(10)=4 (1, 3, 6, 9)
from math import sqrt 
from numpy import array
def isprime(n):
	for i in range(2,n):
		if n%i == 0:
			return False
	return True

def sieve_atkins(limit):
	#create results list
	primes = [False]*(limit+1)
	sqroot = int(sqrt(limit))+1

	if isprime(limit):
		return limit - 1

	for i in range(sqroot):
		for j in range(sqroot):
			#puts in candidate primes
			#integers with an odd number of representations
			#by certain quadratic forms 
			n = 4*i*i+j*j
			if (n <= limit) and (n%12 in [1,5]):
				primes[n]= True
			k = 3*i*i+j*j
			if n < limit and n%12 == 7:
				primes[n]= True
			if i > j:
				k = 3*i*i-j*j
				if n <= limit and n%12 == 11:
					primes[n]= True

	# Special Cases added to prime array
	primes[2] = True
	primes[3] = True
	primes[5] = True
	for num in range(5, limit):
		if primes[num]:
			for mult in range(num*num, limit, num):
				primes[mult] = False
				

	return len([p for p in primes if p==True]), primes
	



if __name__ == '__main__':
	print(sieve_atkins(10))
	print(sieve_atkins(15))
	assert sieve_atkins(7) == 6
	assert sieve_atkins(10) == 4
	assert sieve_atkins(16) == 8

			# if n is prime, omit multiples of its square






