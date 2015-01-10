#Q: find the product of every integer in array except one at that index
#[1, 7, 3, 4]
#returns [84, 12, 28, 21] by calculating   [7*3*4, 1*3*4, 1*7*4, 1*7*3]
#Do not use division
#product of numbers after and before index
#we can store numbers already calculated as we go through the array, 
#we can also already know numbers before the index (these are numbers from lower order calcs)
#previous 0 	7	  1*7		1*7*3
#future 7*3*4   3*4     4   	0

def find_products(input_array):
	 # we make an array with the length of the input array to
    # hold our products
	products = [1]
	i = 1
	# for each integer, we find the product of all the integers
    # before it, storing the total product so far each time
	while i < len(input_array):
		products.append(products[-1]*input_array[i-1])
		i += 1
		
 # for each integer, we find the product of all the integers
    # after it. since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers
	backwards_product = 1
	i = len(input_array) - 1
	while i >= 0:
		products[i] *= backwards_product
		backwards_product *= input_array[i]
		i -= 1
	return products


	


