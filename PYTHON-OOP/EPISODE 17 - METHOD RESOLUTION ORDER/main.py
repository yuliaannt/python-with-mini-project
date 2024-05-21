# method resolution order (MRO) // multiple inheritance
# sesuai urutan C,B,A


class A:
    def show(self):
        print("ini adalah show A")


class B:
    def show(self):
        print("ini adalah show B")


class C(A, B):
    def show(self):
        print("ini adalah show C")


objek = C()
objek.show()
help(objek)
