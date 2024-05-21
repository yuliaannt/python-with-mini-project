#operasi komparasi

#setiap hasil dari operasi komparasi adalah boolean

# >,<,>=,<=,==,!=,is,is not

a = 4 #sama dengan 1 itu assigement kalau == itu perbandingan
b = 2
#DAPAT DIGUNAKAN PADA LITERAL, CONTOH A==4 A:MEMAKAN MEMORRY ADA NILAINYA ; 4 ITU LITERAL

#lebih besar dari >
print('===LEBIH DARI===')
hasil = a > 3
print(a,'>',3,'=',hasil) 
hasil = b > 3
print(b,'>',3,'=',hasil) 
hasil = b > 2
print(b,'>',2,'=',hasil) 

#lebih kecil dari <
print('===KURANG DARI===')
hasil = a < 3
print(a,'<',3,'=',hasil) 
hasil = b < 3
print(b,'<',3,'=',hasil) 
hasil = b < 2
print(b,'<',2,'=',hasil) 

#lebih lebih dari sama dengan
print('===LEBIH DARI SAMA DENGAN===')
hasil = a >= 3
print(a,'>=',3,'=',hasil) 
hasil = b >= 3
print(b,'>=',3,'=',hasil) 
hasil = b >= 2
print(b,'>=',2,'=',hasil) 

#lebih kurang dari sama dengan
print('===KURANG DARI SAMA DENGAN===')
hasil = a <= 3
print(a,'<=',3,'=',hasil) 
hasil = b <= 3
print(b,'<=',3,'=',hasil) 
hasil = b <= 2
print(b,'<=',2,'=',hasil) 

#sama dengan (==)
print('===SAMA DENGAN (==) ===')
hasil = a == 4
print(a,'==',4,'=',hasil) 
hasil = b == 4
print(b,'==',4,'=',hasil) 

#tidak sama dengan (==)
print('===TIDAK SAMA DENGAN (!=) ===')
hasil = a != 4
print(a,'!=',4,'=',hasil) 
hasil = b != 4
print(b,'!=',4,'=',hasil) 


# 'is' sebagai komparasi object identity
print('===OBJECT IDENTITIY IS ===')
x = 5 #ini adalah assigement membuat object
y = 5
print('nilai x =',x,', id = ', hex(id(x))) 
print('nilai y =',y,', id = ', hex(id(x))) 
hasil = x is 5
print('x is 5 = ',hasil)


x = 5 #ini adalah assigement membuat object
y = 6
print('nilai x =',x,', id = ', hex(id(x))) 
print('nilai y =',y,', id = ', hex(id(x))) 
hasil = x is not y
print('x is not y = ',hasil)