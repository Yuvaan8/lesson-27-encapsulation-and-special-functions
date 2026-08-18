class MyClass:
    __privatevar = 27
    def private_meth(self):
        print('im inside a class MyClass')
    def hello(self):
        print('Private variable value', MyClass.__privatevar)
foo = MyClass()
foo.hello()
foo.private_meth()