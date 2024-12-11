class Perpustakaan:
    def _init_(self, buku, penerbit):
        self.buku = buku
        self.penerbit = penerbit

class Jurnal(Perpustakaan):
    def _init_(self, buku, penerbit, tahun):
        super()._init_(buku, penerbit)
        self.tahun = tahun
    
    def peminjaman(self):
        print(f"JUDUL :{self.buku}, PENERBIT : {self.penerbit}, TAHUN : {self.tahun}")
            
pinjam = Jurnal("AVATAR", "UVUTUR", "2000")
pinjam.peminjaman()