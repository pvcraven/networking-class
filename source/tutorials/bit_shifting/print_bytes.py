# How many bits should we encode. Usually 8, or some other multiple of 8
bits_to_encode = 8

# The b means this is a byte array.
# A byte array is different than a string. A letter in a string
# can be represented by multiple bytes. Here it can't. And this
# can have values other than letters if we really wanted.
byte_array = b'This is a message.'

# Loop through each byte in the array
for my_byte in byte_array:

    # Now pull each bit out of the letter.
	for bit_pos in range(bits_to_encode):

		bit = 1 << bit_pos & my_byte
		if bit != 0:
			bit_value = 1
		else:
			bit_value = 0

		print(bit_value, end="")

	# Done with this letter. Go to the next line.
	print()
