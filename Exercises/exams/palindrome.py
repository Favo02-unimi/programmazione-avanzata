def palin(string):
    def solve(s):

        if len(s) <= 1:
            return []
        if s[0] != s[-1]:
            pre = [s[-1]] + solve(s[:-1])
            post = [s[0]] + solve(s[1:])
            if len(pre) <= len(post):
                return pre
            return post

        return solve(s[1:-1])
    res = solve(string)
    return f"The word «{string}» needs {len(res)} insertions to become palindrome: {res}"

if __name__ == "__main__":
    print(palin("casa"))
    print(palin("otto"))
    print(palin("palindromo"))
    print(palin("posero"))
    print(palin("coccinella"))
