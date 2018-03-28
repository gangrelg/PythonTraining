a = 2 + 2
print ("{}{}".format("Hi, your value is ", a))

array = [2, 4 ,6]
print(array)

array.append(8)
print(array)

for x in array:
    print(x)

def myFunction(name, age):
    return "{}{}{}".format("Your name and age are ",name,age)

print(myFunction("Galo ", 24))

class MyClass:
    def anotherFunc(self):
        print("Yes, Im some other method")

myclass = MyClass()
myclass.anotherFunc()