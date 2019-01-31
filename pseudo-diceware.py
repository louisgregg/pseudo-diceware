#!/usr/bin/python
import sys
import random
import re
"""
Count the number of instances of each unique word in a txt file.
I've modified this to covert all words to lowercase. 
Some code snippits taken from:
https://stackoverflow.com/questions/6255641/counting-the-number-of-unique-words-in-a-document-with-python

Dicts are implemented as hash tables and are theremore orders of magnitude faster than lists (i.e. arrays) for lookups. 
 See here:
https://stackoverflow.com/questions/38927794/python-dictionary-vs-list-which-is-faster/38927968
 ---> Will use the dict method below instead of a list.
"""
def string_cleaner(path_to_book):
	# exclude characters are not in a-z A-Z
	clean_string=re.sub('[^a-zA-Z ]',' ', open(path_to_book).read())
	# convert to lower case
	clean_string = clean_string.lower()
	# condense all whitespace and tabs to single spaces. 
	clean_string = re.sub(' +|\t',' ',clean_string)
	return(clean_string)

def create_wordcount_dict(clean_book_string):
	count = {}
	for w in clean_book_string.split(' '):
		if w not in count:
		    count[w] = 1
	print("There are "+str(len(count.keys()))+" unique words in the file.")
	return(count)

def diceware_calculator(count_dictionary, n_words):
	diceware_list = []
	for x in range(0,n_words):
		diceware_list.append(random.choice(list(count_dictionary.keys())))
	return(diceware_list)

def main(path_to_book, n_random_words):
	clean_book_string=string_cleaner(path_to_book)
	word_count_dict = create_wordcount_dict(clean_book_string)
	diceware_list = diceware_calculator(word_count_dict, n_random_words)
	return(diceware_list)

if __name__ == '__main__':
	path_to_book = str(sys.argv[1])
	n_random_words = int(sys.argv[2])
	word_list = main(path_to_book, n_random_words)
	print(word_list)