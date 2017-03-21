def collatz_seq(n):
    sequence = []
    while n > 1:
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        sequence.append(n)
    return sequence

max_length = 0
n_for_max_length = 0
n = 1e6

while n > 1:
    if n % 1000 == 0:
        print(int(n))
    sequence = collatz_seq(n)
    sequence_length = len(sequence)
    if sequence_length > max_length:
        max_length = sequence_length
        n_for_max_length = n
    n -= 1

print(n_for_max_length, ", ", max_length)