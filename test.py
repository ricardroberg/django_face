# import itertools
#
# (K, N) = map(int, input().strip().split(' '))
#
# # reading the K lines and appending lists to 'L'
# L = list()
# for i in range(K):
#     l = list(map(int, input().strip().split(' ')))
#     n = l[0]
#     L.append(l[1:])
#     assert len(L[i]) == n
# print('n = ', n)
# print('L = ', L)
# S_max = 0
# L_max = None
#
# # Looping through Cartesian product of list and getting max sum.
# for l in itertools.product(*L):
#     #print('l = ', l)
#     #input()
#     s = sum([x**2 for x in l]) % N
#
#     if s > S_max:
#         S_max = s
#         L_max = l
#
# print(S_max)

# RESULTADO É 29


def is_leap(year):
    leap = False

    if year%4==0:
        leap = True
        if year%100==0 and not year%400==0:
            leap = False

        return leap


year = 1992
print(is_leap(year))