from pyrsistent import v, pvector, pmap, m, s

# mutation of vectors
# No mutation of vectors once created, instead they
# are "evolved" leaving the original untouched
v1 = v(1, 2, 3)
v2 = v1.append(4)
v3 = v2.set(1, 5)
print(v1)
print(v2)
print(v3)

# Random access and slicing
print(v3[1])
print(v3[1:3])


# Iteration
a = list(x + 1 for x in v3)
print(a)
#[2, 6, 4, 5]
b = pvector(2 * x for x in range(3))
print(b)
# pvector([0, 2, 4])

# -------------------------------------------------------------


# No mutation of maps once created, instead they are
# "evolved" leaving the original untouched
m1 = m(a=1, b=2)
m2 = m1.set('c', 3)
m3 = m2.set('a', 5)
print(m1)
# pmap({'a': 1, 'b': 2})
print(m2)
# pmap({'a': 1, 'c': 3, 'b': 2})
print(m3)
# pmap({'a': 5, 'c': 3, 'b': 2})
print(m3['a'])
# 5

# Evolution of nested persistent structures
m4 = m(a=5, b=6, c=v(1, 2))
print(m4.transform(('c', 1), 17))
# pmap({'a': 5, 'c': pvector([1, 17]), 'b': 6})
m5 = m(a=1, b=2)

# Evolve by merging with other mappings
print(m5.update(m(a=2, c=3), {'a': 17, 'd': 35}))
# pmap({'a': 17, 'c': 3, 'b': 2, 'd': 35})
print(pmap({'x': 1, 'y': 2}) + pmap({'y': 3, 'z': 4}))
# pmap({'y': 3, 'x': 1, 'z': 4})

# Dict-like methods to convert to list and iterate
print(m3.items())
# pvector([('a', 5), ('c', 3), ('b', 2)])
print(list(m3))
# ['a', 'c', 'b']

# ----------------------------------------------------------

# No mutation of sets once created, you know the story...
s1 = s(1, 2, 3, 2)
s2 = s1.add(4)
s3 = s1.remove(1)
print(s1)
# pset([1, 2, 3])
print(s2)
# pset([1, 2, 3, 4])
print(s3)
# pset([2, 3])

# Full support for set operations
print(s1 | s(3, 4, 5))
# pset([1, 2, 3, 4, 5])
print(s1 & s(3, 4, 5))
# pset([3])
print(s1 < s2)
# True
print(s1 < s(3, 4, 5))
# False