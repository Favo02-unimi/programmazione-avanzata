def ruzzles(grid):

    def solve(x, y, seen, word):
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            xx, yy = x+dx, y+dy
            if not (0 <= xx < COLS): continue
            if not (0 <= yy < ROWS): continue
            if (xx, yy) in seen: continue
            nword = word + grid[yy][xx]
            if len(nword) >= 3 and nword in words: res.add(nword)
            solve(xx, yy, seen | {(xx,yy)}, nword)

    res = set()
    for y in range(ROWS):
        for x in range(COLS):
            solve(x, y, set(), "")
    return sorted(list(res))

def load_words():
    with open('ruzzle_words.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

ROWS = 4
COLS = 4

if __name__ == '__main__':
    words = load_words()
    print(ruzzles(["walk", "moon", "hate", "rope"]))
    print(ruzzles(["abbr", "evia", "tion", "alba"]))
    print(ruzzles(["abse", "imtn", "nded", "ssen"]))
    print(ruzzles(["reca", "rwar", "aazp", "syon"]))
