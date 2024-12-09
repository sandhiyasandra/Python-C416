# a={'one','five','two','one'}
# print(a)
# a.add("four")
# print(a)
# a.remove("four")
# print(a)
a={'blue','black','pink','red'}
b={'violet','blue','white','yellow'}
print(a&b)
print(a.intersection(b))
print(a|b)
print(a.union(b))
print(a-b)
print(a.difference(b))
print(a^b)
print(a.symmetric_difference(b))
c={14,23}
d={1,2,3}
print(c>=d)
print(c.issubset(d))
print(c.isdisjoint(d))
print(c==d)
e=d.copy()
print(e)
a=(1,2,3,4,1)
print(a)