# Data Login 
username_Admin = "Mustafid"
password_Admin = "031"

# 1 Validasi Login
percobaan = 0
login_berhasil = False

while percobaan < 3:
    print("=== Login Admin ===")
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    if username.lower() == username_Admin.lower() and password == password_Admin:
        print("Login Berhasil!")
        login_berhasil = True
        break
    else:
        percobaan += 1
        print("Login Gagal")
        print("Username atau Password salah. Silakan coba lagi.")
        print(f"Sisa percobaan: {3 - percobaan}")

if login_berhasil == False:
    print("Anda telah mencapai batas percobaan login. Akses ditolak.")
    print("Program dihentikan")
    exit()

# 2 Input Data Siswa
data_siswa = []

while True:
    print("\n=== Input Data Siswa ===")

    nama = input("Masukkan Nama Siswa: ")
    kelas = input("Masukkan Kelas: ")

    ikut_ujian = input("Apakah siswa ikut ujian? (ya/tidak): ")

    # Jika siswa tidak ikut ujian 
    if ikut_ujian.lower() == "tidak":
        nilai = 0

        data = {
            "Nama": nama,
            "Kelas": kelas,
            "Ikut Ujian": "tidak",
            "Nilai": nilai
        }
        data_siswa.append(data)

        print("siswa tidak ikut ujian")
        print("Nilai otomatis 0")

    # Jika siswa ikut ujian
    elif ikut_ujian.lower() == "ya":

        while True:
            benar = int(input("Jumlah soal benar: "))
            salah = int(input("Jumlah soal salah: "))

            if benar + salah == 20:
                break
            else:
                print("Jumlah soal benar dan salah harus berjumlah 20")
                print("SIlahkan masukkan kembali")

        # Menghitung nilai
        nilai = benar * 5

        data = {
            "Nama": nama,
            "Kelas": kelas,
            "Ikut Ujian": "ya",
            "Nilai": nilai
        }

        data_siswa.append(data)

        print("Data siswa berhasil ditambahkan")
        print("Nilai siswa: ", nilai)

    else:
        print("Input tidak valid!")
        print("Masukkan hanya 'ya' atau 'tidak' ")
        continue

    # 3 lanjut input data siswa
    lanjut = input("Apakah ingin menambahkan data siswa lagi? (ya/tidak): ")
    if lanjut.lower() != "ya":
        break

# 4 Menentukan nilai siswa
for siswa in data_siswa:

    nilai = siswa["Nilai"]

    if nilai >= 80:
        siswa["kategori"] = "Sangat Baik"
    elif nilai >= 60:
        siswa["kategori"] = "Baik"
    elif nilai >= 40:
        siswa["kategori"] = "Cukup"
    else:
        siswa["kategori"] = "Perlu Belajar Lagi"

# 5 daftar kelas
daftar_kelas = []
for siswa in data_siswa:
    if siswa["Kelas"] not in daftar_kelas:
        daftar_kelas.append(siswa["Kelas"])

# output data siswa
print("==================================")
print("         HASIL NILAI SISWA")
print("==================================")

for kelas in daftar_kelas:

    print("-----------------------------------")
    print("KELAS : ", kelas)
    print("-----------------------------------")

    for siswa in data_siswa:

        if siswa["Kelas"] == kelas:

            print("-----------------------------------")
            print("Nama Siswa      :  ", siswa["Nama"])
            print("Kelas           :  ", siswa["Kelas"])
            print("Ikut Ujian      :  ", siswa["Ikut Ujian"])
            print("Nilai           :  ", siswa["Nilai"])
            print("Kategori        :  ", siswa["kategori"])

print("====================================")
print("          PROGRAM SELESAI")
print("====================================")