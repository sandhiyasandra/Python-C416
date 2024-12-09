a=[1,2,3,4,5,6,7,8,9]
print(a)
print(a[6])
print(a[1:6])
print(a[1:6:2])
b=[90,80]
print(a+b)
print(b*3)#repitition
c=[9,8,7,6,4]
for i in c:
    print(i)
a=[9,8,7,8]
a.append([12,90])
print(a)
b=[90,89]
a.extend(b)
print(a)
a.insert(1,90)
print(a)

a.remove(8)
print(a)
a=[1,2,3,4,5]
print(sum(a))
print(min(a))
print(max(a))
print(len(a))
b=(1,2,3,4)

print(b[0:2])
print(b*3)
a=(1,3,5)
b=list(a)
print(b)
c=tuple(b)
print(c)
#25-11-2024
# a=['red','yellow','orange','black','blue','pink']
# b=[i for i in a if 'e' in i]
# print(b)
# for i in a:
#     if 'e' in i:
#         b.append(i)
# print(b)
a=[9,7,9,19,11,23,28,21]
b=a[0]
for i in a:
    if i > b:
        b=i
print(b)
# print(len(a))
# for i in range(len(a)):
#     for j in range(i+1):
#         if a[j]>a[i]:
#             b=a[j]
# print(b)
