import math

def find_ring_sidelen(number):
	"""Find side length of ring number is in"""
	side_len = 1
	while(number > math.pow(side_len, 2)):
		side_len += 2
	return side_len

def find_offset(number, side_len):
	zero_offset = math.pow(side_len, 2) - math.floor(side_len / 2)
	offset = math.inf
	for i in range(0, 4):
		offset = min(abs(number - zero_offset))
		zero_offset = zero_offset - (side_len - 1)
	return offset
