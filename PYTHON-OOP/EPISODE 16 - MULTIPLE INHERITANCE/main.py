class A:

    def method_A(self):
        print("ini adalah method A")


class B:

    def method_b(self):
        print("ini adalah method b")


class C(A, B):
    pass


objek = C()

objek.method_A()
objek.method_B()
