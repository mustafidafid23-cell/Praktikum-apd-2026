from data import akun, genshin_characters, preset, dummy, kategori_dummy, team, build, riwayat, elemen_karakter_valid
from func import *

# ADMIN - KELOLA AKUN
def lihat_semua_akun():
    print("\n=== DAFTAR AKUN ===")
    tabel = PrettyTable()
    tabel.field_names = ["No", "Username", "Role"]
    tabel.align["No"] = "c"
    tabel.align["Username"] = "L"
    tabel.align["Role"] = "c"
    for nomor, (nama_akun, data_akun) in enumerate(akun.items(), start=1):
        tabel.add_row([nomor, nama_akun, data_akun["role"]])
    print(tabel)
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
        tabel = buat_tabel_preset()
        for id_item, data_preset in preset.items():
            tabel.add_row([id_item, data_preset["nama"], data_preset["deskripsi"]])
        print(tabel)
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
        tabel = buat_tabel_dummy()
        for id_item, data_dummy in dummy.items():
            tabel.add_row([id_item, data_dummy["nama"], data_dummy["kategori"], data_dummy["deskripsi"]])
        print(tabel)
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
            print("\nID Build   :", data_build["id"])
            print("Pemilik    :", data_build["username"])
            print("Nama Build :", data_build["nama_build"])
            print("ID Tim     :", data_build["id_team"])
            print("Nama Tim   :", data_build["nama_tim"])
            print("Konfigurasi Karakter:")

            tabel_karakter = PrettyTable()
            tabel_karakter.field_names = ["No", "Karakter", "Elemen", "Senjata", "Artefak"]
            tabel_karakter.align = "l"
            tabel_karakter.align["No"] = "c"

            for nomor, data_karakter in enumerate(data_build["karakter_build"], start=1):
                tabel_karakter.add_row([
                    nomor,
                    data_karakter["karakter"],
                    data_karakter["elemen"],
                    data_karakter["senjata"],
                    data_karakter["artefak"]
                ])

            print(tabel_karakter)
            print(strip_55)
    jeda()

def lihat_seluruh_riwayat():
    bersihkan_layar()
    cetak_header("               SELURUH RIWAYAT TES DPS", garis_55)
    if not riwayat:
        print("Belum ada riwayat pengujian DPS.")
    else:
        tabel_riwayat = PrettyTable()
        tabel_riwayat.field_names = [
            "ID",
            "Info Pengujian",
            "Konfigurasi Build (Elemen | Senjata | Artefak)",
            "Hasil DPS"
        ]
        tabel_riwayat.align = "l"
        tabel_riwayat.align["ID"] = "c"
        tabel_riwayat.align["Hasil DPS"] = "r"
        tabel_riwayat.hrules = ALL

        for data_tes in riwayat:
            preset_dipilih = preset.get(data_tes["id_preset"])
            dummy_dipilih = dummy.get(data_tes["id_dummy"])
            waktu_tes = data_tes.get("waktu", "Tidak diketahui")
            nama_preset = preset_dipilih["nama"] if preset_dipilih else "Preset tidak ditemukan"
            nama_dummy = dummy_dipilih["nama"] if dummy_dipilih else "Target dummy tidak ditemukan"

            info_tes = (
                f"Waktu   : {waktu_tes}\n"
                f"Pemilik : {data_tes['username']}\n"
                f"Tim     : {data_tes['nama_tim']} (ID: {data_tes['id_team']})\n"
                f"Build   : {data_tes['nama_build']} (ID: {data_tes['id_build']})\n"
                f"Preset  : {nama_preset}\n"
                f"Target  : {nama_dummy}"
            )

            baris_karakter = []
            for nomor, dk in enumerate(data_tes["karakter_build"], start=1):
                baris_karakter.append(
                    f"{nomor}. {dk['karakter']} ({dk['elemen']} | {dk['senjata']} | {dk['artefak']})"
                )

            tabel_riwayat.add_row([
                data_tes["id"],
                info_tes,
                "\n".join(baris_karakter),
                format_ribuan(data_tes["dps"])
            ])
        print(tabel_riwayat)
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
        print("7. Tambah Karakter")
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