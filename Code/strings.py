#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text.
    n = len(text) m = len(pattern)
    Worst case time is O(n * m) if it has to do almost m checks n times
    example: text=aaaaaaaaaaaaaaa, pattern=aaaad

    space complexity is m + n, since it needs both in memory.
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    return find_index(text, pattern) is not None

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.

    Same complexity as contains.
    n = len(text) m = len(pattern)
    Worst case time is O(n * m) if it has to do almost m checks n times
    example: text=aaaaaaaaaaaaaaa, pattern=aaaad

    space complexity is m + n, since it needs both in memory.
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    if pattern == '':
        return 0

    result = find_all_indexes(text, pattern, first=True)
    if result == []:
        return None

    return result

def find_all_indexes(text, pattern, first=False):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    Best and worst case are O(n * m) because it goes to the end no matter what.

    Could consider improving by checking when theres less than m chars in the
    text to stop there.
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    if pattern is '':
        return list(range(len(text)))

    found_indicies = []
    for index, char in enumerate(text):
        if char == pattern[0]:
            for offset, p_char in enumerate(pattern):
                if index + offset >= len(text) or p_char != text[index + offset]:
                    break

            else:
                if first == True:
                    return index

                found_indicies.append(index)

    return found_indicies

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
