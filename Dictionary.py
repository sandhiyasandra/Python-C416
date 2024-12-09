# a={'id':1,'name':"sandhiya"}
# print(a)
# print("My id is",a['id'])
# print("My name is",a['name'])
# a['course']="python"
# print(a)
# b={"area":"mylapore","qualification":"12th"}
# a.update(b)
# print(a)
# del a['area']
# print(a)
# a.popitem()
# print(a)
# a.pop('course')
# print(a)
# a.clear()
# print(a)
# print(a.keys())
# print(a.values())
# print(a.items())
#{0:0,1:1,2:4,3:9,4:16,5:25}
a={x:x*x for x in range(6)}
print(a)
a={
    'sesha':20,
    'abhi':21,
    'yuva':21,
    'jeni':17,
    'shiva':18
}
# b={name:age for name,age in a.items() if age>18}
# c=[name for name in b]
# print(c)
b=[]
for name,age in a.items():
    if age>18:
        b.append(name)
print(b)
f={'computer':40000,'phone':35000,'mouse':3000,'headphone':1500}
print(f.get('computer'))
# price=0
# for i in f.values():
#     price=price+i 
# print(price)
# print(price/len(f))
a="apple"
b={}
for i in a:
    print(i)
    b[i]=b.get(i,0)+1
    print(b)
ib="sandhiya"
print(ib)