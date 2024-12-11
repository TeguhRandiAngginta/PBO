class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama

class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama

    def pinjam_buku(self, mahasiswa, buku):
        print(f"Mahasiswa {mahasiswa.nama} meminjam buku '{buku}' dari {self.nama}.")

# Implementasi Asosiasi
mahasiswa = Mahasiswa("Teguh Randi Angginta")
perpustakaan = Perpustakaan("Perpustakaan Pusat")

perpustakaan.pinjam_buku(mahasiswa, "Pemrograman Python")