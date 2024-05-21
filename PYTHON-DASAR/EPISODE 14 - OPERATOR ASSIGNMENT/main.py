# operator yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment

a = 5  # adalah assignment
print("nilai a = ", a)

a += 1  # artinya adalah a = a+1
print(" Nilai a +=", a)

a -= 2  # artinya adalah a = a terakhir-2
print(" Nilai a -=", a)

a *= 5  # artinya adalah a = a terakhir*
print(" Nilai a *=", a)

a /= 2  # artinya adalah a = a terakhir/
print(" Nilai a \=", a)

# modulus dan floor division
b = 10
print(" \nNilai b =", b)
b %= 3
print(" Nilai b %= 3, nilai b menjadi = ", b)

b = 10
print(" \nNilai b =", b)
b //= 3
print(" Nilai b //=, nilai b menjadi = ", b)

# pangkat atau eksponen
a = 5
print(" \nNilai b =", a)
a **= 3
print(" Nilai b //=, nilai b menjadi = ", a)

# operatorbitwise
# OR
c = True
print("\n nilai c =", c)
c |= False
print("nilai c |= False, nilai c menjadi ", c)
c = False
print("\n nilai c =", c)
c |= False
print("nilai c |= False, nilai c menjadi ", c)

# AND
c = True
print("\n nilai c =", c)
c &= False
print("nilai c &= False, nilai c menjadi ", c)
c = True
print("\n nilai c =", c)
c &= True
print("nilai c &= True, nilai c menjadi ", c)

# XOR
c = True
print("\n nilai c =", c)
c ^= False
print("nilai c ^= False, nilai c menjadi ", c)
c = True
print("\n nilai c =", c)
c ^= True
print("nilai c ^= True, nilai c menjadi ", c)


# geser geser
d = 0b0100
print("\nnilai d = ", format(d, "04b"))
d >>= 2
print("\nnilai d >>= 2, nilai d menjadi", format(d, "04b"))
d <<= 1
print("\nnilai d <<= 2, nilai d menjadi", format(d, "04b"))
