import string


BASE_ENCODE = string.digits + string.ascii_lowercase
BASE_DECODE = {digit: val for val, digit in enumerate(BASE_ENCODE)}


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Implement decode - decode digits in any base to a number
    decoded = 0
    for pos, digit in enumerate(reversed(digits)):
        decoded += pow(base,pos) * BASE_DECODE[digit]

    return decoded



def encode(number, base):  # Bens godlike encode
    if number < base:
        return BASE_ENCODE[number]

    div, mod = divmod(number, base)

    return encode(div, base) + BASE_ENCODE[mod]


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    decoded = digits if base1 == 10 else decode(digits, base1)
    return encode(int(decoded), base2)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()



def old_encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    encoded = ''
    highest_power = 1
    multiple = base
    while multiple <= number:
        multiple *= base
        highest_power += 1

    for power in reversed(range(highest_power)):
        multiple = base ** power
        if multiple > number:
            encoded += '0'

        else:
            div, number = divmod(number, multiple)
            encoded += str(BASE_ENCODE[div])

    return encoded


