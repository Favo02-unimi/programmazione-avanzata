def eval(words, bound):
    left = right = 0
    for i, word in enumerate(words):
        w = 0
        for l in word:
            w *= 10
            w += bound[l]
        if i != len(words)-1:
            left += w
        else:
            right += w
    return left == right

def combinations(a, b, banned):

    if len(a) == 1:
        aa = a.pop()
        for bb in b:
            yield [(aa, bb)]
        return

    aa = a.pop()
    for bb in b:
        if (aa, bb) in banned: continue
        for c in combinations(a - {aa}, b - {bb}, banned):
            yield [(aa, bb)] + c

def bruteforce(words):
    print(" + ".join(words[:-1]), "==", words[-1])
    letters = set()
    for w in words:
        letters |= set(w)
    numbers = set(range(10))
    banned = {(w[0], 0) for w in words}
    for c in combinations(letters, numbers, banned):
        c = dict(c)
        if eval(words, c):
            # print(c)
            res = ["".join(str(c[d]) for d in word) for word in words]
            print(" + ".join(res[:-1]), "==", res[-1])

WORDS = ["HAWAII", "IDAHO", "IOWA", "OHIO", "STATES"]
bruteforce(WORDS)
