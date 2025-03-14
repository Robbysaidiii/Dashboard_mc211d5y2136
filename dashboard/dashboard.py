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
    if option == "Distribusi Jumlah Penyewaan Sepeda":
        st.subheader("📈 Distribusi Jumlah Penyewaan Sepeda")
        fig, ax = plt.subplots()
        sns.histplot(filtered_df['cnt_y'], bins=30, kde=True, ax=ax)
        ax.set_title("Data Penyewaan Sepeda")
        ax.set_xlabel("Jumlah Sewa Sepeda")
        ax.set_ylabel("Frekuensi")
        st.pyplot(fig)

    elif option == "Korelasi Antara Variabel DAY":
        st.subheader("🌡️ Korelasi Variabel DAY")
        numerical_columns = day.select_dtypes(include=['number']).columns
        correlation_matrix = day[numerical_columns].corr()
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1, ax=ax)
        ax.set_title("Matriks Korelasi Variabel DAY")
        st.pyplot(fig)

    elif option == "Korelasi Antara Variabel HOUR":
        st.subheader("⏳ Korelasi Variabel HOUR")
        numerical_columns = hour.select_dtypes(include=['number']).columns
        correlation_matrix = hour[numerical_columns].corr()
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1, ax=ax)
        ax.set_title("Heatmap Korelasi Antar Variabel Numerik")
        st.pyplot(fig)

    elif option == "Tren Penyewaan Sepeda per Bulan":
        st.subheader("📅 Tren Penyewaan Sepeda per Bulan")
        monthly_orders_df = filtered_df.groupby('mnth_x').agg({"cnt_y": "sum"}).reset_index()
        monthly_orders_df.columns = ["Bulan", "Total Penyewaan"]
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.lineplot(data=monthly_orders_df, x="Bulan", y="Total Penyewaan", palette="Blues", marker="o", color="#1f77b4", ax=ax)
        ax.set_title("Tren Penyewaan Sepeda per Bulan")
        ax.set_xlabel("Bulan")
        ax.set_ylabel("Total Penyewaan Sepeda")
        ax.grid(axis="y", linestyle="--", alpha=0.7)
        st.pyplot(fig)

    elif option == "Dampak Cuaca terhadap Penyewaan Sepeda":
        st.subheader("☁️ Dampak Cuaca terhadap Penyewaan Sepeda")
        
        if 'weather_label' not in filtered_df.columns or 'cnt_y' not in filtered_df.columns:
            st.error("Kolom 'weather_label' atau 'cnt_y' tidak ditemukan di DataFrame.")
        else:
            weather_rentals = day.groupby('weathersit')['cnt'].mean().reset_index()
            plt.figure(figsize=(10, 6))
            sns.barplot(x='weathersit', y='cnt', data=weather_rentals)
            plt.title(' VIsualdata Dampak cuaca terhadap penyewaan sepeda')
            plt.xlabel('Kondisi Cuaca')
            plt.ylabel('Rata-rata Penyewaan Sepeda')
            plt.show()

    elif option == "Distribusi Jumlah Sewa Sepeda Berdasarkan Jam":
        st.subheader("⏰ Distribusi Jumlah Sewa Sepeda Berdasarkan Jam")
        fig, ax = plt.subplots()
        sns.histplot(hour['cnt'], bins=30, kde=True, ax=ax)
        ax.set_title("Data Penyewaan Sepeda yang Diaggregasi per Jam (cnt)")
        ax.set_xlabel("Jumlah Sewa Sepeda")
        ax.set_ylabel("Frekuensi")
        st.pyplot(fig)
