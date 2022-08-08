"""
    The solution can be represented as a chain where each link
    represents a generation, for example:

    solution('4', '7') = 4

    M - 1 -> 2 -> 3     -> 7
    F - 1          -> 4
    
    For each generation in the chain, one of the following happen:
        - M += F
        - F += M

    It is also known that as a consequence of a single addition
    operation per generation in the chain, one of the following
    conditions will be true for the last M and F values in the
    chain:
        - M > F
        - F > M

    Given a final M and F value, the chain's operations can be
    reversed.

    First, variable "bigger" and "smaller" are assigned their
    respective values from inputs M and F

    Next, "smaller" is subtracted from "bigger" until the result
    is less than "smaller", representing a switch in the chain
    where
    
    M += F

    switches to

    F += M

    This process is repeated assigning
        - bigger = smaller
        - smaller = result (The next value in which the chain switches)

    The number of required steps can be represented as the number
    of iterations required to satisfy condition
        - bigger > 1 and smaller >= 1 (The value at which the chain begins)

    This process yields all required steps, but is too computationally
    intensive for problem necessitated constraints:
        - M || F >= 10^50

    The problem does not necessitate all steps be calculated, just the
    quantity of steps,

    As such we drop the iterations to retrieve each individual step by
    calculating modulo between "bigger" and "smaller", yielding "result"

    Instead of utilizing each iteration as a step in the chain, we use
    the sum of a base-rounded divison between "bigger" and
    "smaller" for each step, yielding the number of steps

"""

def solution(x, y):
    M = int(x)
    F = int(y)
    
    bigger = M if M > F else F
    smaller = M if M < F else F

    # Conditions where problem is impossible
    if (bigger < 1 or smaller < 1) or (bigger != 1 and smaller !=1 and bigger == smaller):
        return "impossible"

    steps = 0
    while (bigger > 1):
        result = bigger % smaller

        # Impossible case
        if bigger != 2 and smaller != 1 and result == 0:
            return "impossible"

        steps += bigger // smaller
        bigger = smaller
        smaller = result

    return str(steps - 1 if steps - 1 > -1 else 0)