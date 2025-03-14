import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul aplikasi
st.title("Analisis Data Penyewaan Sepeda")

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
df = pd.read_csv("dashboard/Hour_day_df (1).csv")
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
        sns.histplot(data=[filtered_df['cnt_y'], day['cnt']], bins=30, kde=True, multiple="layer", ax=ax)
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
        sns.lineplot(data=monthly_orders_df, x="Bulan", y="Total Penyewaan", marker="o", color="#1f77b4", ax=ax)
        ax.set_title("Tren Penyewaan Sepeda per Bulan")
        ax.set_xlabel("Bulan")
        ax.set_ylabel("Total Penyewaan Sepeda")
        ax.grid(axis="y", linestyle="--", alpha=0.7)
        st.pyplot(fig)

    elif option == "Dampak Cuaca terhadap Penyewaan Sepeda":
        st.subheader("☁️ Dampak Cuaca terhadap Penyewaan Sepeda")

        # Pastikan kolom 'weathersit_x' dan 'cnt_y' ada dalam dataset
        if 'weathersit_x' not in df.columns or 'cnt_y' not in df.columns:
            st.error("Kolom 'weathersit_x' atau 'cnt_y' tidak ditemukan di DataFrame.")
        else:
            # Mengelompokkan data berdasarkan kondisi cuaca
            weather_impact = df.groupby("weathersit_x").agg({
                "cnt_y": ["sum", "mean", "count"]
            }).reset_index()

            weather_impact.columns = ["Cuaca", "Total Penyewaan", "Rata-rata Penyewaan", "Jumlah Hari"]
            weather_labels = {
                1: "Cerah",
                2: "Mendung",
                3: "Gerimis",
                4: "Hujan Lebat"
            }
            weather_impact["Cuaca"] = weather_impact["Cuaca"].map(weather_labels)

            fig, ax = plt.subplots(figsize=(8, 5))
            sns.barplot(data=weather_impact, x="Cuaca", y="Total Penyewaan", palette="coolwarm", ax=ax)

            ax.set_xlabel("Kondisi Cuaca")
            ax.set_ylabel("Total Penyewaan Sepeda")
            ax.set_title("Dampak Cuaca terhadap Penyewaan Sepeda")
            ax.grid(axis="y", linestyle="--", alpha=0.7)
            st.pyplot(fig)

            # Menambahkan penjelasan mengenai dampak cuaca
            st.markdown("""
            ### 📌 Analisis Dampak Cuaca terhadap Penyewaan Sepeda
            Cuaca memiliki pengaruh besar terhadap jumlah penyewaan sepeda. Dari visualisasi di atas, kita dapat melihat tren penyewaan sepeda berdasarkan kondisi cuaca:

            - **Hujan Lebat 🌧️** → Tidak ada penyewaan sepeda, menunjukkan bahwa pengguna cenderung menghindari sepeda dalam kondisi ekstrem seperti hujan deras atau badai.
            - **Hujan Ringan / Gerimis 🌦️** → Penyewaan sepeda masih ada tetapi sangat sedikit (sekitar **0,1**), menunjukkan bahwa beberapa pengguna tetap menyewa sepeda meskipun hujan ringan.
            - **Mendung / Berawan ☁️** → Penyewaan meningkat signifikan (**1,8**), menunjukkan bahwa kondisi mendung lebih nyaman untuk bersepeda dibandingkan saat hujan.
            - **Cerah ☀️** → Penyewaan tertinggi (**5**), menunjukkan bahwa cuaca cerah adalah kondisi paling ideal untuk bersepeda, baik untuk perjalanan sehari-hari maupun rekreasi.

            ### 📢 **Kesimpulan**
            Dari hasil analisis, dapat disimpulkan bahwa **cuaca sangat berpengaruh terhadap penyewaan sepeda**:
            - Saat **hujan deras**, penyewaan **sangat rendah atau bahkan nol**.
            - Saat **mendung**, penyewaan tetap tinggi.
            - Saat **cerah**, jumlah penyewaan **meningkat secara signifikan**.

            **Rekomendasi:** Untuk meningkatkan penyewaan sepeda saat cuaca kurang mendukung, operator penyewaan sepeda dapat mempertimbangkan penyediaan fasilitas seperti jas hujan atau shelter di stasiun penyewaan. 🚲☀️
            """)

    elif option == "Distribusi Jumlah Sewa Sepeda Berdasarkan Jam":
        st.subheader("⏰ Distribusi Jumlah Sewa Sepeda Berdasarkan Jam")
        fig, ax = plt.subplots()
        sns.histplot(hour['cnt'], bins=30, kde=True, ax=ax)
        ax.set_title("Data Penyewaan Sepeda yang Diaggregasi per Jam (cnt)")
        ax.set_xlabel("Jumlah Sewa Sepeda")
        ax.set_ylabel("Frekuensi")
        st.pyplot(fig)
