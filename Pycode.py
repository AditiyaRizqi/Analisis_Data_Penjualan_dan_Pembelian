import matplotlib.pyplot as plt

# Data penjualan fiktif
data_penjualan = {
    'Barang A': {'pembelian': 300000, 'penjualan': 700000},
    'Barang B': {'pembelian': 200000, 'penjualan': 900000},
    'Barang C': {'pembelian': 250000, 'penjualan': 900000}
}

# Menyiapkan data untuk scatter plot
items = list(data_penjualan.keys())
pembelian = [data_penjualan[item]['pembelian'] for item in items]
penjualan = [data_penjualan[item]['penjualan'] for item in items]

# Membuat scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(pembelian, penjualan, color='blue')
for i, item in enumerate(items):
    plt.text(pembelian[i], penjualan[i], item)

plt.xlabel('Harga Pembelian (Rp)')
plt.ylabel('Pendapatan Penjualan (Rp)')
plt.title('Scatter Plot Penjualan Fiktif')
plt.show()

# Menyiapkan data untuk pie chart
labels = list(data_penjualan.keys())
penjualan = [data_penjualan[item]['penjualan'] for item in labels]

# Membuat pie chart
plt.figure(figsize=(8, 8))
plt.pie(penjualan, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart Pendapatan Penjualan Fiktif')
plt.show()

import matplotlib.pyplot as plt
import pandas as pd

# Creating the data for plotting
data = {
    'Faktur': ['PJ004', 'PJ005', 'PJ006'],
    'Pendapatan Fiktif': [700000, 900000, 900000],
    'Pembelian': [500000, 600000, 600000]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Plotting the histogram
fig, ax = plt.subplots(figsize=(10, 6))

# Setting the positions and width for the bars
bar_width = 0.35
r1 = range(len(df['Faktur']))
r2 = [x + bar_width for x in r1]

# Creating the bars
ax.bar(r1, df['Pendapatan Fiktif'], color='blue', width=bar_width, edgecolor='grey', label='Pendapatan Fiktif')
ax.bar(r2, df['Pembelian'], color='green', width=bar_width, edgecolor='grey', label='Pembelian')

# Adding labels and title
ax.set_xlabel('Faktur', fontweight='bold')
ax.set_ylabel('Rupiah', fontweight='bold')
ax.set_title('Perbandingan Pendapatan Fiktif dan Pembelian')
ax.set_xticks([r + bar_width/2 for r in range(len(df['Faktur']))])
ax.set_xticklabels(df['Faktur'])

# Adding the legend
ax.legend()

# Showing the plot
plt.show()

# First, you need to install the matplotlib_venn package if you haven't already
# !pip install matplotlib_venn

import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Define the data
sets = {
    'PJ004': set(['Barang A']),
    'PJ005': set(['Barang B']),
    'PJ006': set(['Barang C'])
}

# Creating the Venn diagram
venn3([sets['PJ004'], sets['PJ005'], sets['PJ006']],
      ('PJ004', 'PJ005', 'PJ006'))

# Adding a title
plt.title('Venn Diagram of Fictitious Sales Invoices')

# Showing the plot
plt.show()
