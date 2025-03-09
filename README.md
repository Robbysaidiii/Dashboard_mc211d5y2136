
# Proyek Analisis Data: Bike Sharing Dataset

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data penyewaan sepeda dari dataset *Bike Sharing Dataset*. Data yang digunakan mencakup informasi harian (*day.csv*) dan per jam (*hour.csv*). Selain itu, data yang telah diproses dan digabungkan dari kedua dataset ini disimpan dalam *Hour_day_df.csv*.

## Penjelasan Dataset
- **day.csv**: Berisi data harian penyewaan sepeda.
- **hour.csv**: Berisi data penyewaan sepeda per jam.
- **Hour_day_df.csv**: Dataset hasil penggabungan *day.csv* dan *hour.csv* yang telah diolah dan dibersihkan.

## Permasalahan dan Pertanyaan yang Diajukan
1. Seberapa besar dampak cuaca terhadap jumlah penyewaan sepeda?
2. bagaimana penyewaaan sepeda setiap bulan nya?

## Kesimpulan
Kesimpulan akan dijawab berdasarkan analisis yang telah dilakukan menggunakan dataset yang benar (*Hour_day_df.csv*). Setelah melakukan analisis yang lebih mendalam, hasilnya akan diupdate di bagian ini.

## Cara Menjalankan Program
1. Pastikan semua pustaka yang ada di *requirements.txt* telah diinstal.
2. Jalankan *Dashboard.py* untuk melihat visualisasi data:
   ```sh
   python dashboard/Dashboard.py
   ```
3. Analisis data dapat dilakukan menggunakan *Proyek_Analisis_Data.ipynb* di Jupyter Notebook.

## Catatan Tambahan
Jika ada kendala atau perbaikan yang diperlukan, silakan cek kembali dataset yang digunakan dan pastikan data yang digunakan adalah *Hour_day_df.csv* yang sudah diproses dengan benar.

# Setup environment
conda create --name mc211d5y2136 python=3.9
conda activate mc211d5y2136
pip install -r requirements.txt

# Run steamlit app
streamlit run dashboard/Dashboard.py


