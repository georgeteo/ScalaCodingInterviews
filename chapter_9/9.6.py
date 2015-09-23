'''
CCC 9.6: Implement an algorithm to print all valid combinations of n-pairs
of parentheses.
'''

def paren_func(n):
    storage = []
    inner_paren_func("", storage, n, n)
    return storage


def inner_paren_func(base_string, storage, opens_left, closes_left):
    if opens_left == closes_left == 0:
        storage.append(base_string)
    if closes_left > opens_left:
        inner_paren_func(base_string + ")", storage, opens_left, closes_left-1)
    if opens_left > 0:
        inner_paren_func(base_string + "(", storage, opens_left-1, closes_left)


if __name__ == "__main__":
    print paren_func(5)
