# HELPER FUNCTIONS FOR BIT MANIPULATION


def byte_to_bits(byte_value):
    # Take byte as output by python's read() and format to string of bits
    return format(byte_value, '08b')


def bits_to_byte(bits):
    # Take string of bits and output byte data
    return int(bits, 2).to_bytes(len(bits) // 8, byteorder='big')


def reverse_bits(bits):
    return bits[::-1]


def bit_string_to_int(bit_string):
    # Translate string of bits to int
    out = 0
    for bit in bit_string:
        out = (out << 1) | int(bit)
    return out


def int_to_bit_list(n, min_size):
    # Translate int to workable list of bits with zero padding
    bits = [1 if digit == '1' else 0 for digit in bin(n)[2:]]
    if len(bits) < min_size:
        bits = [0] * (min_size - len(bits)) + bits
    return bits


def read_bits(data, offset, size):
    # Take byte data and read bits specified by offset and size (number of bits to read), while performing all of the
    # required manipulations due to the way diablo 2 handles bit data. Return int value of bits.
    byte_start = int(offset / 8)  # Since python can't read individual bits, we need to read the entire byte range
    byte_end = int((offset + size)/8)
    bytes_to_read = byte_end - byte_start + 1
    result = []

    for byte_idx in range(bytes_to_read):
        byte = byte_start + byte_idx  # Current byte to read
        bits_raw = reverse_bits(byte_to_bits(data[byte]))  # Convert byte to bit data and reverse due to endian
        # Next, create a mask of which bits we are actually interested in and filter the bit data using the mask
        bits_to_read = [1 if offset <= byte * 8 + bit_idx < offset + size
                        else 0
                        for bit_idx in range(8)]
        bits = [i for (i, v) in zip(bits_raw, bits_to_read) if v]
        result = result + bits  # Add to result

    return bit_string_to_int(reverse_bits(result))  # Flip bits again due to endian, translate to int and return


def write_bits(data, offset, size, value_to_write):
    # Take int value and replace the desired range in given byte data, zero padding as necessary according to the
    # given size, while performing the required bit manipulations.
    value_reversed = reverse_bits(int_to_bit_list(value_to_write, size))  # First translate int to bit list and reverse
    byte_start = int(offset / 8)  # Since python can't read individual bits, we need to replace the entire byte range
    byte_end = int((offset + size - 1)/8)
    bytes_to_read = byte_end - byte_start + 1
    data_new = data[:byte_start]  # Binary literals in python are immutable, so we need to create a new byte object.
    # Anything up to the starting byte remains unchanged to we can copy from the original.

    for byte_idx in range(bytes_to_read):
        byte = byte_start + byte_idx
        bits_raw = reverse_bits(byte_to_bits(data[byte]))  # Convert byte to bit data and reverse due to endian
        bits_new = ''
        for bit_idx, bit in enumerate(bits_raw):  # For each bit, check if we need to replace it. If we do, pop from the
            # prepared bit list. If not (i.e. we have either not reached or already passed the range we want to replace)
            # then simply use the original data
            if offset <= byte * 8 + bit_idx < offset + size:
                bits_new += str(value_reversed.pop(0))
            else:
                bits_new += bits_raw[bit_idx]
        data_new += bits_to_byte(reverse_bits(bits_new))  # Reverse bits in byte due to endian and append to new data
    data_new += data[byte_end + 1:]  # Finally, everything past the last byte in the range is unchanged
    return data_new


def find_next_null(data, start):
    # Return relative position of next null character
    cur = start
    while cur < len(data) and data[cur] != 0:
        cur += 1
    return cur
