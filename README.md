
# README - Proyek Analisis Data: Bike Sharing Dataset

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis dataset Bike Sharing yang mencakup data harian (`day.csv`) dan data per jam (`hour.csv`). Dataset ini berisi informasi tentang penyewaan sepeda berdasarkan berbagai faktor seperti musim, cuaca, suhu, kelembaban, dan lainnya. Proyek ini dilakukan oleh Robby Saidi Prasetyo dengan email robbysaidiii@gmail.com dan ID Dicoding mc211d5y2136.

## Library yang Digunakan
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Google Colab Drive

## Data Wrangling

### Gathering Data
- Dataset `day.csv` dan `hour.csv` diambil dari Google Drive.
- Dataset `day.csv` berisi 731 baris dan 16 kolom.
- Dataset `hour.csv` berisi 17.379 baris dan 17 kolom.

### Assessing Data
- **Dataset `day.csv`:
  - Tidak ada nilai yang hilang (missing values).
  - Tidak ada data yang terduplikat.
  - Statistik deskriptif menunjukkan data yang konsisten dan tidak ada nilai yang tidak masuk akal.

- **Dataset `hour.csv`:
  - Tidak ada nilai yang hilang (missing values).
  - Tidak ada data yang terduplikat.
  - Statistik deskriptif menunjukkan data yang konsisten dan tidak ada nilai yang tidak masuk akal.

### Cleaning Data
- Duplicate Data:
  - Tidak ada data yang terduplikat di kedua dataset, namun dilakukan penghapusan duplikat sebagai langkah pencegahan.
  
- **Missing Values:**
  - Tidak ada missing values di kedua dataset.

- **Inaccurate Values:**
  - Tidak ditemukan nilai yang tidak masuk akal di kedua dataset setelah dilakukan pengecekan statistik deskriptif.

## Insight
- Dataset `day.csv` dan `hour.csv` sudah bersih dan siap untuk dianalisis lebih lanjut.
- Tidak ada masalah signifikan yang ditemukan dalam proses data wrangling.

## Langkah Selanjutnya
- Melakukan analisis lebih lanjut untuk menjawab pertanyaan bisnis yang telah ditentukan.
- Membuat visualisasi data untuk mendapatkan insight yang lebih mendalam.
- Menyusun kesimpulan dan rekomendasi berdasarkan hasil analisis.

# Setup environment
conda create --name mc211d5y2136 python=3.9
conda activate mc211d5y2136
pip install -r requirements.txt

# Run steamlit app
streamlit run dashboard/Dashboard.py


