#operasi logika atau boolean

#not, or, and, xor

#NOT
print('===NOT===')
a = True
c = not a
print('data a = ',a)
print('------------------NOT')
print('data c = ',c)

#OR kaya ditambah
print('===OR===')
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b
print(a,'OR',b,' =',c)
a = True
b = False
c = a or b
print(a,' OR',b,'=',c)
a = True
b = True
c = a or b
print(a,' OR',b,' =',c)
#OR = Jika salah satu true maka hasilnya true

#AND kaya dikali
print('===AND===')
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,' =',c)
a = True
b = False
c = a and b
print(a,' AND',b,'=',c)
a = True
b = True
c = a and b
print(a,' AND',b,' =',c)
#AND = Jika salah satu true maka hasilnya false

#XOR 
print('===XOR===')
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,' =',c)
a = True
b = False
c = a ^ b
print(a,' XOR',b,'=',c)
a = True
b = True
c = a ^ b
print(a,' XOR',b,' =',c)
#XOR = Jika salah satu true, sisanya false