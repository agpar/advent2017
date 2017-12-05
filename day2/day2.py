def checksum1(input_text):
	matrix = parse_input(input_text)
	result = 0
	for row in matrix:
		larger, smaller = max(row), min(row)
		result += larger - smaller
	return result

def checksum2(input_text):
	matrix = parse_input(input_text)
	result = 0
	for row in matrix:
		larger, smaller = find_divisors(row)
		result += larger / smaller
	return result

def find_divisors(row):
	for i in range(0, len(row)):
		for j in range(i+1, len(row)):
			i_term = row[i]
			j_term = row[j]
			larger = max(i_term, j_term)
			smaller = min(i_term, j_term)
			if(larger % smaller == 0):
				return (larger, smaller)

def parse_input(input_text):
	matrix = [[int(x) for x in y.split(' ') if x] for y in input_text.split('\n')]
	return matrix

with open('input.txt', 'r') as f:
	input_text = f.read()