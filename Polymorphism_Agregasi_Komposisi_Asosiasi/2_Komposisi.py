class Modul:
    def __init__(self, judul):
        self.judul = judul

class MataKuliah:
    def __init__(self, nama, kode):
        self.nama = nama
        self.kode = kode
        self.modul = []

    def tambah_modul(self, judul):
        modul = Modul(judul)
        self.modul.append(modul)

# Implementasi Komposisi
mk = MataKuliah("Algoritma", "A101")
mk.tambah_modul("Pendahuluan Algoritma")
mk.tambah_modul("Sorting dan Searching")

print(f"Mata Kuliah {mk.nama} memiliki modul: ")
for modul in mk.modul:
    print(f"- {modul.judul}")