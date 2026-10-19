#==============================
#Tugas Mandiri Modul 1 - Program Percabangan
#Nama : Intan Cahya Putri
#Nim : 714260027
#Kelas : D4 Kelas B (12)
#==============================

#Program Percabangan



print("==================================")
print("MELIHAT NILAI MAHASISWA")
print("==================================")

Nama = (input("Masukan Nama Anda :"))
Prodi = (input("Masukan Prodi Anda :"))
NPM = (input("Masukan NPM Anda :"))
Nilai = int(input("Masukan Nilai Anda : "))

if Nilai < 0 or Nilai > 100:
    print("Nilai tidak boleh kurang dari 0 atau lebih dari 100.")
    if Nilai <= 65:
        print("Maaf, Anda dinyatakan Belum Lulus")
    print("Anda Mendapat Nilai (E)")
    if Nilai >= 100:
        print("Nilai Tidak Valid!")
elif Nilai <= 0:
    print("Nilai Tidak Valid!")
elif Nilai == 100:
    print("Selamat, Anda Dinyatakan Lulus")
    print("Anda Mendapat Nilai (A)")
elif Nilai >= 90:
    print("Selamat, Anda Dinyatakan Lulus")
    print("Anda Mendapat Nilai (B)")
elif Nilai >= 80:
    print("Selamat, Anda Dinyatakan Lulus")
    print("Anda Mendapat Nilai (C)")
elif Nilai >= 70:
    print("Maaf, Anda dinyatakan Belum Lulus")
    print("Anda Mendapat Nilai (D)")
elif Nilai >= 65:
    print("Maaf, Anda dinyatakan Belum Lulus")
    print("Anda Mendapat Nilai (E)")
else:
    print("Nilai tidak bisa bersifat Negative")

print("===================================================")
print("Terima Kasih telah menggunakan program ini")
print("===================================================")
