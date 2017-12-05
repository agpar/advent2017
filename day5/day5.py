def jump2(txt_input):
	int_list = [int(x) for x in txt_input.split('\n') if x]
	indx = 0
	steps = 0
	while indx >= 0 and indx < len(int_list):
		steps += 1
		next_indx = indx + int_list[indx]
		if int_list[indx] >= 3:
			int_list[indx] -= 1
		else:
			int_list[indx] += 1
		indx = next_indx
	return steps

def jump1(txt_input):
	int_list = [int(x) for x in txt_input.split('\n') if x]
	indx = 0
	steps = 0
	while indx >= 0 and indx < len(int_list):
		steps += 1
		next_indx = indx + int_list[indx]
		int_list[indx] += 1
		indx = next_indx
	return steps

with open('input.txt', 'r') as f:
	f_input = f.read()