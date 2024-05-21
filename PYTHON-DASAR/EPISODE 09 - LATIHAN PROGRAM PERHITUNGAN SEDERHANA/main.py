#latihan konversi satuan temperature

#program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATURE")

celcius = float(input('Masukkan suhu dalam celcius : '))
print("suhu adalah ", celcius,"celcius")

#reamur
reamur = (4/5)* celcius
print("suhu dalam reamur adalah ",reamur, "Reamur")

#farenheit
farenheit = (9/5)*celcius + 32
print("suhu dalam farenheit adalah ", farenheit,"farenheit") 

#kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah ", kelvin ,"kelvin") 

