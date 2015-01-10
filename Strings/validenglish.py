#Determine if a word is a valid english word
#import enchant

def check_english(word):
	d = enchant.Dict("en_US")
	return d.check(word)

#without using dictionary
def check_english_file(word):
	word = word.lower()
	for wrd in open_dict(word):
		if word == wrd:
			return True
	return False



def open_dict(word):	
	with open('/usr/share/dict/words', 'r') as f:
		for line in f:
			wrd = line.strip().lower()
			if wrd.startswith(word[0]):
				yield wrd 


if __name__ == '__main__':
	print(check_english_file("Toast"))