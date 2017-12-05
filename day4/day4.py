from collections import defaultdict

def is_phrase_valid2(phrase):
	words = phrase.split(' ')
	seen = set()
	for word in words:
		if contains_anagram(seen, word):
			return False
		seen.add(word)
	return True

def is_phrase_valid1(phrase):
	words = phrase.split(' ')
	seen = set()
	for word in words:
		if word in seen:
			return False
		seen.add(word)
	return True

def contains_anagram(wordset, word):
	word_char_count = get_char_count(word)
	for testword in wordset:
		test_char_count = get_char_count(testword)
		if counts_equal(word_char_count, test_char_count):
			return True
	return False

def counts_equal(char_count_1, char_count_2):
	if len(char_count_1.keys()) != len(char_count_2.keys()):
		return False

	for key in char_count_1.keys():
		if key not in char_count_2.keys():
			return False
		if char_count_1[key] != char_count_2[key]:
			return False
	return True

def get_char_count(word):
	counts = defaultdict(int)
	for c in word:
		counts[c] += 1
	return counts


def count_valid_passphrases(in_text):
	phrases = in_text.split('\n')
	count = 0
	for phrase in phrases:
		if(is_phrase_valid2(phrase)):
			count += 1

	return count

with open('input.txt', 'r') as f:
	in_text = f.read()