#Determine if String has all unique characters
from collections import Counter
import pdb 

def unique_str(input_str):
	counter = Counter(input_str)
	for char in input_str:
		print("char is %s and count is %d" % (char, counter[char]))
		if counter[char] > 1:
			return False
	return True

def unique_no_ADT(input_str):
	#unique without additional data structures
	for char1 in input_str:
		count = 0
		for char2 in input_str:
			if char1 == char2:
				count +=1
		if count > 2:
			return False
	return True

def str_reverse(input_str):
	#reverse a string and add null character
	count = len(input_str)-1
	outstring = list()

	while count >= 0:
		outstring.append(input_str[count])
		count -=1
	outstring.append('\0')
	return "".join(outstring)

def remove_dups_nobuf(input_str):
	#remove duplicates without a temp buffer
	i=0
	n=len(input_str)
	while i<n:
		if input_str[i] in input_str[:i]:
			input_str = input_str[:i]+input_str[i+1:]
			n-=1
		else:
			i+=1
	return input_str


def anagram(input_str):
#check if anagrams
	output = list()
	i= len(input_str)-1
	while i >= 0:
		output.append(input_str[i])
		i-=1
	out_str="".join(output)
	print("anagram is %s"%out_str)
	return out_str==input_str


def replace_spaces(input_str):
	#replace spaces with '%20'
	n=0
	l = len(input_str)
	while n<l:
		if input_str[n] == ' ':
			input_str=input_str[:n]+'%20'+input_str[n+1:]
			l+=2
		n+=1
	return input_str


def rotate(in_matrix):
	#rotate a matric by 90 degrees
	



def set_zero(in_matrix):
	#for input matrix, if any element is 0, set row, col to 0
	pass

def check_rotation(input_str):
	#check if words are rotions of each other
	#ex waterbottle is roation of erbottlewat
	pass


if __name__ == '__main__':

	print(unique_no_ADT('abcse'))
	print(unique_no_ADT('abcdeeea'))
	print(str_reverse("hat"))

	print(str_reverse("James"))

	print(remove_dups_nobuf("The fast horse jumped over acres"))
	print(anagram("madam"))

	print(anagram("hello"))
	print(replace_spaces("The fast horse jumped over acres"))
	mat = [[1,2,3],[4,5,6]]
	t = rotate(mat)
	pdb.set_trace()
	
	