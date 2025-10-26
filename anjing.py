class Anjing:
    def __init__(self, nama: str, hobi: str, sifat: list[str], spot_nongkrong: list[str]):
        self.nama = nama
        self.hobi = hobi
        self.sifat = sifat
        self.spot_nongkrong = spot_nongkrong

    def menggonggong(self):
        return "guk guk"

def buat_anjing_baru():
    nama = input("masukkan nama anjing: ")
    hobi = input("masukkan hobinya anjing: ")
    sifat = input("masukkan sifat-sifatnya anjing: ").split(", ")
    spot_nongkrong = input("masukkan spot nongkrong kucing: ").split(", ")
    anjing = Anjing(
        nama = nama,
        hobi = hobi,
        sifat = sifat,
        spot_nongkrong = spot_nongkrong
    )
    
    return anjing

