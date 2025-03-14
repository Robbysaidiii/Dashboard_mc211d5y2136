import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul aplikasi
st.title("📊 Analisis Data Penyewaan Sepeda")

# Sidebar untuk informasi pengguna dan filter
st.sidebar.header("Robby Saidi Prasetyo mc211d5y2136")
option = st.sidebar.selectbox(
    "Pilih visualisasi:",
    [
        "Distribusi Jumlah Penyewaan Sepeda",
        "Korelasi Antara Variabel DAY",
        "Korelasi Antara Variabel HOUR",
        "Tren Penyewaan Sepeda per Bulan",
        "Dampak Cuaca terhadap Penyewaan Sepeda",
        "Distribusi Jumlah Sewa Sepeda Berdasarkan Jam"
    ]
)

# Membaca data
df = pd.read_csv("dashboard/Hour_day_df.csv")
hour = pd.read_csv("data/hour.csv")
day = pd.read_csv("data/day.csv")

# Mapping untuk musim
season_mapping = {1: "Musim Semi", 2: "Musim Panas", 3: "Musim Gugur", 4: "Musim Dingin"}
df['season_label'] = df['season_x'].map(season_mapping)

# Mapping untuk cuaca
weather_mapping = {
    1: "Cerah",
    2: "Kabut/Berawan",
    3: "Hujan Ringan/Salju Ringan",
    4: "Hujan Lebat/Salju Lebat"
}
df['weather_label'] = df['weathersit_x'].map(weather_mapping)

# Filter berdasarkan musim
season_filter = st.sidebar.selectbox("Pilih Musim", ["Semua"] + list(season_mapping.values()))
filtered_df = df if season_filter == "Semua" else df[df['season_label'] == season_filter]

# Filter berdasarkan cuaca
weather_filter = st.sidebar.selectbox("Pilih Cuaca", ["Semua"] + list(weather_mapping.values()))
filtered_df = filtered_df if weather_filter == "Semua" else filtered_df[filtered_df['weather_label'] == weather_filter]

# Pengecekan data kosong setelah filter
if filtered_df.empty:
    st.warning("Tidak ada data yang sesuai dengan filter yang dipilih.")
else:
    if option == "Dampak Cuaca terhadap Penyewaan Sepeda":
        st.subheader("☁️ Dampak Cuaca terhadap Penyewaan Sepeda")

        # Pastikan DataFrame 'day' memiliki kolom yang diperlukan
        required_columns = {'weathersit_y', 'cnt_y'}
        missing_columns = required_columns - set(day.columns)
        
        if missing_columns:
            st.error(f"Kolom berikut tidak ditemukan di DataFrame: {', '.join(missing_columns)}")
        else:
            # Mapping nilai numerik cuaca ke label deskriptif
            weather_mapping = {
                1: "Cerah",
                2: "Kabut/Berawan",
                3: "Hujan Ringan/Salju Ringan",
                4: "Hujan Lebat/Salju Lebat"
            }
            day = day.copy()  # Hindari SettingWithCopyWarning
            day['weather_label'] = day['weathersit_y'].map(weather_mapping)

            # Hapus baris dengan nilai NaN setelah mapping
            day = day.dropna(subset=['weather_label'])
            
            if day.empty:
                st.warning("Tidak ada data cuaca yang valid setelah mapping dan filter.")
            else:
                # Hitung rata-rata penyewaan berdasarkan kondisi cuaca
                weather_rentals = day.groupby('weather_label', as_index=False)['cnt_y'].mean()
                
                # Visualisasi dengan seaborn
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.barplot(x='weather_label', y='cnt_y', data=weather_rentals, ax=ax, palette="Blues")
                ax.set_title('Dampak Cuaca terhadap Penyewaan Sepeda')
                ax.set_xlabel('Kondisi Cuaca')
                ax.set_ylabel('Rata-rata Penyewaan Sepeda')
                ax.set_xticklabels(ax.get_xticklabels(), rotation=30)
                
                # Tampilkan plot di Streamlit
                st.pyplot(fig)
