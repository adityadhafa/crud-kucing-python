import requests # Hei, asisten, siap-siap!
from typing import Any

'''
Bayangin lo adalah Mandor Proyek Konstruksi.

Program Python lo: Itu Lo (Si Mandor).

Server/Website (misal TheCatAPI, Google, dll): Itu Gudang Material Raksasa di pusat kota.

API: Itu Petugas Loket di gudang itu.

Lo (Mandor) nggak boleh masuk-masuk ke Gudang (Server) dan ambil barang seenaknya. Lo WAJIB lewat Petugas Loket (API).

"API Calling" itu adalah proses lo (Mandor) nyerahin Formulir Permintaan Barang (PO) ke si Petugas Loket.

'''

# Ini alamat loketnya (KEPADA:)
url = "https://gudang-material-jaya.com/loket/semen" 
'''
ini adalah tujuan SPESIFIK formulir lo. Dan lo bener, ini gabungan dari:

Alamat Utama (URL Utama): Alamat gudangnya.

Contoh: https://gudang-material-jaya.com

Endpoint (Pesanan Kita): Loket spesifik yang lo tuju di gudang itu.

Contoh: /loket/semen atau /loket/besi-beton

Jadi, url bersih = Alamat lengkap loketnya. url = "https://gudang-material-jaya.com/loket/semen"
'''


# Ini detail barangnya (DETAIL BARANG:)
params: dict[str, Any] = {
    "merek": "tiga roda", 
    "jumlah": 50
}

'''
Ini adalah detail barang yang lo minta. Lo NULISNYA TERPISAH di badan formulir, BUKAN di alamat.

KEPADA: https://gudang-material-jaya.com/loket/semen

DETAIL BARANG:

merek: tiga roda

jumlah: 50

kemasan: sak

Di Python, ini jadi: params = {'merek': 'tiga roda', 'jumlah': 50}
'''

# Ini ID Proyek kita (LAMPIRAN ID:)
headers = {
    "x-api-key": "ID-PROYEK-AMAN-12345"
}
'''
Petugas loket pasti nanya: "Anda siapa? Mana surat izin dari PT. Anda?"

Ini adalah "kunci" atau "kartu member" lo. Lo NULISNYA TERPISAH juga, biasanya di-staples bareng PO.

KEPADA: https://gudang-material-jaya.com/loket/semen

DETAIL BARANG: (Isi params)

LAMPIRAN ID:

x-api-key: ID-PROYEK-AMAN-12345

Di Python, ini jadi: headers = {'x-api-key': 'ID-PROYEK-AMAN-12345'}
'''

# Perintah ke asisten:
# "Tolong AMBILKAN (get) barang ke 'url' ini,"
# "Kasih 'params' (catatan PO) ini,"
# "Dan tunjukkin 'headers' (ID Proyek) ini."
response = requests.get(url, params=params, headers=headers)
# ohh jadi get() ini nanti bakal ngereturn objek.. jadi hasil dari get() ini nanti bakal dibuatkan ke class dan jadilah objek

# 1. Suruh asisten berangkat
print("Asisten lagi jalan ke gudang...")
response = requests.get(url, params=params)

# 2. Asisten balik. CEK SURAT JALAN-nya dulu!
if response.status_code == 200:
    # 3. Kode 200 (OK)! Perintah: BONGKAR BARANG!
    print("Sukses! Kode 200. Siap bongkar barang...")
    data = response.json()
    
    # 4. Ambil barang spesifik yang udah rapi
    url_gambar_kucing = data[0]['url']
    print(f"Nih barangnya (URL): {url_gambar_kucing}")

elif response.status_code == 404 :
    # 3. Kodenya BUKAN 200! Gagal.
    print(f"Gagal, Bos! Surat jalannya nunjukkin kode: {response.status_code}")
    print("Ini omelan dari petugas loketnya:")
    print(response.text) # Cetak aja isi omelannya (error message)
    
    
# ngasih surat jalan dulu, baru ngasih barangnya, gitu emang
