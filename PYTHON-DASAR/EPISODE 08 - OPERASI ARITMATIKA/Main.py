#operasi Aritmatika

a = 10
b = 3

#operasi penambahan
hasil = a + b
print(a,' + ',b,'=',hasil)

#operasi pngurangan
hasil = a * b
print(a,'x', b,'=',hasil)

#operasi pembagian
hasil = a/b
print(a,'/',b,'=',hasil)

#operasi eksponen (pangkat) **
hasil = a ** b
print(a,'pangkat',b, '=', hasil)

#operasi modulus (sisa bagi) %
hasil = a % b
print(a,'%',b, '=', hasil)

#operasi floor division // pembulatan dari pembagian
hasil = a // b
print(a,'//',b, '=', hasil)

#priorotas operasi, operational precedence

'''
  1. ()
  2. eksponen **
  3. perkalian dan teman-teman * / ** % //
  4. pertambahan dan pengurangan + -

'''

x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x 
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=', hasil)

#yang diprioritaskan
#() eksponen perkalian pertambahan

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)
#kurung akan mengambil kurung paling awal
hasil = (x + y) * z
print('(',x,'+',y,')','*',z,'=',hasil)