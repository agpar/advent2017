import math

def find_ring_sidelen(number):
	"""Find side length of ring number is in"""
	side_len = 1
	while(number > math.pow(side_len, 2)):
		side_len += 2
	return side_len

def find_offset(number, side_len):
	zero_offset = int(math.pow(side_len, 2) - math.floor(side_len / 2))
	offset = math.inf
	for i in range(0, 4):
		offset = min(abs(number - zero_offset), offset)
		zero_offset = zero_offset - (side_len - 1)
	return offset

def find_ring_depth(number):
	i = 0
	side_len = 1
	while(number > math.pow(side_len, 2)):
		side_len += 2
		i += 1
	return i

def find_man_distance(number):
	return find_ring_depth(number) + find_offset(number, find_ring_sidelen(number))