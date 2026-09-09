#
# def pop(num):
#     if isEmpty(num):
#         return True
#     else:
#         print(num.pop())
#         return num
#
# def isEmpty(num):
#     if not num:
#         return True
#     else:
#         return False
#
# num = []
# num.append(1)
# print(num)
# num.append(2)
# print(num)
# num.append(3)
# print(num)
# num.append(4)
# print(num)
#
#
# pop(num)
# pop(num)


#------------------{ haker rank If-Else Python }------------------

# n = input()
#
# if (n % 2) != 0:
#     print("Weird")
# elif (n % 2) == 0:
#     if n >= 2 and n <= 5:
#         print("Not Weird")
#     elif n >= 6 and n <= 20:
#         print("Weird")
#     elif n > 20:
#         print("Not Weird")

#------------------{ haker rank Aithmatic Operator }------------------

# a = int(input())
# b = int(input())
#
# print(a + b)
# print(a - b)
# print(a * b)

#------------------{ haker rank Division Python }------------------

# a = int(input())
# b = int(input())
#
# print(a // b)
# print(a / b)

#------------------{ haker rank Loops }------------------

# n = int(input())
# list1 = []
#
# for i in range(0, n):
#     list1.append(i)
#
# for i in list1:
#     print(i**2)

#------------------{ haker rank leap year }------------------

# def is_leap(year):
#     if (year % 4) == 0:
#         if (year % 100) == 0:
#             if (year % 400) == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
# year = int(input())
# print(is_leap(year))

# -----------{ The included code stub will read an integer, n , from STDIN. Without using any string methods, try to print the following: }-------------

# n = int(input())
#
# for i in range(1, n + 1):
#     print(i, end='')

#------------------{ haker rank Comprehension list }------------------

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# output = []
# for i in range(x + 1):
#     for j in range(y + 1):
#         for k in range(z + 1):
#             if i + j + k == n:
#                 continue
#             else:
#                 output.append([i, j, k])
#
# print(output)


# -----------{ hacker rank Find the Runner Up Score }-----------

# n = int(input("Enter n: - "))
# arr = map(int, input("Enter arr: - ").split())
#
# arr = list(dict.fromkeys(arr))
# arr.sort()
# arr.reverse()
# print(arr[1])

# ------{ map function }--------

# def square(num):
#     return num ** 2
#
# l = ["hashmat", "ali"]
#
# squared = map(len, l)
#
# print(list(squared))


#--------{ Hackerrank Nested Lists }------------

# score_list = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     score_list.append([name, score])
# second_highest = sorted(set([score for name, score in score_list]))[1]
# print('\n'.join(sorted([name for name, score in score_list if score == second_highest])))


#==================================================================
#                        S T R I N G S
#==================================================================

#------------------{ hacker rank Alphabet Rangoli }------------------
# NOTE: the stub is print_rangoli(size) and it must PRINT, not return.

# def print_rangoli(size):
#     letters = [chr(ord('a') + i) for i in range(size)]
#     width = 4 * size - 3
#     for i in range(size - 1, -size, -1):
#         idx = abs(i)
#         row = letters[size - 1:idx:-1] + letters[idx:]
#         print('-'.join(row).center(width, '-'))
#
#
# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)

#------------------{ hacker rank Capitalize! }------------------
# NOTE: use .capitalize() per word, NOT .title() -> 12abc must stay 12abc.
# Split on ' ' (not .split()) so multiple spaces are preserved.

# def solve(s):
#     return ' '.join(word.capitalize() for word in s.split(' '))
#
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     s = input()
#     result = solve(s)
#     fptr.write(result + '\n')
#     fptr.close()

#------------------{ hacker rank The Minion Game }------------------
# A char at index i starts len(s) - i substrings. No substring generation
# needed -> O(n) instead of timing out on length 10**6.

# def minion_game(string):
#     vowels = 'AEIOU'
#     n = len(string)
#     kevin = stuart = 0
#     for i, ch in enumerate(string):
#         if ch in vowels:
#             kevin += n - i
#         else:
#             stuart += n - i
#     if kevin > stuart:
#         print('Kevin', kevin)
#     elif stuart > kevin:
#         print('Stuart', stuart)
#     else:
#         print('Draw')
#
#
# if __name__ == '__main__':
#     s = input()
#     minion_game(s)

#------------------{ hacker rank Merge the Tools! }------------------
# dict.fromkeys() dedups while keeping insertion order.

# def merge_the_tools(string, k):
#     for i in range(0, len(string), k):
#         chunk = string[i:i + k]
#         print(''.join(dict.fromkeys(chunk)))
#
#
# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)


#==================================================================
#                           S E T S
#==================================================================

#------------------{ hacker rank Symmetric Difference }------------------
# a ^ b computes symmetric difference; sorted() outputs in ascending order.

# _ = input()
# a = set(map(int, input().split()))
# _ = input()
# b = set(map(int, input().split()))
# print(*sorted(a ^ b), sep='\n')

#------------------{ hacker rank No Idea! }------------------
# Use set lookup O(1) for A and B. (x in A) gives +1, (x in B) gives -1.

# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# A = set(map(int, input().split()))
# B = set(map(int, input().split()))
#
# print(sum((x in A) - (x in B) for x in arr))

#------------------{ hacker rank Set .add() }------------------
# Add distinct country stamps to a set and print len(set).

# countries = set()
# for _ in range(int(input())):
#     countries.add(input())
# print(len(countries))

#------------------{ hacker rank Set .discard(), .remove() & .pop() }------------------
# Executes pop, remove, or discard commands on set, then outputs sum(set).

# n = int(input())
# s = set(map(int, input().split()))
# for _ in range(int(input())):
#     cmd = input().split()
#     if cmd[0] == 'pop':
#         s.pop()
#     elif cmd[0] == 'remove':
#         s.remove(int(cmd[1]))
#     elif cmd[0] == 'discard':
#         s.discard(int(cmd[1]))
# print(sum(s))

#------------------{ hacker rank Set .union() Operation }------------------

# n = int(input())
# english = set(input().split())
# m = int(input())
# french = set(input().split())
# print(len(english.union(french)))

#------------------{ hacker rank Set .intersection() Operation }------------------

# n = int(input())
# english = set(input().split())
# m = int(input())
# french = set(input().split())
# print(len(english.intersection(french)))

#------------------{ hacker rank Set .difference() Operation }------------------
# Order matters: english - french = English only.

# n = int(input())
# english = set(input().split())
# m = int(input())
# french = set(input().split())
# print(len(english.difference(french)))

#------------------{ hacker rank Set .symmetric_difference() Operation }------------------

# n = int(input())
# english = set(input().split())
# m = int(input())
# french = set(input().split())
# print(len(english.symmetric_difference(french)))

#------------------{ hacker rank Set Mutations }------------------
# getattr(A, op) dispatches the operation name string to the set method.

# n = int(input())
# A = set(map(int, input().split()))
# m = int(input())
#
# for _ in range(m):
#     op, _count = input().split()
#     other = set(map(int, input().split()))
#     getattr(A, op)(other)
#
# print(sum(A))

#------------------{ hacker rank The Captain's Room }------------------
# K * sum(set) - sum(list) == (K - 1) * captain

# K = int(input())
# rooms = list(map(int, input().split()))
# unique = set(rooms)
# print((K * sum(unique) - sum(rooms)) // (K - 1))
#
# --- alternative, more readable ---
# from collections import Counter
# K = int(input())
# counts = Counter(map(int, input().split()))
# print(next(room for room, c in counts.items() if c == 1))

#------------------{ hacker rank Check Subset }------------------

# for _ in range(int(input())):
#     input()
#     A = set(input().split())
#     input()
#     B = set(input().split())
#     print(A.issubset(B))

#------------------{ hacker rank Check Strict Superset }------------------
# Use > (strict). >= / issuperset() would wrongly return True on equal sets.

# A = set(input().split())
# n = int(input())
# print(all(A > set(input().split()) for _ in range(n)))


#==================================================================
#                          N U M P Y
#==================================================================

#------------------{ hacker rank Arrays }------------------
# Return reversed NumPy array with dtype float.

# import numpy
#
# def arrays(arr):
#     return numpy.array(arr[::-1], float)
#
# arr = input().strip().split(' ')
# result = arrays(arr)
# print(result)

#------------------{ hacker rank Shape and Reshape }------------------

# import numpy
#
# print(numpy.array(input().split(), int).reshape(3, 3))

#------------------{ hacker rank Transpose and Flatten }------------------
# flatten() runs on the ORIGINAL array, not on the transpose.

# import numpy
#
# n, m = map(int, input().split())
# arr = numpy.array([input().split() for _ in range(n)], int)
#
# print(numpy.transpose(arr))
# print(arr.flatten())

#------------------{ hacker rank Concatenate }------------------

# import numpy
#
# n, m, p = map(int, input().split())
# arr_1 = numpy.array([input().split() for _ in range(n)], int)
# arr_2 = numpy.array([input().split() for _ in range(m)], int)
#
# print(numpy.concatenate((arr_1, arr_2), axis=0))

#------------------{ hacker rank Zeros and Ones }------------------
# dtype=int (plain int) -- numpy.int was removed in NumPy 1.24.

# import numpy
#
# shape = tuple(map(int, input().split()))
#
# print(numpy.zeros(shape, dtype=int))
# print(numpy.ones(shape, dtype=int))

#------------------{ hacker rank Eye and Identity }------------------
# legacy='1.13' is required for the "[ 1.  0.  0.]" padded spacing.
# eye() (not identity()) because the array can be non-square.

# import numpy
# numpy.set_printoptions(legacy='1.13')
#
# n, m = map(int, input().split())
# print(numpy.eye(n, m))

#------------------{ hacker rank Array Mathematics }------------------
# Keep dtype int -- expected output shows [[0 0 0 0]] for the division.

# import numpy
#
# n, m = map(int, input().split())
# a = numpy.array([input().split() for _ in range(n)], int)
# b = numpy.array([input().split() for _ in range(n)], int)
#
# print(a + b)
# print(a - b)
# print(a * b)
# print(a // b)
# print(a % b)
# print(a ** b)

#------------------{ hacker rank Floor, Ceil and Rint }------------------

# import numpy
# numpy.set_printoptions(legacy='1.13')
#
# A = numpy.array(input().split(), float)
#
# print(numpy.floor(A))
# print(numpy.ceil(A))
# print(numpy.rint(A))

#------------------{ hacker rank Sum and Prod }------------------

# import numpy
#
# n, m = map(int, input().split())
# arr = numpy.array([input().split() for _ in range(n)], int)
#
# print(numpy.prod(numpy.sum(arr, axis=0)))

#------------------{ hacker rank Min and Max }------------------

# import numpy
#
# n, m = map(int, input().split())
# arr = numpy.array([input().split() for _ in range(n)], int)
#
# print(numpy.max(numpy.min(arr, axis=1)))

#------------------{ hacker rank Mean, Var, and Std }------------------
# GOTCHA: their expected files mix NumPy formats.
#   - arrays  -> modern format, so NO set_printoptions legacy line
#   - the std -> old format = 11 DECIMAL PLACES with trailing zeros stripped
#     ({:.12g} looks right for 1.11803398875 but gives 0.829156197589
#      where the grader wants 0.82915619759)

# import numpy
#
# n, m = map(int, input().split())
# arr = numpy.array([input().split() for _ in range(n)], float)
#
# print(numpy.mean(arr, axis=1))
# print(numpy.var(arr, axis=0))
#
# s = '{:.11f}'.format(float(numpy.std(arr))).rstrip('0')
# print(s + '0' if s.endswith('.') else s)

#------------------{ hacker rank Dot and Cross }------------------

# import numpy
#
# n = int(input())
# A = numpy.array([input().split() for _ in range(n)], int)
# B = numpy.array([input().split() for _ in range(n)], int)
#
# print(numpy.dot(A, B))

#------------------{ hacker rank Inner and Outer }------------------

# import numpy
#
# A = numpy.array(input().split(), int)
# B = numpy.array(input().split(), int)
#
# print(numpy.inner(A, B))
# print(numpy.outer(A, B))

#------------------{ hacker rank Polynomials }------------------

# import numpy
#
# coeffs = list(map(float, input().split()))
# x = float(input())
#
# print(numpy.polyval(coeffs, x))

#------------------{ hacker rank Linear Algebra }------------------
# + 0.0 normalizes a -0.0 determinant so it prints as 0.0

# import numpy
#
# n = int(input())
# matrix = numpy.array([input().split() for _ in range(n)], float)
#
# print(round(float(numpy.linalg.det(matrix)) + 0.0, 2))


#==================================================================
#                      C O L L E C T I O N S
#==================================================================

#------------------{ hacker rank collections.Counter() }------------------
# Track shoe inventory with Counter; decrement count when purchased.

# from collections import Counter
#
# num_shoes = int(input())
# inventory = Counter(map(int, input().split()))
# num_customers = int(input())
#
# total_earnings = 0
# for _ in range(num_customers):
#     size, price = map(int, input().split())
#     if inventory[size] > 0:
#         total_earnings += price
#         inventory[size] -= 1
#
# print(total_earnings)

#------------------{ hacker rank DefaultDict Tutorial }------------------
# Store 1-based indices of words in Group A; print indices or -1 for Group B.

# from collections import defaultdict
#
# n, m = map(int, input().split())
# d = defaultdict(list)
#
# for i in range(1, n + 1):
#     d[input().strip()].append(str(i))
#
# for _ in range(m):
#     word = input().strip()
#     print(' '.join(d[word]) if word in d else -1)

#------------------{ hacker rank Collections.namedtuple() }------------------
# Solved in 4 lines: unpack headers dynamically into namedtuple, then average MARKS.

# from collections import namedtuple
#
# n, Student = int(input()), namedtuple('Student', input().split())
# print(f"{sum(int(Student(*input().split()).MARKS) for _ in range(n)) / n:.2f}")

#------------------{ hacker rank Collections.OrderedDict() }------------------
# Use rsplit(' ', 1) to split multi-word item name from price; accumulate in OrderedDict.

# from collections import OrderedDict
#
# d = OrderedDict()
# for _ in range(int(input())):
#     item, price = input().rsplit(' ', 1)
#     d[item] = d.get(item, 0) + int(price)
#
# for item, net_price in d.items():
#     print(item, net_price)

#------------------{ hacker rank Word Order }------------------
# Count words in order of appearance using OrderedDict (or Counter).

# from collections import OrderedDict
#
# d = OrderedDict()
# for _ in range(int(input())):
#     w = input().strip()
#     d[w] = d.get(w, 0) + 1
#
# print(len(d))
# print(*d.values())

#------------------{ hacker rank Collections.deque() }------------------
# Dynamically dispatch operations (append, appendleft, pop, popleft) using getattr.

# from collections import deque
#
# d = deque()
# for _ in range(int(input())):
#     cmd = input().split()
#     getattr(d, cmd[0])(*[int(cmd[1])] if len(cmd) > 1 else [])
#
# print(*d)

#------------------{ hacker rank Piling Up! }------------------
# Greedily pick the larger end; must be <= the current top block.

# from collections import deque
#
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     blocks = deque(map(int, input().split()))
#     top = float('inf')
#     possible = True
#     while blocks:
#         if blocks[0] >= blocks[-1]:
#             pick = blocks.popleft()
#         else:
#             pick = blocks.pop()
#         if pick <= top:
#             top = pick
#         else:
#             possible = False
#             break
#     print("Yes" if possible else "No")

#------------------{ hacker rank Company Logo }------------------
# Sort by descending frequency (-count), then alphabetical order (char).

# from collections import Counter
#
# if __name__ == '__main__':
#     s = input()
#     counts = Counter(s)
#     sorted_chars = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
#     for char, count in sorted_chars[:3]:
#         print(char, count)


#==================================================================
#                      B U I L T - I N S
#==================================================================

#------------------{ hacker rank Zipped! }------------------
# zip(*scores) transposes subject rows into student columns to compute averages.

# n, x = map(int, input().split())
# scores = [map(float, input().split()) for _ in range(x)]
# for student in zip(*scores):
#     print(f"{sum(student) / x:.1f}")

#------------------{ hacker rank Athlete Sort }------------------
# Stable sort on k-th index; Python's list.sort() preserves input order on ties.

# if __name__ == '__main__':
#     n, m = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     k = int(input())
#     arr.sort(key=lambda row: row[k])
#     for row in arr:
#         print(*row)

#------------------{ hacker rank Any or All }------------------
# Solved in 3 lines: all numbers positive AND any number palindromic.

# _ = input()
# nums = input().split()
# print(all(int(x) > 0 for x in nums) and any(x == x[::-1] for x in nums))

#------------------{ hacker rank ginortS }------------------
# Custom sort tuple key: (category_priority, char)
# 0: lowercase, 1: uppercase, 2: odd digits, 3: even digits

# s = input()
# print(''.join(sorted(s, key=lambda c: (
#     0 if c.islower() else 
#     1 if c.isupper() else 
#     2 if int(c) % 2 != 0 else 
#     3, 
#     c
# ))))

#------------------{ hacker rank Input() (Python 2) }------------------
# In Python 2, input() is equivalent to eval(raw_input()).
# In Python 3: print(eval(input()) == k)

# x, k = map(int, raw_input().split())
# print input() == k

#------------------{ hacker rank Python Evaluation }------------------
# The input line already contains print(...), so eval(input()) executes it directly.

# eval(input())


#==================================================================
#                           M A T H
#==================================================================

#------------------{ hacker rank Polar Coordinates }------------------
# cmath.polar(z) returns (r, phi), where r is modulus (abs) and phi is phase.

# import cmath
#
# z = complex(input())
# print(abs(z))
# print(cmath.phase(z))

#------------------{ hacker rank Mod Divmod }------------------

# a = int(input())
# b = int(input())
#
# print(a // b)
# print(a % b)
# print(divmod(a, b))

#------------------{ hacker rank Power - Mod Power }------------------

# a = int(input())
# b = int(input())
# m = int(input())
#
# print(pow(a, b))
# print(pow(a, b, m))

#------------------{ hacker rank Integers Come In All Sizes }------------------

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# print(pow(a, b) + pow(c, d))

#------------------{ hacker rank Triangle Quest }------------------
# (10**i // 9) generates repunits (1, 11, 111, ...); multiply by i to get repdigits.
# No strings allowed per rules.

# for i in range(1, int(input())):
#     print((10**i // 9) * i)

#------------------{ hacker rank Triangle Quest 2 }------------------
# Square of repunits: 1^2=1, 11^2=121, 111^2=12321...
# Repunit i = (10**i // 9). No strings allowed per rules.

# for i in range(1, int(input()) + 1):
#     print((10**i // 9)**2)

#------------------{ hacker rank Find Angle MBC }------------------
# In right triangle ABC with midpoint M of hypotenuse, BM = MC, so angle MBC = angle ACB.
# angle ACB = atan2(AB, BC). Use chr(176) for degree symbol '°'.

# import math
#
# ab = int(input())
# bc = int(input())
# print(f"{round(math.degrees(math.atan2(ab, bc)))}{chr(176)}")


#==================================================================
#                     I T E R T O O L S
#==================================================================

#------------------{ hacker rank itertools.product() }------------------
# Computes cartesian product of lists A and B.

# from itertools import product
#
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# print(*product(A, B))

#------------------{ hacker rank itertools.permutations() }------------------
# Sort characters first (sorted(s)) to ensure permutations are emitted in lexicographical order.

# from itertools import permutations
#
# s, k = input().split()
# for p in permutations(sorted(s), int(k)):
#     print(''.join(p))

#------------------{ hacker rank itertools.combinations() }------------------
# Sort characters first (sorted(s)) to ensure combinations are emitted in lexicographical order.

# from itertools import combinations
#
# s, k = input().split()
# for i in range(1, int(k) + 1):
#     for c in combinations(sorted(s), i):
#         print(''.join(c))

#------------------{ hacker rank itertools.combinations_with_replacement() }------------------
# Generates combinations with replacement of exact size k on sorted(s).

# from itertools import combinations_with_replacement
#
# s, k = input().split()
# for c in combinations_with_replacement(sorted(s), int(k)):
#     print(''.join(c))

#------------------{ hacker rank Compress the String! }------------------
# itertools.groupby groups consecutive identical characters: (count, int(char)).

# from itertools import groupby
#
# print(*[(len(list(g)), int(k)) for k, g in groupby(input())])

#------------------{ hacker rank Iterables and Iterators }------------------
# Generate all combinations of k elements and find fraction containing 'a'.

# from itertools import combinations
#
# n = int(input())
# letters = input().split()
# k = int(input())
#
# combs = list(combinations(letters, k))
# print(f"{sum(1 for c in combs if 'a' in c) / len(combs):.4f}")

#------------------{ hacker rank Maximize It! }------------------
# itertools.product generates all combinations across K lists (max 7^7 combinations).
# Remember to slice [1:] to skip each line's length count element.

# from itertools import product
#
# k, m = map(int, input().split())
# lists = [list(map(int, input().split()))[1:] for _ in range(k)]
#
# print(max(sum(x**2 for x in combo) % m for combo in product(*lists)))


#==================================================================
#               R E G E X   A N D   P A R S I N G
#==================================================================

#------------------{ hacker rank Detect Floating Point Number }------------------
# Optional sign [+-]?, digits before dot [0-9]*, literal dot \., at least one digit after [0-9]+.

# import re
#
# pattern = re.compile(r'^[+-]?[0-9]*\.[0-9]+$')
# for _ in range(int(input())):
#     print(bool(pattern.match(input())))

#------------------{ hacker rank Re.split() }------------------
# Split on commas and dots using character class [,.]

# regex_pattern = r"[,.]"
# import re
# print("\n".join(re.split(regex_pattern, input())))

#------------------{ hacker rank Group(), Groups() & Groupdict() }------------------
# Find first alphanumeric character with consecutive repetition using ([a-zA-Z0-9])\1.
# Avoid \w because \w matches '_' (underscore), which is not alphanumeric.

# import re
#
# m = re.search(r'([a-zA-Z0-9])\1', input())
# print(m.group(1) if m else -1)

#------------------{ hacker rank Incorrect Regex }------------------
# GOTCHA: Python 3.11+ added possessive quantifiers (*+, ++, ?+) so re.compile('.*+')
# succeeds in modern Python, but HackerRank's test suite was written when '*+' was
# an invalid "multiple repeat". Check for (?<!\\)[*+?][*+] before compiling.

# import re
#
# for _ in range(int(input())):
#     s = input()
#     try:
#         if re.search(r'(?<!\\)[*+?][*+]', s):
#             print(False)
#         else:
#             re.compile(s)
#             print(True)
#     except re.error:
#         print(False)

#------------------{ hacker rank Re.findall() & Re.finditer() }------------------
# Lookbehind and lookahead ensure vowels are between consonants without consuming trailing consonant.

# import re
#
# s = input()
# pattern = r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])'
# matches = re.findall(pattern, s, re.IGNORECASE)
#
# if matches:
#     print(*matches, sep='\n')
# else:
#     print(-1)

#------------------{ hacker rank Re.start() & Re.end() }------------------
# Lookahead (?=(...)) captures overlapping matches; end index is m.end(1) - 1.

# import re
#
# s = input()
# k = input()
# pattern = re.compile(rf'(?=({re.escape(k)}))')
# matches = list(pattern.finditer(s))
#
# if matches:
#     for m in matches:
#         print((m.start(1), m.end(1) - 1))
# else:
#     print((-1, -1))

#------------------{ hacker rank Regex Substitution }------------------
# Lookaround (?<= ) and (?= ) ensures '&&' and '||' have spaces on both sides without consuming spaces.

# import re
#
# pattern = re.compile(r'(?<= )(&&|\|\|)(?= )')
# repl = lambda m: 'and' if m.group() == '&&' else 'or'
#
# for _ in range(int(input())):
#     print(pattern.sub(repl, input()))

#------------------{ hacker rank Validating Roman Numerals }------------------
# Breakdown:
# Thousands: M{0,3} (0-3000)
# Hundreds:  (C[MD]|D?C{0,3}) (0-900)
# Tens:      (X[CL]|L?X{0,3}) (0-90)
# Units:     (I[XV]|V?I{0,3}) (0-9)

# regex_pattern = r"^M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$"
# import re
# print(str(bool(re.match(regex_pattern, input()))))

#------------------{ hacker rank Validating and Parsing Email Addresses }------------------
# Parse name/email with email.utils.parseaddr, match regex, format with email.utils.formataddr.

# import email.utils
# import re
#
# pattern = re.compile(r'^[a-zA-Z][a-zA-Z0-9_.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$')
# for _ in range(int(input())):
#     name, addr = email.utils.parseaddr(input())
#     if pattern.match(addr):
#         print(email.utils.formataddr((name, addr)))

#------------------{ hacker rank HTML Parser - Part 1 }------------------
# Handle start, end, and empty tags separately, along with attributes.

# from html.parser import HTMLParser
#
# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print("Start :", tag)
#         for attr in attrs:
#             print(f"-> {attr[0]} > {attr[1]}")
#
#     def handle_endtag(self, tag):
#         print("End   :", tag)
#
#     def handle_startendtag(self, tag, attrs):
#         print("Empty :", tag)
#         for attr in attrs:
#             print(f"-> {attr[0]} > {attr[1]}")
#
# html = '\n'.join([input() for _ in range(int(input()))])
# parser = MyHTMLParser()
# parser.feed(html)

#------------------{ hacker rank HTML Parser - Part 2 }------------------
# Check for '\n' in comment data to distinguish Multi-line vs Single-line.
# Ignore data if data == '\n'.

# from html.parser import HTMLParser
#
# class MyHTMLParser(HTMLParser):
#     def handle_comment(self, data):
#         if '\n' in data:
#             print(">>> Multi-line Comment")
#         else:
#             print(">>> Single-line Comment")
#         print(data)
#
#     def handle_data(self, data):
#         if data != '\n':
#             print(">>> Data")
#             print(data)
#
# html = ""
# for i in range(int(input())):
#     html += input().rstrip() + '\n'
#
# parser = MyHTMLParser()
# parser.feed(html)
# parser.close()

#------------------{ hacker rank Detect HTML Tags, Attributes and Attribute Values }------------------
# handle_starttag and handle_startendtag print tag name followed by each '-> attr > val'.
# Comments are ignored automatically by HTMLParser.

# from html.parser import HTMLParser
#
# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print(tag)
#         for attr, val in attrs:
#             print(f"-> {attr} > {val}")
#
#     def handle_startendtag(self, tag, attrs):
#         print(tag)
#         for attr, val in attrs:
#             print(f"-> {attr} > {val}")
#
# html = '\n'.join([input() for _ in range(int(input()))])
# parser = MyHTMLParser()
# parser.feed(html)
# parser.close()

#------------------{ hacker rank Validating UID }------------------
# Rules: 10 chars, alphanumeric, unique characters, >= 2 uppercase, >= 3 digits.

# def is_valid(uid):
#     return (
#         len(uid) == 10 and
#         uid.isalnum() and
#         len(set(uid)) == 10 and
#         sum(1 for c in uid if c.isupper()) >= 2 and
#         sum(1 for c in uid if c.isdigit()) >= 3
#     )
#
# for _ in range(int(input())):
#     print('Valid' if is_valid(input().strip()) else 'Invalid')

#------------------{ hacker rank Validating Credit Card Numbers }------------------
# GOTCHAS:
#   1. Format must strictly be either 16 continuous digits or 4 groups of 4 separated by '-'.
#      Never use (-?\d{4}){3} as it accidentally permits mixed hyphens like 4123-456745674567.
#   2. Remove hyphens BEFORE checking for 4 consecutive repeated digits (e.g. 5133-3367).

# import re
#
# pattern = re.compile(r'^[456](?:\d{15}|\d{3}-\d{4}-\d{4}-\d{4})$')
#
# def is_valid_card(card):
#     if not pattern.match(card):
#         return 'Invalid'
#     digits = card.replace('-', '')
#     if re.search(r'(\d)\1{3}', digits):
#         return 'Invalid'
#     return 'Valid'
#
# for _ in range(int(input())):
#     print(is_valid_card(input().strip()))

#------------------{ hacker rank Validating Postal Codes }------------------
# Lookahead (?=\d\1) finds overlapping alternating pairs without consuming intermediate digits.

# regex_integer_in_range = r"^[1-9][0-9]{5}$"
# regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"
#
# import re
# P = input()
# print(bool(re.match(regex_integer_in_range, P)) 
#       and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

#------------------{ hacker rank Matrix Script }------------------
# 1. Read column-by-column (matrix[r][c] for c in range(m) for r in range(n)).
# 2. Use lookbehind (?<=[a-zA-Z0-9]) and lookahead (?=[a-zA-Z0-9]) around [^a-zA-Z0-9]+.
#    Avoid \w because \w matches '_' (underscore), which is a symbol in this challenge!

# import re
#
# n, m = map(int, input().split())
# matrix = [input() for _ in range(n)]
#
# raw = ''.join(matrix[r][c] for c in range(m) for r in range(n))
# print(re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])', ' ', raw))

#------------------{ hacker rank Validating phone numbers }------------------
# A valid mobile number starts with 7, 8, or 9 and has exactly 10 digits.

# import re
#
# pattern = re.compile(r'^[789]\d{9}$')
# for _ in range(int(input())):
#     print('YES' if pattern.match(input().strip()) else 'NO')


#==================================================================
#        C L O S U R E S   A N D   D E C O R A T O R S
#==================================================================

#------------------{ hacker rank Standardize Mobile Number Using Decorators }------------------
# Standardize by slicing the last 10 digits: num[-10:-5] and num[-5:].

# def wrapper(f):
#     def fun(l):
#         f([f"+91 {num[-10:-5]} {num[-5:]}" for num in l])
#     return fun
#
# @wrapper
# def sort_phone(l):
#     print(*sorted(l), sep='\n')
#
# if __name__ == '__main__':
#     l = [input() for _ in range(int(input()))]
#     sort_phone(l)

#------------------{ hacker rank Decorators 2 - Name Directory }------------------
# Sort people by age numerically (int(person[2])), then apply format function f to each.

# def person_lister(f):
#     def inner(people):
#         return map(f, sorted(people, key=lambda x: int(x[2])))
#     return inner
#
# @person_lister
# def name_format(person):
#     return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
#
# if __name__ == '__main__':
#     people = [input().split() for _ in range(int(input()))]
#     print(*name_format(people), sep='\n')


#==================================================================
#                          C L A S S E S
#==================================================================

#------------------{ hacker rank Class 1 - Dealing with Complex Numbers }------------------
# Operator overloading for complex arithmetic: +, -, *, /, and modulus.

# import math
#
# class Complex(object):
#     def __init__(self, real, imaginary):
#         self.real = real
#         self.imaginary = imaginary
#
#     def __add__(self, no):
#         return Complex(self.real + no.real, self.imaginary + no.imaginary)
#
#     def __sub__(self, no):
#         return Complex(self.real - no.real, self.imaginary - no.imaginary)
#
#     def __mul__(self, no):
#         real = self.real * no.real - self.imaginary * no.imaginary
#         imag = self.real * no.imaginary + self.imaginary * no.real
#         return Complex(real, imag)
#
#     def __truediv__(self, no):
#         denom = no.real**2 + no.imaginary**2
#         real = (self.real * no.real + self.imaginary * no.imaginary) / denom
#         imag = (self.imaginary * no.real - self.real * no.imaginary) / denom
#         return Complex(real, imag)
#
#     def mod(self):
#         return Complex(math.hypot(self.real, self.imaginary), 0)

#------------------{ hacker rank Class 2 - Find the Torsional Angle }------------------
# Implements 3D vector subtraction, dot product, and cross product.

# import math
#
# class Points(object):
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __sub__(self, no):
#         return Points(self.x - no.x, self.y - no.y, self.z - no.z)
#
#     def dot(self, no):
#         return self.x * no.x + self.y * no.y + self.z * no.z
#
#     def cross(self, no):
#         return Points(
#             self.y * no.z - self.z * no.y,
#             self.z * no.x - self.x * no.z,
#             self.x * no.y - self.y * no.x
#         )
#         
#     def absolute(self):
#         return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
#
# if __name__ == '__main__':
#     points = list()
#     for i in range(4):
#         a = list(map(float, input().split()))
#         points.append(a)
#
#     a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
#     x = (b - a).cross(c - b)
#     y = (c - b).cross(d - c)
#     angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))
#     print("%.2f" % math.degrees(angle))


#==================================================================
#               P Y T H O N   F U N C T I O N A L S
#==================================================================

#------------------{ hacker rank Map and Lambda Function }------------------
# Generate first n Fibonacci numbers (0-indexed) and cube each via map.

# cube = lambda x: x ** 3
#
# def fibonacci(n):
#     fib = [0, 1]
#     for i in range(2, n):
#         fib.append(fib[i - 1] + fib[i - 2])
#     return fib[:n]

#------------------{ hacker rank Validating Email Addresses With a Filter }------------------
# username: [a-zA-Z0-9_-]+, website: [a-zA-Z0-9]+, extension: [a-zA-Z]{1,3}

# import re
#
# def fun(s):
#     pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
#     return bool(re.match(pattern, s))
#
# def filter_mail(emails):
#     return list(filter(fun, emails))
#
# if __name__ == '__main__':
#     n = int(input())
#     emails = [input() for _ in range(n)]
#     filtered_emails = filter_mail(emails)
#     filtered_emails.sort()
#     print(filtered_emails)

#------------------{ hacker rank Reduce Function }------------------
# Multiply rational numbers (Fractions) cumulatively using functools.reduce.

# from fractions import Fraction
# from functools import reduce
#
# def product(fracs):
#     t = reduce(lambda x, y: x * y, fracs)
#     return t.numerator, t.denominator
#
# if __name__ == '__main__':
#     fracs = []
#     for _ in range(int(input())):
#         fracs.append(Fraction(*map(int, input().split())))
#     result = product(fracs)
#     print(*result)


#==================================================================
#                        D E B U G G I N G
#==================================================================

#------------------{ hacker rank Words Score }------------------
# Bugfix: change `score = 1` (or `score = 0`) in the else block to `score += 1`.
# Note: 'y' is included as a vowel per the problem definition.

# def is_vowel(letter):
#     return letter in ['a', 'e', 'i', 'o', 'u', 'y']
#
# def score_words(words):
#     score = 0
#     for word in words:
#         num_vowels = sum(1 for letter in word if is_vowel(letter))
#         if num_vowels % 2 == 0:
#             score += 2
#         else:
#             score += 1
#     return score
#
# n = int(input())
# words = input().split()
# print(score_words(words))

#------------------{ hacker rank Default Arguments }------------------
# Bugfix: default argument stream=EvenStream() is instantiated only once (mutable default argument).
# Fix: use stream=None, and instantiate stream = EvenStream() inside function when stream is None.

# def print_from_stream(n, stream=None):
#     if stream is None:
#         stream = EvenStream()
#     for _ in range(n):
#         print(stream.get_next())


#==================================================================
#                 D A T E   A N D   T I M E
#==================================================================

#------------------{ hacker rank Calendar Module }------------------
# Note: calendar.weekday takes (year, month, day). Use .upper() for output.

# import calendar
#
# m, d, y = map(int, input().split())
# print(calendar.day_name[calendar.weekday(y, m, d)].upper())

#------------------{ hacker rank Time Delta }------------------
# Parse timestamp with %z (UTC offset) using datetime.strptime, then return abs difference in seconds.

# from datetime import datetime
#
# def time_delta(t1, t2):
#     fmt = '%a %d %b %Y %H:%M:%S %z'
#     dt1 = datetime.strptime(t1, fmt)
#     dt2 = datetime.strptime(t2, fmt)
#     return str(int(abs((dt1 - dt2).total_seconds())))


#==================================================================
#                             X M L
#==================================================================

#------------------{ hacker rank XML 1 - Find the Score }------------------
# node.iter() traverses node and all descendants; sum len(elem.attrib).

# import sys
# import xml.etree.ElementTree as etree
#
# def get_attr_number(node):
#     return sum(len(elem.attrib) for elem in node.iter())

#------------------{ hacker rank XML2 - Find the Maximum Depth }------------------
# Recursively increment level and update global maxdepth.

# maxdepth = 0
# def depth(elem, level):
#     global maxdepth
#     level += 1
#     if level > maxdepth:
#         maxdepth = level
#     for child in elem:
#         depth(child, level)


#==================================================================
#             E R R O R S   A N D   E X C E P T I O N S
#==================================================================

#------------------{ hacker rank Exceptions }------------------
# GOTCHA: In PyPy 3 / certain Python environments, ZeroDivisionError produces "division by zero"
# instead of "integer division or modulo by zero". Explicitly print the required string.

# for _ in range(int(input())):
#     try:
#         a, b = map(int, input().split())
#         print(a // b)
#     except ZeroDivisionError:
#         print("Error Code: integer division or modulo by zero")
#     except ValueError as e:
#         print("Error Code:", e)


