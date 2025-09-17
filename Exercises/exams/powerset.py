def powerset(elems):
    # # per versione con pattern matching, if o eccezione
    # return rec(set(), set(elems), rec)
    return rec(set(), list(elems), rec)

# pattern matching al posto dell'if
# def rec(cur, rem, next):
#     match len(rem):
#         case 0:
#             return [cur]
#         case _:
#             e = rem.pop()
#             add = next(cur | {e}, rem - {e}, next)
#             skip = next(cur, rem - {e}, next)
#             return add + skip

def cases(cur, rem, next):
    return next(cur | {rem[0]}, rem[1:], next) + next(cur, rem[1:], next)

def rec(cur, rem, next):
    return (len(rem) == 0 and [cur]) or cases(cur, rem, next)

# # versione con if (è strutturale? è control flow?)
# def rec(cur, rem, next):
#     if len(rem) == 0:
#         return [cur]
#     e = rem.pop()
#     add = next(cur | {e}, rem - {e}, rec)
#     skip = next(cur, rem - {e}, rec)
#     return add + skip

# # con eccezione (non funzionale?)
# def rec(cur, rem, next):
#     try:
#         1 / len(rem)
#         e = rem.pop()
#         add = next(cur | {e}, rem - {e}, rec)
#         skip = next(cur, rem - {e}, rec)
#         return add + skip
#     except ZeroDivisionError:
#         return [cur]

print(powerset([1,2,3]))
