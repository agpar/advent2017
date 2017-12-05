def count_circular_digits(digit_string):
	digit_list = [int(x) for x in digit_string]
	result = 0;
	for i in range(0, len(digit_list)):
		matched_digit = get_matched_digit(digit_list, i)
		if(matched_digit == digit_list[i]):
			result += matched_digit
	return result

def get_matched_digit(digit_list, index):
	jump_size = int(len(digit_list) / 2)
	next_index = (index + jump_size) % len(digit_list)
	return digit_list[next_index]


with open('input.txt', 'r') as f:
	input_text = f.read()