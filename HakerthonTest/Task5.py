from collections import defaultdict


#
# d = defaultdict(list)
# d['python'].append("awesome")
# d['something-else'].append('not relevant')
# d['python'].append("language")
# for i in d.items():
#     print(i)

# Group A contains 'a', 'b', 'a'
# Group B contains 'a', 'c'
# For the first word in group B, 'a', it appears at positions 1 and 3 in group A.
# The second word, 'c', does not appear in group A, so print -1
# Sample Input
# 5 2, group A size n = 5, group B size m = 2
# a    group A contains 'a', 'a', 'b', 'a', 'b'
# a
# b
# a
# b
# a     group B contains 'a', 'b'
# Sample Output
# 1 2 4
# 3 5
# Explanation
# a' appeared 3 times in positions 1,2 and 4 .
# 'b' appeared 2 times in positions 3 and 5.
# In the sample problem, if 'c' also appeared in word group B , you would print -1.

def first_method():
    n, m = map(int, input("Enter n and m :").split())
    a = defaultdict(list)
    for i in range(1, n + 1):
        a[input("Type Your n(A) Input: ")].append(i)

    for i in range(1, m + 1):
        key = input("Type Your m(B) Input: ")
        if len(a[key]) > 0:
            print(" ".join(str(c) for c in a[key]))
        else:
            print(-1)
        print(key)


first_method()


def second_method():
    d = defaultdict(list)
    n, m = map(int, input("N and M :").split())

    for i in range(1, n + 1):
        d[input("N[A] :")].append(str(i))
    for j in range(m):
        print(' '.join(d[input("M[B] :")]) or -1)


second_method()
