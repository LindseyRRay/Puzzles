#rev_str of words
# Given an input string, reverse the string word by word.

# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
import string

def reverseWords(s):

	#return " ".join([s.pop() for i in range(len(s)) if s[-1]!=" "])
	words = [word for word in s.strip().split(" ") if word != '']
	return " ".join([words.pop() for i in range(len(words))]).strip()

def revWords(s):
	return ' '.join(s.split()[::-1])

def palindrome_recursive(phrase):
#remove whitespace
	exclude = set(string.punctuation)
	phrase = "".join(ch for ch in phrase if ch not in exclude and ch !=' ')
	rev_str = rev_str_rec(phrase)
	print(rev_str)
	return rev_str

def rev_str_rec(phrase):
	if phrase == "":
		return phrase
	else:
		return phrase[-1]+rev_str_rec(phrase[:-1])


if __name__ == '__main__':

	# print(reverseWords("  a      b "))
	# print(reverseWords(" "))
	# print(reverseWords(" the sky is blue "))



	# print(revWords("  a      b "))
	# print(revWords(" "))
	# print(revWords(" the sky is blue "))
	print(palindrome_recursive("the sky is blue"))
	print(palindrome_recursive("madam my name is adam"))
