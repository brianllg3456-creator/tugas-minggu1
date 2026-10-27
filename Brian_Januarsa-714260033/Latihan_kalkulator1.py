#====================================
#latihan 1 - Kalkulator konsol sederhana
#Pelatihan Dasar  Pemrograman  MORRIS IF 26
#====================================

print("===================================")
print("   KALKULATOR KONSOL SEDERHANA")
print("Operasi yang tersedia: +, -, *, /")
print("-----------------------------------")

# --- Bagian masukan pengguna ---
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
operator = input("Masukkan operator (+, -, *, /): ")

print("-----------------------------------")

#--- Bagian perhitungan ---
if operator == "+":
    hasil = angka1 + angka2
    print(f"Hasil: {angka1} + {angka2} = {hasil}")

elif operator == "-":
    hasil = angka1 - angka2
    print(f"Hasil: {angka1} - {angka2} = {hasil}")
elif operator == "*":
    hasil = angka1 * angka2
    print(f"Hasil: {angka1} * {angka2} = {hasil}")
elif operator == "/":
    if angka2 == 0:
        print("kesalahan: bilangan tidak dapat dibagi dengan nol.")
    else:
        hasil = angka1 / angka2
        print(f"Hasil: {angka1} / {angka2} = {hasil}")

else:
    print(f"Operator '{operator}' tidak dikenali.")
    print("gunakan salah satu dari: +, -, *, /")

    print("===================================")
    print("Terima kasih telah menggunakan kalkulator ini.")