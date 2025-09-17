from string import ascii_lowercase

def chain(fr, to):


    def hop(cur, seen):
        for i in range(len(cur)):
            news = [cur[:i] + let + cur[i+1:] for let in ascii_lowercase]
            news = [new for new in news if new not in seen and new in WORDS]
            if not news: continue
            breakpoint()
            yield [[cur] + sub for new in news for sub in rec(new, seen | {new})]
            # yield [[cur] + sub for sub in subs]

    def rec(cur, seen):
        return (cur == to and [[to]]) or hop(cur, seen)

    res = list(rec(fr, {fr}))
    sres = []
    for path in res:
        sres.append(str(path))
    return "\n".join(sres)

WORDS = set(map(str.strip, open("word_of_mouth_words.txt").readlines()))

if __name__ == '__main__':
  print("### witness → fatness")
  print(chain("witness", "fatness"))
  print("### warning → earring")
  print(chain("warning", "earring"))
  print("### sailing → writing")
  print(chain("sailing", "writing"))
