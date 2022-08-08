def solution(src, dest):
    """
        Pre-determined mask calculated using recurssion to apply to chess board position
        From a given position, there is always going to be a specific number of lowest steps
        to get to the next position, so this mask holds those predetermined step requirements
        and is used to apply upon an individual position on a chess board, similar to holding
        a piece of transparent paper ontop of the knight's position to denote the minimum
        required moves to egress to a given spot
    """
    steps_required_from_start = [
        [6, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 6],
        [5, 4, 5, 4, 3, 4, 3, 4, 3, 4, 3, 4, 5, 4, 5],
        [4, 5, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 5, 4],
        [5, 4, 3, 4, 3, 2, 3, 2, 3, 2, 3, 4, 3, 4, 5],
        [4, 3, 4, 3, 2, 3, 2, 3, 2, 3, 2, 3, 4, 3, 4],
        [5, 4, 3, 2, 3, 4, 1, 2, 1, 4, 3, 2, 3, 4, 5],
        [4, 3, 4, 3, 2, 1, 2, 3, 2, 1, 2, 3, 4, 3, 4],
        [5, 4, 3, 2, 3, 2, 3, 0, 3, 2, 3, 2, 3, 4, 5],
        [4, 3, 4, 3, 2, 1, 2, 3, 2, 1, 2, 3, 4, 3, 4],
        [5, 4, 3, 2, 3, 4, 1, 2, 1, 4, 3, 2, 3, 4, 5],
        [4, 3, 4, 3, 2, 3, 2, 3, 2, 3, 2, 3, 4, 3, 4],
        [5, 4, 3, 4, 3, 2, 3, 2, 3, 2, 3, 4, 3, 4, 5],
        [4, 5, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 5, 4],
        [5, 4, 5, 4, 3, 4, 3, 4, 3, 4, 3, 4, 5, 4, 5],
        [6, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 6]
    ]

    # Derive the source x & y coordinates from a scalar value
    src_y = src / 8
    src_x = src - (src_y * 8)

    # Derive the destination x & y coordinates from a scalar value
    dest_y = dest / 8
    dest_x = dest - (dest_y * 8)

    # Shift the coordinate plane onto the correct mask position
    masked_x = 7 - src_x
    masked_y = 7 - src_y

    return steps_required_from_start[masked_x + dest_x][masked_y + dest_y]
