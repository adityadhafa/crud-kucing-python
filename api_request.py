import requests
from typing import Any

url_or_alamat = "https://api.thecatapi.com/v1"
loket = "/image/search"

# Ini ID Proyek kita (LAMPIRAN ID:)
id_card = {
    "x-api-key": "live_wQ6pRMkN6Jmw172E9eHDcCxocqFFhPjSzIJglUKfrlIBvYj8CTFGQdm8p2L3gInH"
}

# di the cat api bisaa minta cuma kucing ras bengal doang, ituu pake key breeds_ids, dann tiap ras ada idsnya sendiri, bisa di cek aja di guidenya
# limit 10 itu berarti kita minta 10 foto kucingnya
spesifikasi_permintaan: dict[str, Any] = {
    "limit": 10,
    "breed_ids": "beng"  # This is why we need our VIP key!
}

hasil_request_or_minta = requests.get(url_or_alamat + loket, headers= id_card, params= spesifikasi_permintaan)

if hasil_request_or_minta.status_code == 200:
    print(hasil_request_or_minta) # hasilnya masih jelek, masih json sting
    data_bagus = hasil_request_or_minta.json()
    print(data_bagus)
    
    # 4. Ambil barang spesifik yang udah rapi
    url_gambar_kucing = data_bagus[0]['url']
    print(f"Nih barangnya (URL): {url_gambar_kucing}")
else:
    print(hasil_request_or_minta.text)
    
    



# minta berapa foto? oh segini foto, ras apa atau random? oh random, oke ini lah foto dan juga fun fact fun factnya