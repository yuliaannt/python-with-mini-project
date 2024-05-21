'''
1. ubalah farenhait ke kelvin
2. ubalah kelvin ke farenheit
'''

print("\nPROGRAM KONVERSI TEMPERATURE")

#1. Farenheit ke Kelvin
farenheit = float(input('Masukkan derajat dalam farenheit : '))
print("Suhu farenheit : ", farenheit)
kelvin = (5/9)*(farenheit-32)+273
print("Suhu dalam kelvin adalah ", kelvin)

#2. Kelvin ke Farenheit
kelvin = (float(input('Masukkan derajat dalam kelvin : ')))
print("Suhu dalam kelvin : ", kelvin)
farenheit = (9/5)*(kelvin - 273)+32
print("Suhu dalam farenheit adalah ", farenheit)

