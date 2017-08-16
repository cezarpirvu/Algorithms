# Solving the Hanoi Towers problem
# It takes 2^N - 1 moves in order to solve it

# solve problem
def solveHanoi(numDisks, fromPeg, toPeg, sparePeg):
    if numDisks == 1:
        print("Move disk %s from %s to %s" %(numDisks, fromPeg, toPeg))
    else:
        solveHanoi(numDisks - 1, fromPeg, sparePeg, toPeg)
        print("Move disk %s from %s to %s" % (numDisks, fromPeg, toPeg))
        #solveHanoi(1, fromPeg, toPeg, sparePeg)
        solveHanoi(numDisks - 1, sparePeg, toPeg, fromPeg)

solveHanoi(2, "A", "B", "C")