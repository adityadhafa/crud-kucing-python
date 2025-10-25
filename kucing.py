
from typing import Any

# OKEE ini nge-oop in yaa
class Kucing: # ini blueprint pembuatan produknya
    
    # ini pabrik pembuatan satu-satu produknya
    def __init__(self, nama: str, hobi: str, sifat: list[str], spot_nongkrong: list[str]):
        self.nama = nama
        self.hobi = hobi
        self.sifat = sifat # ini nanti langsung jadi list apa gimana sih
        self.spot_nongkrong = spot_nongkrong
        self.energi_awal_kucing = 100
        # self.simpan_data_kucing_to_dict() # kalo kaya gini bisa ga sih? 
        # oh ya ini ga perlu ternyata, mending langsung bikin fungsi/mesin aja buatt ngebuat objek dari Class atau prbrik Kucing ini yang mana nanti sekalian manggil fungsi nama_variabel_objek.simpan_data_kucing_to_dict() kaya yang udah kulakuin di fungsi

    # ini skill-skillnya yang dipunyai produk produknya (masing masing produk di blueprint yang sama)
    def mengeong(self): #self parameter itu maksudnya yaa produknya itu sendiri nanti yang meng-skill ini
        print("meong! maong!")

    def tampilkan_informasi_kucing(self):
        # print(f" namanya {self.nama}, hobinya {self.hobi}, sifatnya {", ".join(self.sifat)}, sukanya nongkrong di {", ".join(self.spot_nongkrong)}") # aku juga mau sekaligus dia ini emang beneran melakukan pengeprint-an teks, jadi ga cuma nyimpen doang, jadi dia/fungsi ini bisa nyimpen value dan value yang disimpan itu bisa dipake variabel atau fungsi lain, kemudiaan fungsi ini ketika dipanggil juga akan melakukan sesuatu yaitu print itu tadi yang mana melakukan sesuatu ini yaa ga bisa di pake sama fungsi lain soalnya yaa ini kan yang lakuin tampilkan informasi kucing. hah gimana sih penjelasannya wkkw. ya pookonya gitu lah
        return(f" namanya {self.nama}, hobinya {self.hobi}, sifatnya {", ".join(self.sifat)}, sukanya nongkrong di {", ".join(self.spot_nongkrong)}") # karena ini returnn, jadii dia ini bakal menyimpan hal itu juga, return itu bisa jadi bahasa bayinya adalah "kusimpan value x di fungsi ini" (ya gasih)
        # inget yaa, jangann lupaa, karenaa sifat samaa spot nongkrong ini dia sifatnya adalah listt (pabrik init kita nyimpennya sebagai list langsung), makaa kita butuh joinkan dia semua (listnya) menjadiii satu stringg untuk diprintkan jadi satu stringg yang ga pake kotak kotakk begituu, oke?? gaskan
        #jangan cuma print doang, kembaliin juga namanya
        
    def ubah_data_salah_satu_kucing(self): # jadi tiap satu satu produk kucing dari blueprint ini bisa mengubah datanya lewat/dengna mempunyai fungsi ubah data ini
        
        # kalo pake class gini jadinya ga perlu for-loop dah buat nyocokin namanya, kalo namanya sama baru execute perintahnya, itu kelamaan sih
        print("1. nama")
        print("2. hobi")
        print("3. sifat")
        print("4. spot nongkron")
        ngetik_integer = False
        while ngetik_integer == False:
            nomor_pilihan_user = int(input("mau ubah data yang mana? (ketik nomornya saja) "))
            match nomor_pilihan_user:
                case 1: # case 1: apa (gitu sintaksnya)
                    self.nama = input("masukkan nama yang baru untuk kucing ini: ") # kalo ini mah ga perlu ngereturn, otomatis udah keubah ini namanya si kucing self
                    print(f"okay data sudah terubah ya, nih dia {self.tampilkan_informasi_kucing()}")
                    ngetik_integer = True
                case 2:
                    self.hobi = input("masukkan hobi yang baru untuk kucing ini: ")
                    print(f"okay data sudah terubah ya, nih dia {self.tampilkan_informasi_kucing()}")
                    ngetik_integer = True
                case 3:
                    self.sifat = input("masukkan sifat-sifat baru untuk kucing ini: ").split(", ") # pake split yaa, soalnya user nginputnya pake koma dann banyak biasanya, jadi ntar banyaknya itu bakal langsung jadi list
                    print(f"okay data sudah terubah ya, nih dia {self.tampilkan_informasi_kucing()}")
                    ngetik_integer = True
                case 4: 
                    self.spot_nongkrong = input("masukkan spot nongkrong yang baru untuk kucing ini: ").split(", ")
                    print(f"okay data sudah terubah ya, nih dia {self.tampilkan_informasi_kucing()}") # kalo fungsi itu harus ada gininya: fungsi()
                    ngetik_integer = True
                # ini case kalo unhandled ya
                case _: # ini itu udah kaya if not integer atau if not one of the case case-nya gitu
                    print("woyy pilihanmu ga adaa")
                    
    # data kucing to dictionary
    #ini buat masing masing kucingnya gitu buat nanti dipanggil secara berulang di fungsi lain. anjay
    def simpan_data_kucing_to_dict(self):
        # hmm ini itu ngubaha jadi list of dictionary ya berarti supaya bisa dibaca json
        data_kucing_dict: dict[str, Any] = {
            "nama": self.nama,
            "hobi": self.hobi,
            "sifat": self.sifat,
            "spot nongkrong": self.spot_nongkrong
        }
        
        # nih kata bang geminai: Tugas class Kucing adalah ngurus satu kucing (dirinya sendiri, self). Jadi, fungsi ini harusnya cuma return satu dict aja, yang isinya data self. bener juga sih, mantap mantap
        
        return data_kucing_dict