#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    sol = 0
    position = 0
    # TODO: Decode digits from binary (base 2)
    if base == 2:
        for i in digits[::-1]:
            if int(i) == 1:
                sol += 2**position
            position += 1
        return sol

    # TODO: Decode digits from hexadecimal (base 16)
    if base == 16:
        base_16 = string.digits + string.ascii_uppercase[:7]
        for i in digits[::-1]:
            if i == '0':
                pass
            else:
                if i in base_16:
                    sol += base_16.index(i)*(16**position)
            position += 1
            print(sol)
        # TODO: Decode digits from any base (2 up to 36)
    else:
        base_chars = string.digits + string.ascii_uppercase
        base_chars = base_chars[:base]
        for i in digits[::-1]:
            if i == '0':
                pass
            else:
                if i in base_chars:
                    sol += base_chars.index(i)*(len(base_chars)**position)
                print(sol)


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    if base == 2:
        binary = ''
        while number != 0:
            bit = number % 2
            print(bit)
            binary += str(bit)
            number = number//2
        return binary
    # TODO: Encode number in hexadecimal (base 16)
    if base == 16:
        base_16 = string.digits + string.ascii_uppercase[:7]
        hexa = ''
        while number != 0:
            bit = base_16[(number % 16)]
            print(bit, number)
            hexa += str(bit)
            number = number//16
        return hexa
    # TODO: Encode number in any base (2 up to 36)
    else:
        base_chars = string.digits + string.ascii_uppercase
        base_chars = base_chars[:base]
        sol = ''
        while number != 0:
            bit = base_chars[(number % base)]
            sol += str(bit)
            number = number//base
        return sol

# convert("101", 2, 16)


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    if base1 == 2 and base2 == 16:
        number = decode(digits, 2)
        encode(number, 16)
    if base1 == 16 and base2 == 2:
        number = decode(digits, 16)
        return encode(number, 2)
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    if base1 == 2 and base2 == 10:
        return decode(digits, 2)
    if base1 == 10 and base2 == 2:
        return encode(int(digits), 2)
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    if base1 == 10 and base2 == 16:
        return encode(int(number), 16)
    if base1 == 16 and base2 == 10:
        return decode(digits, 16)

    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...
    base10result = decode(digits, base1)
    finalresult = encode(base10result, base2)
    return finalresult


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
        print('{} in base {} is {} in base {}'.format(
            digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
    base10 = decode("101", 2)
    print(base10)
