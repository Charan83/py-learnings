#   mro
#       - when there is multiple inheritance to understand the method resolution order, we can use
#           - <class>.__mro__
#           - <class>.mro()
#           - help(<class>)

class A():
    def do_something(self):
        print("Method in : A")


class B(A):
    def do_something(self):
        print("Method in : B")


class C(A):
    def do_something(self):
        print("Method in : C")


class D(B, C):
    pass
    """ def do_something(self):
        print("Method in : D") """


todo = D()
todo.do_something()

""" print(D.__mro__)
print(D.mro())
help(D) """
