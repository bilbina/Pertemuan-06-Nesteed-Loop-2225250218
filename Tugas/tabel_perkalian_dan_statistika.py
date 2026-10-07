print("Tabel Perkalian dan Statistik")

# 1. Validasi input n dengan loop while (harus angka positif > 0)
n = int(input("n: "))
while n <= 0:
    print("Nilai n harus lebih besar dari 0!")
    n = int(input("n: "))

# 2. Inisialisasi total keseluruhan dan counter genap
total_semua = 0
count_genap = 0

print("\n--- Tabel Perkalian ---")

# 3. Nested loop untuk tabel perkalian dan perhitungan statistik
for i in range(1, n + 1):
    total_baris = 0  # Inisialisasi ulang total baris setiap ganti baris baru
    
    for j in range(1, n + 1):
        hasil = i * j
        print(f"{hasil:4}", end="")  # Format rapi dengan lebar 4 karakter
        
        # Hitung statistik
        total_baris += hasil
        total_semua += hasil
        
        # Pencacahan jika hasil perkalian adalah bilangan genap
        if hasil % 2 == 0:
            count_genap += 1
            
    print(f"  | Total Baris {i} = {total_baris}")

# 4. Menampilkan statistik keseluruhan
print("-" * 35)
print(f"Total Keseluruhan     = {total_semua}")
print(f"Banyak Perkalian Genap = {count_genap}")