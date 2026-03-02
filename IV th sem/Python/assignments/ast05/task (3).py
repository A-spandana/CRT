def collatz_sequence(n):
    sequence = [n]

    while n != 1:
        if n % 2 == 0:      # if n is even
            n = n // 2
        else:               # if n is odd
            n = 3 * n + 1
        sequence.append(n)

    return sequence


if __name__ == "__main__":
    n = int(input())
    print(collatz_sequence(n))