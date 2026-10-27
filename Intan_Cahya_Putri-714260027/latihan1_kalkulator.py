#=================================================================
#latihan 1-kalkulator konsol sderhana
#Pelatihan Dasar Pemrograman MORRIS IF 2026
#==================================================================

print("========================================")
print("   Kalkulator konsol Sederhana   ")
print("========================================")
print("operasi tersedia : + - * /")
print("----------------------------------------")

#---bagian masukan pengguna---
angka1 = float(input("Masukkan bilangan pertama: "))
angka2 = float(input("Masukkan bilangan kedua: "))
operator = input("Masukkan operator (+, -, *, /): ")

print("----------------------------------------")

#---bagian proses perhitungan---
if operator == "+":
    hasil = angka1 + angka2
    print(f"hasil : {angka1} + {angka2} = {hasil:2f}")

elif operator == "-":
    hasil = angka1 - angka2
    print(f"hasil : {angka1} - {angka2} = {hasil:2f}")

elif operator == "*":
    hasil = angka1 * angka2
    print(f"hasil : {angka1} * {angka2} = {hasil:2f}")

elif operator == "/":
    if angka2 == 0:
        print("Kesalahan bilangan tidak dapat dibagi dengan nol")
    else:
        hasil = angka1 / angka2
        print(f"hasil : {angka1} / {angka2} = {hasil:2f}")

else:
    print(f"operator '{operator}' tidak dikenali.")
    print("Gunakan salah satu dari : + - * /")

print("=========================================")
print("Terima kasih telah menggunakan kalkulator ini")
#=================================================================
#latihan 1-kalkulator konsol sderhana
#Pelatihan Dasar Pemrograman MORRIS IF 2026
#==================================================================

print("========================================")
print("   Kalkulator konsol Sederhana   ")
print("========================================")
print("operasi tersedia : + - * /")
print("----------------------------------------")

#---bagian masukan pengguna---
angka1 = float(input("Masukkan bilangan pertama: "))
angka2 = float(input("Masukkan bilangan kedua: "))
operator = input("Masukkan operator (+, -, *, /): ")

print("----------------------------------------")

#---bagian proses perhitungan---
if operator == "+":
    hasil = angka1 + angka2
    print(f"hasil : {angka1} + {angka2} = {hasil:2f}")

elif operator == "-":
    hasil = angka1 - angka2
    print(f"hasil : {angka1} - {angka2} = {hasil:2f}")

elif operator == "*":
    hasil = angka1 * angka2
    print(f"hasil : {angka1} * {angka2} = {hasil:2f}")

elif operator == "/":
    if angka2 == 0:
        print("Kesalahan bilangan tidak dapat dibagi dengan nol")
    else:
        hasil = angka1 / angka2
        print(f"hasil : {angka1} / {angka2} = {hasil:2f}")

else:
    print(f"operator '{operator}' tidak dikenali.")
    print("Gunakan salah satu dari : + - * /")

print("=========================================")
print("Terima kasih telah menggunakan kalkulator ini")