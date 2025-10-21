# =====================================
# PORTAL PELAMAR KARYAWAN PT. RIMBO PERADUAN
# Fahrezy Maulana Haz
# =====================================

import datetime

# -------------------------------------
# Data Pelamar
# -------------------------------------
data_pelamar = [
    {
        "ID": "P001",
        "Nama": "Fahrezy Maulana Haz",
        "Posisi": "Surveyor",
        "Pengalaman": "2 tahun",
        "Pendidikan": "S1 Teknik Geodesi",
        "Kontak": "089509125473",
        "Email": "farez@gmail.com",
        "Status": "Lolos Interview"
    },
    {
        "ID": "P002",
        "Nama": "Jimmy Neutron",
        "Posisi": "IT Support",
        "Pengalaman": "1 tahun",
        "Pendidikan": "D3 Teknik Informatika",
        "Kontak": "089876543210",
        "Email": "jimmy@gmail.com",
        "Status": "Menunggu"
    },
    {
        "ID": "P003",
        "Nama": "Sandy Cheeks",
        "Posisi": "Safety Officer",
        "Pengalaman": "3 tahun",
        "Pendidikan": "S1 Teknik K3",
        "Kontak": "081234567891",
        "Email": "sandy@gmail.com",
        "Status": "Menunggu"
    }
]

# -------------------------------------
# Riwayat perubahan data
# -------------------------------------
riwayat_perubahan = []

# -------------------------------------
# Fungsi Validasi Input
# -------------------------------------
def input_tidak_kosong(pesan):
    while True:
        data = input(pesan).strip()
        if data == "":
            print("Input tidak boleh kosong! Silakan isi kembali.")
        else:
            return data

def validasi_email():
    while True:
        email = input("Email: ").strip().lower()
        if not email.endswith("@gmail.com"):
            print("Email harus menggunakan domain @gmail.com!")
        elif " " in email or len(email) < 12:
            print("Email tidak valid! Pastikan format benar, contoh: nama@gmail.com")
        else:
            return email

def validasi_nomor():
    while True:
        kontak = input("Nomor HP: ").strip()
        if not kontak.isdigit():
            print("Nomor HP hanya boleh berisi angka!")
        elif len(kontak) < 10:
            print("Nomor HP terlalu pendek! Minimal 10 digit.")
        else:
            return kontak

# -------------------------------------
# Fungsi Login
# -------------------------------------
akun_login = {"farez": "12345", "matteo": "67890"}
user_login = None

def login():
    global user_login
    percobaan = 3
    while percobaan > 0:
        print("=== LOGIN ADMIN HRD ===")
        user = input("Masukkan Username : ")
        pwd = input("Masukkan Password : ")
        if user in akun_login and akun_login[user] == pwd:
            user_login = user
            print(f"\nLogin berhasil! Selamat datang, {user.title()} di Portal Pelamar PT. Rimbo Peraduan.\n")
            return True
        else:
            percobaan -= 1
            print(f"Username atau password salah! Sisa percobaan: {percobaan}\n")
            if percobaan == 0:
                print("Anda telah 3 kali gagal login. Kembali ke menu utama.\n")
                return False

# -------------------------------------
# Fungsi Auto ID
# -------------------------------------
def generate_id_otomatis():
    if not data_pelamar:
        return "P001"
    last_id = max(int(p["ID"][1:]) for p in data_pelamar)
    return f"P{last_id + 1:03d}"

# -------------------------------------
# Fungsi Tampilkan Semua Data
# -------------------------------------
def tampilkan_semua_data():
    if not data_pelamar:
        print("\nBelum ada data pelamar.\n")
    else:
        print("\nDAFTAR DATA PELAMAR\n")
        print("="*120)
        print(f"{'ID':<6} {'Nama':<25} {'Posisi':<20} {'Pendidikan':<25} {'Pengalaman':<12} {'Status':<15}")
        print("-"*120)
        for p in data_pelamar:
            print(f"{p['ID']:<6} {p['Nama']:<25} {p['Posisi']:<20} {p['Pendidikan']:<25} {p['Pengalaman']:<12} {p['Status']:<15}")
        print("="*120)

# -------------------------------------
# MENU READ (Tampilkan Data + Cari Pelamar)
# -------------------------------------
def tampilkan_data():
    while True:
        print("\n=== MENU REPORT DATA PELAMAR ===")
        print("1. Tampilkan semua data pelamar")
        print("2. Cari pelamar berdasarkan ID")
        print("3. Kembali ke menu utama")
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            tampilkan_semua_data()
        elif pilihan == "2":
            cari_id = input_tidak_kosong("Masukkan ID Pelamar: ").upper()
            ditemukan = False
            for p in data_pelamar:
                if p["ID"] == cari_id:
                    print("\nDATA PELAMAR DITEMUKAN\n")
                    print("="*50)
                    for k, v in p.items():
                        print(f"{k:<15}: {v}")
                    print("="*50)
                    ditemukan = True
                    break
            if not ditemukan:
                print("\nData dengan ID tersebut tidak ditemukan.\n")
        elif pilihan == "3":
            break
        else:
            print("\nPilihan tidak valid!\n")

# -------------------------------------
# MENU CREATE (Tambah Data)
# -------------------------------------
def tambah_data():
    print("\n=== MENU MENAMBAHKAN DATA PELAMAR ===")
    tampilkan_semua_data()
    id_baru = generate_id_otomatis()
    print(f"\nID Pelamar otomatis dibuat: {id_baru}")

    nama = input_tidak_kosong("Nama: ")
    posisi = input_tidak_kosong("Posisi dilamar: ")
    pengalaman = input_tidak_kosong("Pengalaman (contoh: 2 tahun): ")
    pendidikan = input_tidak_kosong("Pendidikan terakhir: ")
    kontak = validasi_nomor()
    email = validasi_email()
    status = input_tidak_kosong("Status lamaran: ")

    simpan = input("Simpan data ini? (Y/N): ").upper()
    if simpan == "Y":
        data_pelamar.append({
            "ID": id_baru,
            "Nama": nama,
            "Posisi": posisi,
            "Pengalaman": pengalaman,
            "Pendidikan": pendidikan,
            "Kontak": kontak,
            "Email": email,
            "Status": status
        })
        print(f"\nData pelamar {nama} berhasil ditambahkan dengan ID {id_baru}.\n")
    else:
        print("\nData tidak disimpan.\n")

# -------------------------------------
# MENU UPDATE (Ubah Data + Simpan Riwayat)
# -------------------------------------
def ubah_data():
    print("\n=== MENU MENGUBAH DATA PELAMAR ===")
    tampilkan_semua_data()
    id_edit = input_tidak_kosong("Masukkan ID Pelamar yang ingin diubah: ").upper()

    for p in data_pelamar:
        if p["ID"] == id_edit:
            print("\nDATA DITEMUKAN\n")
            for k, v in p.items():
                print(f"{k:<15}: {v}")

            kolom_opsi = ["Nama", "Posisi", "Pengalaman", "Pendidikan", "Kontak", "Email", "Status"]
            print("\nPilih kolom yang ingin diubah:")
            for i, kolom in enumerate(kolom_opsi, start=1):
                print(f"{i}. {kolom}")

            pilihan = input_tidak_kosong("Pilih nomor kolom (1-7): ")

            if pilihan.isdigit() and 1 <= int(pilihan) <= 7:
                kolom = kolom_opsi[int(pilihan) - 1]
                nilai_lama = p[kolom]

                if kolom == "Email":
                    p[kolom] = validasi_email()
                elif kolom == "Kontak":
                    p[kolom] = validasi_nomor()
                elif kolom == "Status":
                    print("\nPilih status lamaran:")
                    print("1. Menunggu")
                    print("2. Lolos Administrasi")
                    print("3. Lolos Interview")
                    print("4. Tidak Lolos")
                    pilih_status = input("Pilih (1-4): ")
                    status_baru = {
                        "1": "Menunggu",
                        "2": "Lolos Administrasi",
                        "3": "Lolos Interview",
                        "4": "Tidak Lolos"
                    }.get(pilih_status, None)
                    if status_baru:
                        p["Status"] = status_baru
                        nilai_baru = status_baru
                    else:
                        print("\nPilihan tidak valid, status tidak diubah.\n")
                        return
                else:
                    nilai_baru = input_tidak_kosong(f"Masukkan nilai baru untuk {kolom}: ")
                    p[kolom] = nilai_baru

                # Simpan ke riwayat
                riwayat_perubahan.append({
                    "Waktu": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                    "Admin": user_login,
                    "ID": id_edit,
                    "Kolom": kolom,
                    "Dari": nilai_lama,
                    "Ke": p[kolom]
                })

                print(f"\nData '{kolom}' berhasil diperbarui dari '{nilai_lama}' menjadi '{p[kolom]}'.\n")
            else:
                print("\nNomor kolom tidak valid!\n")
            break
    else:
        print("\nData tidak ditemukan.\n")

# -------------------------------------
# MENU DELETE (Hapus Data)
# -------------------------------------
def hapus_data():
    print("\n=== MENU MENGHAPUS DATA PELAMAR ===")
    tampilkan_semua_data()
    id_list = input_tidak_kosong("\nMasukkan ID Pelamar yang ingin dihapus (pisahkan dengan koma jika lebih dari satu): ").upper().replace(" ", "").split(",")

    ditemukan = False
    for id_del in id_list:
        for p in data_pelamar[:]:
            if p["ID"] == id_del:
                konfirmasi = input(f"Yakin ingin menghapus data {p['Nama']} ({p['ID']})? (Y/N): ").upper()
                if konfirmasi == "Y":
                    data_pelamar.remove(p)
                    print(f"Data pelamar {p['Nama']} berhasil dihapus.")
                    ditemukan = True
                else:
                    print(f"Data {p['Nama']} batal dihapus.")
    if not ditemukan:
        print("\nTidak ada data yang dihapus (ID tidak ditemukan).\n")

# -------------------------------------
# MENU HISTORY (Tampilkan Riwayat)
# -------------------------------------
def tampilkan_riwayat():
    print("\n=== RIWAYAT PERUBAHAN DATA PELAMAR ===")
    if not riwayat_perubahan:
        print("Belum ada riwayat perubahan data.\n")
    else:
        print("="*110)
        print(f"{'Waktu':<20} {'Admin':<10} {'ID Pelamar':<10} {'Kolom':<15} {'Dari':<20} {'Ke':<20}")
        print("-"*110)
        for r in riwayat_perubahan:
            print(f"{r['Waktu']:<20} {r['Admin']:<10} {r['ID']:<10} {r['Kolom']:<15} {r['Dari']:<20} {r['Ke']:<20}")
        print("="*110)

# -------------------------------------
# MENU UTAMA
# -------------------------------------
def menu_utama():
    while True:
        print("=" * 70)
        print("=== MENU UTAMA PORTAL PELAMAR ===")
        print("1. Tampilkan Data Pelamar")
        print("2. Tambahkan Data Pelamar")
        print("3. Mengubah Data Pelamar")
        print("4. Menghapus Data Pelamar")
        print("5. Tampilkan Riwayat Perubahan")
        print("6. Logout")
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tampilkan_data()
        elif pilihan == "2":
            tambah_data()
        elif pilihan == "3":
            ubah_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            tampilkan_riwayat()
        elif pilihan == "6":
            print("\nLogout berhasil. Kembali ke menu login.\n")
            break
        else:
            print("Pilihan tidak valid!\n")

# -------------------------------------
# PROGRAM UTAMA
# -------------------------------------
if __name__ == "__main__":
    while True:
        print("=" * 70)
        print("=== SELAMAT DATANG DI PORTAL PELAMAR KARYAWAN PT. RIMBO PERADUAN ===")
        print("1. Login")
        print("2. Exit")
        pilihan = input("Pilih menu (1/2): ")

        if pilihan == "1":
            if login():
                menu_utama()
        elif pilihan == "2":
            print("\nTerima kasih telah mengunjungi Portal Pelamar PT. Rimbo Peraduan.")
            print("Sistem ditutup dengan aman. Sampai jumpa kembali!\n")
            break
        else:
            print("\nPilihan tidak valid! Silakan pilih 1 atau 2.\n")
