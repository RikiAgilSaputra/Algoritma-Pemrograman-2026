from math import gcd

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

# Fungsi untuk menyederhanakan pecahan
def sederhanakan_pecahan(pembilang, penyebut):
    faktor_persekutuan = gcd(abs(pembilang), abs(penyebut))
    pembilang_sederhana = pembilang // faktor_persekutuan
    penyebut_sederhana = penyebut // faktor_persekutuan
    return pembilang_sederhana, penyebut_sederhana


# Menyederhanakan hasil akhir
pembilang_sederhana, penyebut_sederhana = sederhanakan_pecahan(
    pembilang_hasil, penyebut_hasil
)

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

print(f"Hasil sederhana : {pembilang_sederhana}/{penyebut_sederhana}")

if pembilang_sederhana == pembilang_hasil and penyebut_sederhana == penyebut_hasil:
    print("hasil sudah dalam bentuk paling sederhana")

print("======================================")
print ("SEMOGA SUKSES")
print ("TERUS BERLATIH DAN JANGAN MENYERAH")
print ("SEMANGAT")