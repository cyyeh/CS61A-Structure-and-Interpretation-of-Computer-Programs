""" Optional problems for Lab 6 """

## Nonlocal practice
def vending_machine(snacks):
    """Cycles through sequence of snacks.

    >>> vender = vending_machine(('chips', 'chocolate', 'popcorn'))
    >>> vender()
    'chips'
    >>> vender()
    'chocolate'
    >>> vender()
    'popcorn'
    >>> vender()
    'chips'
    >>> other = vending_machine(('brownie',))
    >>> other()
    'brownie'
    >>> vender()
    'chocolate'
    """
    "*** YOUR CODE HERE ***"
    current_index = 0
    snacks_size = len(snacks)

    def cycle():
        nonlocal current_index

        current = snacks[current_index]
        if current_index < snacks_size - 1:
            current_index += 1
        else:
            current_index = 0

        return current

    return cycle