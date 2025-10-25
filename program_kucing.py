from typing import Any # ini buat type hint
import json # mau mindah data ke json supaya jadi data permanen ya import json dulu dong

# ini itu bisa banget buat di oop-kan ga sih
# pgn tak kembangin sampe oop dan pgn tak kembangin sampee aku panggil API anjing dan kucing, untuk kucing kucingya buk Sai, terus nanti aku pgn tampilin fotonya gitu terus aku mau bikin kaya mini game vs vs an yang mana misal yaa kaya kartu lah, kartu anjing ini dengan kartu kucing ini satu tim misal ,dan 2 vs 2, dan masing masing kartu nyimpen biodatanya sendiri dan kaya semacam powernya gitu lah, ya gitu, kalo ga nanti untuk menang atau ga-nya dirandom aja dah 


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
        print(f" namanya {self.nama}, hobinya {self.hobi}, sifatnya {", ".join(self.sifat)}, sukanya nongkrong di {", ".join(self.spot_nongkrong)}") # aku juga mau sekaligus dia ini emang beneran melakukan pengeprint-an teks, jadi ga cuma nyimpen doang, jadi dia/fungsi ini bisa nyimpen value dan value yang disimpan itu bisa dipake variabel atau fungsi lain, kemudiaan fungsi ini ketika dipanggil juga akan melakukan sesuatu yaitu print itu tadi yang mana melakukan sesuatu ini yaa ga bisa di pake sama fungsi lain soalnya yaa ini kan yang lakuin tampilkan informasi kucing. hah gimana sih penjelasannya wkkw. ya pookonya gitu lah
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
    def simpan_data_kucing_to_dict(self):
        # hmm ini itu ngubaha jadi list of dictionary ya berarti supaya bisa dibaca json
        data_kucing_saat_ini: dict[str, Any] = {
            "nama": self.nama,
            "hobi": self.hobi,
            "sifat": self.sifat,
            "spot nongkrong": self.spot_nongkrong
        }
        
        # nih kata bang geminai: Tugas class Kucing adalah ngurus satu kucing (dirinya sendiri, self). Jadi, fungsi ini harusnya cuma return satu dict aja, yang isinya data self. bener juga sih, mantap mantap
        
        return data_kucing_saat_ini
    
    # kalo mau nambah data kucing baru kan ya tinggal ini ya, tinggal bikin object baru dari class
    # nah kalo mau delete/remove data kucingnya gimana?
    
    
def ask_user_to_add_kucing_baru(): # gini bener ga ya, bener ternyata kata bang geminai
    print("yok masukkan data kucing (baru): ")
    nama = input("masukin namanya: ")
    hobi = input("hobinya apa? ")
    sifat:list[str] = input("sifat-sifatnya gimana? ").split(", ") # justru pakein split supayaa nanti string fullnya client yang diketik full pake komaa itu bisa pisah pisah jadi list of daftar yangg bisa dipisah pisa gitu berdasarkan komanyaa
    spot_nongkrong: list[str] = input("biasanya suka nongkrong di mana aja? ").split(", ")
    data_kucing_yang_dibuat = Kucing(
        nama,
        hobi,
        sifat,
        spot_nongkrong
    )
    
    daftar_kucingnya_buk_sai.append(data_kucing_yang_dibuat) 
    # return data_dict
    # ga perlu return kek nya, karena emang fungsi ini ga perlu nyimpen apa apa yang bakal kepakee sama fungsi lain sih, yakan, ini bukan alat yang menghasilkan jus untuk diolah sama mesin/orang lain gitu? yakan? idk ma

def ubah_list_dari_json_ke_objek(nama:str, hobi: str, sifat: list[str], spot_nongkrong: list[str]):
    data_kucing_yang_dibuat_jadi_objek = Kucing(
        nama,
        hobi,
        sifat,
        spot_nongkrong
    )
    return data_kucing_yang_dibuat_jadi_objek

# ini adalah contoh yang mana sebuah fungsi pgnnya dia dibuat untuk menampilkan nilai juga menyimpan atau mereturn nilainya ke dalam sebuah fungsinya, dah gitu
# gimana ya analogi yang paling baiknya buat ke anak kecil gitu
def tanya_ke_user():
    jawaban_user = input("halo namamu siapa? ")
    print(f"halo {jawaban_user}")
    return jawaban_user

# bagian user choice ya

def nyambut_user(): # type hint returnya fungsi -> int
    print("halo selamat datang di database kucingnya buk Sai!")
    print("1. mau ubah/update data")
    print("2. mau nambah data kucing")
    print("3. mau delete data kucing")
    print("4. mau tampilin data kucing")
    print("5. Exit, udah")
    
    message_one:  int # ini cara ngedefine variabel langsung dengan tipe datanya, ini ga ngedefine sih, ini cuma ngetype hint doang biar si pylance diem
    status = False # variabel Boolean tuh manja banget, harus ada value awalnya dulu loh
    # oh iya ya bener juga, kita bisa bikin while true di sini pokonya sampe user itu masukin yang benar, yaitu masukin angka
    while status == False:
        try: # karena bisa jadi user malah input "satu" yang ga bisa diubah sama int.
            #jadi intinya itu ya, try yang bener terus return yang bener
            message_one = int(input("mau ngapain? (tulis aja nomornya) "))
            status = True
            return message_one # kalo misalnya di coba dan berhasil yaa langsung return aja
        except ValueError: # dan intinya, except (atau) keculai yang try/yang bener itu maka return atau lakukan ini, gitu, biar ga crash
            print("itu bukan angka buset, tulis cuma ANGKA doang aja") # ga perlu pake print langsung return aja
                    # gimana kalo misalnya ini return nyambut_user() lagi biar yaa ngulang lagi kan?
                    # aku jujur masih ga tau sih gimana cara kerjanya try dan except ini, apakah otomatis ngulang apa gimana
    # "memaksa" user ngasih jawaban bener. 
    # ya jangan nge return pesan error dong, masa nanti di variabel yang kesimpen yang pake fungsi ini isinya pesan error
    # makanya kita paksa dan ulang ulang terus aja itu si user buat sampe bener


        

def lower_upper_okay(masukan: str, yang_sebenarnya:str):
    return masukan.strip().lower() == yang_sebenarnya.strip().lower() # langsung aja ini kan ngereturn boolean ya, sebenernya bisa langsung diterapin kaya di bawah, jadi ya sama aja, kan hasilnya boolen if true yakan
    #jadi ini logikanya itu ya kalo misalnya katanya sama tapi cuma beda uppercase atau loweercase aja di bebrapa hurufnya, yaa langsung di lowercase aja semuanya kalo semuanya sama sama lowercase dan kalo katanya itu kata yang sama maka ya pasti bakal true dong yakan

def cari_kucing(nama_kucing_dicari: str): # Optional (bisa None atau ga ngembaliin apa apa). Optional[type]
    for each_kucing in daftar_kucingnya_buk_sai:
        if nama_kucing_dicari.strip().lower() == each_kucing["nama"].strip().lower(): # or sebenenrya ini ya kalo pake lower_upper_okay() itu jadinya if lower_upper_okay(nama_kucing_dicari, satu_data_kucing["nama"])
            # retun satu_data_kucing, gitu. tp ini bakal kelamaan soalnya make dua blender sekaligus. lompat lompat juga
            return each_kucing
            #kalo habis return itu yaudah berhentu dan ngereturn itu, gitu kalo fungsi itu
    return None # makanya ini disini gapapa sebagai default returnnya


def cari_kucing_object_version(nama_kucing_dicari: str):
    for each_kucing in daftar_kucingnya_buk_sai:
        if nama_kucing_dicari.strip().lower() == each_kucing.name.strip().lower():
            return each_kucing

def save_data():
    with open("data_kucing_buk_sai.json", "w") as file: # "w" itu maksudnya write, write itu artinya ya dari data masukan kita di python di write ke json
        json.dump(daftar_kucingnya_buk_sai, file, indent=4)

def ambil_data():
    with open("data_kucing_buk_sai.json", "r") as file: # kalo "r" itu maksudnya read, ya artinya kita read/baca file json jadii ke data python gitu
        try: 
            daftar_kucingnya_buk_sai_di_json = json.load(file)
            list_kucing_buk_sai_in_object : list[object] = []
            for each_kucing in daftar_kucingnya_buk_sai_di_json:
                sementara = ubah_list_dari_json_ke_objek(each_kucing["nama"], each_kucing["hobi"], each_kucing["sifat"], each_kucing["spot_nongkrong"]) # ini kan dia di sini berubah jadi object ya satu persatu, teurs.. kita simpen ke list pakee append gitu kah? hmm kucing banget lah
                list_kucing_buk_sai_in_object.append(sementara)
            return list_kucing_buk_sai_in_object # atau sebenenrya ya bisa aja langsung return json.load(file) biar lgsg return jsonnya langsung ngeload filenya
        except:
            list_kucing_buk_sai_in_object: list[object] = [] # define dulu list kosongannya di sini
            return list_kucing_buk_sai_in_object # ga boleh nge defin langsung di return ya
        '''except FileNotFoundError:
            daftar_kucingnya_buk_sai_di_json: list[dict[str, Any]] = []
            return daftar_kucingnya_buk_sai_di_json
        except json.decoder.JSONDecodeError:
            daftar_kucingnya_buk_sai_di_json: list[dict[str, Any]] = []
            return daftar_kucingnya_buk_sai_di_json'''

            
        
            
            

'''daftar_kucingnya_buk_sai: list[dict[str, Any]] = [
    { # kucing pertama, paling nakal, dan artinya ini di indeks ke 0 dari listnya
        "nama": "acip",
        "hobi": "mengais sampah",
        "sifat": ["pemarah", "maong maong"],
        "spot nongkrong": ["kantin", "kelas"]
    },
    {
        "nama": "cemong",
        "hobi": "ga tau",
        "sifat": ["pendiam", "meing meing"],
        "spot nongkrong": ["kantin"]
    },
    {
        "nama": "mucing",
        "hobi": "mengeong",
        "sifat": ["maong meong", "eek di lapangan"],
        "spot nongkrong": ["everywhere"]
    }
]'''

# bisa kaya gini nih
daftar_kucingnya_buk_sai: list[object] = ambil_data() # langsung jadi list of dict
# yang atas udah ga kepake. yang kepake yang ini:

user_choice = nyambut_user()

while user_choice != 5:
    match user_choice:
        case 2:
            nama_baru = input("masukkan nama kucing buk Sai: ")
            hobi_baru = input("masukkan hobi kucing buk Sai: ")
            sifat_baru = input("masukkan sifat-sifat kucing buk Sai: ").split(", ") # ini nanti bakal jadi list yang di split berdasarkan koma dan spasinya ", "
            spot_nongkrong_baru = input(
                "masukkan spot-spot nongkrong kucingnya buk Sai: "
            ).split(", ")

            kucing_baru: dict[str, Any] = {
                "nama": nama_baru,
                "hobi": hobi_baru,
                "sifat": sifat_baru,
                "spot nongkrong": spot_nongkrong_baru,
            }
            daftar_kucingnya_buk_sai.append(kucing_baru)  # masukin dict kucing_baru ke daftar_kucingnya_buk_sai
            # append itu fungsi bawaannya list buatt masukin data baruu langsung ke paling belakang tapi, dan ini cara paling aman paling real
            
            save_data()

        case 1: # UPDATE
            # kalo mau liat data kucingnya siapa aja pake case read aja berarti kalo gitu yaa
            siapa_yang_mau_diubah = str(input("datanya siapa yang mau diubah? "))
        
            
            data_kucing = cari_kucing(siapa_yang_mau_diubah)
            
            '''if data_kucing != None:  # kalo nama_yang_mau_diubah ada di dict nama nama kucing
                ingin_ubah_data_yang = input("mau ubah data kucing yang mana? ketik salah satu dari 1. nama, 2. hobi, 3. sifat, 4. spot nongkrong: ")
                if ingin_ubah_data_yang == "nama":
                    nama_update = input("masukkan nama baru: ") # kalo langsung sama dengan gini ya jadinya dia nimpa valuenya
                    data_kucing["nama"] = nama_update
                elif ingin_ubah_data_yang == "hobi":
                    hobi_update = input("masukkan hobi baru: ")
                    data_kucing["hobi"] = hobi_update
                elif ingin_ubah_data_yang == "sifat":
                    sifat_update = input("masukkan sifat-sifat barunya: ").split(", ") # di split aja biar jadi list
                    data_kucing['sifat'] = sifat_update
                else:
                    spot_nongkrong_update = input("masukkan update-an spot nongkrongnya: ").split(", ")
                    data_kucing["spot nongkrong"] = spot_nongkrong_update
            else:
                print("tidak ada mucingnya buk Sai yang namanya ituu woy")'''
            
                
            
            
            # harusnya cukup gini aja
            # karena nilai status_cari yang di awal udah di set defaultnya, maka kalo ketemu true, kalo ga ya passti defaultnya itu false

            save_data()
            
        case 4: # NAMPILKAN DATA 
            print("nama nama kucing yang kita punya saat ini: ") # bener juga ya harusnya ini di sini
            for each_kucing in daftar_kucingnya_buk_sai:
                print(each_kucing["nama"]) # gausah pake \n (newline) kalo for loopnya python ngabsenin ya otomatis new line kok

            siapa_yang_ditampilin = input("siapa yang mau ditampilin datanya? atau mau liat full semua? (type: full)")
            data_kucing = cari_kucing(siapa_yang_ditampilin)

            if siapa_yang_ditampilin == "full":
                # nampilin data dengan rapi, maka kudu dipisah?
                for kucing in daftar_kucingnya_buk_sai:
                    print(f"{kucing['nama']} hobinya {kucing['hobi']}, sifatnya {", ".join(kucing['sifat'])}, dan suka nongkrong di {", ".join(kucing['spot nongkrong'])}\n")

            elif data_kucing != None: # pastikan ajaa dulu data_kucingnya itu ga none untuk masuk ke pengerjaan di bawahnya
                print(f"nama: {data_kucing["nama"]}")
                print(f"hobinya: {data_kucing['hobi']}")
                print(f"sifatnya: {", ".join(data_kucing["sifat"])}")
                print(f"suka nongkrong di: {", ".join(data_kucing["spot nongkrong"])}")
                # break itu buat ngebreak loop
            else:
                print("tidak ada mucingnya buk Sai yang namanya ituu woy")

        case 3: # DELETE
            # bagian delete
            nama_mau_dihapus = input("mau ngehapus datanya siapa? (ketik namanya) ")
            data_kucing = cari_kucing(nama_mau_dihapus)

            if data_kucing != None:
                daftar_kucingnya_buk_sai.remove(data_kucing) # remove itu fungsi bawaan list yang langsung ngeremove satu data di satu index list lgsg

            else:
                print("tidak ada mucingnya buk Sai yang namanya ituu woy")
                
            save_data()

        case _: # in case none (_)
            print("Pilihan tidak dikenal, coba lagi ya!")

    user_choice = nyambut_user()

    '''if user_choice == 5:
        break   ''' # i don't even need this wokaokwo, karena while loop ya otomatis udah selalu ngecek kondisinya sendiri
                    # soalnya kan user choicenya selalu diupdate jugaa kan setiap masuk ke whil loop
