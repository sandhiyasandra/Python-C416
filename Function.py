# # without argument with return type
# # def demo():
# #     return "hello"
# # print(demo())
# # def add():
# #     a=int(input("enter A no"))
# #     b=20
# #     return a+b
# # print("the sum of 2 no is",add())
# # print("the add of 2 no is",add())
# # def add(a,b=20):
# #     return a+b
# # print(add(100))
# def info(name,age):
#     print("name",name)
#     print("age",age)
# info(age=21,name=
#      "abc")

# def fun1(a):
#     a=a+"2"
#     a=a*2
#     return a
# print(fun1("5"))
# def sample():
#     global a
#     a=90
#     print(a)
# sample()
# print(a+9)
# a=lambda x,y:x+y
# print(a(2,3))

from functools import reduce
a=[1,2,3,4,5]
even=reduce(lambda x,y:x+y,a)
max=reduce(lambda x,y:x if x<
y else y,a)
print(max)
# from math import sqrt
# print(sqrt(100))



