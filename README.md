"""
======================================================================
Pertemuan 06: Nested Loop Python
File       : tugas/tabel_perkalian_dan_statistik.py
Deskripsi  : Program tabel perkalian dengan validasi input, akumulator,
             pencacahan (counter), dan refleksi nested loop.
======================================================================

REFLEKSI NESTED LOOP:
Salah satu kesalahan umum pada nested loop adalah meletakkan inisialisasi
variabel akumulator baris (total_baris = 0) di luar loop luar. Kesalahan
ini menyebabkan nilai total_baris tidak ter-reset kembali ke nol saat
berpindah ke baris baru, sehingga total nilai baris berikutnya terus
terakumulasi dengan penjumlahan dari baris-baris sebelumnya. Cara
memperbaikinya adalah dengan memindahkan inisialisasi total_baris = 0
ke dalam loop luar tepat sebelum loop dalam (for j) dimulai, sehingga
setiap baris baru selalu menghitung ulang totalnya dari nol.
======================================================================
"""

print("Tabel Perkalian dan Statistik")

# 1. Validasi input n dengan loop while (harus angka positif > 0)
n = int(input("n: "))
while n <= 0:
    print("Nilai n harus lebih besar dari 0!")
    n = int(input("n: "))

# 2. Inisialisasi total keseluruhan dan counter genap (sebelum loop luar)
total_semua = 0
count_genap = 0

print("\n--- Tabel Perkalian ---")

# 3. Nested loop untuk tabel perkalian dan statistik
for i in range(1, n + 1):
    # REFLEKSI PERBAIKAN: total_baris di-reset ke 0 di DALAM loop luar
    total_baris = 0  
    
    for j in range(1, n + 1):
        hasil = i * j
        print(f"{hasil:4}", end="")  # Format rapi lebar 4 karakter
        
        # Akumulasi nilai
        total_baris += hasil
        total_semua += hasil
        
        # Pencacahan (counter) bilangan genap
        if hasil % 2 == 0:
            count_genap += 1
            
    print(f"  | Total Baris {i} = {total_baris}")

# 4. Menampilkan statistik keseluruhan
print("-" * 35)
print(f"Total Keseluruhan     = {total_semua}")
print(f"Banyak Perkalian Genap = {count_genap}")