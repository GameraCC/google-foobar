def solution(n):
    n = int(n)

    """
        Assuming the goal is to divide as much as possible, and
        the goal is to minimize the number of times an extra
        add or subtract operation is conducted

        The algorithm works as follows:
            - Check if the number is even
                - If not
                    - Add 1
                    - Subtract 1
                    - Check if splitting added or subtracted result is even
                    - Choose the even pathway
            - Else Divide by 2
            - Repeat
            
        3 is an edge case in which adding 1 is longer than removing 1
        to get to 1
    """

    steps = 0
    while (n != 1):
        if (n % 2 != 0):
            n_minus = n - 1
            n_plus = n + 1
            
            n_minus_split = n_minus / 2
            if n == 3:
                steps += 2
                n = 1
            elif (n_minus_split) % 2 == 0:
                n = n_minus / 4
                steps += 3
            else:
                n = n_plus / 4
                steps += 3
        else:
            n /= 2
            steps += 1
    
    return steps