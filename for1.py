# for i in range(6):
#     print(i)
# a="python"
# for j in a:
#     print(j)

# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25

# *
# **
# ***
# ****
# *****
# for row in range(6):
#     for col in range(row+1):
#         print("* ",end="")
#     print()

'''
row=1  row<6 row=row+1---outerloop

1<6---Trues--outer loop

   col=1 col<row+1 col=col+1
    1<1+1---1<2---T
   col=col+1---1+1=2
   col=2
   2<2---F---innerloop false
outer loop 

row=1
row=row+1==1+1=2
row=2
2<6---T
   col=1 col<row+1 col=col+1
   1<2+1==1<3---T
   col=col+1==1+1=2
   col=2
   2<3---T
   col=3
   3<3---F---innerloop false
row=2
row=row+1
row=2+1
row=3
  col=1 col<row+1 col=col+1
  1<3+1==1<4---T
  col=2
  2<4---T
  col=3
  3<4---T
  col=4
  4<4--F innerloop false
'''
# for i in range(1,6):
#     for j in range(1,6):
#         print(i*j,end=" ")
#     print()

# * * * * *
# * * * *
# * * *
# * *
# *
row=5
# for i in range(5,0,-1):
#   for j in range(i):
#     print("* ",end=" ")
#   print()

# * * * * * 
#   * * * *
#     * * *
#       * *
#         *
row=5
for i in range(row,0,-1):
  print(i)
  for j in range(row-i):
    print(" ",end='')
  for j in range(i):
    print("*",end='')
  print()
