print("======================================")
print("   PROGRAM PENJUMLAHAN PECAHAN")
print("======================================")

# Input pecahan pertama
pembilang1 = int(input("Masukkan pembilang pecahan pertama: "))
penyebut1 = int(input("Masukkan penyebut pecahan pertama: "))

# Input pecahan kedua
pembilang2 = int(input("Masukkan pembilang pecahan kedua: "))
penyebut2 = int(input("Masukkan penyebut pecahan kedua: "))

# Proses
pembilang_hasil = (pembilang1 * penyebut2) + (pembilang2 * penyebut1)
penyebut_hasil = penyebut1 * penyebut2

# Output
print("\n======================================")
print("HASIL PERHITUNGAN")
print("======================================")

print(f"Pecahan pertama : {pembilang1}/{penyebut1}")
print(f"Pecahan kedua   : {pembilang2}/{penyebut2}")

print(
    f"Hasil           : "
    f"{pembilang_hasil}/{penyebut_hasil}"
)

print("======================================")
print ("SEMOGA SUKSES")
print ("TERUS BERLATIH DAN JANGAN MENYERAH")
print ("SEMANGAT")