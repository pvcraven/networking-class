# This program prints out the bits in a number.

# How many bits should we encode. Usually 8, or some other multiple of 8
bits_to_encode = 8

# What number do we want to encode?
number_to_encode = 23

# You can also encode letters by using ord(), which fetches
# the value of the letter.
# number_to_encode = ord('X')

# Loop for each bit
for bit_pos in range(bits_to_encode):

	# Use a single 1, and bit shift it with << to the
	# spot we are interested in.

	# 1 << 0 = 0000 0001 =   1
	# 1 << 1 = 0000 0010 =   2
	# 1 << 2 = 0000 0100 =   4
	# 1 << 3 = 0000 1000 =   8
	# 1 << 4 = 0001 0000 =  16
	# 1 << 5 = 0010 0000 =  32
	# 1 << 6 = 0100 0000 =  64
	# 1 << 7 = 1000 0000 = 128

	# Then use a bitwise and & to filter out every other
	# bit.

	# For example:

	# First bit
	#   0111 1010
	# & 0000 0001
	#   ---------
	#   0000 0000 = 0
	#
	# Second bit
	#   0111 1010
	# & 0000 0010
	#   ---------
	#   0000 0010 = 2 (non-zero)
	#
	# Third bit
	#   0111 1010
	# & 0000 0100
	#   ---------
	#   0000 0000 = 0
	#
	# Fourth bit
	#   0111 1010
	# & 0000 1000
	#   ---------
	#   0000 1000 = 8 (non-zero)

	bit = (1 << bit_pos) & number_to_encode
	if bit != 0:
		bit_value = 1
	else:
		bit_value = 0

	print("Bit position {:2} is {} which is worth {:2}".format(bit_pos, bit_value, bit))
