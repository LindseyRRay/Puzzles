#Determine if a word is a valid english word
#import enchant

def check_english(word):
	d = enchant.Dict("en_US")
	return d.check(word)

#without using dictionary
def check_english_file(word):
	for wrd in open_dict(word):
		print(wrd)
		if word == wrd:
			return True
	return False



def open_dict(word):	
	with open('/usr/share/dict/words', 'r') as f:
		for line in f:
			wrd = line.strip().lower()
			if wrd.startwith(word[0].lower()):
				yield wrd 


if __name__ == '__main__':
	check_english_file("Toast")