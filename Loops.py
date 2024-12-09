'''
while condition:
   statement
'''
# a=1 
# while a<=5:
#     print(a)
#     a=a+1

a=1
while a<=5:
    psd=input("enter the password")
    if psd=="S@n123":
        print("home page")
        break
    else:
        print("retry")
    a=a+1
else:
    print("wait for 30 seconds")