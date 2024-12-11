class Matakuliah:
    def __init__(self, nama, kode, sks):
        self.nama = nama
        self.kode = kode
        self.sks = sks

    def info(self):
        return f"{self.nama} ({self.kode}, {self.sks} SKS)"

class Dosen:
    def __init__(self, nama):
        self.nama = nama
        self.mata_kuliah = []

    def tambah_mata_kuliah(self, mata_kuliah):
        self.mata_kuliah.append(mata_kuliah)

    def total_sks(self):
        return sum(mk.sks for mk in self.mata_kuliah)

# Implementasi Agregasi: Objek Matakuliah terpisah dari Dosen tetapi dapat ditambahkan ke dalam daftar mata_kuliah dosen
mk1 = Matakuliah("Pemrograman", "P101", 3)
mk2 = Matakuliah("Struktur Data", "S102", 4)

dosen = Dosen("Dr. Ahmad")
dosen.tambah_mata_kuliah(mk1)
dosen.tambah_mata_kuliah(mk2)

print(f"Dosen {dosen.nama} mengajar:")
for mk in dosen.mata_kuliah:
    print(f"- {mk.info()}")
print(f"Total SKS yang diajar: {dosen.total_sks()}\n")

class Modul:
    def __init__(self, judul):
        self.judul = judul

    def info(self):
        return f"Modul: {self.judul}"

class MataKuliah:
    def __init__(self, nama, kode, sks):
        self.nama = nama
        self.kode = kode
        self.sks = sks
        self.modul = []

    def tambah_modul(self, judul):
        modul = Modul(judul)
        self.modul.append(modul)

    def info(self, detail=False):
        if detail:
            modul_info = "\n  ".join(modul.info() for modul in self.modul)
            return f"{self.nama} ({self.kode}, {self.sks} SKS)\n  {modul_info}"
        return f"{self.nama} ({self.kode}, {self.sks} SKS)"

# Implementasi Komposisi: Objek Modul bergantung pada MataKuliah dan dibuat di dalamnya
mk = MataKuliah("Algoritma", "A101", 3)
mk.tambah_modul("Pendahuluan Algoritma")
mk.tambah_modul("Sorting dan Searching")

print(f"Mata Kuliah {mk.nama} memiliki detail:")
print(mk.info(detail=True))

class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama

class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama

    def pinjam_buku(self, mahasiswa, buku):
        print(f"Mahasiswa {mahasiswa.nama} meminjam buku '{buku}' dari {self.nama}.")

# Implementasi Asosiasi: Objek Mahasiswa dan Perpustakaan terpisah tetapi saling berhubungan melalui metode pinjam_buku
mahasiswa = Mahasiswa("Teguh Randi Angginta")
perpustakaan = Perpustakaan("Perpustakaan Pusat")

perpustakaan.pinjam_buku(mahasiswa, "Pemrograman Python")