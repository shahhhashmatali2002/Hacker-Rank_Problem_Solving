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

#------------------{ hacker rank Arrays (shape / reshape) }------------------

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
