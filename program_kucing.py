from kucing import Kucing
from manajer_data_kucing import save_data, ambil_data
import api_manager
from rich import print
from rich.panel import Panel
import questionary
from rich.table import Table

import os ## ini buat ngeclear tiap ngulang programnya

# bagian user choice ya
def nyambut_user(): # type hint returnya fungsi -> int
    
    text_nyambut_full = '''
        Haloo selamat datang di database kucingnya Buk Saii
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

def cari_kucing_object_version(nama_kucing_dicari: str):
    for each_kucing in daftar_kucingnya_buk_sai:
        if nama_kucing_dicari.strip().lower() == each_kucing.nama.strip().lower():
            return each_kucing # return 'object' kucing itu. var each_kucing kan objek di list daftar_kucingnya_buk_sai
    return None

# bisa kaya gini nih
daftar_kucingnya_buk_sai: list[Kucing] = ambil_data() # langsung jadi list of dict
# yang atas udah ga kepake. yang kepake yang ini:

user_choice = nyambut_user()

while user_choice != 5:
    os.system('cls' if os.name == 'nt' else 'clear')
    match user_choice:
        case 2:
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

            save_data(daftar_kucingnya_buk_sai)
            
            ## pake panel aja biar bagus
            full_text = f'''
                nama: {data_kucing_yang_dibuat.nama}
                hobi: {data_kucing_yang_dibuat.hobi}
                sifat: {",".join(data_kucing_yang_dibuat.sifat)}
                spot nongkrong: {",".join(data_kucing_yang_dibuat.spot_nongkrong)}
            '''
            
            kotak_panel = Panel(
                full_text,
                title="data kucing berhasil disimpan dan ditambahkan!",
                border_style= "green"
            )
            
            print(kotak_panel)

        case 1: # UPDATE
            # kalo mau liat data kucingnya siapa aja pake case read aja berarti kalo gitu yaa
                    # 1. Bikin objek mejanya
            tabel_kucing = Table(title="[bold]Daftar Kucing[/bold]")

            # 2. Bikin header kolom-kolomnya
            tabel_kucing.add_column("Nama Kucing", style="cyan", justify="left")
            tabel_kucing.add_column("Hobi", style="magenta")
            tabel_kucing.add_column("Sifat", style="green")
            tabel_kucing.add_column("Spot Nongkrong", style="green")

            # --- Langkah 3: Isi Datanya ---
            # (Di project beneran, ini lo lakuin di dalem 'for loop')
            
            for each_kucing in daftar_kucingnya_buk_sai:
                tabel_kucing.add_row(each_kucing.nama, each_kucing.hobi, ", ".join(each_kucing.sifat), ", ".join(each_kucing.spot_nongkrong))

            # --- Langkah Terakhir: Tampilkan Mejanya ---
            print(tabel_kucing)
            
            siapa_yang_mau_diubah = str(input("datanya siapa yang mau diubah? "))
            kucing_object = cari_kucing_object_version(siapa_yang_mau_diubah)
            
            pilihan_update = questionary.select("Pilih mau update apa: ", choices=[
                "1. Nama",
                "2. Hobi",
                "3. Sifat",
                "4. Spot Nongkrong"
            ]).ask()
            angka = int(pilihan_update[0])

            if kucing_object:
                if angka == 1:
                    nama_baru = input("masukkan nama baru: ")
                    kucing_object.set_nama(nama_baru= nama_baru)
                elif angka == 2:
                    hobi_baru = input("masukkan hobi baru: ")
                    kucing_object.set_hobi(hobi_baru= hobi_baru)
                elif angka == 3:
                    sifat_baru = input("masukkan sifat-sifat baru: ").split(", ")
                    kucing_object.set_sifat(sifat_baru= sifat_baru)
                else:
                    spot_nongkrong_baru = input("masukkan spot-spot nongkrong: ").split(", ")
                    kucing_object.set_spot_nongkrong(spot_nongkrong_baru= spot_nongkrong_baru)
                
                ## pake panel aja biar bagus
                
                full_text = f'''
                    nama: {kucing_object.nama}
                    hobi: {kucing_object.hobi}
                    sifat: {",".join(kucing_object.sifat)}
                    spot nongkrong: {",".join(kucing_object.spot_nongkrong)}
                '''
                
                kotak_panel = Panel(
                    full_text,
                    title="data berhasil diubah!",
                    border_style= "green"
                )
                
                print(kotak_panel)
                
            else:
                print("kau salah ketik nama woy")
            
            save_data(daftar_kucingnya_buk_sai)
            
        case 4: # NAMPILKAN DATA 
            status = False
            angka: int
            while status == False:
                try:
                    user_choice = questionary.select("Pilih: ", choices=[
                                        "1. tampilin data salah satu kucing", 
                                        "2. tampilin semua kucing yang ada",
                                        ]).ask()
                    ## nanti si questionary ini bakal ngereturn full text soalnya
                    angka = int(user_choice[0]) ## ambil huruf pertamanya aja dari full stringnya, yaitu nanti yang kena bakal angka nomernya doang
                    if type(angka) == int:
                        status = True
                    
                    if angka == 1:
                        siapa_yang_ditampilin = input("masukkan nama kucing yang mau ditampilkan: ")
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
                        tabel_kucing.add_column("Hobi", style="magenta")
                        tabel_kucing.add_column("Sifat", style="green")
                        tabel_kucing.add_column("Spot Nongkrong", style="green")

                        # --- Langkah 3: Isi Datanya ---
                        # (Di project beneran, ini lo lakuin di dalem 'for loop')
                        
                        for each_kucing in daftar_kucingnya_buk_sai:
                            tabel_kucing.add_row(each_kucing.nama, each_kucing.hobi, ", ".join(each_kucing.sifat), ", ".join(each_kucing.spot_nongkrong))

                        # --- Langkah Terakhir: Tampilkan Mejanya ---
                        print(tabel_kucing)
                
                except Exception as e:
                    print(f"{e}")
                
        case 3: # DELETE
            # bagian delete
            
            # 1. Bikin objek mejanya
            tabel_kucing = Table(title="[bold]Daftar Kucing[/bold]")

            # 2. Bikin header kolom-kolomnya
            tabel_kucing.add_column("Nama Kucing", style="cyan", justify="left")
            tabel_kucing.add_column("Hobi", style="magenta")
            tabel_kucing.add_column("Sifat", style="green")
            tabel_kucing.add_column("Spot Nongkrong", style="green")

            # --- Langkah 3: Isi Datanya ---
            # (Di project beneran, ini lo lakuin di dalem 'for loop')
            
            for each_kucing in daftar_kucingnya_buk_sai:
                tabel_kucing.add_row(each_kucing.nama, each_kucing.hobi, ", ".join(each_kucing.sifat), ", ".join(each_kucing.spot_nongkrong))

            # --- Langkah Terakhir: Tampilkan Mejanya ---
            print(tabel_kucing)
            
            nama_mau_dihapus = input("mau ngehapus datanya siapa? (ketik namanya) ")
            data_kucing = cari_kucing_object_version(nama_mau_dihapus)

            if data_kucing:
                daftar_kucingnya_buk_sai.remove(data_kucing) # remove itu fungsi bawaan list yang langsung ngeremove satu data di satu index list lgsg

            else:
                print("tidak ada mucingnya buk Sai yang namanya ituu woy")
                
            save_data(daftar_kucingnya_buk_sai)
            
            print("data berhasil di delete!")
            
            tabel_kucing = Table(title="[bold]Daftar Kucing[/bold]")

            # 2. Bikin header kolom-kolomnya
            tabel_kucing.add_column("Nama Kucing", style="cyan", justify="left")
            tabel_kucing.add_column("Hobi", style="magenta")
            tabel_kucing.add_column("Sifat", style="green")
            tabel_kucing.add_column("Spot Nongkrong", style="green")

            # --- Langkah 3: Isi Datanya ---
            # (Di project beneran, ini lo lakuin di dalem 'for loop')
            
            for each_kucing in daftar_kucingnya_buk_sai:
                tabel_kucing.add_row(each_kucing.nama, each_kucing.hobi, ", ".join(each_kucing.sifat), ", ".join(each_kucing.spot_nongkrong))

            # --- Langkah Terakhir: Tampilkan Mejanya ---
            print(tabel_kucing)

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
                daftar_ras = api_manager.tampilkan_semua_ras()
                print("--- DAFTAR RAS KUCING ---")
                print(daftar_ras)

            else:
                print("Pilihan nggak ada.")
        
        case _: # in case none (_)
            print("Pilihan tidak dikenal, coba lagi ya!")

    input("Tekan Enter untuk lanjut...")
    user_choice = nyambut_user()
