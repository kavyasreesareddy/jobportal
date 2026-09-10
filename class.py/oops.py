#inheritance multiple,single level
 
# class srinu:
#     surname = "sareddy"

#     def __init__(self, x, y):
#         print(x, y)

#     def colour(self):
#         c = "white"
#         print(c)

#     def iq(self):
#         iq = 170
#         print(iq)


# class vamsi(srinu):
#     def __init__(self, x, y):
#         super().__init__(x, y)
#         print(super().surname)
#         super().colour()
#         super().iq()


# obj = vamsi(10, 20)


# class vamsichild(vamsi):
#     def __init__(self, x, y):
#         super().__init__(x, y)


# obj2 = vamsichild(10, 20)

# multiple heritance


 

class hari:
    name = "hari"
    surname = "sareddy"

    def __init__(self):
        print("father init method")

    def iq(self):
        v = 200
        print(v)

    def properties(self):
        land = 1
        gold = 1
        silver = 1
        print(land, silver, gold)


class kavya(hari):
    def __init__(self):
        print(super().surname)
        super().properties()

    def abc(self):
        print("abc method")


obj1 = kavya()
obj1.abc()
print(obj1.surname)


class tharun(hari):
    def __init__(self):
        print(super().surname)
        super().properties()


obj2 = tharun()
print(obj2.surname)
obj2.properties()