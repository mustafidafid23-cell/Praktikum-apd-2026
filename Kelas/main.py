"""
Genshin DPS Tracker
-------------------
Aplikasi PENCATATAN saja. Pengujian dilakukan langsung di dalam game,
lalu hasilnya diinput manual oleh User. Aplikasi ini TIDAK menjalankan
simulasi, TIDAK menghitung DPS, dan TIDAK mengambil data dari game.

Role:
  - Admin : kelola akun User, Test Preset, Target Dummy
  - User  : kelola Tim, Build Karakter, Log Hasil Tes

Akun Admin default (ganti password setelah login pertama!):
  username: admin   password: admin123

Jalankan:  python genshin_dps_tracker.py
"""

import getpass
import hashlib
import hmac
import os
import sqlite3
from datetime import datetime

DB_FILE = "genshin_dps_tracker.db"
CATEGORIES = ["Standard", "Boss", "Multi-target"]
MAX_TEAM_SIZE = 4

# ---------------------------------------------------------------------------
# Data awal (seed)
# ---------------------------------------------------------------------------
SEED_CHARACTERS = [
    ("Flins", "Electro"), ("Columbina", "Hydro"), ("Nahida", "Dendro"),
    ("Raiden Shogun", "Electro"), ("Xiangling", "Pyro"), ("Bennett", "Pyro"),
    ("Xingqiu", "Hydro"), ("Furina", "Hydro"), ("Zhongli", "Geo"),
    ("Kazuha", "Anemo"), ("Hu Tao", "Pyro"), ("Yelan", "Hydro"),
    ("Ayaka", "Cryo"), ("Mona", "Hydro"), ("Fischl", "Electro"),
    ("Ganyu", "Cryo"), ("Alhaitham", "Dendro"), ("Neuvillette", "Hydro"),
]
SEED_PRESETS = [
    ("Abyss Floor 12", "Kondisi Spiral Abyss lantai 12, dua ruangan berurutan."),
    ("Stygian Onslaught", "Mode Stygian Onslaught dengan buff/debuff sesuai versi."),
]
SEED_DUMMIES = [
    ("Training Dummy", "Standard", "Target tunggal tanpa mekanik khusus."),
    ("Boss Mingguan", "Boss", "Boss immune to freeze, ada fase invulnerable."),
    ("Kelompok Hilichurl", "Multi-target", "Multi-target for AoE."),
]

# ---------------------------------------------------------------------------
# Database
# ---------------------------------------------------------------------------
db = sqlite3.connect(DB_FILE)
db.row_factory = sqlite3.Row
db.execute("PRAGMA foreign_keys = ON")


def hash_password(password, salt=None):
    salt = salt or os.urandom(16).hex()
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 100_000).hex()
    return f"{salt}${digest}"


def verify_password(password, stored):
    salt, _ = stored.split("$")
    return hmac.compare_digest(hash_password(password, salt), stored)


def init_db():
    db.executescript("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL CHECK (role IN ('admin','user')),
        created_at TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS characters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        element TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS test_presets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        description TEXT NOT NULL DEFAULT ''
    );
    CREATE TABLE IF NOT EXISTS target_dummies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        category TEXT NOT NULL,
        description TEXT NOT NULL DEFAULT ''
    );
    CREATE TABLE IF NOT EXISTS teams (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        name TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS team_members (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        team_id INTEGER NOT NULL REFERENCES teams(id) ON DELETE CASCADE,
        character_id INTEGER NOT NULL REFERENCES characters(id),
        weapon TEXT NOT NULL DEFAULT '',
        artifact TEXT NOT NULL DEFAULT ''
    );
    CREATE TABLE IF NOT EXISTS test_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        team_id INTEGER NOT NULL REFERENCES teams(id) ON DELETE CASCADE,
        preset_id INTEGER REFERENCES test_presets(id) ON DELETE SET NULL,
        dummy_id INTEGER REFERENCES target_dummies(id) ON DELETE SET NULL,
        total_time REAL NOT NULL,
        total_damage INTEGER NOT NULL,
        strongest_hit INTEGER NOT NULL,
        notes TEXT NOT NULL DEFAULT '',
        created_at TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS log_distribution (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        log_id INTEGER NOT NULL REFERENCES test_logs(id) ON DELETE CASCADE,
        character_id INTEGER NOT NULL REFERENCES characters(id),
        percent REAL NOT NULL
    );
    """)
    if not db.execute("SELECT 1 FROM users WHERE role='admin'").fetchone():
        db.execute("INSERT INTO users (username, password, role, created_at) VALUES (?,?,?,?)",
                   ("admin", hash_password("admin123"), "admin", now()))
    if not db.execute("SELECT 1 FROM characters").fetchone():
        db.executemany("INSERT INTO characters (name, element) VALUES (?,?)", SEED_CHARACTERS)
    if not db.execute("SELECT 1 FROM test_presets").fetchone():
        db.executemany("INSERT INTO test_presets (name, description) VALUES (?,?)", SEED_PRESETS)
    if not db.execute("SELECT 1 FROM target_dummies").fetchone():
        db.executemany("INSERT INTO target_dummies (name, category, description) VALUES (?,?,?)",
                       SEED_DUMMIES)
    db.commit()


# ---------------------------------------------------------------------------
# Helper input / tampilan
# ---------------------------------------------------------------------------
def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def fmt(n):
    """Format angka dengan pemisah titik: 1500000 -> 1.500.000"""
    return f"{int(n):,}".replace(",", ".")


def ask(prompt, default=None, required=True):
    suffix = f" [{default}]" if default not in (None, "") else ""
    while True:
        val = input(f"{prompt}{suffix}: ").strip()
        if val:
            return val
        if default is not None:
            return str(default)
        if not required:
            return ""
        print("  ! Tidak boleh kosong.")


def ask_int(prompt, default=None, minimum=0):
    while True:
        raw = ask(prompt, default)
        try:
            val = int(raw.replace(".", "").replace(",", "").replace("_", "").replace(" ", ""))
            if val < minimum:
                raise ValueError
            return val
        except ValueError:
            print(f"  ! Masukkan bilangan bulat >= {minimum}.")


def ask_float(prompt, default=None, minimum=0.0, maximum=None):
    while True:
        raw = ask(prompt, default)
        try:
            val = float(raw.replace(",", "."))
            if val < minimum or (maximum is not None and val > maximum):
                raise ValueError
            return val
        except ValueError:
            rng = f"{minimum}-{maximum}" if maximum is not None else f">= {minimum}"
            print(f"  ! Masukkan angka ({rng}).")


def confirm(prompt):
    return input(f"{prompt} (y/n): ").strip().lower() == "y"


def pause():
    input("\nTekan Enter untuk lanjut...")


def header(title):
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)


def menu(title, options):
    """Tampilkan menu, kembalikan nomor pilihan (0 = kembali/keluar)."""
    header(title)
    for i, label in enumerate(options, 1):
        print(f" {i}. {label}")
    print(" 0. Kembali / Keluar")
    while True:
        raw = input("Pilih: ").strip()
        if raw.isdigit() and 0 <= int(raw) <= len(options):
            return int(raw)
        print("  ! Pilihan tidak valid.")


def ask_id(prompt, valid_ids, allow_blank=False):
    while True:
        raw = input(f"{prompt}: ").strip()
        if allow_blank and raw == "":
            return None
        if raw.isdigit() and int(raw) in valid_ids:
            return int(raw)
        print("  ! ID tidak valid.")


def print_rows(rows, columns):
    """columns = [(judul, key_atau_fungsi, lebar)]"""
    if not rows:
        print("  (Belum ada data)")
        return
    print(" ".join(f"{t:<{w}}" for t, _, w in columns))
    print("-" * (sum(w for _, _, w in columns) + len(columns)))
    for r in rows:
        cells = []
        for _, key, w in columns:
            val = key(r) if callable(key) else r[key]
            cells.append(f"{str(val)[:w]:<{w}}")
        print(" ".join(cells))


# ---------------------------------------------------------------------------
# AUTH
# ---------------------------------------------------------------------------
def login():
    header("LOGIN - Genshin DPS Tracker")
    username = input("Username/UID: ").strip()
    password = getpass.getpass("Password: ")
    row = db.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()
    if row and verify_password(password, row["password"]):
        return row
    print("  ! Username atau password salah.")
    return None


# ---------------------------------------------------------------------------
# ADMIN: kelola User
# ---------------------------------------------------------------------------
def show_users():
    rows = db.execute("SELECT * FROM users ORDER BY id").fetchall()
    print_rows(rows, [("ID", "id", 4), ("Username", "username", 24),
                      ("Role", "role", 8), ("Dibuat", "created_at", 17)])
    return rows


def admin_create_user():
    username = ask("Username/UID baru")
    if db.execute("SELECT 1 FROM users WHERE username=?", (username,)).fetchone():
        print("  ! Username sudah dipakai.")
        return
    password = ask("Password")
    db.execute("INSERT INTO users (username, password, role, created_at) VALUES (?,?,?,?)",
               (username, hash_password(password), "user", now()))
    db.commit()
    print("  ✓ User berhasil dibuat.")


def admin_edit_user():
    rows = show_users()
    uid = ask_id("ID user yang diedit", {r["id"] for r in rows})
    row = db.execute("SELECT * FROM users WHERE id=?", (uid,)).fetchone()
    new_name = ask("Username baru (Enter = tetap)", row["username"])
    if new_name != row["username"] and db.execute(
            "SELECT 1 FROM users WHERE username=?", (new_name,)).fetchone():
        print("  ! Username sudah dipakai.")
        return
    new_pass = getpass.getpass("Password baru / reset (Enter = tetap): ")
    stored = hash_password(new_pass) if new_pass else row["password"]
    db.execute("UPDATE users SET username=?, password=? WHERE id=?", (new_name, stored, uid))
    db.commit()
    print("  ✓ Data user diperbarui.")


def admin_delete_user(current_admin):
    rows = show_users()
    uid = ask_id("ID user yang dihapus", {r["id"] for r in rows})
    if uid == current_admin["id"]:
        print("  ! Tidak bisa menghapus akun yang sedang dipakai.")
        return
    if confirm("Semua tim & log milik user ini ikut terhapus. Lanjut?"):
        db.execute("DELETE FROM users WHERE id=?", (uid,))
        db.commit()
        print("  ✓ User dihapus.")


# ---------------------------------------------------------------------------
# ADMIN: Test Preset
# ---------------------------------------------------------------------------
def show_presets():
    rows = db.execute("SELECT * FROM test_presets ORDER BY id").fetchall()
    print_rows(rows, [("ID", "id", 4), ("Nama", "name", 24), ("Deskripsi", "description", 40)])
    return rows


def admin_create_preset():
    name = ask("Nama preset (mis. Abyss Floor 12)")
    desc = ask("Deskripsi", required=False)
    try:
        db.execute("INSERT INTO test_presets (name, description) VALUES (?,?)", (name, desc))
        db.commit()
        print("  ✓ Test Preset ditambahkan.")
    except sqlite3.IntegrityError:
        print("  ! Nama preset sudah ada.")


def admin_edit_preset():
    rows = show_presets()
    pid = ask_id("ID preset yang diedit", {r["id"] for r in rows})
    row = db.execute("SELECT * FROM test_presets WHERE id=?", (pid,)).fetchone()
    name = ask("Nama baru", row["name"])
    desc = ask("Deskripsi baru", row["description"], required=False)
    try:
        db.execute("UPDATE test_presets SET name=?, description=? WHERE id=?", (name, desc, pid))
        db.commit()
        print("  ✓ Test Preset diperbarui.")
    except sqlite3.IntegrityError:
        print("  ! Nama preset sudah ada.")


def admin_delete_preset():
    rows = show_presets()
    pid = ask_id("ID preset yang dihapus", {r["id"] for r in rows})
    if confirm("Log lama yang memakai preset ini akan tampil sebagai '(dihapus)'. Lanjut?"):
        db.execute("DELETE FROM test_presets WHERE id=?", (pid,))
        db.commit()
        print("  ✓ Test Preset dihapus.")


# ---------------------------------------------------------------------------
# ADMIN: Target Dummy
# ---------------------------------------------------------------------------
def show_dummies():
    rows = db.execute("SELECT * FROM target_dummies ORDER BY category, id").fetchall()
    print_rows(rows, [("ID", "id", 4), ("Nama", "name", 22), ("Kategori", "category", 13),
                      ("Deskripsi", "description", 36)])
    return rows


def ask_category(default=None):
    for i, c in enumerate(CATEGORIES, 1):
        print(f"  {i}. {c}")
    while True:
        raw = ask("Kategori (nomor)", CATEGORIES.index(default) + 1 if default else None)
        if raw.isdigit() and 1 <= int(raw) <= len(CATEGORIES):
            return CATEGORIES[int(raw) - 1]
        print("  ! Pilihan tidak valid.")


def admin_create_dummy():
    name = ask("Nama target dummy")
    category = ask_category()
    desc = ask("Deskripsi", required=False)
    try:
        db.execute("INSERT INTO target_dummies (name, category, description) VALUES (?,?,?)",
                   (name, category, desc))
        db.commit()
        print("  ✓ Target Dummy ditambahkan.")
    except sqlite3.IntegrityError:
        print("  ! Nama dummy sudah ada.")


def admin_edit_dummy():
    rows = show_dummies()
    did = ask_id("ID dummy yang diedit", {r["id"] for r in rows})
    row = db.execute("SELECT * FROM target_dummies WHERE id=?", (did,)).fetchone()
    name = ask("Nama baru", row["name"])
    category = ask_category(row["category"])
    desc = ask("Deskripsi baru", row["description"], required=False)
    try:
        db.execute("UPDATE target_dummies SET name=?, category=?, description=? WHERE id=?",
                   (name, category, desc, did))
        db.commit()
        print("  ✓ Target Dummy diperbarui.")
    except sqlite3.IntegrityError:
        print("  ! Nama dummy sudah ada.")


def admin_delete_dummy():
    rows = show_dummies()
    did = ask_id("ID dummy yang dihapus", {r["id"] for r in rows})
    if confirm("Log lama yang memakai dummy ini akan tampil sebagai '(dihapus)'. Lanjut?"):
        db.execute("DELETE FROM target_dummies WHERE id=?", (did,))
        db.commit()
        print("  ✓ Target Dummy dihapus.")


# ---------------------------------------------------------------------------
# MENU ADMIN
# ---------------------------------------------------------------------------
def admin_menu(admin):
    while True:
        c = menu(f"MENU ADMIN  ({admin['username']})", [
            "Daftar User", "Tambah User", "Edit User / Reset Password", "Hapus User",
            "Daftar Test Preset", "Tambah Test Preset", "Edit Test Preset", "Hapus Test Preset",
            "Daftar Target Dummy", "Tambah Target Dummy", "Edit Target Dummy", "Hapus Target Dummy",
        ])
        if c == 0:
            return
        actions = {
            1: show_users, 2: admin_create_user, 3: admin_edit_user,
            4: lambda: admin_delete_user(admin),
            5: show_presets, 6: admin_create_preset, 7: admin_edit_preset, 8: admin_delete_preset,
            9: show_dummies, 10: admin_create_dummy, 11: admin_edit_dummy, 12: admin_delete_dummy,
        }
        print()
        actions[c]()
        pause()


# ---------------------------------------------------------------------------
# USER: Dictionary karakter & Tim
# ---------------------------------------------------------------------------
def show_characters():
    rows = db.execute("SELECT * FROM characters ORDER BY name").fetchall()
    print_rows(rows, [("ID", "id", 4), ("Karakter", "name", 22), ("Elemen", "element", 10)])
    return rows


def get_team_members(team_id):
    return db.execute("""
        SELECT tm.*, c.name AS char_name, c.element
        FROM team_members tm JOIN characters c ON c.id = tm.character_id
        WHERE tm.team_id=? ORDER BY tm.id""", (team_id,)).fetchall()


def show_teams(user):
    teams = db.execute("SELECT * FROM teams WHERE user_id=? ORDER BY id", (user["id"],)).fetchall()
    if not teams:
        print("  (Belum ada tim)")
        return teams
    for t in teams:
        print(f"\n[{t['id']}] {t['name']}")
        for m in get_team_members(t["id"]):
            print(f"     - {m['char_name']:<16} ({m['element']:<7}) "
                  f"Senjata: {m['weapon'] or '-':<18} Artefak: {m['artifact'] or '-'}")
    return teams


def user_create_team(user):
    name = ask("Nama tim")
    chars = show_characters()
    valid = {c["id"] for c in chars}
    chosen = []
    print(f"\nPilih 1-{MAX_TEAM_SIZE} karakter (ID), kosongkan untuk selesai.")
    while len(chosen) < MAX_TEAM_SIZE:
        cid = ask_id(f"Karakter ke-{len(chosen) + 1}", valid - set(chosen), allow_blank=True)
        if cid is None:
            break
        chosen.append(cid)
    if not chosen:
        print("  ! Tim harus punya minimal 1 karakter.")
        return
    cur = db.execute("INSERT INTO teams (user_id, name) VALUES (?,?)", (user["id"], name))
    team_id = cur.lastrowid
    print("\nCatat build tiap karakter (Enter untuk lewati):")
    for cid in chosen:
        cname = db.execute("SELECT name FROM characters WHERE id=?", (cid,)).fetchone()["name"]
        weapon = ask(f"  Senjata {cname}", required=False)
        artifact = ask(f"  Artefak {cname}", required=False)
        db.execute("INSERT INTO team_members (team_id, character_id, weapon, artifact) "
                   "VALUES (?,?,?,?)", (team_id, cid, weapon, artifact))
    db.commit()
    print("  ✓ Tim tersimpan.")


def user_edit_team(user):
    teams = show_teams(user)
    if not teams:
        return
    tid = ask_id("\nID tim yang diedit", {t["id"] for t in teams})
    team = db.execute("SELECT * FROM teams WHERE id=?", (tid,)).fetchone()
    db.execute("UPDATE teams SET name=? WHERE id=?", (ask("Nama tim", team["name"]), tid))
    print("\nPerbarui build (Enter = tetap):")
    for m in get_team_members(tid):
        weapon = ask(f"  Senjata {m['char_name']}", m["weapon"], required=False)
        artifact = ask(f"  Artefak {m['char_name']}", m["artifact"], required=False)
        db.execute("UPDATE team_members SET weapon=?, artifact=? WHERE id=?",
                   (weapon, artifact, m["id"]))
    db.commit()
    print("  ✓ Tim/build diperbarui.")


def user_delete_team(user):
    teams = show_teams(user)
    if not teams:
        return
    tid = ask_id("\nID tim yang dihapus", {t["id"] for t in teams})
    if confirm("Log hasil tes yang memakai tim ini ikut terhapus. Lanjut?"):
        db.execute("DELETE FROM teams WHERE id=?", (tid,))
        db.commit()
        print("  ✓ Tim dihapus.")


# ---------------------------------------------------------------------------
# USER: Log hasil tes
# ---------------------------------------------------------------------------
def show_label_options():
    print("\n-- Test Preset --")
    presets = db.execute("SELECT * FROM test_presets ORDER BY id").fetchall()
    for p in presets:
        print(f"  [{p['id']}] {p['name']}  -  {p['description']}")
    print("\n-- Target Dummy --")
    dummies = db.execute("SELECT * FROM target_dummies ORDER BY category, id").fetchall()
    for d in dummies:
        print(f"  [{d['id']}] {d['name']} ({d['category']})  -  {d['description']}")
    return presets, dummies


def input_distribution(team_id):
    """Input persentase damage tiap anggota tim, apa adanya dari game."""
    result = []
    print("\nDamage Distribution (persen dari game, Enter = lewati karakter):")
    for m in get_team_members(team_id):
        raw = input(f"  {m['char_name']} (%): ").strip()
        if raw:
            try:
                pct = float(raw.replace(",", ".").replace("%", ""))
                if 0 <= pct <= 100:
                    result.append((m["character_id"], pct))
                else:
                    print("    ! Di luar 0-100, dilewati.")
            except ValueError:
                print("    ! Bukan angka, dilewati.")
    total = sum(p for _, p in result)
    if result and abs(total - 100) > 0.5:
        print(f"  (Info: total persentase = {total:g}%, bukan 100%. Tetap disimpan.)")
    return result


def user_create_log(user):
    teams = db.execute("SELECT * FROM teams WHERE user_id=? ORDER BY id", (user["id"],)).fetchall()
    if not teams:
        print("  ! Buat tim dulu sebelum mencatat hasil tes.")
        return
    presets, dummies = show_label_options()
    if not presets or not dummies:
        print("  ! Admin belum menyediakan Test Preset / Target Dummy.")
        return
    print("\n-- Tim Kamu --")
    show_teams(user)
    team_id = ask_id("\nID tim yang dites", {t["id"] for t in teams})
    preset_id = ask_id("ID Test Preset", {p["id"] for p in presets})
    dummy_id = ask_id("ID Target Dummy", {d["id"] for d in dummies})

    print("\nMasukkan angka persis seperti yang terlihat di game:")
    total_time = ask_float("Total Waktu (detik)", minimum=0.1)
    total_damage = ask_int("Total Damage", minimum=0)
    strongest = ask_int("Strongest Hit", minimum=0)
    dist = input_distribution(team_id)
    notes = ask("Catatan (opsional)", required=False)

    cur = db.execute("""INSERT INTO test_logs (user_id, team_id, preset_id, dummy_id,
                        total_time, total_damage, strongest_hit, notes, created_at)
                        VALUES (?,?,?,?,?,?,?,?,?)""",
                     (user["id"], team_id, preset_id, dummy_id, total_time,
                      total_damage, strongest, notes, now()))
    db.executemany("INSERT INTO log_distribution (log_id, character_id, percent) VALUES (?,?,?)",
                   [(cur.lastrowid, cid, pct) for cid, pct in dist])
    db.commit()
    print("  ✓ Hasil tes tercatat.")


def fetch_logs(user):
    return db.execute("""
        SELECT l.*, t.name AS team_name,
               COALESCE(p.name, '(dihapus)') AS preset_name,
               COALESCE(d.name, '(dihapus)') AS dummy_name
        FROM test_logs l
        JOIN teams t ON t.id = l.team_id
        LEFT JOIN test_presets p ON p.id = l.preset_id
        LEFT JOIN target_dummies d ON d.id = l.dummy_id
        WHERE l.user_id=? ORDER BY l.id DESC""", (user["id"],)).fetchall()


def user_history(user):
    logs = fetch_logs(user)
    if not logs:
        print("  (Belum ada riwayat)")
        return logs
    for l in logs:
        dist = db.execute("""SELECT c.name, ld.percent FROM log_distribution ld
                             JOIN characters c ON c.id = ld.character_id
                             WHERE ld.log_id=?""", (l["id"],)).fetchall()
        dist_txt = ", ".join(f"{d['name']} {d['percent']:g}%" for d in dist) or "-"
        print(f"\n[#{l['id']}] {l['created_at']}  |  Tim: {l['team_name']}")
        print(f"   Preset: {l['preset_name']}   Dummy: {l['dummy_name']}")
        print(f"   Waktu: {l['total_time']:g} dtk   Total Damage: {fmt(l['total_damage'])}   "
              f"Strongest Hit: {fmt(l['strongest_hit'])}")
        print(f"   Distribusi: {dist_txt}")
        if l["notes"]:
            print(f"   Catatan: {l['notes']}")
    return logs


def user_edit_log(user):
    logs = user_history(user)
    if not logs:
        return
    lid = ask_id("\nID log yang diedit (angka setelah #)", {l["id"] for l in logs})
    log = db.execute("SELECT * FROM test_logs WHERE id=? AND user_id=?", (lid, user["id"])).fetchone()
    presets, dummies = show_label_options()
    print("\nEnter = pertahankan nilai lama.")
    pid = ask_id(f"ID Test Preset [{log['preset_id']}]", {p["id"] for p in presets}, allow_blank=True)
    did = ask_id(f"ID Target Dummy [{log['dummy_id']}]", {d["id"] for d in dummies}, allow_blank=True)
    total_time = ask_float("Total Waktu (detik)", f"{log['total_time']:g}", minimum=0.1)
    total_damage = ask_int("Total Damage", log["total_damage"])
    strongest = ask_int("Strongest Hit", log["strongest_hit"])
    notes = ask("Catatan", log["notes"], required=False)
    db.execute("""UPDATE test_logs SET preset_id=?, dummy_id=?, total_time=?, total_damage=?,
                  strongest_hit=?, notes=? WHERE id=?""",
               (pid or log["preset_id"], did or log["dummy_id"], total_time,
                total_damage, strongest, notes, lid))
    if confirm("Input ulang Damage Distribution?"):
        db.execute("DELETE FROM log_distribution WHERE log_id=?", (lid,))
        db.executemany("INSERT INTO log_distribution (log_id, character_id, percent) VALUES (?,?,?)",
                       [(lid, cid, pct) for cid, pct in input_distribution(log["team_id"])])
    db.commit()
    print("  ✓ Catatan tes diperbarui.")


def user_delete_log(user):
    logs = user_history(user)
    if not logs:
        return
    lid = ask_id("\nID log yang dihapus (angka setelah #)", {l["id"] for l in logs})
    if confirm("Yakin hapus catatan ini?"):
        db.execute("DELETE FROM test_logs WHERE id=? AND user_id=?", (lid, user["id"]))
        db.commit()
        print("  ✓ Catatan dihapus.")


def user_change_password(user):
    old = getpass.getpass("Password lama: ")
    if not verify_password(old, user["password"]):
        print("  ! Password lama salah.")
        return
    new = getpass.getpass("Password baru: ")
    if not new:
        print("  ! Password tidak boleh kosong.")
        return
    db.execute("UPDATE users SET password=? WHERE id=?", (hash_password(new), user["id"]))
    db.commit()
    print("  ✓ Password diganti. Silakan login ulang.")


# ---------------------------------------------------------------------------
# MENU USER
# ---------------------------------------------------------------------------
def user_menu(user):
    while True:
        c = menu(f"MENU USER  ({user['username']})", [
            "Riwayat Hasil Tes", "Catat Hasil Tes Baru", "Edit Catatan Tes", "Hapus Catatan Tes",
            "Daftar Tim & Build", "Buat Tim Baru", "Edit Tim / Build", "Hapus Tim",
            "Lihat Dictionary Karakter", "Lihat Info Test Preset & Target Dummy",
            "Ganti Password",
        ])
        if c == 0:
            return
        actions = {
            1: lambda: user_history(user), 2: lambda: user_create_log(user),
            3: lambda: user_edit_log(user), 4: lambda: user_delete_log(user),
            5: lambda: show_teams(user), 6: lambda: user_create_team(user),
            7: lambda: user_edit_team(user), 8: lambda: user_delete_team(user),
            9: show_characters, 10: show_label_options,
            11: lambda: user_change_password(user),
        }
        print()
        actions[c]()
        pause()
        if c == 11:
            return  # paksa login ulang


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main():
    init_db()
    print("Genshin DPS Tracker - buku catatan hasil tes in-game")
    while True:
        user = login()
        if user is None:
            if not confirm("Coba lagi?"):
                break
            continue
        if user["role"] == "admin":
            admin_menu(user)
        else:
            user_menu(user)
        if not confirm("\nLogin sebagai akun lain?"):
            break
    print("Sampai jumpa!")
    db.close()


if __name__ == "__main__":
    main()