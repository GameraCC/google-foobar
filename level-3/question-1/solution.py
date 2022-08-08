def solution(l):
    divisable_counts = [0] * len(l)

    # Calculate the number of lucky doubles to the right of each number, and store the count
    # This solves for (y, z) where z % y == 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[j] % l[i] == 0:
                divisable_counts[i] += 1

    # Calculate the number of lucky triples to the right of each number, and if add the number
    # of lucky doubles to the lucky triple count because each lucky double is also a lucky
    # triple if (x, y, z) and y % x == 0 and z % y == 0
    lucky_triples = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[j] % l[i] == 0:
                lucky_triples += divisable_counts[j]

    return lucky_triples


def main():
    print(solution([1, 2, 3, 4, 5, 6]))


main()
