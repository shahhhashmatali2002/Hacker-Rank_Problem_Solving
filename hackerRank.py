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















