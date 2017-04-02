
def find(string, pattern):
    """return True if the item is found or False if item is not found"""
    # implement find_iterative and find_recursive below, then
    # change this to call your implementation to verify it passes all tests


    # return find_iterative(string, pattern)
    return find_recursive(string, pattern)

def find_iterative(string, pattern):
    string = string.lower()
    pattern = pattern.lower()
    pattern_count = 0
    for char in string:
        if char == pattern[pattern_count]:
            pattern_count += 1
        else:
            pattern_count = 0
        if pattern_count == len(pattern):
            return True
    return False

def find_recursive(string, pattern, index=0, pattern_count=0):
    if index == 0 and pattern_count == 0:
        string = string.lower()
        pattern = pattern.lower()

    if pattern_count == len(pattern):
        return True
    elif index >= len(string) or len(pattern) > len(string):
        print "Return False"
        return False
    elif string[index] == pattern[pattern_count]:
        index += 1
        pattern_count += 1
        return find_recursive(string, pattern, index, pattern_count)
    else:
        index += 1
        pattern_count = 0
        return find_recursive(string, pattern, index, pattern_count)
