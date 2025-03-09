import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul aplikasi
st.title("Analisis Data Bike Sharing")

# Sidebar untuk navigasi
st.sidebar.header("Robby Saidi Prasetyo_mc211d5y2136")
option = st.sidebar.selectbox(
    "Pilih visualisasi:",
    ["Distribusi Jumlah Penyewaan Sepeda", "Korelasi Suhu dan Jumlah Sewa Sepeda", "Dampak Cuaca terhadap Penyewaan Sepeda", "Distribusi Jumlah Sewa Sepeda Berdasarkan Musim", "Distribusi Jumlah Sewa Sepeda Berdasarkan Tahun"]
)

# Memuat dataset dari file yang benar
df = pd.read_csv("Hour_day_df.csv")

if option == "Distribusi Jumlah Penyewaan Sepeda":
    st.subheader(" Distribusi Jumlah Penyewaan Sepeda")
    fig, ax = plt.subplots()
    sns.histplot(df['cnt_y'], bins=30, kde=True, ax=ax)
    ax.set_title("Data Penyewaan Sepeda")
    ax.set_xlabel("Jumlah Sewa Sepeda")
    ax.set_ylabel("Frekuensi")
    st.pyplot(fig)
    st.write("Gambar ini menunjukkan distribusi frekuensi jumlah penyewaan sepeda. Frekuensi penyewaan sepeda ditampilkan dalam rentang dari 0 hingga 1200, dengan jumlah sewa sepeda berkisar dari 0 hingga 8000. Grafik ini membantu memahami seberapa sering jumlah sewa sepeda tertentu terjadi.")

elif option == "Korelasi Suhu dan Jumlah Sewa Sepeda":
    st.subheader("🌡️ Korelasi Suhu dan Jumlah Sewa Sepeda")
    fig, ax = plt.subplots()
    sns.scatterplot(x=df['temp_y'], y=df['cnt_y'], ax=ax)
    ax.set_title("Korelasi Suhu dan Jumlah Sewa Sepeda")
    ax.set_xlabel("Suhu (Normalisasi)")
    ax.set_ylabel("Jumlah Sewa Sepeda")
    st.pyplot(fig)
    st.write("Gambar ini menampilkan hubungan antara suhu (yang dinormalisasi) dan jumlah sewa sepeda. Jumlah sewa sepeda berkisar dari 2000 hingga 8000, dan suhu dinormalisasi dalam skala dari 0.1 hingga 0.9. Grafik ini membantu memahami bagaimana suhu memengaruhi jumlah sewa sepeda.")


elif option == "Tren Penyewaan Sepeda per Bulan":
    st.subheader("📅 Tren Penyewaan Sepeda per Bulan")
    monthly_orders_df = df.groupby('mnth_x').agg({"cnt_y": "sum"}).reset_index()
    monthly_orders_df.columns = ["Bulan", "Total Penyewaan"]
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=monthly_orders_df, x="Bulan", y="Total Penyewaan", palette="Blues", ax=ax)
    ax.set_title("Tren Penyewaan Sepeda per Bulan")
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Total Penyewaan Sepeda")
    ax.grid(axis="y", linestyle="--", alpha=0.7)
    st.pyplot(fig)
    st.write("Gambar ini menampilkan tren penyewaan sepeda dari bulan ke bulan. Tren ini ditunjukkan dengan angka yang mungkin mewakili jumlah sewa sepeda atau indeks tertentu. Informasi ini membantu memahami fluktuasi penyewaan sepeda sepanjang tahun.")

elif option == "Dampak Cuaca terhadap Penyewaan Sepeda":
    st.subheader("☁️ Dampak Cuaca terhadap Penyewaan Sepeda")
    weather_impact = df.groupby('weathersit_x').agg({"cnt_y": "sum"}).reset_index()
    weather_impact.columns = ["Cuaca", "Total Penyewaan"]
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=weather_impact, x="Cuaca", y="Total Penyewaan", palette="coolwarm", ax=ax)
    ax.set_title("Dampak Cuaca terhadap Penyewaan Sepeda")
    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Total Penyewaan Sepeda")
    ax.grid(axis="y", linestyle="--", alpha=0.7)
    st.pyplot(fig)
    st.write("""cuaca sangat mempengaruhi penyewaan sepeda bisa dilihat dalam visualisai tersebut bahwa cuaca saat hujan tidak ada yang menyewa sepeda dan pada saat hujan ringan mendapatkan penyewaan sebesar 0,1 . dan dimendung mendapatkan angka di 1,8 yang berarti ada banyak penyewa sepeda di saat  mendung dan di cerah mendapatkan penyewaan sepeda yang lebih signifikan meningkat yaitu di angka 5
 kesimpulan: cuaca sangat mempengaruhi terhadap penyewaan sepeda""")
    
elif option == "Distribusi Jumlah Sewa Sepeda Berdasarkan Musim":
    st.subheader("Distribusi Jumlah Sewa Sepeda Berdasarkan Musim")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(df, x='cnt_y', hue='season_x', bins=30, kde=True, palette='coolwarm', ax=ax)
    ax.set_title('Distribusi Jumlah Sewa Sepeda Berdasarkan Musim')
    ax.set_xlabel('Jumlah Sewa Sepeda')
    ax.set_ylabel('Frekuensi')
    st.pyplot(fig)
    st.write("""Sumbu Vertikal (Y-axis): Menunjukkan jumlah sewa sepeda dengan rentang dari 0 hingga 8000, yang mungkin meningkat dalam interval 500 atau 1000 unit.

Sumbu Horizontal (X-axis): Menampilkan empat musim, yaitu Spring (Musim Semi), Summer (Musim Panas), Fall (Musim Gugur), dan Winter (Musim Dingin).

Batang (Bars): Setiap batang mewakili jumlah sewa sepeda pada musim tertentu. Tinggi batang menunjukkan seberapa banyak sepeda yang disewa pada musim tersebut. Misalnya, jika batang untuk Summer mencapai 8000, itu berarti ada 8000 sewa sepeda selama musim panas.

Warna atau Pola Batang: Biasanya, setiap batang memiliki warna atau pola yang berbeda untuk membedakan antara musim, memudahkan pembaca untuk membandingkan jumlah sewa sepeda antar musim.

Interpretasi Visual: Diagram ini memungkinkan pembaca untuk dengan cepat melihat musim mana yang memiliki jumlah sewa sepeda tertinggi dan terendah. Misalnya, jika batang untuk Summer lebih tinggi daripada batang untuk Winter, itu menunjukkan bahwa lebih banyak orang menyewa sepeda di musim panas daripada di musim dingin.

Kesalahan atau Ketidakjelasan: Istilah "Prekuensi" mungkin merupakan kesalahan ketik dan seharusnya adalah "Frekuensi", yang mengacu pada frekuensi atau jumlah sewa sepeda pada setiap musim.""")

elif option == "Distribusi Jumlah Sewa Sepeda Berdasarkan Tahun":
    st.subheader("Distribusi Jumlah Sewa Sepeda Berdasarkan Tahun")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(df, x='cnt_y', hue='yr_x', bins=30, kde=True, palette='bwr', ax=ax)
    ax.set_title('Distribusi Jumlah Sewa Sepeda Berdasarkan Tahun')
    ax.set_xlabel('Jumlah Sewa Sepeda')
    ax.set_ylabel('Frekuensi')
    st.pyplot(fig)
    st.write("""diagram batang atau grafik garis yang menunjukkan distribusi jumlah sewa sepeda berdasarkan tahun (2011 dan 2012). Sumbu vertikal (Y-axis) menampilkan jumlah sewa sepeda (0-8000), sedangkan sumbu horizontal (X-axis) menunjukkan tahun.

Jika diagram batang, tinggi batang mewakili jumlah sewa sepeda pada tahun tersebut.

Jika grafik garis, titik data menunjukkan jumlah sewa, dan garis menghubungkannya.

Visual ini memungkinkan pembaca untuk membandingkan jumlah sewa sepeda antara 2011 dan 2012, membantu memahami tren sewa dari tahun ke tahun.""")