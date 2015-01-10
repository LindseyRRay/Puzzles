#: check stringanagram

def check_anagram(word, comparison):
	#change case
	word = list(map(lambda x: x.upper(), word))
	comparison = list(map(lambda x: x.upper(), comparison))
	return (sorted(word) == sorted(comparison))
