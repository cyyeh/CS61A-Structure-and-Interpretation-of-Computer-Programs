HW_SOURCE_FILE = 'hw04.py'

###############
#  Questions  #
###############

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    return abs(street(a) - street(b)) + abs(avenue(a) - avenue(b))

def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    import math
    return [ int(math.sqrt(element)) for element in s if element == math.pow(int(math.sqrt(element)), 2) ]
    

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    if n <= 3:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)
    

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    if n <= 3:
        return n
    else:
        n_1 = 3
        n_2 = 2
        n_3 = 1
        for i in range(4, n + 1):
            n_1, n_2, n_3 = n_1 + 2 * n_2 + 3 * n_3, n_1, n_2
        return n_1
    

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    def get_pingpong_at(index, current, direction):
        if index == n:
            return current
        else:
            if index % 7 == 0 or has_seven(index):
                if direction:
                    return get_pingpong_at(index + 1, current - 1, not direction)
                else:
                    return get_pingpong_at(index + 1, current + 1, not direction)
            else:
                if direction:
                    return get_pingpong_at(index + 1, current + 1, direction)
                else:
                    return get_pingpong_at(index + 1, current - 1, direction)

    return get_pingpong_at(1, 1, True)

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    basis_total = 0
    change = amount
    while change > 0:
        change //= 2
        basis_total += 1
    
    def count_k(n,k):
        def add(n, k, f):
            if k == 1:
                return f(n - 2 ** k)
            else:
                return f(n - 2 ** k) + add(n, k - 1, f)
            
        def fib(n):
            if n == 1:
                return 1
            elif n <= k:
                return add(n, n - 1, fib) + 1
            else:
                return add(n, k, fib)
            
        return fib(n)
    
    return count_k(amount, basis_total)

###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return lambda x: ((lambda f: f(f,x))(lambda f, x: 1 if x == 0 else mul(x, f(f, sub(x, 1)))))
