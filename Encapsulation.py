# # class emp:
# #     def fun1(self):
# #         print("hlo...")
# #     def _fun2(self):
# #         print("hii...")
# #     def _emp__fun3(self):
# #         print("welcome...")
# #     def fun4(self):
# #         self.__fun3()
# # e1=emp()
# # e1.fun1()
# # e1._emp__fun3()
# # e1.fun4()
# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius  # Private attribute

   
#     def radius(self):  # Getter for radius
#         return self.__radius

    
#     def radius(self, value):  # Setter for radius
#         if value < 0:
#             raise ValueError("Radius cannot be negative.")
#         self.__radius = value

    
#     def area(self):  # Read-only property (no setter)
#         return 3.14159 * (self.__radius ** 2)

# # Usage
# circle = Circle(5)
# print(circle.radius)
# circle.radius = 10 
# print(circle.radius)  
# print(circle.area)
