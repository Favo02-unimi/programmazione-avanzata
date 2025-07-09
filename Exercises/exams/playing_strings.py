def reverse(s):
    if len(s) == 1: return s
    return reverse(s[1:]) + s[0]

def strip(s, chars):
    def _strip(s, res=""):
        if not s: return res
        if s[0] not in chars: res += s[0]
        return _strip(s[1:], res)
    return _strip(s)

def split(s, seps):
    def _split(s, open="", res=[]):
        if len(s) == 0:
            if open: return res + [open]
            return res
        if s[0] in seps:
            if open: res += [open]
            return _split(s[1:], "", res)
        return _split(s[1:], open + s[0], res)
    return _split(s)

def find(s, ch):
    def _find(s, index=0):
        if not s: return -1
        if s[0] == ch: return index
        return _find(s[1:], index+1)

    if find.last_find_call == (s, ch) and find.last_find_res != -1:
        res = _find(s[find.last_find_res+1:])
        if res != -1: res += find.last_find_res+1
    else:
        res = _find(s)
    find.last_find_call = (s, ch)
    find.last_find_res = res
    return res

find.last_find_call = None
find.last_find_res = None

if __name__ == "__main__":
    s0 = "The deadline is approximately midnight though it could vary."
    s1 = "She is a fascinating lady; she has an astonishing smile, an alluring voice and an entertaining sense of humor."
    s2 = "The topic is appealing nevertheless the speaker was too monotonous."
    s3 = "The topic ais appealing nevertheless the speaker was too monotonous."
    print(strip(s0, "aeiou"))
    print(reverse(s0))
    print(strip(reverse(s0), "aeiou"))
    print(split(s1, " ;,."))
    print(reverse(s2))
    print("tests on find:")
    print(find(s2, "a"))
    print(find(s2, "a"))
    print(find(s2, "a"))
    print(find(s3, "a"))
    print(find(s3, "t"))
    print(find(s3, "t"))
    print(find(s3, "t"))
    print(find(s3, "t"))
    print(find(s3, "t"))
    print(find(s3, "t"))
    print(find(s3, "t"))
