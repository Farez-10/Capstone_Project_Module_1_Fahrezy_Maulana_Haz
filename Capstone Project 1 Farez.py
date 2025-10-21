# =====================================
# PORTAL PELAMAR KARYAWAN PT. RIMBO PERADUAN
# Fahrezy Maulana Haz
# =====================================

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
# Fungsi Validasi Input
# -------------------------------------
def input_tidak_kosong(pesan):
    """Memastikan input tidak kosong"""
    while True:
        data = input(pesan).strip()
        if data == "":
            print("Input tidak boleh kosong! Silakan isi kembali.")
        else:
            return data

def validasi_email():
    """Memastikan format email valid dan hanya Gmail"""
    while True:
        email = input("Email: ").strip().lower()
        if not email.endswith("@gmail.com"):
            print("Email harus menggunakan domain @gmail.com!")
        elif " " in email or len(email) < 12:
            print("Email tidak valid! Pastikan format benar, contoh: nama@gmail.com")
        else:
            return email

def validasi_nomor():
    """Memastikan nomor HP hanya angka dan minimal 10 digit"""
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
def login():
    akun_login = {
        "farez": "12345",
        "matteo": "67890"
    }

    percobaan = 3
    while percobaan > 0:
        print("=== LOGIN ADMIN HRD ===")
        user = input("Masukkan Username : ")
        pwd = input("Masukkan Password : ")

        if user in akun_login and akun_login[user] == pwd:
            print(f"\nLogin berhasil! Selamat datang, {user.title()} di Portal Pelamar PT. Rimbo Peraduan.\n")
            return True
        else:
            percobaan -= 1
            print(f"Username atau password salah! Sisa percobaan: {percobaan}\n")
            if percobaan == 0:
                print("Anda telah 3 kali gagal login. Kembali ke menu utama.\n")
                return False

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
    id_baru = input_tidak_kosong("Masukkan ID Pelamar: ").upper()

    if any(p["ID"] == id_baru for p in data_pelamar):
        print("\nID sudah ada, gunakan ID lain!\n")
        return

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
        print("\nData pelamar berhasil ditambahkan.\n")
    else:
        print("\nData tidak disimpan.\n")

# -------------------------------------
# MENU UPDATE (Ubah Data)
# -------------------------------------
def ubah_data():
    print("\n=== MENU MENGUBAH DATA PELAMAR ===")
    id_edit = input_tidak_kosong("Masukkan ID Pelamar yang ingin diubah: ").upper()
    for p in data_pelamar:
        if p["ID"] == id_edit:
            print("\nDATA DITEMUKAN\n")
            for k, v in p.items():
                print(f"{k:<15}: {v}")
            kolom = input_tidak_kosong("\nMasukkan kolom yang ingin diubah (Nama/Posisi/Pengalaman/Pendidikan/Kontak/Email/Status): ").capitalize()
            if kolom in p:
                if kolom == "Email":
                    nilai_baru = validasi_email()
                elif kolom == "Kontak":
                    nilai_baru = validasi_nomor()
                else:
                    nilai_baru = input_tidak_kosong(f"Masukkan nilai baru untuk {kolom}: ")
                p[kolom] = nilai_baru
                print("\nData berhasil diperbarui.\n")
            else:
                print("\nKolom tidak ditemukan.\n")
            break
    else:
        print("\nData tidak ditemukan.\n")

# -------------------------------------
# Fungsi tampilkan semua data tanpa menu
# -------------------------------------
def tampilkan_semua_data():
    """Menampilkan seluruh data pelamar dalam bentuk tabel"""
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
# MENU DELETE (Hapus Data - Multiple Delete)
# -------------------------------------
def hapus_data():
    print("\n=== MENU MENGHAPUS DATA PELAMAR ===")
    print("1. Hapus pelamar berdasarkan ID")
    print("2. Kembali ke menu utama")
    pilih = input("Pilih menu (1/2): ")

    if pilih == "1":
        tampilkan_semua_data()  # ganti fungsi agar tidak muncul menu lain
        print("\nKamu bisa menghapus beberapa pelamar sekaligus dengan memisahkan ID dengan koma (misal: P001,P002)")
        id_list = input_tidak_kosong("\nMasukkan ID Pelamar yang ingin dihapus: ").upper().replace(" ", "").split(",")

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

    elif pilih == "2":
        return
    else:
        print("Pilihan tidak valid!\n")

# -------------------------------------
# MENU UTAMA
# -------------------------------------
def menu_utama():
    while True:
        print("=" * 60)
        print("=== MENU UTAMA PORTAL PELAMAR ===")
        print("1. Tampilkan Data Pelamar")
        print("2. Tambahkan Data Pelamar")
        print("3. Mengubah Data Pelamar")
        print("4. Menghapus Data Pelamar")
        print("5. Logout")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tampilkan_data()
        elif pilihan == "2":
            tambah_data()
        elif pilihan == "3":
            ubah_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            print("\nLogout berhasil. Kembali ke menu login.\n")
            break
        else:
            print("Pilihan tidak valid!\n")

# -------------------------------------
# PROGRAM UTAMA
# -------------------------------------
if __name__ == "__main__":
    while True:
        print("=" * 60)
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
