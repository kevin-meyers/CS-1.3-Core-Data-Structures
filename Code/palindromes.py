#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)

    # make sure all letters are lowercase
    text = [char.lower() for char in text if char.isalpha()]

    # If its 0 or 1 it is automatically a palindrome
    if len(text) < 2:
        return True

    # Calculate the halway point up front to abstract similar code.
    halfway = (len(text) - 1) // 2
    return is_palindrome_recursive(text, halfway)


def is_palindrome_iterative(text, halfway):
    index = 0
    while index <= halfway:
        if text[index] != text[-(index + 1)]:
            return False

        index += 1

    return True


def is_palindrome_recursive(text, halfway, index=0):
    if index > halfway:
        return True

    if text[index] != text[-(index + 1)]:
        return False

    return is_palindrome_recursive(text, halfway, index + 1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
