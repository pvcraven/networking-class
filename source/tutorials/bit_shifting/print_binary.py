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
	# Then use a bitwise and & to filter out every other
	# bit.
	# This requires a bit of explanation so don't glaze over
	# it, have the instructor spend time with you until you are
	# sure you understand shifting bits, and bit-wise and.
	bit = 1 << bit_pos & number_to_encode
	if bit != 0:
		bit_value = 1
	else:
		bit_value = 0

	print("Bit position {:2} is {} which is worth {:2}".format(bit_pos, bit_value, bit))
