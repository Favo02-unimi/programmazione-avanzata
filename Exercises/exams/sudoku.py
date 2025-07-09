def sudoku():

    def all(grid, i):
        if i >= len(grid):
            yield grid
            return
        for n in range(1, 5):
            if n in row(grid, i): continue
            if n in col(grid, i): continue
            if n in quad(grid, i): continue
            ngrid = grid.copy()
            ngrid[i] = n
            for sub in all(ngrid, i+1):
                yield sub

    def row(grid, i):
        return set(grid[i-(i % 4):i-(i % 4)+4])

    def col(grid, i):
        return {grid[ii] for ii in range(i%4, 16, 4)}

    def quad(grid, i):
        row = (i // 4) < 2
        col = (i % 4) < 2
        return {grid[ii] for ii in range(16) if (((ii // 4) < 2) == row) and (((ii % 4) < 2) == col)}

    return map(lambda g: [tuple(g[:4]), tuple(g[4:8]), tuple(g[8:12]), tuple(g[12:])], all([0]*16, 0))

if __name__ == "__main__":
    S = sudoku()
    for i in range(1,101):
        print("S[{:3}] :- {}".format(i,next(S)))
