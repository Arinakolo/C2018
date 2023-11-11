class MyClass:
    def init(self, attributemy):
        self.attributemy = attributemy

    def method1(self):
        print("This is method A from MyClass")

class TooMyClass:
    def init(self, attributetoomy):
        self.attributetoomy = attributetoomy

    def method2(self):
        print("This is method B from TooMyClass")

class MixedClass(MyClass, TooMyClass):
    def init(self, attributemy, attributetoomy, attributealsomy):
        MyClass.init(self, attributemy)
        TooMyClass.init(self, attributetoomy)
        self.attributealsomy = attributealsomy

    def method3(self):
        print("This is method 3 from MixedClass")