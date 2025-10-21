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
    }
]

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
        user = input("Masukkan Username : ").lower()
        pwd = input("Masukkan Password : ")

# Mengecek apakah username dan password sesuai
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
# MENU READ (Tampilkan Data)
# -------------------------------------
def tampilkan_data():
    while True:
        print("\n=== MENU REPORT DATA PELAMAR ===")
        print("1. Tampilkan semua data pelamar")
        print("2. Cari pelamar berdasarkan ID")
        print("3. Kembali ke menu utama")
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            if len(data_pelamar) == 0:
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
            cari = input("Masukkan ID Pelamar: ").upper()
            ditemukan = False
            for p in data_pelamar:
                if p["ID"] == cari:
                    print("\nDATA DITEMUKAN\n")
                    print("="*60)
                    for k, v in p.items():
                        print(f"{k:<15}: {v}")
                    print("="*60)
                    ditemukan = True
                    break
            if not ditemukan:
                print("\nData tidak ditemukan.\n")
        elif pilihan == "3":
            break
        else:
            print("\nPilihan tidak valid!\n")

# -------------------------------------
# MENU CREATE (Tambah Data)
# -------------------------------------
def tambah_data():
    while True:
        print("\n=== MENU MENAMBAHKAN DATA PELAMAR ===")
        print("1. Tambah pelamar baru")
        print("2. Kembali ke menu utama")
        pilih = input("Pilih menu (1/2): ")

        if pilih == "1":
            id_baru = input("Masukkan ID Pelamar: ").upper()
            if any(p["ID"] == id_baru for p in data_pelamar):
                print("\nID sudah ada, gunakan ID lain!\n")
                continue
            nama = input("Nama: ")
            posisi = input("Posisi dilamar: ")
            pengalaman = (input("Pengalaman (tahun): "))
            pendidikan = input("Pendidikan terakhir: ")
            kontak = input("Kontak: ")
            email = input("Email: ")
            status = input("Status lamaran: ")

            while True:
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
                    break
                elif simpan == "N":
                    print("\nData tidak disimpan.\n")
                    break
                else:
                    print("Masukkan pilihan Y atau N saja.")
        elif pilih == "2":
            break
        else:
            print("Pilihan tidak valid!\n")

# -------------------------------------
# MENU UPDATE (Ubah Data)
# -------------------------------------
def ubah_data():
    while True:
        print("\n=== MENU MENGUBAH DATA PELAMAR ===")
        print("1. Ubah data pelamar berdasarkan ID")
        print("2. Kembali ke menu utama")
        pilih = input("Pilih menu (1/2): ")

        if pilih == "1":
            id_edit = input("Masukkan ID Pelamar: ").upper()
            for p in data_pelamar:
                if p["ID"] == id_edit:
                    print("\nDATA DITEMUKAN\n")
                    for k, v in p.items():
                        print(f"{k:<15}: {v}")
                    konfirmasi = input("\nApakah ingin mengubah data ini? (Y/N): ").upper()
                    if konfirmasi == "Y":
                        kolom = input("Masukkan nama kolom yang ingin diubah (Nama/Posisi/Pengalaman/Pendidikan/Kontak/Email/Status): ")
                        if kolom in p:
                            nilai_baru = input(f"Masukkan nilai baru untuk {kolom}: ")
                            p[kolom] = int(nilai_baru) if kolom == "Pengalaman" else nilai_baru
                            print("\nData berhasil diperbarui.\n")
                        else:
                            print("\nKolom tidak ditemukan.\n")
                    elif konfirmasi == "N":
                        print("\nPerubahan dibatalkan.\n")
                    else:
                        print("Masukkan Y atau N saja.")
                    break
            else:
                print("\nData tidak ditemukan.\n")
        elif pilih == "2":
            break
        else:
            print("Pilihan tidak valid!\n")

# -------------------------------------
# MENU DELETE (Hapus Data)
# -------------------------------------
def hapus_data():
    while True:
        print("\n=== MENU MENGHAPUS DATA PELAMAR ===")
        print("1. Hapus pelamar berdasarkan ID")
        print("2. Kembali ke menu utama")
        pilih = input("Pilih menu (1/2): ")

        if pilih == "1":
            id_del = input("Masukkan ID Pelamar: ").upper()
            for p in data_pelamar:
                if p["ID"] == id_del:
                    while True:
                        konfirmasi = input(f"Yakin ingin menghapus data {p['Nama']}? (Y/N): ").upper()
                        if konfirmasi == "Y":
                            data_pelamar.remove(p)
                            print("\nData pelamar berhasil dihapus.\n")
                            break
                        elif konfirmasi == "N":
                            print("\nPenghapusan dibatalkan.\n")
                            break
                        else:
                            print("Masukkan Y atau N saja.")
                    break
            else:
                print("\nData tidak ditemukan.\n")
        elif pilih == "2":
            break
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
        print("2. Tambah Data Pelamar")
        print("3. Ubah Data Pelamar")
        print("4. Hapus Data Pelamar")
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
        print("=== SELAMAT DATANG DI PORTAL PELAMAR PT. RIMBO PERADUAN ===")
        print("1. Login")
        print("2. Exit")
        pilihan = input("Pilih menu (1/2): ")

        if pilihan == "1":
            if login():
                menu_utama()
        elif pilihan == "2":
            print("\nTerima kasih telah menggunjungi Portal Pelamar PT. Rimbo Peraduan.")
            print("Sistem ditutup dengan aman. Sampai jumpa kembali!\n")
            break
        else:
            print("\nPilihan tidak valid! Silakan pilih 1 atau 2.\n")
