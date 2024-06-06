import pandas as pd

# Definisikan data dari tabel
table_data = {
    "Tanggal": ["01/06/2024", "03/06/2024", "05/06/2024"],
    "No. Faktur": ["PB001", "PB002", "PB003"],
    "Nama Supplier": ["CV AFI", "CV PDF", "CV GHI"],
    "Barang": ["Barang A", "Barang B", "Barang C"],
    "Jumlah": [10, 20, 15],
    "Harga Satuan": ["Rp 50.000", "Rp 30.000", "Rp 40.000"],
    "Total Harga": ["Rp 500.000", "Rp 600.000", "Rp 600.000"],
}

# Buat DataFrame dari data tabel
df = pd.DataFrame(table_data)

# Tampilkan data
print("Data dari tabel:")
print(df)

# Hitung mean, median, dan modus dari kolom Jumlah
mean_jumlah = df["Jumlah"].mean()
median_jumlah = df["Jumlah"].median()
mode_jumlah = df["Jumlah"].mode().iloc[0]

print("\nAnalisis:")
print(f"Mean Jumlah: {mean_jumlah}")
print(f"Median Jumlah: {median_jumlah}")
print(f"Modus Jumlah: {mode_jumlah}")
