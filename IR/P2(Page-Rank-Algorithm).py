"""What is PageRank?

PageRank is an algorithm used by search engines to rank web pages in their search results.
It measures the importance of web pages based on the links between them.
"""



import numpy as np
from scipy.sparse import csc_matrix
from fractions import Fraction

def float_format(vector, decimal):
    return np.round(vector.astype(float), decimals=decimal)

G = np.matrix([[1, 1, 0],
                [1, 0, 1],
                [0, 1, 0]])

n = len(G)

M = csc_matrix(G, dtype=float)
rsums = np.array(M.sum(axis=1))[:, 0]
ri, ci = M.nonzero()
M.data /= rsums[ri]

dp = Fraction(1, n)
E = np.zeros((3, 3))
E[:] = dp

beta = 0.85
A = beta * M + ((1 - beta) * E)

r = np.matrix([dp, dp, dp]).T

previous_r = r
for it in range(1, 30):
    r = A * r
    if (previous_r == r).all():
        break
    previous_r = r

print("Final:\n", float_format(r, 3))
print("Sum:", np.sum(r))