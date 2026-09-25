# ==========================================
# PROGRAM TRANSAKSI PENGISIAN BBM DI SPBU
# ==========================================

# data login
nama_user = "mustafid"
nim_user = "31"

print("==========================================")
print("       PROGRAM TRANSAKSI BBM SPBU")
print("==========================================")

# 1. Validasi login
nama = input("Masukkan nama anda : ")
nim = input("Masukkan 2 digit terakhir nim : ")

if nama. lower() == nama_user. lower() and nim == nim_user:
    print ("Login Berhasil")

    # 2. Pilihan jenis BMM
    print("\n==========================================")
    print("             PILIHAN JENIS BBM")
    print("============================================")
    print("1. Pertalite       - Rp10.000/liter")
    print("2. Pertamax        - Rp12.500/liter")
    print("3. Pertamax Turbo  - Rp15.000/liter")
    print("============================================")

    pilihan = int(input("PIlih jenis BBM (1-3) : "))
    liter = float(input("Jumlah liter yg dibeli : "))

    # Menentukan Jenis BMM dan Harga
    if pilihan == 1:
        jenis_bbm = "Pertalite"
        harga_per_liter = 10000
    elif pilihan == 2:
        jenis_bbm = "Pertamax"
        harga_per_liter = 12500
    elif pilihan == 3:
        jenis_bbm = "Pertamax Turbo"
        harga_per_liter = 15000
    else:
        print ("Pilihan BBM tidak valid.")
        exit()

    # 3. Menghitung total harga  & Validasi Liter
    if liter <= 0:
            print("Jumlah liter tidak valid!")
            print("Silakan masukkan jumlah liter lebih dari 0.")
            exit()

    total_harga = harga_per_liter + liter

    # 4. Menetukan diskon berdasarkan jumlah liter
    if liter >= 10:
        persen_diskon = 10
    elif liter >= 5:
        persen_diskon = 5
    else:
        persen_diskon = 0

    diskon_pembelian = (persen_diskon / 100) * total_harga

    # 5. Status Member
    member = input("Apakah anda member? (ya/tidak) : ")

    if member. lower() == "ya":
        persen_diskon_member = 2
        diskon_member = (2/100) * total_harga
        print("Yey! Anda adalah member.")
        print("Anda mendapatkan diskon tambahan sebesar 2% !")
    elif member. lower () == "tidak":
        persen_diskon_member = 0
        diskon_member = 0
        print("Anda bukan member.")
        print("Anda tidak mendapatkan diskon tambahan.")
    else:
        print("Input tidak valid. Silakan masukkan 'ya' atau 'tidak'.")
        exit()

    # 6. Total bayar 
    total_diskon = diskon_pembelian + diskon_member
    total_bayar = total_harga - total_diskon

    # 7. OUTPUT 
    print("==========================================")
    print("             DETAIL TRANSAKSI")
    print("==========================================")
    print("| Data                  | Nilai")
    print("|-----------------------|----------------")
    print(f"| Nama                  | {nama}")
    print(f"| NIM                   | {nim}")
    print(f"| Jenis BBM             | {jenis_bbm}")
    print(f"| Harga/Liter           | Rp{harga_per_liter}")
    print(f"| Jumlah Liter          | {liter} liter")
    print(f"| Total Harga           | Rp{total_harga}")
    print(f"| Diskon Pembelian      | Rp{diskon_pembelian}")
    print(f"| Diskon Member (2%)    | Rp{diskon_member}")
    print(f"| Total Diskon          | Rp{total_diskon}")
    print(f"| TOTAL BAYAR           | Rp{total_bayar}")
    print("============================================")
    print("       Terima kasih telah bertransaksi!")
    print("============================================")

else:
    print("LOGIN GAGAL")
    print("Nama Anda atau 2 digit terakhir NIM salah.")
    print("Program dihentikan")