#!python

# Hint: use string.ascii_letters (all letters in ASCII character set)
import string


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing"""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    string = ''.join(e for e in text if e.isalnum()).lower()
    length = len(string)
    for index in range(0, length):
        if string[index] != string[(length-1)-index]:
            return False
    return True
    pass


def is_palindrome_recursive(text, left=None, right=None):
    if text is None:
        return False
    if text == "":
        return True
    string = ''.join(e for e in text if e.isalnum()).lower()
    left = string[0]
    right = string[len(string)-1]
    if left != right:
        return False
    else:
        str = string[1:-1]
        return is_palindrome_recursive(str, left, right)
    return True


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            str_not = 'a' if is_pal else 'not a'
            print('{}: {} is {} palindrome'.format(result, repr(arg), str_not))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
