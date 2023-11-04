class Grandparent:
    height = 170
    satiety = 100
    def about(self):
        print("I'm Grandparent")

class Parent(Grandparent):
    def about_myself(self):
        print("I am Parent")

class Child(Parent):
    height = 95
    def __init__(self):
        super().about()
        super().about_myself()


ch = Child()


class Hello_world:
    hello = "Hello"
    _hello = "_Hello"
    __hello = "__Hello"

    def __init__(self):
        self.world = "world"
        self._world = "_world"
        self.__world = "__world"

    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)
class Hi(Hello_world):
    def hi_print(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)
hello = Hello_world()
hello.printer()


class BuildingError(Exception):
    def __str__(self):
        return f"With so much material the house can not be built!"

    def check_material(material, limit_material):
        if material > limit_material:
            return "enough material"
        else:
            raise BuildingError(material)
    material = 500
    print(check_material(material, limit_material=300))

    import sys
    print(sys.executable)
    print(sys.version)
    print(sys.platform)
    print(sys.modules)
    for name, module_path in sys.modeles.items():
        print(name, module_path)

for _ in dir(__builtins__):
    print(_)

print(dir(__builtins__))
print(help("tuple"))

class Counter:
    def __init__(self, start, stop):
        self.i = start
        self.j = stop
    def __iter__(self):
        self.i= self.start
        return self
    def __next__(self):
        self.i += 1
        if self.i > self.j - 1:
            raise StopIteration
        return self.i
count = Counter(start=5, stop=10)
for i in count:
    print(i)
print()
for i in range(5,10):
    print(i)

