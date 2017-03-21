"""
Makes use of the fact that for one column of height n, there's n paths from the top left hand node to the bottom right
hand node. When adding another column to the left of the first one, for each additional node, the number of paths
depends on where the node sits in the grid. Using a 4x4 as an example:
       5 ___
        |   |
       4|___|
        |   |
       3|___|
        |   |
       2|___|
        |   |
       1|___|

        (5+4+3+2+1) = 15 ___   5 ___
                        |   |   |   |
          (4+3+2+1) = 10|___|  4|___|
                        |   |   |   |
            (3+2+1) =  6|___|  3|___|
                        |   |   |   |
              (2+1) =  3|___|  2|___|
                        |   |   |   |
                 1  =  1|___|  1|___|

       (15+10+6+3+1) = 35 ___ 15 ___   5 ___
                         |   |  |   |   |   |
          (10+6+3+1) = 20|___|10|___|  4|___|
                         |   |  |   |   |   |
             (6+3+1) = 10|___| 6|___|  3|___|
                         |   |  |   |   |   |
               (3+1) =  4|___| 3|___|  2|___|
                         |   |  |   |   |   |
                  1  =  1|___| 1|___|  1|___|

      (35+20+10+4+1) = 70 ___ 35 ___ 15 ___   5 ___
                         |   |  |   |  |   |   |   |
         (20+10+4+1) = 35|___|20|___|10|___|  4|___|
                         |   |  |   |  |   |   |   |
            (10+4+1) = 15|___|10|___| 6|___|  3|___|
                         |   |  |   |  |   |   |   |
               (4+1)  = 5|___| 4|___| 3|___|  2|___|
                         |   |  |   |  |   |   |   |
                   1  = 1|___| 1|___| 1|___|  1|___|


The above illustrates that there are 70 paths from the top left hand node to the bottom right hand node for n == 4.

"""
import math

n = 4

prev_col = list(range(1, n+2))

for i in range(1,n):
    next_col = []
    for j, x in enumerate(prev_col):
        next_col.append(sum(prev_col[:j+1]))
    prev_col = next_col

print(next_col[-1])




