class RumahSakit:
    def obat(self):
        return "Paracetamol"

class Apotik(RumahSakit):
    def obat(self):
        return "Ibu profet"

apotik = Apotik()
print(apotik.obat()) 