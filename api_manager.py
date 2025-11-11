import requests
from typing import Any

## jadiin variabel global dan jadiin konstanta (gede semua)
URL_DASAR = "https://api.thecatapi.com/v1"
LOKET_GAMBAR = "/images/search" # <-- beda sama loket breeds
LOKET_RAS = "/breeds"
ID_CARD = {
    "x-api-key": "live_wQ6pRMkN6Jmw172E9eHDcCxocqFFhPjSzIJglUKfrlIBvYj8CTFGQdm8p2L3gInH"
}

def tampilkan_foto_kucing_random():
    params: dict[str, Any] ={
        "limit": 10
    }
    
    try:
        
        hasil = requests.get(URL_DASAR + LOKET_GAMBAR, headers= ID_CARD, params= params)
    
        if hasil.status_code == 200:
            json_dict_rapi = hasil.json()
            '''
            for i in range(len(json_dict_rapi)):
                url_gambar_kucing = json_dict_rapi[i]["url"]
                print(url_gambar_kucing)'''
            for kucing in json_dict_rapi: ## wah iya anying, kan di python itu udah langsung ngabsenin list, ga perlu pake index
                url_gambar_kucing = kucing["url"]
                print(url_gambar_kucing)
            ## soalnya ini juga: 
            # Masalahnya (Bug #2 - LEBIH BAHAYA): Lo minta 10 foto. Gimana kalo API-nya (buat ras tertentu) cuma punya 3 foto? json_dict_rapi lo isinya cuma 3. Pas looping lo nyoba ngambil json_dict_rapi[3], program lo bakal CRASH dengan IndexError.
        else:
            print(hasil.text)
        
    except requests.exceptions.ConnectionError:
        print("ga ada koneksi woyy")
        
    except Exception as error:
        print(f"ada error {error} nih")
    

def tampilkan_semua_ras():
    
    try: 
        hasil = requests.get(URL_DASAR+LOKET_RAS, headers= ID_CARD)
        
        if hasil.status_code == 200:
            json_dict_rapi = hasil.json()
            '''
            for i in range(0, len(json_dict_rapi)):
                macam_ras = json_dict_rapi[i]["breeds"]
                print(macam_ras)'''
            for ras in json_dict_rapi: # <-- Loop tiap ras di list
                # Ambil 'name' dan 'id' nya, BUKAN 'breeds'
                print(f"Nama Ras: {ras['name']}, ID: {ras['id']}")
        else:
            print(hasil.text)

    except requests.exceptions.ConnectionError:
        print("ga ada internet woyy")
    except Exception as error:
        print(f"ada error {error} nih")
        
        
def tampilkan_foto_kucing_ras(ras: str):
    params: dict[str, Any] = {
        'limit': 10,
        'breed_ids': ras
    }
    
    try:
        hasil = requests.get(URL_DASAR + LOKET_GAMBAR, headers= ID_CARD, params= params)
    
        if hasil.status_code == 200:
            json_dict_rapi = hasil.json()
            
            if json_dict_rapi: ## ngecek apakah json_dict_rapi ini ada apa ngga, wow, bisa gini ya, cool
                for kucing in json_dict_rapi:
                    url_gambar_kucing = kucing["url"]
                    print(url_gambar_kucing)
            else:
                print("ngawur lu")
            '''for i in range(0, 9):
                url_gambar_kucing = json_dict_rapi[i]["url"]
                print(url_gambar_kucing)'''
        else:
            print(hasil.text)
    except requests.exceptions.ConnectionError:
        print("ga ada koneksi woyy")
    except Exception as error:
        print(f"ada error {error} nih")
    


def cek_data():
        
    try:
        hasil = requests.get(URL_DASAR + LOKET_RAS, headers=ID_CARD)
    
        if hasil.status_code == 200:
            json_dict_rapi = hasil.json()
            
            # --- NAH, DI SINILAH "RAHASIA"-NYA ---
            # 
            # SEBELUM lo looping, lo "intip" dulu 1 barang aja
            # Coba tambahin baris ini SEMENTARA:
            print("--- ISI CONTOH 1 BARANG ---")
            print(json_dict_rapi[0]) 
            print("----------------------------")
        else:
            print(hasil.text)
        
    except requests.exceptions.ConnectionError:
        print("ga ada koneksi woyy")
    except Exception as error:
        print(f"ada error {error} nih")