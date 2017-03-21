import math

n = 20

prev_col = list(range(1,n+2))

print(prev_col)
for i in range(1,n):
    next_col = []
    for j, x in enumerate(prev_col):
        next_col.append(sum(prev_col[:j+1]))
    prev_col = next_col

print(next_col[-1])

