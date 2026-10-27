##==============================
#Tugas Mandiri Modul 1 - Program Percabangan
#Nama : Muhammad Fikry Auladi Insani
#Nim : 714260020
#Kelas : D4 Kelas B (12)
#==============================

#Program Percabangan

print("==================================")
print("Periksa Nilai Dan Kelulusan Anda")
print("==================================")

Nama = (input("Masukan Nama Anda :"))
Prodi = (input("Masukan Prodi Anda :"))
NPM = (input("Masukan NPM Anda :"))
Nilai = int(input("Masukan Nilai Anda : "))

if Nilai <= 60:
    print("Maaf, Anda dinyatakan Belum Lulus")
    print("Anda Mendapat Nilai (E)")
    if Nilai <= 0:
        print("Nilai Tidak Valid!")
elif Nilai >= 100:
    print("Nilai Tidak Valid!")
elif Nilai == 100:
    print("Selamat, Anda Dinyatakan Lulus")
    print("Anda Mendapat Nilai (A)")
elif Nilai >= 85:
    print("Selamat, Anda Dinyatakan Lulus")
    print("Anda Mendapat Nilai (B)")
elif Nilai >= 75:
    print("Selamat, Anda Dinyatakan Lulus")
    print("Anda Mendapat Nilai (C)")
elif Nilai >= 60:
    print("Maaf, Anda dinyatakan Belum Lulus")
    print("Anda Mendapat Nilai (D)")
else:
    print("Nilai tidak bisa bersifat Negative")
if Nilai < 0 or Nilai > 100:
    print("Nilai tidak boleh kurang dari 0 atau lebih dari 100.")
print("===================================================")
print("Terima Kasih Sudah Meluangkan Waktunya :)")
print("===================================================")