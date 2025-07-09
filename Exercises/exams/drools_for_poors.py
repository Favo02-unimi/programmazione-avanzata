from itertools import permutations

def combinations(a, b):
    if len(a) == 1:
        yield [(a[0], bb) for bb in b]
        return
    for i, bb in enumerate(b):
        for sub in combinations(a[1:], b[:i] + b[i+1:]):
            yield [(a[0], bb)] + sub

class Drools:
    def __init__(self, rules, names, pants, pos):
        self.rules = rules
        self.names = names
        self.pants = pants
        self.pos = pos

    def eval(self):
        def format(p):
            for i, (name, pants) in enumerate(p):
                print(f"Golfer {name} is in position {i+1} and wears some {pants} pants")

        for c in combinations(self.names, self.pants):
            for p in permutations(c):
                if self.check(p):
                    format(p)
                    return

    def check(self, p):
        for r in self.rules:
            if not r(p): return False
        return True

# rules validatet: receives a list of golfers in the format:
# (name, pants), the index is the position
rules = [
    # exactly one red pants
    lambda g: len([gg for gg in g if gg[1] == 'red']) == 1,
    # fred is not last to right
    lambda g: [gg[0] for gg in g].index('fred') < (len(g) -1),
    # fred right is wearing blue pants
    lambda g: g[[gg[0] for gg in g].index('fred') + 1][1] == 'blue',
    # joe second
    lambda g: g[1][0] == 'joe',
    # bob plaid pants
    lambda g: g[[gg[0] for gg in g].index('bob')][1] == 'plaid',
    # tom isnt position 1 or 4
    lambda g: [gg[0] for gg in g].index('tom') not in [0, 3],
    # tom not orange pants
    lambda g: g[[gg[0] for gg in g].index('tom')][1] != 'orange',
]

if __name__ == "__main__":
    d = Drools(rules,
        ['bob', 'joe', 'fred', 'tom'],
        ['red', 'orange', 'blue', 'plaid'],
        list(range(1,5)))
    d.eval()
