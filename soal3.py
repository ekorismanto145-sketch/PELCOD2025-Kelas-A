#soal no.3
import math

print("=== PERJALANAN MOTOR ===")
print("1. Hitung bensin dari jarak")
print("2. Hitung jarak dari bensin")
pilihan = input("pilih menu (1/2):")

# data dasar
konsumsi = 2.7 # km per liter

if pilihan == "1":
    #Input Jarak
    Jarak_Tempuh = float(input("Masukan total jarak (km):"))
    NIM3 = int(input("Masukan 3 angka terakhir NIM:"))
    NIM1 = (int(input("Masukan 1 angka terakhir NIM:")))

    kapasitas_tangki = NIM1 if NIM1 != 0 else 5
    harga_bensin = int("1" + str(NIM3) + "0")

    #Hitung Bensin
    total_bensin = Jarak_Tempuh / konsumsi

    #Diskon Jika > 3 liter
    if total_bensin > 3:
        harga_bensin -= 500

    total_biaya = total_bensin * harga_bensin
    isi_tangki = math.floor(total_bensin/kapasitas_tangki)

    print("=== Hasil ===")
    print(f"Total Bensin Dibutuhkan : {total_bensin:.2f} liter")
    print(f"Harga Bensin / Liter    : Rp {harga_bensin:,}")
    print(f"Total Biaya Bensin      : Rp {total_biaya:,.0f}")
    print(f"Isi Tangki Penuh        : {isi_tangki} Kali")
elif pilihan == "2":
    # Input Bensin
    bensin = float(input("Masukan Total Bensin (Liter):"))
    Jarak = bensin * konsumsi
    print("=== Hasil ===")
    print(f"Dengan {bensin:.2f} Liter bensin, motor bisa menempuh {Jarak:.2f} km")

else:
    print("Pilihan tidak valid.")
