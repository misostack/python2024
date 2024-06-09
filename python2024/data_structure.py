#!/usr/bin/env python

"""
1. Tuple
- A kind of data structure
- Ordered, Immutable, Allow Duplicate Values
- Start and end with parentheses: (1, "a", (2, "b"), 3, "c")
2. List
- A kind of data structure
- Ordered, Mutable, Allow Duplicate Values
- Start and end with square brackets: [1, "a", [2, "b], 3, "c"]
3. Set
- A kind of data structure
- Unordered, no duplication
- Start and end with curly braces: {1, 2, "a", "b"}
"""

tp = (1, "a", (2, "b"), 3, "c")
tp_matrix = (("a", "b"), ("c", "d"), ("e", "f"))
print(tp_matrix[0][0].upper())

ls = [1, "a", [2, "b"], 3, "c"]
ls_matrix = [["a1", "a2", "a3"], ["b1", "b2", "b3"], ["c1", "c2", "c3"]]
ls_matrix[0][0] = ls_matrix[0][0].upper()
print(ls_matrix)

# concatenation

tp2 = tp + (4, "d")
print(tp2)

ls[3] = ls[2] + [22, "bb"]
print(ls)

# extend
ls.extend([[4, "d"], [44, "dd"]])
print(ls)

ls.append([5, "e"])
print(ls)

del (ls[0])
print(ls)

# alias and reference value, clone

ls1 = [3, 2, 1]
ls2 = ls1
ls3 = ls1[:]  # clone
ls1.sort()

print(ls1)
print(ls2)
print(ls3)

# help

# help(ls1)
l1 = [1, 2, ]
s1 = {1, 2, 1, 1, 1, "a", "a", "b"}
s2 = set("abcdefg")
l2 = list("abcdefg")
print(s1)
print(s2)
print(l2)
print(1 in s1)
print(3 in s2)

s3 = {1, 2, 5}
s4 = {2, 4, 6}
# intersection
s5 = s3 & s4
print(s5)
# union
s6 = s3 | s4
print(s6)
# difference
s7 = s3 - s4
print(s7)
# in a or b not both
s8 = s3 ^ s4
print(s8)
