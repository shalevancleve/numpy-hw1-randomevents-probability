import numpy as np

np.random.seed(0)
# 1000 throws of two fair six dice
throws = np.random.randint(1, 7, size=(1000, 2))
# Calculate empirical probability of double sixes
doubleSixes = np.sum((throws[:, 0] == 6) & (throws[:, 1] == 6))
empiricalProb = doubleSixes / len(throws)
print("empirical probability of double sixes: ", empiricalProb)

moreThrows = np.random.randint(1, 7, size=(10000, 2))
moreDoubleSixes = np.sum((moreThrows[:, 0] == 6) & (moreThrows[:, 1] == 6))
moreEmpiricalProb = moreDoubleSixes / len(moreThrows)
print("empirical probability of double sixes with 10000 throws: ", moreEmpiricalProb)