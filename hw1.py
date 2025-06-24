import numpy

numpy.random.seed(0)
throws = numpy.random.randint(1, 7, size=(1000, 2))
#empirical probability of double sixes
doubleSixes = numpy.sum((throws[:, 0] == 6) & (throws[:, 1] == 6))
empiricalProb = doubleSixes / len(throws)
print("empirical probability of double sixes with 1000 thrown: ", empiricalProb)

moreThrows = numpy.random.randint(1, 7, size=(10000, 2))
moreDoubleSixes = numpy.sum((moreThrows[:, 0] == 6) & (moreThrows[:, 1] == 6))
moreEmpiricalProb = moreDoubleSixes / len(moreThrows)
print("empirical probability of double sixes with 10000 throws: ", moreEmpiricalProb)

#for part 3c
def computeWinProbability():
    table = [[0.0 for _ in range(5)] for _ in range(5)]

    #base cases
    for j in range(4):
        table[4][j] = 1.0  #win
    for i in range(4):
        table[i][4] = 0.0  #loss

    #fill the table -> bottom up
    for i in reversed(range(4)):
        for j in reversed(range(4)):
            if i == j:
                table[i][j] = 0.5
            else:
                table[i][j] = 0.5 * table[i + 1][j] + 0.5 * table[i][j + 1]

    for i in range(4):
        for j in range(4):
            print(f"P(W | S=({i}, {j})) = {table[i][j]:.5f}")
    
    return table

computeWinProbability()
