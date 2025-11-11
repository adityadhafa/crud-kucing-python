# from typing import Any # ini buat type hint
# import json # mau mindah data ke json supaya jadi data permanen ya import json dulu dong

from kucing import Kucing
from manajer_data_kucing import save_data, ambil_data
import api_manager
from rich import print
from rich.panel import Panel
import questionary
from rich.table import Table

import os ## ini buat ngeclear tiap ngulang programnya

# ini itu bisa banget buat di oop-kan ga sih
# pgn tak kembangin sampe oop dan pgn tak kembangin sampee aku panggil API anjing dan kucing, untuk kucing kucingya buk Sai, terus nanti aku pgn tampilin fotonya gitu terus aku mau bikin kaya mini game vs vs an yang mana misal yaa kaya kartu lah, kartu anjing ini dengan kartu kucing ini satu tim misal ,dan 2 vs 2, dan masing masing kartu nyimpen biodatanya sendiri dan kaya semacam powernya gitu lah, ya gitu, kalo ga nanti untuk menang atau ga-nya dirandom aja dah 


    
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



# ini adalah contoh yang mana sebuah fungsi pgnnya dia dibuat untuk menampilkan nilai juga menyimpan atau mereturn nilainya ke dalam sebuah fungsinya, dah gitu
# gimana ya analogi yang paling baiknya buat ke anak kecil gitu
def tanya_ke_user():
    jawaban_user = input("halo namamu siapa? ")
    print(f"halo {jawaban_user}")
    return jawaban_user

# bagian user choice ya

def nyambut_user(): # type hint returnya fungsi -> int
    
    text_nyambut_full = '''
        1. mau ubah/update data"
        "2. mau nambah data kucing
        "3. mau delete data kucing"
        "4. mau tampilin data kucing"
        "5. Exit, udah"
        "6. mau liat foto kucing kah
    '''
    
    ## ternyata cara multi line string itu pake ''' ... ''' toh.. oke
    
    # Contoh pake hiasan
    panel_hias = Panel(
        text_nyambut_full,# Teks-nya
        title="[bold]DATABASE KUCING BUK SAI[/bold]",          # Nambahin judul
        border_style="green"                          # Ganti warna bingkainya
    )
    
    print(panel_hias)
    
    status = False
    while status == False:
        try:
            user_choice = questionary.select("mau ngapain?", choices=[
                                "1. mau ubah/update data", 
                                "2. mau nambah data kucing",
                                "3. mau delete data kucing",
                                "4. mau tampilin data kucing",
                                "5. Exit, udah",
                                "6. mau liat foto kucing kah"
                                ]).ask()
            ## nanti si questionary ini bakal ngereturn full text soalnya
            status = True
            angka = user_choice[0] ## ambil huruf pertamanya aja dari full stringnya, yaitu nanti yang kena bakal angka nomernya doang
            return int(angka) ## nah terus dari yang awalnya character jadiin integer deh
        except Exception as e:
            print(f"{e}")
    '''
    # ini cara ngedefine variabel langsung dengan tipe datanya, ini ga ngedefine sih, ini cuma ngetype hint doang biar si pylance diem
    status = False # variabel Boolean tuh manja banget, harus ada value awalnya dulu loh
    # oh iya ya bener juga, kita bisa bikin while true di sini pokonya sampe user itu masukin yang benar, yaitu masukin angka
    while status == False:
        try: # karena bisa jadi user malah input "satu" yang ga bisa diubah sama int.
            #jadi intinya itu ya, try yang bener terus return yang bener
            message_one =  questionary.select("mau ngapain?", choices=[
                                "1. mau ubah/update data", 
                                "2. mau nambah data kucing",
                                "3. mau delete data kucing",
                                "4. mau tampilin data kucing",
                                "5. Exit, udah",
                                "6. mau liat foto kucing kah"
                                ])
            status = True
            return message_one # kalo misalnya di coba dan berhasil yaa langsung return aja
        except ValueError: # dan intinya, except (atau) keculai yang try/yang bener itu maka return atau lakukan ini, gitu, biar ga crash
            print("itu bukan angka buset, tulis cuma ANGKA doang aja") # ga perlu pake print langsung return aja
                    # gimana kalo misalnya ini return nyambut_user() lagi biar yaa ngulang lagi kan?
                    # aku jujur masih ga tau sih gimana cara kerjanya try dan except ini, apakah otomatis ngulang apa gimana
    # "memaksa" user ngasih jawaban bener. 
    # ya jangan nge return pesan error dong, masa nanti di variabel yang kesimpen yang pake fungsi ini isinya pesan error
    # makanya kita paksa dan ulang ulang terus aja itu si user buat sampe bener
    '''

        

'''def lower_upper_okay(masukan: str, yang_sebenarnya:str):
    return masukan.strip().lower() == yang_sebenarnya.strip().lower() # langsung aja ini kan ngereturn boolean ya, sebenernya bisa langsung diterapin kaya di bawah, jadi ya sama aja, kan hasilnya boolen if true yakan
    #jadi ini logikanya itu ya kalo misalnya katanya sama tapi cuma beda uppercase atau loweercase aja di bebrapa hurufnya, yaa langsung di lowercase aja semuanya kalo semuanya sama sama lowercase dan kalo katanya itu kata yang sama maka ya pasti bakal true dong yakan
    '''

'''def cari_kucing(nama_kucing_dicari: str): # Optional (bisa None atau ga ngembaliin apa apa). Optional[type]
    for each_kucing in daftar_kucingnya_buk_sai:
        if nama_kucing_dicari.strip().lower() == each_kucing["nama"].strip().lower(): # or sebenenrya ini ya kalo pake lower_upper_okay() itu jadinya if lower_upper_okay(nama_kucing_dicari, satu_data_kucing["nama"])
            # retun satu_data_kucing, gitu. tp ini bakal kelamaan soalnya make dua blender sekaligus. lompat lompat juga
            return each_kucing
            #kalo habis return itu yaudah berhentu dan ngereturn itu, gitu kalo fungsi itu
    return None # makanya ini disini gapapa sebagai default returnnya
'''

def cari_kucing_object_version(nama_kucing_dicari: str):
    for each_kucing in daftar_kucingnya_buk_sai:
        if nama_kucing_dicari.strip().lower() == each_kucing.nama.strip().lower():
            return each_kucing # return 'object' kucing itu. var each_kucing kan objek di list daftar_kucingnya_buk_sai
    return None

            
        
            
            

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
daftar_kucingnya_buk_sai: list[Kucing] = ambil_data() # langsung jadi list of dict
# yang atas udah ga kepake. yang kepake yang ini:

user_choice = nyambut_user()

while user_choice != 5:
    match user_choice:
        case 2:
            '''nama_baru = input("masukkan nama kucing buk Sai: ")
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
            # append itu fungsi bawaannya list buatt masukin data baruu langsung ke paling belakang tapi, dan ini cara paling aman paling real'''
            
            ask_user_to_add_kucing_baru()
            save_data(daftar_kucingnya_buk_sai)

        case 1: # UPDATE
            # kalo mau liat data kucingnya siapa aja pake case read aja berarti kalo gitu yaa
            siapa_yang_mau_diubah = str(input("datanya siapa yang mau diubah? "))
            kucing_object = cari_kucing_object_version(siapa_yang_mau_diubah)
            kucing_object = cari_kucing_object_version(siapa_yang_mau_diubah)
            if kucing_object != None:
                print("Mau ubah apa? 1. Nama, 2. Hobi") # <-- Lo yang nanya
                pilihan_ubah = input("Pilih: ")
                if pilihan_ubah == "1":
                    nama_baru = input("Nama barunya apa? ") # <-- Lo yang nanya
                    kucing_object.set_nama(nama_baru) # <-- Suruh si object buat diem2 ganti nama
                else:
                    hobi_baru = input("Hobi barunya apa? ")
                    kucing_object.set_hobi(hobi_baru)
                # ...dan seterusnya...
            '''if kucing_object != None:
                kucing_object.ubah_data_salah_satu_kucing()
                save_data(daftar_kucingnya_buk_sai)
            else:
                print("buk sai ga punya mucing itu woyy")'''
            '''if data_kucing != None:
                ingin_ubah_data_yang = input("mau ubah data kucing yang mana? ketik salah satu dari 1. nama, 2. hobi, 3. sifat, 4. spot nongkrong: ")
                if ingin_ubah_data_yang == "nama":
                    nama_update = input("masukkan nama baru: ") # kalo langsung sama dengan gini ya jadinya dia nimpa valuenya
                    data_kucing.nama = nama_update
                elif ingin_ubah_data_yang == "hobi":
                    hobi_update = input("masukkan hobi baru: ")
                    data_kucing.hobi = hobi_update
                elif ingin_ubah_data_yang == "sifat":
                    sifat_update = input("masukkan sifat-sifat barunya: ").split(", ") # di split aja biar jadi list
                    data_kucing.sifat = sifat_update
                else:
                    spot_nongkrong_update = input("masukkan update-an spot nongkrongnya: ").split(", ")
                    data_kucing.spot_nongkrong = spot_nongkrong_update
            else:
                print("hah apa sih") # masa aku ngeprint gini doang'''
                
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
            
        case 4: # NAMPILKAN DATA 
            
            '''
            print("nama nama kucing yang kita punya saat ini: ") # bener juga ya harusnya ini di sini
            for each_kucing in daftar_kucingnya_buk_sai:
                print(each_kucing.nama) # gausah pake \n (newline) kalo for loopnya python ngabsenin ya otomatis new line kok
            '''
            
            #artinya adalah data kucingnya itu ada untuk ditampilin maka do this # pastikan ajaa dulu data_kucingnya itu ga none untuk masuk ke pengerjaan di bawahnya
            '''print(f"nama: {data_kucing["nama"]}")
                print(f"hobinya: {data_kucing['hobi']}")
                print(f"sifatnya: {", ".join(data_kucing["sifat"])}")
                print(f"suka nongkrong di: {", ".join(data_kucing["spot nongkrong"])}")'''
                # break itu buat ngebreak loop
                
                
            
            status = False
            angka: int
            while status == False:
                try:
                    user_choice = questionary.select("mau nampilkan?", choices=[
                                        "1. tampilin data salah satu kucing", 
                                        "2. tampilin semua kucing yang ada",
                                        ]).ask()
                    ## nanti si questionary ini bakal ngereturn full text soalnya
                    angka = int(user_choice[0]) ## ambil huruf pertamanya aja dari full stringnya, yaitu nanti yang kena bakal angka nomernya doang
                    if type(angka) == int:
                        status = True
                    
                    if angka == 1:
                        nama_dicari = input("masukkan nama kucing yang mau ditampilkan: ")
                        siapa_yang_ditampilin = input("siapa yang mau ditampilin datanya? ")
                        data_kucing = cari_kucing_object_version(siapa_yang_ditampilin)

                        if data_kucing:
                            
                            ## pake panel aja biar bagus
                            
                            full_text = f'''
                                nama: {data_kucing.nama}
                                hobi: {data_kucing.hobi}
                                sifat: {",".join(data_kucing.sifat)}
                                spot nongkrong: {",".join(data_kucing.spot_nongkrong)}
                            '''
                            
                            kotak_panel = Panel(
                                full_text,
                                title=data_kucing.nama,
                                border_style= "green"
                            )
                            
                            print(kotak_panel)
                            
                        else:
                            print("tidak ada mucingnya buk Sai yang namanya ituu woy")
                    else:
                        # --- Langkah 1 & 2: Bikin Meja & Kolom ---

                        # 1. Bikin objek mejanya
                        tabel_kucing = Table(title="[bold]Daftar Kucing[/bold]")

                        # 2. Bikin header kolom-kolomnya
                        tabel_kucing.add_column("Nama Kucing", style="cyan", justify="left")
                        tabel_kucing.add_column("Hobi", style="magenta", justify="right")
                        tabel_kucing.add_column("Sifat", style="green")

                        # --- Langkah 3: Isi Datanya ---
                        # (Di project beneran, ini lo lakuin di dalem 'for loop')
                        
                        for each_kucing in daftar_kucingnya_buk_sai:
                            tabel_kucing.add_row(each_kucing.nama, each_kucing.hobi, ", ".join(each_kucing.sifat))

                        # --- Langkah Terakhir: Tampilkan Mejanya ---
                        print(tabel_kucing)
                
                except Exception as e:
                    print(f"{e}")
                


            
        case 3: # DELETE
            # bagian delete
            nama_mau_dihapus = input("mau ngehapus datanya siapa? (ketik namanya) ")
            data_kucing = cari_kucing_object_version(nama_mau_dihapus)

            if data_kucing != None:
                daftar_kucingnya_buk_sai.remove(data_kucing) # remove itu fungsi bawaan list yang langsung ngeremove satu data di satu index list lgsg

            else:
                print("tidak ada mucingnya buk Sai yang namanya ituu woy")
                
            save_data(daftar_kucingnya_buk_sai)

        case 6:
            print("Mau foto kucing apa?")
            print("1. Foto acak aja")
            print("2. Foto berdasarkan ras (misal Bengal)")
            print("3. Cek daftar ID ras dulu")

            pilihan_api = input("Pilih (1/2/3): ")

            if pilihan_api == "1":
                print("Lagi minta foto ke server...")
                hasil_url = api_manager.tampilkan_foto_kucing_random()
                print(hasil_url)

            elif pilihan_api == "2":
                ras_id = input("Masukkan 4 huruf ID ras (misal 'beng' buat Bengal): ")
                print(f"Lagi nyari foto ras '{ras_id}'...")
                hasil_url = api_manager.tampilkan_foto_kucing_ras(ras_id)
                print(hasil_url)

            elif pilihan_api == "3":
                print("Lagi ngambil daftar ras...")
                daftar_ras = api_manager.tampilkan_semua_ras
                print("--- DAFTAR RAS KUCING ---")
                print(daftar_ras)

            else:
                print("Pilihan nggak ada.")
        
        case _: # in case none (_)
            print("Pilihan tidak dikenal, coba lagi ya!")

    user_choice = nyambut_user()

    '''if user_choice == 5:
        break   ''' # i don't even need this wokaokwo, karena while loop ya otomatis udah selalu ngecek kondisinya sendiri
                    # soalnya kan user choicenya selalu diupdate jugaa kan setiap masuk ke whil loop
