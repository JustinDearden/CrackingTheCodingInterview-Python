# Determine whether or not one string is a permutation of another.

from collections import Counter

def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = Counter()
    for c in str1:
        counter[c] += 1
        print(c)
    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True

if __name__ == "__main__":
  import sys
  print(check_permutation(sys.argv[-2], sys.argv[-1]))
