import json

from kucing import Kucing
from typing import Any


'''def ubah_list_dari_json_ke_objek(nama:str, hobi: str, sifat: list[str], spot_nongkrong: list[str]):
    data_kucing_yang_dibuat_jadi_objek = Kucing(
        nama,
        hobi,
        sifat,
        spot_nongkrong
    )
    return data_kucing_yang_dibuat_jadi_objek'''

def save_data(daftar_kucingnya_buk_sai: list[Kucing]):
    data_kucing_dict: list[dict[str, Any]] = []
    for each_kucing in daftar_kucingnya_buk_sai:
        data_kucing_dict.append(each_kucing.simpan_data_kucing_to_dict())

    # LIST ITU KALO MAU NAMBAHIN PAKE APPEND() BRO, INGET INGET INI, AKU INGETNYA KOK MALAH += TERUS. PAKE APPEND() YAA KALO MAU NAMBAHIN ITEM KE LISTT OKEEE? UDAH JANGAN BINGUNG LAGI
    
    
    with open("data_kucing_buk_sai.json", "w") as file: # "w" itu maksudnya write, write itu artinya ya dari data masukan kita di python di write ke json
        
    # nah di sini itu aku harus nerapin object to dictionary
    
        json.dump(data_kucing_dict, file, indent=4)

def ambil_data():
    with open("data_kucing_buk_sai.json", "r") as file: # kalo "r" itu maksudnya read, ya artinya kita read/baca file json jadii ke data python gitu
        try: 
            daftar_kucingnya_buk_sai_di_json = json.load(file)
            list_kucing_buk_sai_in_object : list[Kucing] = []
            for each_kucing in daftar_kucingnya_buk_sai_di_json:
                satu_per_satu = Kucing(each_kucing["nama"], each_kucing["hobi"], each_kucing["sifat"], each_kucing["spot_nongkrong"])
                # ini kan dia di sini berubah jadi object ya satu persatu, teurs.. kita simpen ke list pakee append gitu kah? hmm kucing banget lah
                list_kucing_buk_sai_in_object.append(satu_per_satu)
            return list_kucing_buk_sai_in_object # atau sebenenrya ya bisa aja langsung return json.load(file) biar lgsg return jsonnya langsung ngeload filenya
        except FileNotFoundError:
            list_kucing_buk_sai_in_object: list[Kucing] = [] # define dulu list kosongannya di sini
            return list_kucing_buk_sai_in_object # ga boleh nge defin langsung di return ya
        except json.JSONDecodeError: 
            list_kucing_buk_sai_in_object: list[Kucing] = [] # define dulu list kosongannya di sini
            return list_kucing_buk_sai_in_object # ga boleh nge defin langsung di return ya
        '''except FileNotFoundError:
            daftar_kucingnya_buk_sai_di_json: list[dict[str, Any]] = []
            return daftar_kucingnya_buk_sai_di_json
        except json.decoder.JSONDecodeError:
            daftar_kucingnya_buk_sai_di_json: list[dict[str, Any]] = []
            return daftar_kucingnya_buk_sai_di_json'''
