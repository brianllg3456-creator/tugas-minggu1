# ==================================================
# Tugas Mandiri Modul 1 - Program Percabangan
# Nama  : (DaryDarwisyRamdhani)
# NIM   : (714260025)
# Kelas : (isi kelas)
# ==================================================

print("======================================")
print("     PROGRAM KONVERSI NILAI")
print("======================================")

# Memasukkan identitas nilai
nama = input("Masukkan nama mahasiswa: ")
nilai = float(input("Masukkan nilai akhir (0-100): "))

# Memeriksa rentang nilai
if nilai < 0 or nilai > 100:
    print("Maaf, nilai harus berada antara 0 sampai 100!")

else:
    # Menentukan huruf mutu
    if nilai >= 80:
        huruf = "A"
        keterangan = "Lulus"
    elif nilai >= 70:
        huruf = "B"
        keterangan = "Lulus"
    elif nilai >= 60:
        huruf = "C"
        keterangan = "Lulus"
    elif nilai >= 50:
        huruf = "D"
        keterangan = "Tidak Lulus"
    else:
        huruf = "E"
        keterangan = "Tidak Lulus"


# Menampilkan hasil
    print("--------------------------------------")
    print("           HASIL PENILAIAN")
    print("--------------------------------------")
    print(f"Nama          : {nama}")
    print(f"Nilai Angka   : {nilai}")
    print(f"Huruf Mutu    : {huruf}")
    print(f"Keterangan    : {keterangan}")
    print("--------------------------------------")
    print("Terima kasih telah menggunakan program.")
    print("======================================")