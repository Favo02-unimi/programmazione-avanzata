import re
from operator import itemgetter
from collections import Counter

def freqs(filename, number):
  text = open(filename).read()
  tokens = map(str.lower, re.split(r"\W+", text))
  count = Counter(tokens)
  valid = filter(lambda k: k[1] > number, count.items())
  return sorted(valid, reverse=True, key=itemgetter(1))

# same thing more readable:
# def freqs(filename, number):
#   return sorted(filter(lambda k: k[1] > number, Counter(map(str.lower, re.split(r"\W+", open(filename).read()))).items()), reverse=True, key=itemgetter(1))
