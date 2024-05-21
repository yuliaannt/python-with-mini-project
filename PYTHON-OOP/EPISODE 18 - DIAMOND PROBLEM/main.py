# diamond problem


class A:
    def show(self):
        print("ini adalah kelas A")


class B(A):
    def show(self):
        print("ini adalah kelas B")


class C(A):
    def show(self):
        print("ini adalah kelas C")


class D(B, C):
    pass


objek = D()
objek.show()
help(objek)
