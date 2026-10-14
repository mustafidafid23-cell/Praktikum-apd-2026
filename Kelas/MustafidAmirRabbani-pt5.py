# GENSHIN DPS TRACKER
import os
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
                "senjata": "Enggulfing",
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
id_team_berikutnya = 1
id_build_berikutnya = 1
id_tes_berikutnya = 1

# ==================== MENU UTAMA ====================
while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 40)
    print("       GENSHIN DPS TRACKER")
    print("=" * 40)
    print("1. Login")
    print("2. Registrasi")
    print("3. Keluar")
    pilihan = input("Pilih menu: ").strip()

    # MENU REGISTRASI
    if pilihan == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print("=" * 40)
        print("          REGISTRASI AKUN")
        print("=" * 40)

        username_baru = input(
            "Buat username: "
        ).strip()
        password_baru = input(
            "Buat password: "
        )

        if username_baru == "" or password_baru.strip() == "":
            print("Username dan password tidak boleh kosong.")
        elif username_baru in akun:
            print("Username sudah digunakan.")
        else:
            akun[username_baru] = {
                "password": password_baru,
                "role": "User"
            }
            print("Registrasi berhasil!")
            print("Silakan login menggunakan akun baru.")
        input("\nTekan Enter untuk melanjutkan...")

    # MENU LOGIN
    elif pilihan == "1":
        os.system("cls" if os.name == "nt" else "clear")
        print("=" * 40)
        print("             LOGIN")
        print("=" * 40)
        username = input("Username: ").strip()
        password = input("Password: ")

        if username in akun and akun[username]["password"] == password:
            role = akun[username]["role"]
            print("\nLogin berhasil!")
            print("Selamat datang,", username)
            print("Role:", role)
            input("\nTekan Enter untuk masuk ke menu...")

            # MENU ADMIN
            if role == "Admin":
                while True:
                    os.system(
                        "cls" if os.name == "nt" else "clear"
                    )
                    print("=" * 40)
                    print("          MENU ADMIN")
                    print("=" * 40)
                    print("1. Kelola akun pengguna")
                    print("2. Kelola preset pengujian")
                    print("3. Kelola target dummy")
                    print("4. Lihat seluruh tim")
                    print("5. Lihat seluruh build")
                    print("6. Lihat seluruh riwayat tes")
                    print("7. Kelola Karakter")
                    print("8. Logout")
                    menu_admin = input(
                        "Pilih menu: "
                    ).strip()

                    if menu_admin == "1":
                        while True:
                            os.system("cls" if os.name == "nt" else "clear")
                            print("=" * 40)
                            print("       KELOLA AKUN PENGGUNA")
                            print("=" * 40)
                            print("1. Lihat semua akun")
                            print("2. Tambah akun")
                            print("3. Ubah password akun")
                            print("4. Hapus akun")
                            print("5. Kembali")
                            pilihan_akun = input("Pilih menu: ").strip()

                            if pilihan_akun == "1":
                                print("\n=== DAFTAR AKUN ===")
                                for username, data in akun.items():
                                    print("Username:", username)
                                    print("Role:", data["role"])
                                    print("-" * 30)
                                input("\nTekan Enter untuk kembali...")

                            elif pilihan_akun == "2":
                                print("\n=== TAMBAH AKUN ===")
                                username_baru = input(
                                    "Username baru: "
                                ).strip()
                                password_baru = input(
                                    "Password baru: "
                                )
                                if username_baru == "" or password_baru.strip() == "":
                                    print("Username dan password tidak boleh kosong.")

                                elif username_baru in akun:
                                    print("Username sudah digunakan.")

                                else:
                                    akun[username_baru] = {
                                        "password": password_baru,
                                        "role": "User"
                                    }
                                    print("Akun berhasil ditambahkan!")
                                input("\nTekan Enter untuk kembali...")

                            elif pilihan_akun == "3":
                                print("\n=== UBAH PASSWORD ===")
                                username_target = input(
                                    "Username yang ingin diubah: "
                                ).strip()

                                if username_target not in akun:
                                    print("Akun tidak ditemukan.")

                                elif username_target == "admin":
                                    print("Password akun admin utama tidak dapat diubah dari menu ini.")

                                else:
                                    password_baru = input(
                                        "Masukkan password baru: "
                                    )
                                    if password_baru.strip() == "":
                                        print("Password tidak boleh kosong.")
                                    else:
                                        akun[username_target]["password"] = password_baru
                                        print("Password berhasil diubah.")
                                input("\nTekan Enter untuk kembali...")

                            elif pilihan_akun == "4":
                                print("\n=== HAPUS AKUN ===")
                                username_target = input(
                                    "Username yang ingin dihapus: "
                                ).strip()
                                if username_target not in akun:
                                    print("Akun tidak ditemukan.")
                                elif username_target == "admin":
                                    print("Akun admin utama tidak dapat dihapus.")
                                else:
                                    konfirmasi = input(
                                        "Yakin ingin menghapus akun ini? (ya/tidak): "
                                    ).strip().lower()
                                    if konfirmasi == "ya":
                                        del akun[username_target]
                                        print("Akun berhasil dihapus.")
                                    else:
                                        print("Penghapusan dibatalkan.")
                                input("\nTekan Enter untuk kembali...")

                            elif pilihan_akun == "5":
                                break
                            else:
                                print("Pilihan tidak valid.")
                                input("\nTekan Enter untuk kembali...")

                    elif menu_admin == "2":
                        while True:
                            os.system("cls" if os.name == "nt" else "clear")
                            print("=" * 40)
                            print("       KELOLA PRESET PENGUJIAN")
                            print("=" * 40)
                            print("1. Lihat semua preset")
                            print("2. Tambah preset")
                            print("3. Ubah preset")
                            print("4. Hapus preset")
                            print("5. Kembali")
                            pilihan_preset = input("Pilih menu: ").strip()

                            if pilihan_preset == "1":
                                print("\n=== DAFTAR PRESET ===")
                                if len(preset) == 0:
                                    print("Belum ada preset.")
                                else:
                                    for id_preset, data in preset.items():
                                        print("\nID:", id_preset)
                                        print("Nama:", data["nama"])
                                        print("Deskripsi:", data["deskripsi"])
                                        print("-" * 40)
                                input("\nTekan Enter untuk kembali...")

                            elif pilihan_preset == "2":
                                print("\n=== TAMBAH PRESET ===")
                                nama_baru = input("Nama preset: ").strip()
                                deskripsi_baru = input("Deskripsi preset: ").strip()
                                if nama_baru == "" or deskripsi_baru == "":
                                    print("Nama dan deskripsi tidak boleh kosong.")
                                elif any(
                                    data["nama"].lower() == nama_baru.lower()
                                    for data in preset.values()
                                ):
                                    print("Nama preset sudah terdaftar.")

                                else:
                                    if len(preset) == 0:
                                        id_baru = 1
                                    else:
                                        id_baru = max(preset.keys()) + 1
                                    preset[id_baru] = {
                                        "nama": nama_baru,
                                        "deskripsi": deskripsi_baru
                                    }
                                    print("Preset berhasil ditambahkan!")
                                    print("ID preset:", id_baru)
                                input("\nTekan Enter untuk kembali...")

                            elif pilihan_preset == "3":
                                print("\n=== UBAH PRESET ===")
                                for id_preset, data in preset.items():
                                    print(id_preset, "-", data["nama"])
                                id_input = input(
                                    "Masukkan ID preset yang ingin diubah: "
                                ).strip()
                                if not id_input.isdigit():
                                    print("ID harus berupa angka.")
                                elif int(id_input) not in preset:
                                    print("Preset tidak ditemukan.")
                                else:
                                    id_target = int(id_input)
                                    nama_lama = preset[id_target]["nama"]
                                    deskripsi_lama = preset[id_target]["deskripsi"]

                                    print("\nNama saat ini:", nama_lama)
                                    nama_baru = input(
                                        "Nama baru (Enter untuk tetap): "
                                    ).strip()
                                    print("\nDeskripsi saat ini:", deskripsi_lama)
                                    deskripsi_baru = input(
                                        "Deskripsi baru (Enter untuk tetap): "
                                    ).strip()

                                    if nama_baru == "":
                                        nama_baru = nama_lama
                                    if deskripsi_baru == "":
                                        deskripsi_baru = deskripsi_lama
                                    nama_duplikat = any(
                                        id_lain != id_target
                                        and data["nama"].lower() == nama_baru.lower()
                                        for id_lain, data in preset.items()
                                    )
                                    if nama_duplikat:
                                        print("Nama preset sudah digunakan preset lain.")
                                    else:
                                        preset[id_target]["nama"] = nama_baru
                                        preset[id_target]["deskripsi"] = deskripsi_baru
                                        print("Preset berhasil diperbarui.")
                                input("\nTekan Enter untuk kembali...")

                            elif pilihan_preset == "4":
                                print("\n=== HAPUS PRESET ===")
                                for id_preset, data in preset.items():
                                    print(id_preset, "-", data["nama"])
                                id_input = input(
                                    "Masukkan ID preset yang ingin dihapus: "
                                ).strip()

                                if not id_input.isdigit():
                                    print("ID harus berupa angka.")
                                elif int(id_input) not in preset:
                                    print("Preset tidak ditemukan.")
                                else:
                                    id_target = int(id_input)
                                    digunakan = any(
                                        data.get("id_preset") == id_target
                                        for data in riwayat
                                    )
                                    if digunakan:
                                        print(
                                            "Preset tidak dapat dihapus karena "
                                            "masih digunakan dalam riwayat tes."
                                        )
                                    else:
                                        konfirmasi = input(
                                            "Yakin ingin menghapus preset ini? (ya/tidak): "
                                        ).strip().lower()

                                        if konfirmasi == "ya":
                                            del preset[id_target]
                                            print("Preset berhasil dihapus.")
                                        else:
                                            print("Penghapusan dibatalkan.")
                                input("\nTekan Enter untuk kembali...")

                            elif pilihan_preset == "5":
                                break
                            else:
                                print("Pilihan tidak valid.")
                                input("\nTekan Enter untuk kembali...")

                    elif menu_admin == "3":
                        while True:
                            os.system("cls" if os.name == "nt" else "clear")
                            print("=" * 40)
                            print("         KELOLA TARGET DUMMY")
                            print("=" * 40)
                            print("1. Lihat semua target dummy")
                            print("2. Tambah target dummy")
                            print("3. Ubah target dummy")
                            print("4. Hapus target dummy")
                            print("5. Kembali")
                            pilihan_dummy = input("Pilih menu: ").strip()

                            if pilihan_dummy == "1":
                                print("\n=== DAFTAR TARGET DUMMY ===")
                                if len(dummy) == 0:
                                    print("Belum ada target dummy.")
                                else:
                                    for id_dummy, data in dummy.items():
                                        print("\nID:", id_dummy)
                                        print("Nama:", data["nama"])
                                        print("Kategori:", data["kategori"])
                                        print("Deskripsi:", data["deskripsi"])
                                        print("-" * 40)
                                input("\nTekan Enter untuk kembali...")

                            elif pilihan_dummy == "2":
                                print("\n=== TAMBAH TARGET DUMMY ===")
                                nama_baru = input("Nama target: ").strip()
                                kategori_baru = input(
                                    "Kategori (Standard/Boss/Multi-target): "
                                ).strip().title()
                                deskripsi_baru = input("Deskripsi target: ").strip()
                                if (
                                    nama_baru == ""
                                    or kategori_baru == ""
                                    or deskripsi_baru == ""
                                ):
                                    print("Semua kolom wajib diisi.")

                                elif kategori_baru not in kategori_dummy:
                                    print("Kategori tidak valid.")

                                elif any(
                                    data["nama"].lower() == nama_baru.lower()
                                    for data in dummy.values()
                                ):
                                    print("Nama target sudah terdaftar.")

                                else:
                                    if len(dummy) == 0:
                                        id_baru = 1
                                    else:
                                        id_baru = max(dummy.keys()) + 1
                                    dummy[id_baru] = {
                                        "nama": nama_baru,
                                        "kategori": kategori_baru,
                                        "deskripsi": deskripsi_baru
                                    }
                                    print("Target dummy berhasil ditambahkan!")
                                    print("ID target:", id_baru)
                                input("\nTekan Enter untuk kembali...")

                            elif pilihan_dummy == "3":
                                print("\n=== UBAH TARGET DUMMY ===")
                                for id_dummy, data in dummy.items():
                                    print(id_dummy, "-", data["nama"])
                                id_input = input(
                                    "Masukkan ID target yang ingin diubah: "
                                ).strip()

                                if not id_input.isdigit():
                                    print("ID harus berupa angka.")
                                elif int(id_input) not in dummy:
                                    print("Target dummy tidak ditemukan.")
                                else:
                                    id_target = int(id_input)
                                    data_lama = dummy[id_target]
                                    nama_baru = input(
                                        f"Nama baru ({data_lama['nama']}): "
                                    ).strip()
                                    kategori_baru = input(
                                        f"Kategori baru ({data_lama['kategori']}): "
                                    ).strip().title()
                                    deskripsi_baru = input(
                                        f"Deskripsi baru ({data_lama['deskripsi']}): "
                                    ).strip()

                                    if nama_baru == "":
                                        nama_baru = data_lama["nama"]
                                    if kategori_baru == "":
                                        kategori_baru = data_lama["kategori"]
                                    if deskripsi_baru == "":
                                        deskripsi_baru = data_lama["deskripsi"]

                                    nama_duplikat = any(
                                        id_lain != id_target
                                        and data["nama"].lower() == nama_baru.lower()
                                        for id_lain, data in dummy.items()
                                    )

                                    if kategori_baru not in kategori_dummy:
                                        print("Kategori tidak valid.")
                                    elif nama_duplikat:
                                        print("Nama target sudah digunakan.")
                                    else:
                                        dummy[id_target]["nama"] = nama_baru
                                        dummy[id_target]["kategori"] = kategori_baru
                                        dummy[id_target]["deskripsi"] = deskripsi_baru
                                        print("Target dummy berhasil diperbarui.")
                                input("\nTekan Enter untuk kembali...")

                            elif pilihan_dummy == "4":
                                print("\n=== HAPUS TARGET DUMMY ===")
                                for id_dummy, data in dummy.items():
                                    print(id_dummy, "-", data["nama"])
                                id_input = input(
                                    "Masukkan ID target yang ingin dihapus: "
                                ).strip()
                                if not id_input.isdigit():
                                    print("ID harus berupa angka.")

                                elif int(id_input) not in dummy:
                                    print("Target dummy tidak ditemukan.")

                                else:
                                    id_target = int(id_input)
                                    digunakan = any(
                                        data.get("id_dummy") == id_target
                                        for data in riwayat
                                    )
                                    if digunakan:
                                        print(
                                            "Target tidak dapat dihapus karena "
                                            "masih digunakan dalam riwayat tes."
                                        )
                                    else:
                                        konfirmasi = input(
                                            "Yakin ingin menghapus target ini? (ya/tidak): "
                                        ).strip().lower()
                                        if konfirmasi == "ya":
                                            del dummy[id_target]
                                            print("Target dummy berhasil dihapus.")
                                        else:
                                            print("Penghapusan dibatalkan.")
                                input("\nTekan Enter untuk kembali...")

                            elif pilihan_dummy == "5":
                                break
                            else:
                                print("Pilihan tidak valid.")
                                input("\nTekan Enter untuk kembali...")

                    elif menu_admin == "4":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("=" * 40)
                        print("          SELURUH TIM PENGGUNA")
                        print("=" * 40)
                        if len(team) == 0:
                            print("Belum ada tim yang dibuat.")
                        else:
                            for data_team in team:
                                print("\nID Tim:", data_team["id"])
                                print("Pemilik:", data_team["username"])
                                print("Nama Tim:", data_team["nama_tim"])
                                print("Anggota Karakter:")
                                for nama_karakter in data_team["karakter"]:
                                    print("-", nama_karakter)
                                print("-" * 40)
                        input("\nTekan Enter untuk kembali...")

                    elif menu_admin == "5":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("=" * 55)
                        print("              SELURUH BUILD PENGGUNA")
                        print("=" * 55)

                        if len(build) == 0:
                            print("Belum ada konfigurasi build yang dibuat.")
                        else:
                            for data_build in build:
                                print("\nID Build :", data_build["id"])
                                print("Pemilik :", data_build["username"])
                                print("Nama Build :", data_build["nama_build"])
                                print("ID Tim :", data_build["id_team"])
                                print("Nama Tim :", data_build["nama_tim"])
                                print("\nKonfigurasi Karakter:")

                                for nomor, karakter_data in enumerate(
                                    data_build["karakter_build"], start=1
                                ):
                                    print(f"\n  Karakter {nomor}: {karakter_data['karakter']}")
                                    print("Elemen  :", karakter_data["elemen"])
                                    print("Senjata :", karakter_data["senjata"])
                                    print("Artefak :", karakter_data["artefak"])
                                print("-" * 55)
                        input("\nTekan Enter untuk kembali...")

                    elif menu_admin == "6":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("=" * 55)
                        print("               SELURUH RIWAYAT TES DPS")
                        print("=" * 55)

                        if len(riwayat) == 0:
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
                                print(
                                    "Preset       :",
                                    preset_dipilih["nama"]
                                    if preset_dipilih else "Preset tidak ditemukan"
                                )
                                print(
                                    "Target Dummy :",
                                    dummy_dipilih["nama"]
                                    if dummy_dipilih else "Target dummy tidak ditemukan"
                                )
                                print("\nKONFIGURASI BUILD SAAT PENGUJIAN")
                                print("-" * 55)
                                for nomor, karakter_data in enumerate(
                                    data_tes["karakter_build"], start=1
                                ):
                                    print(f"\nKarakter {nomor}: {karakter_data['karakter']}")
                                    print("Elemen  :", karakter_data["elemen"])
                                    print("Senjata :", karakter_data["senjata"])
                                    print("Artefak :", karakter_data["artefak"])
                                print("\nHASIL PENGUJIAN")
                                print("Hasil DPS :", f'{data_tes["dps"]:,}'.replace(",", "."))
                                print("=" * 55)
                        input("\nTekan Enter untuk kembali...")

                    elif menu_admin == "7":
                        print("\n=== TAMBAH KARAKTER BARU ===")
                        nama_baru = input("Nama karakter: ").strip()
                        elemen_baru = input("Elemen karakter: ").strip().capitalize()
                        elemen_valid = {
                            "Anemo", "Geo", "Electro", "Dendro",
                            "Hydro", "Pyro", "Cryo"
                        }

                        if nama_baru == "" or elemen_baru == "":
                            print("Nama dan elemen tidak boleh kosong.")
                        elif nama_baru.lower() in (
                            nama.lower() for nama in genshin_characters
                        ):
                            print("Karakter sudah terdaftar.")
                        elif elemen_baru not in elemen_valid:
                            print("Elemen tidak valid.")
                        else:
                            genshin_characters[nama_baru] = elemen_baru
                            print("\nKarakter berhasil ditambahkan!")
                            print("Nama:", nama_baru)
                            print("Elemen:", elemen_baru)
                        input("\nTekan Enter untuk kembali...")

                    elif menu_admin == "8":
                        print("Logout berhasil.")
                        break
                    else:
                        print("Pilihan tidak valid.")
                        input("\nTekan Enter untuk kembali...")

            # MENU USER
            elif role == "User":
                while True:
                    os.system(
                        "cls" if os.name == "nt" else "clear"
                    )
                    print("=" * 40)
                    print("           MENU USER")
                    print("=" * 40)
                    print("Login sebagai:", username)
                    print("1. Lihat daftar karakter")
                    print("2. Kelola tim")
                    print("3. Kelola build karakter")
                    print("4. Catat hasil pengujian DPS")
                    print("5. Lihat riwayat pengujian")
                    print("6. Lihat preset dan target dummy")
                    print("7. Logout")
                    menu_user = input(
                        "Pilih menu: "
                    ).strip()
                   
                    if menu_user == "1":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("=" * 40)
                        print("          DAFTAR KARAKTER")
                        print("=" * 40)

                        if len(genshin_characters) == 0:
                            print("Belum ada karakter yang tersedia.")
                        else:
                            nomor = 1
                            for nama_karakter, elemen in genshin_characters.items():
                                print(f"{nomor}. {nama_karakter} - {elemen}")
                                nomor += 1
                        print("-" * 40)
                        print("Total Karakter:", len(genshin_characters))
                        input("\nTekan Enter untuk kembali...")

                    elif menu_user == "2":
                        while True:
                            os.system("cls" if os.name == "nt" else "clear")
                            print("=" * 40)
                            print("             KELOLA TIM")
                            print("=" * 40)
                            print("1. Lihat Tim Saya")
                            print("2. Buat Tim")
                            print("3. Ubah Tim")
                            print("4. Hapus Tim")
                            print("5. Kembali")
                            pilihan_tim = input("Pilih menu: ")

                            if pilihan_tim == "1":
                                os.system("cls" if os.name == "nt" else "clear")
                                tim_saya = [
                                    data_tim for data_tim in team
                                    if data_tim["username"] == username
                                ]
                                print("=" * 40)
                                print("               TIM SAYA")
                                print("=" * 40)

                                if len(tim_saya) == 0:
                                    print("Kamu belum memiliki tim.")
                                else:
                                    for data_tim in tim_saya:
                                        print("\nID Tim:", data_tim["id"])
                                        print("Nama Tim:", data_tim["nama_tim"])
                                        print("Anggota:")
                                        for nama_karakter in data_tim["karakter"]:
                                            elemen = data_tim["elemen"].get(
                                                nama_karakter,
                                                genshin_characters[nama_karakter]
                                            )
                                            if isinstance(elemen, set):
                                                print("-", nama_karakter, "-", elemen)
                                            else:
                                                print("-", nama_karakter, "-", elemen)
                                        print("-" * 40)
                                input("\nTekan Enter untuk kembali...")

                            elif pilihan_tim == "2":
                                os.system("cls" if os.name == "nt" else "clear")
                                print("=" * 40)
                                print("               BUAT TIM")
                                print("=" * 40)
                                nama_tim = input("Masukkan nama tim: ").strip()

                                if nama_tim == "":
                                    print("Nama tim tidak boleh kosong.")
                                    input("\nTekan Enter untuk kembali...")
                                    continue
                                nama_duplikat = any(
                                    data_tim["username"] == username
                                    and data_tim["nama_tim"].lower() == nama_tim.lower()
                                    for data_tim in team
                                )

                                if nama_duplikat:
                                    print("Nama tim tersebut sudah di gunakan.")
                                    input("\nTekan Enter untuk kembali...")
                                    continue
                                karakter_tim = []
                                elemen_tim = {}

                                while len(karakter_tim) < 4:
                                    print("\nAnggota saat ini:", karakter_tim)
                                    print("Ketik 'selesai' untuk menyimpan tim.")
                                    pilihan_karakter = input(
                                        "Masukkan nama karakter: "
                                    ).strip()
                                    if pilihan_karakter.lower() == "selesai":
                                        break
                                    nama_valid = None
                                    for nama_karakter in genshin_characters:
                                        if nama_karakter.lower() == pilihan_karakter.lower():
                                            nama_valid = nama_karakter
                                            break
                                    if nama_valid is None:
                                        print("Karakter tidak ditemukan.")
                                        continue
                                    if nama_valid in karakter_tim:
                                        print("Karakter tersebut sudah ada di tim.")
                                        continue
                                    elemen = genshin_characters[nama_valid]

                                    if isinstance(elemen, set):
                                        print("Pilihan elemen Traveler:")
                                        for pilihan_elemen in sorted(elemen):
                                            print("-", pilihan_elemen)
                                        elemen_pilihan = input(
                                            "Pilih elemen Traveler: "
                                        ).strip().title()
                                        elemen_valid = next(
                                            (
                                                item for item in elemen
                                                if item.lower() == elemen_pilihan.lower()
                                            ),
                                            None
                                        )
                                        if elemen_valid is None:
                                            print("Elemen Traveler tidak valid.")
                                            continue
                                        elemen_tim[nama_valid] = elemen_valid
                                    else:
                                        elemen_tim[nama_valid] = elemen

                                    karakter_tim.append(nama_valid)
                                    print("Karakter berhasil ditambahkan.")

                                if len(karakter_tim) == 0:
                                    print("Tim tidak boleh kosong.")
                                else:
                                    id_team_berikutnya = max(
                                        (data["id"] for data in team),
                                        default=0
                                    ) + 1
                                    team.append({
                                        "id": id_team_berikutnya,
                                        "username": username,
                                        "nama_tim": nama_tim,
                                        "karakter": karakter_tim,
                                        "elemen": elemen_tim
                                    })
                                    print("\nTim berhasil dibuat dengan ID:", id_team_berikutnya)
                                input("\nTekan Enter untuk kembali...")

                            elif pilihan_tim == "3":
                                os.system("cls" if os.name == "nt" else "clear")

                                tim_saya = [
                                    data_tim for data_tim in team
                                    if data_tim["username"] == username
                                ]
                                print("=" * 40)
                                print("               UBAH TIM")
                                print("=" * 40)
                                if len(tim_saya) == 0:
                                    print("Kamu belum memiliki tim.")
                                else:
                                    for data_tim in tim_saya:
                                        print(
                                            "ID:", data_tim["id"],
                                            "| Nama:", data_tim["nama_tim"],
                                            "| Anggota:", ", ".join(data_tim["karakter"])
                                        )
                                    id_pilihan = input(
                                        "\nMasukkan ID tim yang ingin diubah: "
                                    )
                                    if not id_pilihan.isdigit():
                                        print("ID tim harus berupa angka.")
                                    else:
                                        tim_dipilih = next(
                                            (
                                                data_tim for data_tim in tim_saya
                                                if data_tim["id"] == int(id_pilihan)
                                            ),
                                            None
                                        )
                                        if tim_dipilih is None:
                                            print("Tim tidak ditemukan.")
                                        else:
                                            nama_baru = input(
                                                "Nama tim baru (Enter untuk tetap): "
                                            ).strip()

                                            if nama_baru != "":
                                                nama_duplikat = any(
                                                    data_tim["id"] != tim_dipilih["id"]
                                                    and data_tim["username"] == username
                                                    and data_tim["nama_tim"].lower() == nama_baru.lower()
                                                    for data_tim in team
                                                )
                                                if nama_duplikat:
                                                    print("Nama tim tersebut sudah kamu gunakan.")
                                                else:
                                                    tim_dipilih["nama_tim"] = nama_baru
                                            print("\nAnggota saat ini:", tim_dipilih["karakter"])
                                            print("Masukkan karakter baru dipisahkan dengan koma.")
                                            print("Ketik 'tetap' untuk mempertahankan anggota.")
                                            input_karakter = input(
                                                "Anggota baru: "
                                            ).strip()

                                            if input_karakter.lower() != "tetap" and input_karakter != "":
                                                daftar_baru = [
                                                    nama.strip()
                                                    for nama in input_karakter.split(",")
                                                    if nama.strip() != ""
                                                ]
                                                karakter_valid = []
                                                elemen_baru = {}
                                                semua_valid = True

                                                for nama in daftar_baru:
                                                    nama_valid = next(
                                                        (
                                                            item for item in genshin_characters
                                                            if item.lower() == nama.lower()
                                                        ),
                                                        None
                                                    )
                                                    if nama_valid is None:
                                                        print("Karakter tidak ditemukan:", nama)
                                                        semua_valid = False
                                                        break
                                                    if nama_valid in karakter_valid:
                                                        print("Karakter duplikat:", nama_valid)
                                                        semua_valid = False
                                                        break
                                                    elemen = genshin_characters[nama_valid]
                                                    if isinstance(elemen, set):
                                                        print("Pilihan elemen Traveler:")
                                                        for pilihan_elemen in sorted(elemen):
                                                            print("-", pilihan_elemen)
                                                        pilihan_elemen = input(
                                                            "Pilih elemen Traveler: "
                                                        ).strip()
                                                        elemen_valid = next(
                                                            (
                                                                item for item in elemen
                                                                if item.lower() == pilihan_elemen.lower()
                                                            ),
                                                            None
                                                        )
                                                        if elemen_valid is None:
                                                            print("Elemen Traveler tidak valid.")
                                                            semua_valid = False
                                                            break
                                                        elemen_baru[nama_valid] = elemen_valid
                                                    else:
                                                        elemen_baru[nama_valid] = elemen
                                                    karakter_valid.append(nama_valid)

                                                if semua_valid and len(karakter_valid) > 0:
                                                    if len(karakter_valid) > 4:
                                                        print("Tim maksimal terdiri dari 4 karakter.")
                                                    else:
                                                        tim_dipakai = (
                                                            any(
                                                                data_build["id_tim"] == tim_dipilih["id"]
                                                                for data_build in build
                                                            )
                                                            or any(
                                                                data_tes["id_tim"] == tim_dipilih["id"]
                                                                for data_tes in riwayat
                                                            )
                                                        )
                                                        if tim_dipakai:
                                                            print(
                                                                "Anggota tim tidak dapat diubah "
                                                                "karena sudah digunakan pada build "
                                                                "atau riwayat tes."
                                                            )
                                                        else:
                                                            tim_dipilih["karakter"] = karakter_valid
                                                            tim_dipilih["elemen"] = elemen_baru

                                                            print("Anggota tim berhasil diperbarui.")
                                                else:
                                                    print("Perubahan anggota dibatalkan.")
                                            print("\nProses perubahan tim selesai.")
                                input("\nTekan Enter untuk kembali...")

                            elif pilihan_tim == "4":
                                os.system("cls" if os.name == "nt" else "clear")
                                tim_saya = [
                                    data_tim for data_tim in team
                                    if data_tim["username"] == username
                                ]
                                print("=" * 40)
                                print("              HAPUS TIM")
                                print("=" * 40)
                                if len(tim_saya) == 0:
                                    print("Kamu belum memiliki tim.")
                                else:
                                    for data_tim in tim_saya:
                                        print(
                                            "ID:", data_tim["id"],
                                            "| Nama:", data_tim["nama_tim"]
                                        )
                                    id_pilihan = input(
                                        "\nMasukkan ID tim yang ingin dihapus: "
                                    )
                                    if not id_pilihan.isdigit():
                                        print("ID tim harus berupa angka.")
                                    else:
                                        tim_dipilih = next(
                                            (
                                                data_tim for data_tim in tim_saya
                                                if data_tim["id"] == int(id_pilihan)
                                            ),
                                            None
                                        )
                                        if tim_dipilih is None:
                                            print("Tim tidak ditemukan.")
                                        else:
                                            dipakai_build = any(
                                                data_build["id_tim"] == tim_dipilih["id"]
                                                for data_build in build
                                            )
                                            dipakai_riwayat = any(
                                                data_tes["id_tim"] == tim_dipilih["id"]
                                                for data_tes in riwayat
                                            )
                                            if dipakai_build or dipakai_riwayat:
                                                print(
                                                    "Tim tidak dapat dihapus karena sudah "
                                                    "digunakan pada build atau riwayat tes."
                                                )
                                            else:
                                                konfirmasi = input(
                                                    "Yakin ingin menghapus tim ini? (ya/tidak): "
                                                ).strip().lower()
                                                if konfirmasi == "ya":
                                                    team.remove(tim_dipilih)
                                                    print("Tim berhasil dihapus.")
                                                else:
                                                    print("Penghapusan dibatalkan.")
                                input("\nTekan Enter untuk kembali...")
                            elif pilihan_tim == "5":
                                break
                            else:
                                print("Pilihan tidak valid.")
                                input("\nTekan Enter untuk mencoba lagi...")

                    elif menu_user == "3":
                        while True:
                            os.system("cls" if os.name == "nt" else "clear")
                            print("=" * 45)
                            print("           KELOLA BUILD KARAKTER")
                            print("=" * 45)
                            print("1. Lihat konfigurasi build")
                            print("2. Buat konfigurasi build")
                            print("3. Edit konfigurasi build")
                            print("4. Hapus konfigurasi build")
                            print("5. Kembali")
                            pilihan_build = input("Pilih menu: ").strip()
                            build_saya = [
                                b for b in build
                                if b["username"] == username
                            ]

                            if pilihan_build == "1":
                                os.system("cls" if os.name == "nt" else "clear")
                                print("=" * 45)
                                print("          DAFTAR KONFIGURASI BUILD")
                                print("=" * 45)

                                if not build_saya:
                                    print("Kamu belum memiliki konfigurasi build.")
                                else:
                                    for data in build_saya:
                                        print("\nID Build   :", data["id"])
                                        print("Nama Build :", data["nama_build"])
                                        print("Nama Tim   :", data["nama_tim"])
                                        for nomor, karakter_data in enumerate(
                                            data["karakter_build"], start=1
                                        ):
                                            print(f"\n  Karakter {nomor}: {karakter_data['karakter']}")
                                            print("  Elemen   :", karakter_data["elemen"])
                                            print("  Senjata  :", karakter_data["senjata"])
                                            print("  Artefak  :", karakter_data["artefak"])
                                        print("-" * 45)
                                input("\nTekan Enter untuk kembali...")

                            elif pilihan_build == "2":
                                os.system("cls" if os.name == "nt" else "clear")
                                team_saya = [
                                    t for t in team
                                    if t["username"] == username
                                ]

                                if not team_saya:
                                    print("Kamu belum memiliki tim.")
                                    input("Tekan Enter untuk kembali...")
                                    continue
                                print("=" * 45)
                                print("          PILIH TIM")
                                print("=" * 45)

                                for data in team_saya:
                                    print(f'ID: {data["id"]} | Nama Tim: {data["nama_tim"]}')
                                    print("Karakter:", ", ".join(data["karakter"]))
                                    print("-" * 45)
                                id_tim_input = input("Masukkan ID tim: ").strip()

                                if not id_tim_input.isdigit():
                                    print("ID tim harus berupa angka.")
                                    input("Tekan Enter untuk kembali...")
                                    continue
                                team_dipilih = next(
                                    (
                                        t for t in team_saya
                                        if t["id"] == int(id_tim_input)
                                    ),
                                    None
                                )

                                if team_dipilih is None:
                                    print("Tim tidak ditemukan.")
                                    input("Tekan Enter untuk kembali...")
                                    continue
                                nama_build = input("Masukkan nama konfigurasi build: ").strip()

                                if not nama_build:
                                    print("Nama konfigurasi tidak boleh kosong.")
                                    input("Tekan Enter untuk kembali...")
                                    continue
                                karakter_build = []
                                print("\nMasukkan build setiap karakter dalam tim.")
                                print("Isi senjata dan artefak untuk keempat karakter.\n")

                                for nomor, nama_karakter in enumerate(
                                    team_dipilih["karakter"], start=1
                                ):
                                    print(f"\nKarakter {nomor}: {nama_karakter}")
                                    elemen = team_dipilih["elemen"][nama_karakter]
                                    senjata = input("Nama senjata: ").strip()
                                    artefak = input("Nama artefak: ").strip()

                                    if not senjata or not artefak:
                                        print("Senjata dan artefak tidak boleh kosong.")
                                        karakter_build = []
                                        break
                                    karakter_build.append({
                                        "karakter": nama_karakter,
                                        "elemen": elemen,
                                        "senjata": senjata,
                                        "artefak": artefak
                                    })
                                if len(karakter_build) != 4:
                                    print("Konfigurasi build tidak disimpan.")
                                    input("Tekan Enter untuk kembali...")
                                    continue

                                id_build_berikutnya = max(
                                    (data["id"] for data in build),
                                    default=0
                                ) + 1
                                build.append({
                                    "id": id_build_berikutnya,
                                    "username": username,
                                    "nama_build": nama_build,
                                    "id_team": team_dipilih["id"],
                                    "nama_tim": team_dipilih["nama_tim"],
                                    "karakter_build": karakter_build
                                })
                                print("\nKonfigurasi build berhasil disimpan.")
                                print("ID Build:", id_build_berikutnya)


                            elif pilihan_build == "3":
                                os.system("cls" if os.name == "nt" else "clear")
                                if not build_saya:
                                    print("Kamu belum memiliki konfigurasi build.")
                                    input("Tekan Enter untuk kembali...")
                                    continue
                                print("=" * 45)
                                print("          EDIT KONFIGURASI BUILD")
                                print("=" * 45)

                                for data in build_saya:
                                    print(
                                        f'ID: {data["id"]} | '
                                        f'Build: {data["nama_build"]} | '
                                        f'Tim: {data["nama_tim"]}'
                                    )
                                id_build_input = input("Masukkan ID build: ").strip()

                                if not id_build_input.isdigit():
                                    print("ID build harus berupa angka.")
                                    input("Tekan Enter untuk kembali...")
                                    continue
                                build_dipilih = next(
                                    (
                                        b for b in build_saya
                                        if b["id"] == int(id_build_input)
                                    ),
                                    None
                                )

                                if build_dipilih is None:
                                    print("Build tidak ditemukan.")
                                    input("Tekan Enter untuk kembali...")
                                    continue
                                print("\n1. Ubah nama konfigurasi")
                                print("2. Ubah build satu karakter")
                                pilihan_edit = input("Pilih menu: ").strip()

                                if pilihan_edit == "1":
                                    nama_baru = input("Nama konfigurasi baru: ").strip()
                                    if nama_baru:
                                        build_dipilih["nama_build"] = nama_baru
                                        print("Nama konfigurasi berhasil diubah.")
                                    else:
                                        print("Nama konfigurasi tidak boleh kosong.")

                                elif pilihan_edit == "2":
                                    for nomor, karakter_data in enumerate(
                                        build_dipilih["karakter_build"], start=1
                                    ):
                                        print(
                                            f'{nomor}. {karakter_data["karakter"]} | '
                                            f'Senjata: {karakter_data["senjata"]} | '
                                            f'Artefak: {karakter_data["artefak"]}'
                                        )

                                    nomor_input = input(
                                        "Pilih nomor karakter yang ingin diedit: "
                                    ).strip()
                                    if not nomor_input.isdigit():
                                        print("Pilihan harus berupa angka.")
                                    elif not 1 <= int(nomor_input) <= 4:
                                        print("Nomor karakter tidak valid.")
                                    else:
                                        karakter_data = build_dipilih["karakter_build"][
                                            int(nomor_input) - 1
                                        ]

                                        print("Karakter:", karakter_data["karakter"])
                                        senjata_baru = input(
                                            "Nama senjata baru: "
                                        ).strip()
                                        artefak_baru = input(
                                            "Nama artefak baru: "
                                        ).strip()

                                        if senjata_baru and artefak_baru:
                                            karakter_data["senjata"] = senjata_baru
                                            karakter_data["artefak"] = artefak_baru
                                            print("Build karakter berhasil diperbarui.")
                                        else:
                                            print("Senjata dan artefak tidak boleh kosong.")
                                else:
                                    print("Pilihan tidak valid.")
                                input("\nTekan Enter untuk kembali...")

                            elif pilihan_build == "4":
                                os.system("cls" if os.name == "nt" else "clear")
                                if not build_saya:
                                    print("Kamu belum memiliki konfigurasi build.")
                                    input("Tekan Enter untuk kembali...")
                                    continue
                                print("=" * 45)
                                print("         HAPUS KONFIGURASI BUILD")
                                print("=" * 45)

                                for data in build_saya:
                                    print(
                                        f'ID: {data["id"]} | '
                                        f'{data["nama_build"]} | '
                                        f'Tim: {data["nama_tim"]}'
                                    )
                                id_build_input = input("Masukkan ID build: ").strip()

                                if not id_build_input.isdigit():
                                    print("ID build harus berupa angka.")
                                    input("Tekan Enter untuk kembali...")
                                    continue
                                build_dipilih = next(
                                    (
                                        b for b in build_saya
                                        if b["id"] == int(id_build_input)
                                    ),
                                    None
                                )

                                if build_dipilih is None:
                                    print("Build tidak ditemukan.")
                                    input("Tekan Enter untuk kembali...")
                                    continue
                                sudah_diuji = any(
                                    r["id_build"] == build_dipilih["id"]
                                    for r in riwayat
                                )

                                if sudah_diuji:
                                    print(
                                        "Build tidak dapat dihapus karena sudah "
                                        "digunakan dalam riwayat pengujian."
                                    )
                                else:
                                    konfirmasi = input(
                                        f'Hapus konfigurasi "{build_dipilih["nama_build"]}"? (ya/tidak): '
                                    ).strip().lower()

                                    if konfirmasi == "ya":
                                        build.remove(build_dipilih)
                                        print("Konfigurasi build berhasil dihapus.")
                                    else:
                                        print("Penghapusan dibatalkan.")
                                input("Tekan Enter untuk kembali...")

                            elif pilihan_build == "5":
                                break
                            else:
                                print("Pilihan tidak valid.")
                                input("Tekan Enter untuk kembali...")

                    elif menu_user == "4":
                        while True:
                            os.system("cls" if os.name == "nt" else "clear")
                            print("=" * 45)
                            print("          CATAT HASIL PENGUJIAN DPS")
                            print("=" * 45)
                            print("1. Catat tes baru")
                            print("2. Kembali")
                            pilihan_tes = input("Pilih menu: ").strip()

                            if pilihan_tes == "1":
                                os.system("cls" if os.name == "nt" else "clear")
                                build_saya = [
                                    b for b in build
                                    if b["username"] == username
                                ]

                                if not build_saya:
                                    print("Kamu belum memiliki konfigurasi build.")
                                    print("Buat konfigurasi terlebih dahulu di menu nomor 3.")
                                    input("\nTekan Enter untuk kembali...")
                                    continue
                                print("=" * 45)
                                print("       PILIH KONFIGURASI BUILD TIM")
                                print("=" * 45)

                                for data in build_saya:
                                    print(f'\nID Build   : {data["id"]}')
                                    print(f'Nama Build : {data["nama_build"]}')
                                    print(f'Nama Tim   : {data["nama_tim"]}')

                                    for nomor, karakter_data in enumerate(
                                        data["karakter_build"], start=1
                                    ):
                                        print(
                                            f'{nomor}. {karakter_data["karakter"]} | '
                                            f'Senjata: {karakter_data["senjata"]} | '
                                            f'Artefak: {karakter_data["artefak"]}'
                                        )
                                    print("-" * 45)
                                id_build_input = input(
                                    "\nMasukkan ID konfigurasi build yang diuji: "
                                ).strip()

                                if not id_build_input.isdigit():
                                    print("ID build harus berupa angka.")
                                    input("Tekan Enter untuk kembali...")
                                    continue
                                build_dipilih = next(
                                    (
                                        b for b in build_saya
                                        if b["id"] == int(id_build_input)
                                    ),
                                    None
                                )

                                if build_dipilih is None:
                                    print("Konfigurasi build tidak ditemukan.")
                                    input("Tekan Enter untuk kembali...")
                                    continue
                                print("\n" + "=" * 45)
                                print("           PILIH PRESET TES")
                                print("=" * 45)

                                for id_preset, data in preset.items():
                                    print(f'\nID Preset : {id_preset}')
                                    print(f'Nama      : {data["nama"]}')
                                    print(f'Deskripsi : {data["deskripsi"]}')
                                id_preset_input = input(
                                    "\nMasukkan ID preset: "
                                ).strip()

                                if not id_preset_input.isdigit():
                                    print("ID preset harus berupa angka.")
                                    input("Tekan Enter untuk kembali...")
                                    continue
                                id_preset = int(id_preset_input)

                                if id_preset not in preset:
                                    print("Preset tidak ditemukan.")
                                    input("Tekan Enter untuk kembali...")
                                    continue
                                print("\n" + "=" * 45)
                                print("          PILIH TARGET DUMMY")
                                print("=" * 45)

                                for id_dummy, data in dummy.items():
                                    print(f'\nID Dummy  : {id_dummy}')
                                    print(f'Nama      : {data["nama"]}')
                                    print(f'Kategori  : {data["kategori"]}')
                                    print(f'Deskripsi : {data["deskripsi"]}')
                                id_dummy_input = input(
                                    "\nMasukkan ID target dummy: "
                                ).strip()

                                if not id_dummy_input.isdigit():
                                    print("ID dummy harus berupa angka.")
                                    input("Tekan Enter untuk kembali...")
                                    continue
                                id_dummy = int(id_dummy_input)

                                if id_dummy not in dummy:
                                    print("Target dummy tidak ditemukan.")
                                    input("Tekan Enter untuk kembali...")
                                    continue
                                print("\n" + "=" * 45)
                                print("          KONFIRMASI PENGUJIAN")
                                print("=" * 45)
                                print("Nama Tim   :", build_dipilih["nama_tim"])
                                print("Nama Build :", build_dipilih["nama_build"])
                                print("Preset     :", preset[id_preset]["nama"])
                                print("Target     :", dummy[id_dummy]["nama"])
                                print("\nKarakter yang akan diuji:")

                                for nomor, karakter_data in enumerate(
                                    build_dipilih["karakter_build"], start=1
                                ):
                                    print(
                                        f'{nomor}. {karakter_data["karakter"]} | '
                                        f'Senjata: {karakter_data["senjata"]} | '
                                        f'Artefak: {karakter_data["artefak"]}'
                                    )

                                konfirmasi = input(
                                    "\nApakah pengujian sudah dilakukan? (ya/tidak): "
                                ).strip().lower()

                                if konfirmasi != "ya":
                                    print("Pencatatan pengujian dibatalkan.")
                                    input("Tekan Enter untuk kembali...")
                                    continue
                                hasil_dps = input(
                                    "\nMasukkan hasil DPS dari game: "
                                ).strip()

                                if not hasil_dps.isdigit():
                                    print("Hasil DPS harus berupa angka bulat.")
                                    input("Tekan Enter untuk kembali...")
                                    continue
                                hasil_dps = int(hasil_dps)

                                if hasil_dps <= 0:
                                    print("Hasil DPS harus lebih besar dari 0.")
                                    input("Tekan Enter untuk kembali...")
                                    continue

                                riwayat.append({
                                    "id": id_tes_berikutnya,
                                    "username": username,
                                    "id_team": build_dipilih["id_team"],
                                    "id_build": build_dipilih["id"],
                                    "nama_tim": build_dipilih["nama_tim"],
                                    "nama_build": build_dipilih["nama_build"],
                                    "karakter_build": [
                                        dict(data)
                                        for data in build_dipilih["karakter_build"]
                                    ],
                                    "id_preset": id_preset,
                                    "id_dummy": id_dummy,
                                    "dps": hasil_dps
                                })
                                print("\nPengujian DPS berhasil dicatat.")
                                print("ID Tes     :", id_tes_berikutnya)
                                print("Nama Tim   :", build_dipilih["nama_tim"])
                                print("Nama Build :", build_dipilih["nama_build"])
                                print("Hasil DPS  :", f"{hasil_dps:,}".replace(",", "."))
                                id_tes_berikutnya += 1
                                input("\nTekan Enter untuk kembali...")

                            elif pilihan_tes == "2":
                                break
                            else:
                                print("Pilihan tidak valid.")
                                input("Tekan Enter untuk kembali...")

                    elif menu_user == "5":
                        while True:
                            os.system("cls" if os.name == "nt" else "clear")
                            print("=" * 55)
                            print("                 RIWAYAT PENGUJIAN DPS")
                            print("=" * 55)
                            print("1. Lihat seluruh riwayat")
                            print("2. Lihat detail riwayat")
                            print("3. Kembali")
                            pilihan_riwayat = input("Pilih menu: ").strip()
                            riwayat_saya = [
                                data for data in riwayat
                                if data["username"] == username
                            ]

                            if pilihan_riwayat == "1":
                                os.system("cls" if os.name == "nt" else "clear")
                                print("=" * 55)
                                print("                 DAFTAR RIWAYAT DPS")
                                print("=" * 55)

                                if not riwayat_saya:
                                    print("Kamu belum memiliki riwayat pengujian DPS.")
                                else:
                                    for data in riwayat_saya:
                                        preset_dipilih = preset.get(data["id_preset"])
                                        dummy_dipilih = dummy.get(data["id_dummy"])

                                        print(f'\nID Tes       : {data["id"]}')
                                        print(f'Nama Tim     : {data["nama_tim"]}')
                                        print(f'Nama Build   : {data["nama_build"]}')
                                        print(
                                            "Preset       :",
                                            preset_dipilih["nama"]
                                            if preset_dipilih else "Preset tidak ditemukan"
                                        )
                                        print(
                                            "Target Dummy :",
                                            dummy_dipilih["nama"]
                                            if dummy_dipilih else "Dummy tidak ditemukan"
                                        )
                                        print(
                                            "Hasil DPS    :",
                                            f'{data["dps"]:,}'.replace(",", ".")
                                        )
                                        print("-" * 55)
                                input("\nTekan Enter untuk kembali...")

                            elif pilihan_riwayat == "2":
                                os.system("cls" if os.name == "nt" else "clear")
                                print("=" * 55)
                                print("                 DETAIL RIWAYAT DPS")
                                print("=" * 55)

                                if not riwayat_saya:
                                    print("Kamu belum memiliki riwayat pengujian DPS.")
                                    input("\nTekan Enter untuk kembali...")
                                    continue
                                for data in riwayat_saya:
                                    print(
                                        f'ID Tes: {data["id"]} | '
                                        f'{data["nama_tim"]} | '
                                        f'{data["nama_build"]} | '
                                        f'DPS: {data["dps"]:,}'.replace(",", ".")
                                    )
                                id_tes_input = input(
                                    "\nMasukkan ID tes yang ingin dilihat: "
                                ).strip()

                                if not id_tes_input.isdigit():
                                    print("ID tes harus berupa angka.")
                                    input("Tekan Enter untuk kembali...")
                                    continue
                                tes_dipilih = next(
                                    (
                                        data for data in riwayat_saya
                                        if data["id"] == int(id_tes_input)
                                    ),
                                    None
                                )

                                if tes_dipilih is None:
                                    print("Riwayat pengujian tidak ditemukan.")
                                    input("Tekan Enter untuk kembali...")
                                    continue
                                os.system("cls" if os.name == "nt" else "clear")
                                preset_dipilih = preset.get(tes_dipilih["id_preset"])
                                dummy_dipilih = dummy.get(tes_dipilih["id_dummy"])

                                print("=" * 55)
                                print("                 DETAIL PENGUJIAN DPS")
                                print("=" * 55)
                                print("ID Tes       :", tes_dipilih["id"])
                                print("Nama Tim     :", tes_dipilih["nama_tim"])
                                print("Nama Build   :", tes_dipilih["nama_build"])
                                print(
                                    "Preset       :",
                                    preset_dipilih["nama"]
                                    if preset_dipilih else "Preset tidak ditemukan"
                                )

                                if preset_dipilih:
                                    print("Deskripsi    :", preset_dipilih["deskripsi"])
                                print(
                                    "Target Dummy :",
                                    dummy_dipilih["nama"]
                                    if dummy_dipilih else "Dummy tidak ditemukan"
                                )

                                if dummy_dipilih:
                                    print("Kategori     :", dummy_dipilih["kategori"])
                                    print("Deskripsi    :", dummy_dipilih["deskripsi"])
                                print("\nKONFIGURASI BUILD SAAT PENGUJIAN")
                                print("-" * 55)
                                for nomor, karakter_data in enumerate(
                                    tes_dipilih["karakter_build"], start=1
                                ):
                                    print(f'\nKarakter {nomor}: {karakter_data["karakter"]}')
                                    print("Elemen   :", karakter_data["elemen"])
                                    print("Senjata  :", karakter_data["senjata"])
                                    print("Artefak  :", karakter_data["artefak"])
                                print("\n" + "=" * 55)
                                print(
                                    "HASIL DPS:",
                                    f'{tes_dipilih["dps"]:,}'.replace(",", ".")
                                )
                                print("=" * 55)
                                input("\nTekan Enter untuk kembali...")

                            elif pilihan_riwayat == "3":
                                break
                            else:
                                print("Pilihan tidak valid.")
                                input("Tekan Enter untuk melanjutkan...")
 
                    elif menu_user == "6":
                        while True:
                            os.system("cls" if os.name == "nt" else "clear")
                            print("=" * 55)
                            print("             PRESET PENGUJIAN DPS")
                            print("=" * 55)

                            if not preset:
                                print("Belum ada preset pengujian.")
                            else:
                                for id_preset, data in preset.items():
                                    print(f"\nID Preset  : {id_preset}")
                                    print(f"Nama       : {data['nama']}")
                                    print(f"Deskripsi  : {data['deskripsi']}")
                                    print("-" * 55)
                            print("\n" + "=" * 55)
                            print("                TARGET DUMMY")
                            print("=" * 55)

                            if not dummy:
                                print("Belum ada target dummy.")
                            else:
                                for id_dummy, data in dummy.items():
                                    print(f"\nID Dummy   : {id_dummy}")
                                    print(f"Nama       : {data['nama']}")
                                    print(f"Kategori   : {data['kategori']}")
                                    print(f"Deskripsi  : {data['deskripsi']}")
                                    print("-" * 55)
                            print("\n1. Kembali")
                            pilihan_preset = input("Pilih menu: ").strip()

                            if pilihan_preset == "1":
                                break
                            else:
                                print("Pilihan tidak valid.")
                                input("Tekan Enter untuk mencoba kembali...")

                    elif menu_user == "7":
                        print("Logout berhasil.")
                        break

                    else:
                        print("Pilihan tidak valid.")
                        input("\nTekan Enter untuk kembali...")

        else:
            print("\nUsername atau password salah.")
            input("Tekan Enter untuk kembali...")
    elif pilihan == "3":
        print("\nTerima kasih telah menggunakan DPS Tracker!")
        break
    else:
        print("Pilihan tidak valid.")
        input("Tekan Enter untuk kembali...")