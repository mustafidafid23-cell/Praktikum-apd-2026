# Data berat bagasi 
bagasi_1 = 12
bagasi_2 = 18
bagasi_3 = 7
bagasi_4 = 15
bagasi_5 = 20
bagasi_6 = 10

bagasi = [bagasi_1, bagasi_2, bagasi_3, bagasi_4, bagasi_5, bagasi_6]

# total berat bagasi 
total_berat = bagasi_1 + bagasi_2 + bagasi_3 + bagasi_4 + bagasi_5 + bagasi_6

# kompensasi 5%
kompensasi = total_berat * 0.05

# hitung total berat akhir
total_berat_akhir = total_berat + kompensasi

# total bayar ????????
total_bayar = total_berat_akhir

# htunng rata rata
rata_rata = total_bayar / len(bagasi)

# variabel nim
nim = 31 
bolean = nim < rata_rata

# Menampilkan semua nilai
print("Bagasi:", bagasi)
print("Bagasi posisi tengah:", bagasi [2:5])
print("Total berat:", total_berat, "kg")
print("Kompensasi 5%:", kompensasi, "kg")
print("Total biaya berat akhir:", total_berat_akhir, "kg")
print("Rata-rata:", rata_rata, "kg")
print("NIM:", nim)
print("Bolean:", bolean)
print("Total berat dalam gram:", total_berat_akhir * 1000, "gram")