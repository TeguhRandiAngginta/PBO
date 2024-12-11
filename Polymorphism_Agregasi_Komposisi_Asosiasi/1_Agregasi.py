class Matakuliah:
    def __init__(self, nama, kode):
        self.nama = nama
        self.kode = kode

class Dosen:
    def __init__(self, nama):
        self.nama = nama
        self.mata_kuliah = []

    def tambah_mata_kuliah(self, mata_kuliah):
        self.mata_kuliah.append(mata_kuliah)

# Implementasi Agregasi
mk1 = Matakuliah("Pemrograman", "P101")
mk2 = Matakuliah("Struktur Data", "S102")

dosen = Dosen("Dr. Ahmad")
dosen.tambah_mata_kuliah(mk1)
dosen.tambah_mata_kuliah(mk2)

print (f"Dosen {dosen.nama} mengajar: ")
for mk in dosen.mata_kuliah:
    print(f"- {mk.nama} ({mk.kode})")