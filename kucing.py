# OKEE ini nge-oop in yaa
from typing import Any
class Kucing: # ini blueprint pembuatan produknya
    
    # ini pabrik pembuatan satu-satu produknya
    def __init__(self, nama: str, hobi: str, sifat: list[str], spot_nongkrong: list[str]):
        self.nama = nama
        self.hobi = hobi
        self.sifat = sifat # ini nanti langsung jadi list apa gimana sih
        self.spot_nongkrong = spot_nongkrong # dia itu akan nerima dalam bentuk apapaun, ya ga sih? ga tau juga ya

    # ini skill-skillnya yang dipunyai produk produknya (masing masing produk di blueprint yang sama)
    def mengeong(self): #self parameter itu maksudnya yaa produknya itu sendiri nanti yang meng-skill ini
        print("meong! maong!")

    def set_nama(self, nama_baru: str):
        self.nama = nama_baru

    def set_hobi(self, hobi_baru: str):
        self.hobi = hobi_baru

    def set_sifat(self, sifat_baru: list[str]):
        self.sifat = sifat_baru
    
    def set_spot_nongkrong(self, spot_nongkrong_baru: list[str]):
        self.spot_nongkrong = spot_nongkrong_baru

    def simpan_data_kucing_to_dict(self) -> dict[str, Any]: ## gini ternyata cara ngasih type hint di fungsi, pake ->, bukan ":"
    # Cuma GUE (si 'self') yang tau daleman gue
        return {
            "nama": self.nama,
            "hobi": self.hobi,
            "sifat": self.sifat,
            "spot nongkrong": self.spot_nongkrong # <--- Ini pake spasi, ngikutin JSON lo
        }

    def tampilkan_informasi_kucing(self):

        return(f" namanya {self.nama}, hobinya {self.hobi}, sifatnya {", ".join(self.sifat)}, sukanya nongkrong di {", ".join(self.spot_nongkrong)}")