# GENSHIN DPS TRACKER
import os

# VARIABEL GLOBAL (dipakai oleh banyak fungsi)
clear_cmd = "cls" if os.name == "nt" else "clear"
garis_40 = "=" * 40
garis_45 = "=" * 45
garis_55 = "=" * 55
strip_30 = "-" * 30
strip_40 = "-" * 40
strip_45 = "-" * 45
strip_55 = "-" * 55
enter_kembali = "\nTekan Enter untuk kembali..."
enter_kembali_rapat = "Tekan Enter untuk kembali..."

# DATA
akun = {
    "admin" : {"password" : "admin123", "role" : "Admin"},
    "astra" : {"password" : "astra", "role" : "User"}
}

genshin_characters = {
    'Venti': 'Anemo', 'Jean': 'Anemo', 'Xiao': 'Anemo', 'Kaedehara Kazuha': 'Anemo', 'Wanderer': 'Anemo', 'Xianyun': 'Anemo', 'Chasca': 'Anemo', 'Lan Yan': 'Anemo', 'Sucrose': 'Anemo', 'Sayu': 'Anemo', 'Shikanoin Heizou': 'Anemo', 'Faruzan': 'Anemo', 'Lynette': 'Anemo', 'Yumemizuku': 'Anemo', 'Varka': 'Anemo', 'Prune': 'Anemo', 'Ifa': 'Anemo', 'Jahoda': 'Anemo',
    'Zhongli': 'Geo', 'Albedo': 'Geo', 'Arataki Itto': 'Geo', 'Navia': 'Geo', 'Chiori': 'Geo', 'Xilonen': 'Geo', 'Ningguang': 'Geo', 'Noelle': 'Geo', 'Gorou': 'Geo', 'Yun Jin': 'Geo', 'Kachina': 'Geo', 'Linnea': 'Geo', 'Illuga': 'Geo', 'Zibai': 'Geo',
    'Raiden Shogun': 'Electro', 'Yae Miko': 'Electro', 'Cyno': 'Electro', 'Keqing': 'Electro', 'Clorinde': 'Electro', 'Fischl': 'Electro', 'Beidou': 'Electro', 'Razor': 'Electro', 'Lisa': 'Electro', 'Kujou Sara': 'Electro', 'Kuki Shinobu': 'Electro', 'Dori': 'Electro', 'Sethos': 'Electro', 'Ororon': 'Electro', 'Iansan': 'Electro', 'Flins': 'Electro', 'Ineffa': 'Electro', 'Varesa': 'Electro',
    'Nahida': 'Dendro', 'Alhaitham': 'Dendro', 'Tighnari': 'Dendro', 'Baizhu': 'Dendro', 'Emilie': 'Dendro', 'Kinich': 'Dendro', 'Collei': 'Dendro', 'Yaoyao': 'Dendro', 'Kaveh': 'Dendro', 'Kirara': 'Dendro', 'lauma': 'Dendro', 'Never': 'Dendro', 
    'Furina': 'Hydro', 'Neuvillette': 'Hydro', 'Yelan': 'Hydro', 'Tartaglia': 'Hydro', 'Kamisato Ayato': 'Hydro', 'Nilou': 'Hydro', 'Sangonomiya Kokomi': 'Hydro', 'Mualani': 'Hydro', 'Mona': 'Hydro', 'Barbara': 'Hydro', 'Xingqiu': 'Hydro', 'Candace': 'Hydro', 'Sigewinne': 'Hydro','Dahlia': 'Hidro', 'Aino': 'Hidro', 'Columbina': 'Hydro',
    'Hu Tao': 'Pyro', 'Yoimiya': 'Pyro', 'Lyney': 'Pyro', 'Arlecchino': 'Pyro', 'Klee': 'Pyro', 'Diluc': 'Pyro', 'Dehya': 'Pyro', 'Mavuika': 'Pyro', 'Xiangling': 'Pyro', 'Bennett': 'Pyro', 'Thoma': 'Pyro', 'Yanfei': 'Pyro', 'Xinyan': 'Pyro', 'Amber': 'Pyro', 'Chevreuse': 'Pyro', 'Gaming': 'Pyro', 'Nicole': 'Pyro', 'Durin': 'Pyro',
    'Kamisato Ayaka': 'Cryo', 'Ganyu': 'Cryo', 'Shenhe': 'Cryo', 'Wriothesley': 'Cryo', 'Eula': 'Cryo', 'Qiqi': 'Cryo', 'Aloy': 'Cryo', 'Citlali': 'Cryo', 'Diona': 'Cryo', 'Rosaria': 'Cryo', 'Chongyun': 'Cryo', 'Kaeya': 'Cryo', 'Layla': 'Cryo', 'Mika': 'Cryo', 'Freminet': 'Cryo', 'Charlotte': 'Cryo', 'Lohen': 'Cryo', 'Escoffier': 'Cryo','Skirk': 'Cryo', 'Sandrone': 'Cryo',
    'Traveler': {'Anemo', 'Geo', 'Electro', 'Dendro', 'Hydro', 'Pyro', 'Cryo'},
}

preset = {
    1: {
        "nama": "Abyss Floor 12",
        "deskripsi": "Target level 100, energi penuh saat mulai, "
                     "pengujian langsung dimulai "
                     "energy drop every 2,5 million damage delt."
    },
    2: {
        "nama": "Stygian Onslaught - Fearless",
        "deskripsi": "Target level 105, tanpa energi sejak awal, "
                     "hitungan mundur 3 detik sebelum pengujian dimulai."
    },
    3: {
        "nama": "Stygian Onslaught - Dire",
        "deskripsi": "Target level 110, tanpa energi sejak awal, "
                     "hitungan mundur 3 detik sebelum pengujian dimulai."
    }
}

dummy = {
    1: {
        "nama": "Standard Enemy",
        "kategori": "Standard",
        "deskripsi": "they are general purpose passive targets dasigned for single target damage testing."
    },
    2: {
        "nama": "Boss Target",
        "kategori": "Boss",
        "deskripsi": "they are the best used to simmulate the endgame performance of freezee team against enemies that cannot be frozen."
    },
    3: {
        "nama": "Multi-target Group",
        "kategori": "Multi-target",
        "deskripsi": "multi terge dummnies are designed for AoE damage testing and display both DPS and DPT."
    }
}
kategori_dummy = {"Standard", "Boss", "Multi-target"}
team = [
    {
        "id": 1,
        "username": "astra",
        "nama_tim": "Flins Lunar",
        "karakter": [
            "Flins",
            "Ineffa",
            "Sucrose",
            "Columbina"
        ],
        "elemen": {
            "Flins": "Electro",
            "Ineffa": "Electro",
            "Sucrose": "Anemo",
            "Columbina": "Hydro"
        }
    }
]
build = [
    {
        "id": 1,
        "username": "astra",
        "nama_build": "Flins Hypercarry",
        "id_team": 1,
        "nama_tim": "Flins Lunar",
        "karakter_build": [
            {
                "karakter": "Flins",
                "elemen": "Electro",
                "senjata": "pjws",
                "artefak": "NotSu"
            },
            {
                "karakter": "Ineffa",
                "elemen": "Electro",
                "senjata": "Engulfing",
                "artefak": "Aubade"
            },
            {
                "karakter": "Sucrose",
                "elemen": "Anemo",
                "senjata": "ttds",
                "artefak": "Viri"
            },
            {
                "karakter": "Columbina",
                "elemen": "Hydro",
                "senjata": "Favonius Codex",
                "artefak": "Silken"
            }
        ]
    }
]
riwayat = []
id_tes_berikutnya = 1
elemen_karakter_valid = {"Anemo", "Geo", "Electro", "Dendro", "Hydro", "Pyro", "Cryo"}

# FUNGSI REKURSIF 
def format_ribuan(angka):
    # Base case
    if angka < 1000:
        return str(angka)
    # Recursive case
    return format_ribuan(angka // 1000) + "." + str(angka % 1000).zfill(3)

def cari_nama_rekursif(daftar_nama, nama, indeks=0):
    # Base case 1: sudah sampai akhir list
    if indeks >= len(daftar_nama):
        return None
    # Base case 2: ditemukan
    if daftar_nama[indeks].lower() == nama.lower():
        return daftar_nama[indeks]
    # Recursive case
    return cari_nama_rekursif(daftar_nama, nama, indeks + 1)

# FUNGSI DENGAN PARAMETER
def cari_karakter(nama):
    try:
        return cari_nama_rekursif(list(genshin_characters), nama)
    except RecursionError:
        # Cadangan jika daftar karakter terlalu panjang untuk rekursi
        return next((item for item in genshin_characters if item.lower() == nama.lower()), None)

def baca_id(teks, label):
    if not teks.isdigit():
        raise ValueError(f"{label} harus berupa angka.")
    return int(teks)

def pilih_id(data, prompt, label, pesan_tidak_ditemukan):
    id_target = baca_id(input(prompt).strip(), label)
    if id_target not in data:
        raise ValueError(pesan_tidak_ditemukan)
    return id_target

def pilih_dari_daftar(daftar, prompt, label, pesan_tidak_ditemukan):
    id_target = baca_id(input(prompt).strip(), label)
    data_dipilih = next((item for item in daftar if item["id"] == id_target), None)
    if data_dipilih is None:
        raise ValueError(pesan_tidak_ditemukan)
    return data_dipilih

def tentukan_elemen(nama_valid):
    elemen = genshin_characters[nama_valid]
    if not isinstance(elemen, set):
        return elemen
    print("Pilihan elemen Traveler:")
    for pilihan_elemen in sorted(elemen):
        print("-", pilihan_elemen)
    elemen_pilihan = input("Pilih elemen Traveler: ").strip()
    elemen_valid = cari_nama_rekursif(sorted(elemen), elemen_pilihan)
    if elemen_valid is None:
        raise ValueError("Elemen Traveler tidak valid.")
    return elemen_valid

def validasi_akun_baru(username_baru, password_baru):
    if username_baru == "" or password_baru.strip() == "":
        raise ValueError("Username dan password tidak boleh kosong.")
    if username_baru in akun:
        raise ValueError("Username sudah digunakan.")

def validasi_anggota_baru(daftar_baru):
    karakter_valid = []
    elemen_baru = {}
    for nama in daftar_baru:
        nama_valid = cari_karakter(nama)
        if nama_valid is None:
            raise ValueError("Karakter tidak ditemukan: " + nama)
        if nama_valid in karakter_valid:
            raise ValueError("Karakter duplikat: " + nama_valid)
        elemen_baru[nama_valid] = tentukan_elemen(nama_valid)
        karakter_valid.append(nama_valid)
    return karakter_valid, elemen_baru

def tim_dipakai(id_tim):
    return (
        any(data_build["id_team"] == id_tim for data_build in build)
        or any(data_tes["id_team"] == id_tim for data_tes in riwayat)
    )

def ambil_tim_saya(username_pemilik):
    return [data_tim for data_tim in team if data_tim["username"] == username_pemilik]

def ambil_build_saya(username_pemilik):
    return [data_build for data_build in build if data_build["username"] == username_pemilik]

def ambil_riwayat_saya(username_pemilik):
    return [data_tes for data_tes in riwayat if data_tes["username"] == username_pemilik]

def konfirmasi_ya(pertanyaan):
    return input(pertanyaan).strip().lower() == "ya"

def kumpulkan_anggota_tim():
    karakter_tim = []
    elemen_tim = {}

    while len(karakter_tim) < 4:
        print("\nAnggota saat ini:", karakter_tim)
        print("Ketik 'selesai' untuk menyimpan tim.")
        pilihan_karakter = input("Masukkan nama karakter: ").strip()
        if pilihan_karakter.lower() == "selesai":
            break

        try:
            nama_valid = cari_karakter(pilihan_karakter)
            if nama_valid is None:
                raise ValueError("Karakter tidak ditemukan.")
            if nama_valid in karakter_tim:
                raise ValueError("Karakter tersebut sudah ada di tim.")
            elemen = tentukan_elemen(nama_valid)
        except ValueError as e:
            print(e)
        else:
            elemen_tim[nama_valid] = elemen
            karakter_tim.append(nama_valid)
            print("Karakter berhasil ditambahkan.")

    return karakter_tim, elemen_tim

def kumpulkan_build_karakter(tim_dipilih):
    karakter_build = []
    print("\nMasukkan build setiap karakter dalam tim.")
    print("Isi senjata dan artefak untuk keempat karakter.\n")

    for nomor, nama_karakter in enumerate(tim_dipilih["karakter"], start=1):
        print(f"\nKarakter {nomor}: {nama_karakter}")
        elemen = tim_dipilih["elemen"][nama_karakter]
        senjata = input("Nama senjata: ").strip()
        artefak = input("Nama artefak: ").strip()

        try:
            if not senjata or not artefak:
                raise ValueError("Senjata dan artefak tidak boleh kosong.")
        except ValueError as e:
            print(e)
            return []
        else:
            karakter_build.append({
                "karakter": nama_karakter,
                "elemen": elemen,
                "senjata": senjata,
                "artefak": artefak
            })
    return karakter_build

# FUNGSI TANPA PARAMETER (mengembalikan nilai)
def minta_pilihan():
    return input("Pilih menu: ").strip()

def buat_id_tes():
    global id_tes_berikutnya
    id_sekarang = id_tes_berikutnya
    id_tes_berikutnya += 1
    return id_sekarang

def hitung_total_karakter():
    return len(genshin_characters)

# PROSEDUR (tanpa return) - TAMPILAN UMUM
def bersihkan_layar():
    os.system(clear_cmd)

def cetak_header(judul, garis):
    print(garis)
    print(judul)
    print(garis)

def jeda(pesan=enter_kembali):
    input(pesan)

def cetak_karakter_build(nomor, data_karakter, indent_judul="", indent_detail="", lebar_label=7):
    print(f"\n{indent_judul}Karakter {nomor}: {data_karakter['karakter']}")
    print(indent_detail + "Elemen".ljust(lebar_label) + " :", data_karakter["elemen"])
    print(indent_detail + "Senjata".ljust(lebar_label) + " :", data_karakter["senjata"])
    print(indent_detail + "Artefak".ljust(lebar_label) + " :", data_karakter["artefak"])

def cetak_ringkas_karakter(daftar_karakter):
    for nomor, data_karakter in enumerate(daftar_karakter, start=1):
        print(
            f'{nomor}. {data_karakter["karakter"]} | '
            f'Senjata: {data_karakter["senjata"]} | '
            f'Artefak: {data_karakter["artefak"]}'
        )

def tampilkan_pilihan_preset():
    print("\n" + garis_45)
    print("           PILIH PRESET TES")
    print(garis_45)
    for id_item, data_preset in preset.items():
        print(f'\nID Preset : {id_item}')
        print(f'Nama      : {data_preset["nama"]}')
        print(f'Deskripsi : {data_preset["deskripsi"]}')

def tampilkan_pilihan_dummy():
    print("\n" + garis_45)
    print("          PILIH TARGET DUMMY")
    print(garis_45)
    for id_item, data_dummy in dummy.items():
        print(f'\nID Dummy  : {id_item}')
        print(f'Nama      : {data_dummy["nama"]}')
        print(f'Kategori  : {data_dummy["kategori"]}')
        print(f'Deskripsi : {data_dummy["deskripsi"]}')

def daftar_id_nama(data):
    for id_item, data_item in data.items():
        print(id_item, "-", data_item["nama"])

# AUTENTIKASI
def registrasi():
    bersihkan_layar()
    cetak_header("          REGISTRASI AKUN", garis_40)

    username_baru = input("Buat username: ").strip()
    password_baru = input("Buat password: ").strip()
    try:
        validasi_akun_baru(username_baru, password_baru)
    except ValueError as e:
        print(e)
    else:
        akun[username_baru] = {"password": password_baru, "role": "User"}
        print("Registrasi berhasil!")
        print("Silakan login menggunakan akun baru.")
    finally:
        jeda()

def login():
    bersihkan_layar()
    cetak_header("             LOGIN", garis_40)
    username_input = input("Username: ").strip()
    password_input = input("Password: ").strip()

    try:
        if username_input not in akun or akun[username_input]["password"] != password_input:
            raise ValueError("\nUsername atau password salah.")
    except ValueError as e:
        print(e)
        jeda(enter_kembali_rapat)
        return None
    else:
        role_akun = akun[username_input]["role"]
        print("\nLogin berhasil!")
        print("Selamat datang,", username_input)
        print("Role:", role_akun)
        jeda("\nTekan Enter untuk masuk ke menu...")
        return username_input, role_akun

# ADMIN - KELOLA AKUN
def lihat_semua_akun():
    print("\n=== DAFTAR AKUN ===")
    for nama_akun, data_akun in akun.items():
        print("Username:", nama_akun)
        print("Role:", data_akun["role"])
        print(strip_30)
    jeda()

def tambah_akun():
    print("\n=== TAMBAH AKUN ===")
    username_baru = input("Username baru: ").strip()
    password_baru = input("Password baru: ")
    try:
        validasi_akun_baru(username_baru, password_baru)
    except ValueError as e:
        print(e)
    else:
        akun[username_baru] = {"password": password_baru, "role": "User"}
        print("Akun berhasil ditambahkan!")
    finally:
        jeda()

def ubah_password_akun():
    print("\n=== UBAH PASSWORD ===")
    username_target = input("Username yang ingin diubah: ").strip()
    try:
        if username_target not in akun:
            raise ValueError("Akun tidak ditemukan.")
        if username_target == "admin":
            raise ValueError("Password akun admin utama tidak dapat diubah dari menu ini.")
        password_baru = input("Masukkan password baru: ")
        if password_baru.strip() == "":
            raise ValueError("Password tidak boleh kosong.")
    except ValueError as e:
        print(e)
    else:
        akun[username_target]["password"] = password_baru
        print("Password berhasil diubah.")
    finally:
        jeda()

def hapus_akun():
    print("\n=== HAPUS AKUN ===")
    username_target = input("Username yang ingin dihapus: ").strip()
    try:
        if username_target not in akun:
            raise ValueError("Akun tidak ditemukan.")
        if username_target == "admin":
            raise ValueError("Akun admin utama tidak dapat dihapus.")
    except ValueError as e:
        print(e)
    else:
        if konfirmasi_ya("Yakin ingin menghapus akun ini? (ya/tidak): "):
            del akun[username_target]
            print("Akun berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")
    finally:
        jeda()

def kelola_akun():
    while True:
        bersihkan_layar()
        cetak_header("       KELOLA AKUN PENGGUNA", garis_40)
        print("1. Lihat semua akun")
        print("2. Tambah akun")
        print("3. Ubah password akun")
        print("4. Hapus akun")
        print("5. Kembali")
        pilihan_akun = minta_pilihan()

        if pilihan_akun == "1":
            lihat_semua_akun()
        elif pilihan_akun == "2":
            tambah_akun()
        elif pilihan_akun == "3":
            ubah_password_akun()
        elif pilihan_akun == "4":
            hapus_akun()
        elif pilihan_akun == "5":
            break
        else:
            print("Pilihan tidak valid.")
            jeda()

# ADMIN - KELOLA PRESET
def lihat_semua_preset():
    print("\n=== DAFTAR PRESET ===")
    if not preset:
        print("Belum ada preset.")
    else:
        for id_item, data_preset in preset.items():
            print("\nID:", id_item)
            print("Nama:", data_preset["nama"])
            print("Deskripsi:", data_preset["deskripsi"])
            print(strip_40)
    jeda()

def tambah_preset():
    print("\n=== TAMBAH PRESET ===")
    nama_baru = input("Nama preset: ").strip()
    deskripsi_baru = input("Deskripsi preset: ").strip()
    try:
        if nama_baru == "" or deskripsi_baru == "":
            raise ValueError("Nama dan deskripsi tidak boleh kosong.")
        if any(data_preset["nama"].lower() == nama_baru.lower() for data_preset in preset.values()):
            raise ValueError("Nama preset sudah terdaftar.")
    except ValueError as e:
        print(e)
    else:
        id_baru = max(preset, default=0) + 1
        preset[id_baru] = {"nama": nama_baru, "deskripsi": deskripsi_baru}
        print("Preset berhasil ditambahkan!")
        print("ID preset:", id_baru)
    finally:
        jeda()

def ubah_preset():
    print("\n=== UBAH PRESET ===")
    daftar_id_nama(preset)
    try:
        id_target = pilih_id(preset, "Masukkan ID preset yang ingin diubah: ", "ID", "Preset tidak ditemukan.")
        nama_lama = preset[id_target]["nama"]
        deskripsi_lama = preset[id_target]["deskripsi"]

        print("\nNama saat ini:", nama_lama)
        nama_baru = input("Nama baru (Enter untuk tetap): ").strip() or nama_lama
        print("\nDeskripsi saat ini:", deskripsi_lama)
        deskripsi_baru = input("Deskripsi baru (Enter untuk tetap): ").strip() or deskripsi_lama

        nama_duplikat = any(
            id_lain != id_target and data_preset["nama"].lower() == nama_baru.lower()
            for id_lain, data_preset in preset.items()
        )
        if nama_duplikat:
            raise ValueError("Nama preset sudah digunakan preset lain.")
    except ValueError as e:
        print(e)
    else:
        preset[id_target]["nama"] = nama_baru
        preset[id_target]["deskripsi"] = deskripsi_baru
        print("Preset berhasil diperbarui.")
    finally:
        jeda()

def hapus_preset():
    print("\n=== HAPUS PRESET ===")
    daftar_id_nama(preset)
    try:
        id_target = pilih_id(preset, "Masukkan ID preset yang ingin dihapus: ", "ID", "Preset tidak ditemukan.")
        if any(data_tes.get("id_preset") == id_target for data_tes in riwayat):
            raise ValueError("Preset tidak dapat dihapus karena masih digunakan dalam riwayat tes.")
    except ValueError as e:
        print(e)
    else:
        if konfirmasi_ya("Yakin ingin menghapus preset ini? (ya/tidak): "):
            del preset[id_target]
            print("Preset berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")
    finally:
        jeda()

def kelola_preset():
    while True:
        bersihkan_layar()
        cetak_header("       KELOLA PRESET PENGUJIAN", garis_40)
        print("1. Lihat semua preset")
        print("2. Tambah preset")
        print("3. Ubah preset")
        print("4. Hapus preset")
        print("5. Kembali")
        pilihan_preset = minta_pilihan()

        if pilihan_preset == "1":
            lihat_semua_preset()
        elif pilihan_preset == "2":
            tambah_preset()
        elif pilihan_preset == "3":
            ubah_preset()
        elif pilihan_preset == "4":
            hapus_preset()
        elif pilihan_preset == "5":
            break
        else:
            print("Pilihan tidak valid.")
            jeda()

# ADMIN - KELOLA TARGET DUMMY
def lihat_semua_dummy():
    print("\n=== DAFTAR TARGET DUMMY ===")
    if not dummy:
        print("Belum ada target dummy.")
    else:
        for id_item, data_dummy in dummy.items():
            print("\nID:", id_item)
            print("Nama:", data_dummy["nama"])
            print("Kategori:", data_dummy["kategori"])
            print("Deskripsi:", data_dummy["deskripsi"])
            print(strip_40)
    jeda()

def tambah_dummy():
    print("\n=== TAMBAH TARGET DUMMY ===")
    nama_baru = input("Nama target: ").strip()
    kategori_baru = input("Kategori (Standard/Boss/Multi-target): ").strip().title()
    deskripsi_baru = input("Deskripsi target: ").strip()
    try:
        if nama_baru == "" or kategori_baru == "" or deskripsi_baru == "":
            raise ValueError("Semua kolom wajib diisi.")
        if kategori_baru not in kategori_dummy:
            raise ValueError("Kategori tidak valid.")
        if any(data_dummy["nama"].lower() == nama_baru.lower() for data_dummy in dummy.values()):
            raise ValueError("Nama target sudah terdaftar.")
    except ValueError as e:
        print(e)
    else:
        id_baru = max(dummy, default=0) + 1
        dummy[id_baru] = {
            "nama": nama_baru,
            "kategori": kategori_baru,
            "deskripsi": deskripsi_baru
        }
        print("Target dummy berhasil ditambahkan!")
        print("ID target:", id_baru)
    finally:
        jeda()

def ubah_dummy():
    print("\n=== UBAH TARGET DUMMY ===")
    daftar_id_nama(dummy)
    try:
        id_target = pilih_id(dummy, "Masukkan ID target yang ingin diubah: ", "ID", "Target dummy tidak ditemukan.")
        data_lama = dummy[id_target]
        nama_baru = input(f"Nama baru ({data_lama['nama']}): ").strip() or data_lama["nama"]
        kategori_baru = input(
            f"Kategori baru ({data_lama['kategori']}): "
        ).strip().title() or data_lama["kategori"]
        deskripsi_baru = input(
            f"Deskripsi baru ({data_lama['deskripsi']}): "
        ).strip() or data_lama["deskripsi"]

        nama_duplikat = any(
            id_lain != id_target and data_dummy["nama"].lower() == nama_baru.lower()
            for id_lain, data_dummy in dummy.items()
        )
        if kategori_baru not in kategori_dummy:
            raise ValueError("Kategori tidak valid.")
        if nama_duplikat:
            raise ValueError("Nama target sudah digunakan.")
    except ValueError as e:
        print(e)
    else:
        dummy[id_target]["nama"] = nama_baru
        dummy[id_target]["kategori"] = kategori_baru
        dummy[id_target]["deskripsi"] = deskripsi_baru
        print("Target dummy berhasil diperbarui.")
    finally:
        jeda()

def hapus_dummy():
    print("\n=== HAPUS TARGET DUMMY ===")
    daftar_id_nama(dummy)
    try:
        id_target = pilih_id(dummy, "Masukkan ID target yang ingin dihapus: ", "ID", "Target dummy tidak ditemukan.")
        if any(data_tes.get("id_dummy") == id_target for data_tes in riwayat):
            raise ValueError("Target tidak dapat dihapus karena masih digunakan dalam riwayat tes.")
    except ValueError as e:
        print(e)
    else:
        if konfirmasi_ya("Yakin ingin menghapus target ini? (ya/tidak): "):
            del dummy[id_target]
            print("Target dummy berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")
    finally:
        jeda()

def kelola_dummy():
    while True:
        bersihkan_layar()
        cetak_header("         KELOLA TARGET DUMMY", garis_40)
        print("1. Lihat semua target dummy")
        print("2. Tambah target dummy")
        print("3. Ubah target dummy")
        print("4. Hapus target dummy")
        print("5. Kembali")
        pilihan_dummy = minta_pilihan()

        if pilihan_dummy == "1":
            lihat_semua_dummy()
        elif pilihan_dummy == "2":
            tambah_dummy()
        elif pilihan_dummy == "3":
            ubah_dummy()
        elif pilihan_dummy == "4":
            hapus_dummy()
        elif pilihan_dummy == "5":
            break
        else:
            print("Pilihan tidak valid.")
            jeda()

# ADMIN - LIHAT TIM / BUILD / RIWAYAT / KARAKTER
def lihat_seluruh_tim():
    bersihkan_layar()
    cetak_header("          SELURUH TIM PENGGUNA", garis_40)
    if not team:
        print("Belum ada tim yang dibuat.")
    else:
        for data_tim in team:
            print("\nID Tim:", data_tim["id"])
            print("Pemilik:", data_tim["username"])
            print("Nama Tim:", data_tim["nama_tim"])
            print("Anggota Karakter:")
            for nama_karakter in data_tim["karakter"]:
                print("-", nama_karakter)
            print(strip_40)
    jeda()

def lihat_seluruh_build():
    bersihkan_layar()
    cetak_header("              SELURUH BUILD PENGGUNA", garis_55)
    if not build:
        print("Belum ada konfigurasi build yang dibuat.")
    else:
        for data_build in build:
            print("\nID Build :", data_build["id"])
            print("Pemilik :", data_build["username"])
            print("Nama Build :", data_build["nama_build"])
            print("ID Tim :", data_build["id_team"])
            print("Nama Tim :", data_build["nama_tim"])
            print("\nKonfigurasi Karakter:")
            for nomor, data_karakter in enumerate(data_build["karakter_build"], start=1):
                cetak_karakter_build(nomor, data_karakter, indent_judul="  ")
            print(strip_55)
    jeda()

def lihat_seluruh_riwayat():
    bersihkan_layar()
    cetak_header("               SELURUH RIWAYAT TES DPS", garis_55)
    if not riwayat:
        print("Belum ada riwayat pengujian DPS.")
    else:
        for data_tes in riwayat:
            preset_dipilih = preset.get(data_tes["id_preset"])
            dummy_dipilih = dummy.get(data_tes["id_dummy"])
            print("\nID Tes :", data_tes["id"])

            print("ID Tim :", data_tes["id_team"])
            print("ID Build :", data_tes["id_build"])
            print("Pemilik :", data_tes["username"])
            print("Nama Tim :", data_tes["nama_tim"])
            print("Nama Build :", data_tes["nama_build"])
            print("Preset       :", preset_dipilih["nama"] if preset_dipilih else "Preset tidak ditemukan")
            print("Target Dummy :", dummy_dipilih["nama"] if dummy_dipilih else "Target dummy tidak ditemukan")
            print("\nKONFIGURASI BUILD SAAT PENGUJIAN")
            print(strip_55)
            for nomor, data_karakter in enumerate(data_tes["karakter_build"], start=1):
                cetak_karakter_build(nomor, data_karakter)
            print("\nHASIL PENGUJIAN")
            print("Hasil DPS :", format_ribuan(data_tes["dps"]))
            print(garis_55)
    jeda()

def tambah_karakter():
    print("\n=== TAMBAH KARAKTER BARU ===")
    nama_baru = input("Nama karakter: ").strip()
    elemen_baru = input("Elemen karakter: ").strip().capitalize()
    try:
        if nama_baru == "" or elemen_baru == "":
            raise ValueError("Nama dan elemen tidak boleh kosong.")
        if cari_karakter(nama_baru) is not None:
            raise ValueError("Karakter sudah terdaftar.")
        if elemen_baru not in elemen_karakter_valid:
            raise ValueError("Elemen tidak valid.")
    except ValueError as e:
        print(e)
    else:
        genshin_characters[nama_baru] = elemen_baru
        print("\nKarakter berhasil ditambahkan!")
        print("Nama:", nama_baru)
        print("Elemen:", elemen_baru)
    finally:
        jeda()

# MENU ADMIN
def menu_admin():
    while True:
        bersihkan_layar()
        cetak_header("          MENU ADMIN", garis_40)
        print("1. Kelola akun pengguna")
        print("2. Kelola preset pengujian")
        print("3. Kelola target dummy")
        print("4. Lihat seluruh tim")
        print("5. Lihat seluruh build")
        print("6. Lihat seluruh riwayat tes")
        print("7. Kelola Karakter")
        print("8. Logout")
        pilihan_admin = minta_pilihan()

        if pilihan_admin == "1":
            kelola_akun()
        elif pilihan_admin == "2":
            kelola_preset()
        elif pilihan_admin == "3":
            kelola_dummy()
        elif pilihan_admin == "4":
            lihat_seluruh_tim()
        elif pilihan_admin == "5":
            lihat_seluruh_build()
        elif pilihan_admin == "6":
            lihat_seluruh_riwayat()
        elif pilihan_admin == "7":
            tambah_karakter()
        elif pilihan_admin == "8":
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid.")
            jeda()

# USER - DAFTAR KARAKTER
def lihat_daftar_karakter():
    bersihkan_layar()
    cetak_header("          DAFTAR KARAKTER", garis_40)

    if not genshin_characters:
        print("Belum ada karakter yang tersedia.")
    else:
        for nomor, (nama_karakter, elemen) in enumerate(genshin_characters.items(), start=1):
            print(f"{nomor}. {nama_karakter} - {elemen}")
    print(strip_40)
    print("Total Karakter:", hitung_total_karakter())
    jeda()

# USER - KELOLA TIM
def lihat_tim_saya(username_aktif):
    bersihkan_layar()
    cetak_header("               TIM SAYA", garis_40)
    tim_saya = ambil_tim_saya(username_aktif)

    if not tim_saya:
        print("Kamu belum memiliki tim.")
    else:
        for data_tim in tim_saya:
            print("\nID Tim:", data_tim["id"])
            print("Nama Tim:", data_tim["nama_tim"])
            print("Anggota:")
            for nama_karakter in data_tim["karakter"]:
                elemen = data_tim["elemen"].get(nama_karakter, genshin_characters[nama_karakter])
                print("-", nama_karakter, "-", elemen)
            print(strip_40)
    jeda()

def buat_tim(username_aktif):
    bersihkan_layar()
    cetak_header("               BUAT TIM", garis_40)
    nama_tim = input("Masukkan nama tim: ").strip()

    try:
        if nama_tim == "":
            raise ValueError("Nama tim tidak boleh kosong.")
        if any(
            data_tim["username"] == username_aktif and data_tim["nama_tim"].lower() == nama_tim.lower()
            for data_tim in team
        ):
            raise ValueError("Nama tim tersebut sudah di gunakan.")
    except ValueError as e:
        print(e)
        jeda()
        return

    karakter_tim, elemen_tim = kumpulkan_anggota_tim()

    try:
        if len(karakter_tim) == 0:
            raise ValueError("Tim tidak boleh kosong.")
    except ValueError as e:
        print(e)
    else:
        id_team_baru = max((data_tim["id"] for data_tim in team), default=0) + 1
        team.append({
            "id": id_team_baru,
            "username": username_aktif,
            "nama_tim": nama_tim,
            "karakter": karakter_tim,
            "elemen": elemen_tim
        })
        print("\nTim berhasil dibuat dengan ID:", id_team_baru)
    finally:
        jeda()

def ubah_nama_tim(tim_dipilih, username_aktif):
    nama_baru = input("Nama tim baru (Enter untuk tetap): ").strip()
    if nama_baru == "":
        return
    try:
        nama_duplikat = any(
            data_tim["id"] != tim_dipilih["id"]
            and data_tim["username"] == username_aktif
            and data_tim["nama_tim"].lower() == nama_baru.lower()
            for data_tim in team
        )
        if nama_duplikat:
            raise ValueError("Nama tim tersebut sudah kamu gunakan.")
    except ValueError as e:
        print(e)
    else:
        tim_dipilih["nama_tim"] = nama_baru

def ubah_anggota_tim(tim_dipilih):
    print("\nAnggota saat ini:", tim_dipilih["karakter"])
    print("Masukkan karakter baru dipisahkan dengan koma.")
    print("Ketik 'tetap' untuk mempertahankan anggota.")
    input_karakter = input("Anggota baru: ").strip()

    if input_karakter.lower() == "tetap" or input_karakter == "":
        return

    daftar_baru = [nama.strip() for nama in input_karakter.split(",") if nama.strip() != ""]

    try:
        karakter_valid, elemen_baru = validasi_anggota_baru(daftar_baru)
    except ValueError as e:
        print(e)
        print("Perubahan anggota dibatalkan.")
        return
    if len(karakter_valid) == 0:
        print("Perubahan anggota dibatalkan.")
        return

    try:
        if len(karakter_valid) > 4:
            raise ValueError("Tim maksimal terdiri dari 4 karakter.")
        if tim_dipakai(tim_dipilih["id"]):
            raise ValueError(
                "Anggota tim tidak dapat diubah "
                "karena sudah digunakan pada build "
                "atau riwayat tes."
            )
    except ValueError as e:
        print(e)
    else:
        tim_dipilih["karakter"] = karakter_valid
        tim_dipilih["elemen"] = elemen_baru
        print("Anggota tim berhasil diperbarui.")

def ubah_tim(username_aktif):
    bersihkan_layar()
    cetak_header("               UBAH TIM", garis_40)
    tim_saya = ambil_tim_saya(username_aktif)
    if not tim_saya:
        print("Kamu belum memiliki tim.")
        jeda()
        return

    for data_tim in tim_saya:
        print(
            "ID:", data_tim["id"],
            "| Nama:", data_tim["nama_tim"],
            "| Anggota:", ", ".join(data_tim["karakter"])
        )

    try:
        tim_dipilih = pilih_dari_daftar(
            tim_saya, "\nMasukkan ID tim yang ingin diubah: ", "ID tim", "Tim tidak ditemukan."
        )
    except ValueError as e:
        print(e)
        jeda()
        return

    ubah_nama_tim(tim_dipilih, username_aktif)
    ubah_anggota_tim(tim_dipilih)
    print("\nProses perubahan tim selesai.")
    jeda()

def hapus_tim(username_aktif):
    bersihkan_layar()
    cetak_header("              HAPUS TIM", garis_40)
    tim_saya = ambil_tim_saya(username_aktif)
    if not tim_saya:
        print("Kamu belum memiliki tim.")
        jeda()
        return

    for data_tim in tim_saya:
        print("ID:", data_tim["id"], "| Nama:", data_tim["nama_tim"])

    try:
        tim_dipilih = pilih_dari_daftar(
            tim_saya, "\nMasukkan ID tim yang ingin dihapus: ", "ID tim", "Tim tidak ditemukan."
        )
        if tim_dipakai(tim_dipilih["id"]):
            raise ValueError("Tim tidak dapat dihapus karena sudah digunakan pada build atau riwayat tes.")
    except ValueError as e:
        print(e)
    else:
        if konfirmasi_ya("Yakin ingin menghapus tim ini? (ya/tidak): "):
            team.remove(tim_dipilih)
            print("Tim berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")
    finally:
        jeda()

def kelola_tim(username_aktif):
    while True:
        bersihkan_layar()
        cetak_header("             KELOLA TIM", garis_40)
        print("1. Lihat Tim Saya")
        print("2. Buat Tim")
        print("3. Ubah Tim")
        print("4. Hapus Tim")
        print("5. Kembali")
        pilihan_tim = minta_pilihan()

        if pilihan_tim == "1":
            lihat_tim_saya(username_aktif)
        elif pilihan_tim == "2":
            buat_tim(username_aktif)
        elif pilihan_tim == "3":
            ubah_tim(username_aktif)
        elif pilihan_tim == "4":
            hapus_tim(username_aktif)
        elif pilihan_tim == "5":
            break
        else:
            print("Pilihan tidak valid.")
            jeda("\nTekan Enter untuk mencoba lagi...")

# USER - KELOLA BUILD KARAKTER
def lihat_build_saya(username_aktif):
    bersihkan_layar()
    cetak_header("          DAFTAR KONFIGURASI BUILD", garis_45)
    build_saya = ambil_build_saya(username_aktif)

    if not build_saya:
        print("Kamu belum memiliki konfigurasi build.")
    else:
        for data_build in build_saya:
            print("\nID Build   :", data_build["id"])
            print("Nama Build :", data_build["nama_build"])
            print("Nama Tim   :", data_build["nama_tim"])
            for nomor, data_karakter in enumerate(data_build["karakter_build"], start=1):
                cetak_karakter_build(nomor, data_karakter, indent_judul="  ", indent_detail="  ", lebar_label=8)
            print(strip_45)
    jeda()

def buat_build(username_aktif):
    bersihkan_layar()
    tim_saya = ambil_tim_saya(username_aktif)
    if not tim_saya:
        print("Kamu belum memiliki tim.")
        jeda(enter_kembali_rapat)
        return

    cetak_header("          PILIH TIM", garis_45)
    for data_tim in tim_saya:
        print(f'ID: {data_tim["id"]} | Nama Tim: {data_tim["nama_tim"]}')
        print("Karakter:", ", ".join(data_tim["karakter"]))
        print(strip_45)

    try:
        tim_dipilih = pilih_dari_daftar(tim_saya, "Masukkan ID tim: ", "ID tim", "Tim tidak ditemukan.")
        nama_build = input("Masukkan nama konfigurasi build: ").strip()
        if not nama_build:
            raise ValueError("Nama konfigurasi tidak boleh kosong.")
    except ValueError as e:
        print(e)
        jeda(enter_kembali_rapat)
        return

    karakter_build = kumpulkan_build_karakter(tim_dipilih)

    if len(karakter_build) != 4:
        print("Konfigurasi build tidak disimpan.")
        jeda(enter_kembali_rapat)
        return

    id_build_baru = max((data_build["id"] for data_build in build), default=0) + 1
    build.append({
        "id": id_build_baru,
        "username": username_aktif,
        "nama_build": nama_build,
        "id_team": tim_dipilih["id"],
        "nama_tim": tim_dipilih["nama_tim"],
        "karakter_build": karakter_build
    })
    print("\nKonfigurasi build berhasil disimpan.")
    print("ID Build:", id_build_baru)

def edit_build(username_aktif):
    bersihkan_layar()
    build_saya = ambil_build_saya(username_aktif)
    if not build_saya:
        print("Kamu belum memiliki konfigurasi build.")
        jeda(enter_kembali_rapat)
        return

    cetak_header("          EDIT KONFIGURASI BUILD", garis_45)
    for data_build in build_saya:
        print(
            f'ID: {data_build["id"]} | '
            f'Build: {data_build["nama_build"]} | '
            f'Tim: {data_build["nama_tim"]}'
        )

    try:
        build_dipilih = pilih_dari_daftar(
            build_saya, "Masukkan ID build: ", "ID build", "Build tidak ditemukan."
        )
    except ValueError as e:
        print(e)
        jeda(enter_kembali_rapat)
        return

    print("\n1. Ubah nama konfigurasi")
    print("2. Ubah build satu karakter")
    pilihan_edit = minta_pilihan()

    try:
        if pilihan_edit == "1":
            nama_baru = input("Nama konfigurasi baru: ").strip()
            if not nama_baru:
                raise ValueError("Nama konfigurasi tidak boleh kosong.")
            build_dipilih["nama_build"] = nama_baru
            print("Nama konfigurasi berhasil diubah.")

        elif pilihan_edit == "2":
            cetak_ringkas_karakter(build_dipilih["karakter_build"])
            nomor_input = input("Pilih nomor karakter yang ingin diedit: ").strip()
            nomor_pilihan = baca_id(nomor_input, "Pilihan")
            if not 1 <= nomor_pilihan <= 4:
                raise ValueError("Nomor karakter tidak valid.")
            data_karakter = build_dipilih["karakter_build"][nomor_pilihan - 1]
            print("Karakter:", data_karakter["karakter"])
            senjata_baru = input("Nama senjata baru: ").strip()
            artefak_baru = input("Nama artefak baru: ").strip()
            if not (senjata_baru and artefak_baru):
                raise ValueError("Senjata dan artefak tidak boleh kosong.")
            data_karakter["senjata"] = senjata_baru
            data_karakter["artefak"] = artefak_baru
            print("Build karakter berhasil diperbarui.")

        else:
            raise ValueError("Pilihan tidak valid.")
    except (ValueError, IndexError) as e:
        print(e)
    finally:
        jeda()

def hapus_build(username_aktif):
    bersihkan_layar()
    build_saya = ambil_build_saya(username_aktif)
    if not build_saya:
        print("Kamu belum memiliki konfigurasi build.")
        jeda(enter_kembali_rapat)
        return

    cetak_header("         HAPUS KONFIGURASI BUILD", garis_45)
    for data_build in build_saya:
        print(
            f'ID: {data_build["id"]} | '
            f'{data_build["nama_build"]} | '
            f'Tim: {data_build["nama_tim"]}'
        )

    try:
        build_dipilih = pilih_dari_daftar(
            build_saya, "Masukkan ID build: ", "ID build", "Build tidak ditemukan."
        )
    except ValueError as e:
        print(e)
        jeda(enter_kembali_rapat)
        return

    try:
        if any(data_tes["id_build"] == build_dipilih["id"] for data_tes in riwayat):
            raise ValueError("Build tidak dapat dihapus karena sudah digunakan dalam riwayat pengujian.")
    except ValueError as e:
        print(e)
    else:
        if konfirmasi_ya(f'Hapus konfigurasi "{build_dipilih["nama_build"]}"? (ya/tidak): '):
            build.remove(build_dipilih)
            print("Konfigurasi build berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")
    finally:
        jeda(enter_kembali_rapat)

def kelola_build(username_aktif):
    while True:
        bersihkan_layar()
        cetak_header("           KELOLA BUILD KARAKTER", garis_45)
        print("1. Lihat konfigurasi build")
        print("2. Buat konfigurasi build")
        print("3. Edit konfigurasi build")
        print("4. Hapus konfigurasi build")
        print("5. Kembali")
        pilihan_build = minta_pilihan()

        if pilihan_build == "1":
            lihat_build_saya(username_aktif)
        elif pilihan_build == "2":
            buat_build(username_aktif)
        elif pilihan_build == "3":
            edit_build(username_aktif)
        elif pilihan_build == "4":
            hapus_build(username_aktif)
        elif pilihan_build == "5":
            break
        else:
            print("Pilihan tidak valid.")
            jeda(enter_kembali_rapat)

# USER - CATAT HASIL PENGUJIAN DPS
def catat_tes_baru(username_aktif):
    bersihkan_layar()
    build_saya = ambil_build_saya(username_aktif)
    if not build_saya:
        print("Kamu belum memiliki konfigurasi build.")
        print("Buat konfigurasi terlebih dahulu di menu nomor 3.")
        jeda()
        return

    # Pilih build
    cetak_header("       PILIH KONFIGURASI BUILD TIM", garis_45)
    for data_build in build_saya:
        print(f'\nID Build   : {data_build["id"]}')
        print(f'Nama Build : {data_build["nama_build"]}')
        print(f'Nama Tim   : {data_build["nama_tim"]}')
        cetak_ringkas_karakter(data_build["karakter_build"])
        print(strip_45)

    try:
        build_dipilih = pilih_dari_daftar(
            build_saya, "\nMasukkan ID konfigurasi build yang diuji: ",
            "ID build", "Konfigurasi build tidak ditemukan."
        )
        # Pilih preset
        tampilkan_pilihan_preset()
        id_preset = pilih_id(preset, "\nMasukkan ID preset: ", "ID preset", "Preset tidak ditemukan.")
        # Pilih target dummy
        tampilkan_pilihan_dummy()
        id_dummy = pilih_id(dummy, "\nMasukkan ID target dummy: ", "ID dummy", "Target dummy tidak ditemukan.")
    except ValueError as e:
        print(e)
        jeda(enter_kembali_rapat)
        return

    # Konfirmasi pengujian
    print("\n" + garis_45)
    print("          KONFIRMASI PENGUJIAN")
    print(garis_45)
    print("Nama Tim   :", build_dipilih["nama_tim"])
    print("Nama Build :", build_dipilih["nama_build"])
    print("Preset     :", preset[id_preset]["nama"])
    print("Target     :", dummy[id_dummy]["nama"])
    print("\nKarakter yang akan diuji:")
    cetak_ringkas_karakter(build_dipilih["karakter_build"])
    if not konfirmasi_ya("\nApakah pengujian sudah dilakukan? (ya/tidak): "):
        print("Pencatatan pengujian dibatalkan.")
        jeda(enter_kembali_rapat)
        return

    # Input hasil DPS
    try:
        hasil_dps = input("\nMasukkan hasil DPS dari game: ").strip()
        if not hasil_dps.isdigit():
            raise ValueError("Hasil DPS harus berupa angka bulat.")
        hasil_dps = int(hasil_dps)
        if hasil_dps <= 0:
            raise ValueError("Hasil DPS harus lebih besar dari 0.")
    except ValueError as e:
        print(e)
        jeda(enter_kembali_rapat)
        return
    else:
        id_tes_baru = buat_id_tes()
        riwayat.append({
            "id": id_tes_baru,
            "username": username_aktif,
            "id_team": build_dipilih["id_team"],
            "id_build": build_dipilih["id"],
            "nama_tim": build_dipilih["nama_tim"],
            "nama_build": build_dipilih["nama_build"],
            "karakter_build": [dict(data) for data in build_dipilih["karakter_build"]],
            "id_preset": id_preset,
            "id_dummy": id_dummy,
            "dps": hasil_dps
        })
        print("\nPengujian DPS berhasil dicatat.")
        print("ID Tes     :", id_tes_baru)
        print("Nama Tim   :", build_dipilih["nama_tim"])
        print("Nama Build :", build_dipilih["nama_build"])
        print("Hasil DPS  :", format_ribuan(hasil_dps))
    jeda()

def menu_catat_dps(username_aktif):
    while True:
        bersihkan_layar()
        cetak_header("          CATAT HASIL PENGUJIAN DPS", garis_45)
        print("1. Catat tes baru")
        print("2. Kembali")
        pilihan_tes = minta_pilihan()

        if pilihan_tes == "2":
            break
        if pilihan_tes != "1":
            print("Pilihan tidak valid.")
            jeda()
            continue
        catat_tes_baru(username_aktif)

# USER - RIWAYAT PENGUJIAN
def lihat_daftar_riwayat(username_aktif):
    bersihkan_layar()
    cetak_header("                 DAFTAR RIWAYAT DPS", garis_55)
    riwayat_saya = ambil_riwayat_saya(username_aktif)

    if not riwayat_saya:
        print("Kamu belum memiliki riwayat pengujian DPS.")
    else:
        for data_tes in riwayat_saya:
            preset_dipilih = preset.get(data_tes["id_preset"])
            dummy_dipilih = dummy.get(data_tes["id_dummy"])

            print(f'\nID Tes       : {data_tes["id"]}')
            print(f'Nama Tim     : {data_tes["nama_tim"]}')
            print(f'Nama Build   : {data_tes["nama_build"]}')
            print("Preset       :", preset_dipilih["nama"] if preset_dipilih else "Preset tidak ditemukan")
            print("Target Dummy :", dummy_dipilih["nama"] if dummy_dipilih else "Dummy tidak ditemukan")
            print("Hasil DPS    :", format_ribuan(data_tes["dps"]))
            print(strip_55)
    jeda()

def lihat_detail_riwayat(username_aktif):
    bersihkan_layar()
    cetak_header("                 DETAIL RIWAYAT DPS", garis_55)
    riwayat_saya = ambil_riwayat_saya(username_aktif)
    if not riwayat_saya:
        print("Kamu belum memiliki riwayat pengujian DPS.")
        jeda()
        return

    for data_tes in riwayat_saya:
        print(
            f'ID Tes: {data_tes["id"]} | '
            f'{data_tes["nama_tim"]} | '
            f'{data_tes["nama_build"]} | '
            f'DPS: {format_ribuan(data_tes["dps"])}'
        )

    try:
        tes_dipilih = pilih_dari_daftar(
            riwayat_saya, "\nMasukkan ID tes yang ingin dilihat: ",
            "ID tes", "Riwayat pengujian tidak ditemukan."
        )
    except ValueError as e:
        print(e)
        jeda(enter_kembali_rapat)
        return

    bersihkan_layar()
    preset_dipilih = preset.get(tes_dipilih["id_preset"])
    dummy_dipilih = dummy.get(tes_dipilih["id_dummy"])

    cetak_header("                 DETAIL PENGUJIAN DPS", garis_55)
    print("ID Tes       :", tes_dipilih["id"])
    print("Nama Tim     :", tes_dipilih["nama_tim"])
    print("Nama Build   :", tes_dipilih["nama_build"])
    print("Preset       :", preset_dipilih["nama"] if preset_dipilih else "Preset tidak ditemukan")
    if preset_dipilih:
        print("Deskripsi    :", preset_dipilih["deskripsi"])
    print("Target Dummy :", dummy_dipilih["nama"] if dummy_dipilih else "Dummy tidak ditemukan")
    if dummy_dipilih:
        print("Kategori     :", dummy_dipilih["kategori"])
        print("Deskripsi    :", dummy_dipilih["deskripsi"])
    print("\nKONFIGURASI BUILD SAAT PENGUJIAN")
    print(strip_55)
    for nomor, data_karakter in enumerate(tes_dipilih["karakter_build"], start=1):
        cetak_karakter_build(nomor, data_karakter, lebar_label=8)
    print("\n" + garis_55)
    print("HASIL DPS:", format_ribuan(tes_dipilih["dps"]))
    print(garis_55)
    jeda()

def menu_riwayat(username_aktif):
    while True:
        bersihkan_layar()
        cetak_header("                 RIWAYAT PENGUJIAN DPS", garis_55)
        print("1. Lihat seluruh riwayat")
        print("2. Lihat detail riwayat")
        print("3. Kembali")
        pilihan_riwayat = minta_pilihan()

        if pilihan_riwayat == "1":
            lihat_daftar_riwayat(username_aktif)
        elif pilihan_riwayat == "2":
            lihat_detail_riwayat(username_aktif)
        elif pilihan_riwayat == "3":
            break
        else:
            print("Pilihan tidak valid.")
            jeda("Tekan Enter untuk melanjutkan...")

# USER - LIHAT PRESET DAN TARGET DUMMY
def lihat_preset_dan_dummy():
    bersihkan_layar()
    cetak_header("             PRESET PENGUJIAN DPS", garis_55)

    if not preset:
        print("Belum ada preset pengujian.")
    else:
        for id_item, data_preset in preset.items():
            print(f"\nID Preset  : {id_item}")
            print(f"Nama       : {data_preset['nama']}")
            print(f"Deskripsi  : {data_preset['deskripsi']}")
            print(strip_55)

    print("\n" + garis_55)
    print("                TARGET DUMMY")
    print(garis_55)

    if not dummy:
        print("Belum ada target dummy.")
    else:
        for id_item, data_dummy in dummy.items():
            print(f"\nID Dummy   : {id_item}")
            print(f"Nama       : {data_dummy['nama']}")
            print(f"Kategori   : {data_dummy['kategori']}")
            print(f"Deskripsi  : {data_dummy['deskripsi']}")
            print(strip_55)
    jeda()

# MENU USER
def menu_user(username_aktif):
    while True:
        bersihkan_layar()
        cetak_header("           MENU USER", garis_40)
        print("Login sebagai:", username_aktif)
        print("1. Lihat daftar karakter")
        print("2. Kelola tim")
        print("3. Kelola build karakter")
        print("4. Catat hasil pengujian DPS")
        print("5. Lihat riwayat pengujian")
        print("6. Lihat preset dan target dummy")
        print("7. Logout")
        pilihan_user = minta_pilihan()

        if pilihan_user == "1":
            lihat_daftar_karakter()
        elif pilihan_user == "2":
            kelola_tim(username_aktif)
        elif pilihan_user == "3":
            kelola_build(username_aktif)
        elif pilihan_user == "4":
            menu_catat_dps(username_aktif)
        elif pilihan_user == "5":
            menu_riwayat(username_aktif)
        elif pilihan_user == "6":
            lihat_preset_dan_dummy()
        elif pilihan_user == "7":
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid.")
            jeda()

# PROGRAM UTAMA (Multiuser: Admin & User)
def main():
    while True:
        bersihkan_layar()
        cetak_header("       GENSHIN DPS TRACKER", garis_40)
        print("1. Login")
        print("2. Registrasi")
        print("3. Keluar")
        pilihan_awal = input("Pilih menu: ").strip()

        if pilihan_awal == "3":
            print("\nTerima kasih telah menggunakan DPS Tracker!")
            break
        if pilihan_awal == "2":
            registrasi()
            continue
        if pilihan_awal != "1":
            print("Pilihan tidak valid.")
            jeda(enter_kembali_rapat)
            continue

        hasil_login = login()
        if hasil_login is None:
            continue

        username_aktif, role_aktif = hasil_login
        if role_aktif == "Admin":
            menu_admin()
        elif role_aktif == "User":
            menu_user(username_aktif)

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nProgram dihentikan.")