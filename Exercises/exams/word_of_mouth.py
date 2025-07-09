def load_words():
    words = set()
    with open("word_of_mouth_words.txt") as f:
        for line in f:
            words.add(line.strip())
    return words

def chain(start, target):
    words = load_words()
    res = []

    # vengono usati sia un set che una lista anche se sono
    # popolati dalle stesse cose in modo da:
    # - avere check efficienti per evitare duplicati (set)
    # - ma ricordando l'ordine di visita (lista)
    def solve(cur, seen, path):
        if cur == target:
            res.append(path)
            return

        for i in range(len(cur)):
            for l in sorted("qwertyuiopasdfghjklzxcvbnm"):
                neww = cur[:i] + l + cur[i+1:]
                if neww not in seen and neww in words:
                    solve(neww, seen | {neww}, path + [neww])

    solve(start, {start}, [start])
    return "\n".join(map(str, res)) + "\n"

if __name__ == '__main__':
    print("### witness → fatness")
    print(chain("witness", "fatness"))
    print("### warning → earring")
    print(chain("warning", "earring"))
    print("### sailing → writing")
    print(chain("sailing", "writing"))
