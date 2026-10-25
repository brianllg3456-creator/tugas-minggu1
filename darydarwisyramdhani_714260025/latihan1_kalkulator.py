# =================================================
# Latuhan 1 - kakulator konsol serdehana 
# Pelatihan dasr pemrograman Morris IF 26
# ==================================================


print("=======================================")
print("         KAKULATOR KONSOL SEDERHANA")
print("Operasi tersedia: + - * /")
print("----------------------------------------")


# --- Bagian masukan pengguna ---
angka1 = float(input("masukan bilangan pertama :"))
angka2 = float(input("masukan bilangan kedua : "))
operator = input("masukan operator (+ - * /)")


print("-----------------------------")


# --- Bagian proses ---
if operator == "+":
    hasil = angka1 + angka2
    print(f"hasil: {angka1} + {angka2} = {hasil:.2f}")


elif operator == "-":
    hasil = angka1 + angka2
    print(f"hasil: {angka1} - {angka2} = {hasil:.2f}")

elif operator == "*":
    hasil = angka1 * angka2
    print(f"hasil: {angka1} x {angka2} = {hasil:.2f}")

elif operator == "/":
    if angka2 == 0:
        print("kesalahan: bilangan tidak dapat dibagi dengan nol.")
    else:
        hasil = angka1 / angka2
        print(f"hasil: {angka1} : {angka2} = {hasil:.2f}")


else:
    print(f"operator '{operator}' : tidak dikenali.")
    print("gunakan salah satu dari: + - * /")
     
print("====================================================")
print("terima kasih telah menggunkan kalkulator ini.")