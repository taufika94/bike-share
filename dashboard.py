import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Dashboard Analisis Penyewaan Sepeda", layout="wide")

# Title
st.title("Proyek Analisis Data Penyewaan Sepeda")
st.subheader("Nama: Taufika Retno Wulan")
st.write("Email: m297b4kx4298@bangkit.academy")
st.write("ID Dicoding: taufika_retno_wulan_m297b4kx4298_SgMm")

# Upload data
st.sidebar.header("Upload Data")
uploaded_file_hour = st.sidebar.file_uploader("Upload hour.csv", type=['csv'])
uploaded_file_day = st.sidebar.file_uploader("Upload day.csv", type=['csv'])

if uploaded_file_hour is not None and uploaded_file_day is not None:
    # Load data
    hour_df = pd.read_csv(uploaded_file_hour)
    day_df = pd.read_csv(uploaded_file_day)

    # Data Wrangling
    merged_df = pd.merge(
        left=hour_df,
        right=day_df,
        how="left",
        left_on="dteday",
        right_on="dteday"
    )

    # Clean data: Convert date columns to datetime
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

    # Display DataFrame
    st.write("Tabel Hour Data", hour_df.head())
    st.write("Tabel Day Data", day_df.head())

    # Exploratory Data Analysis
    st.subheader("Analisis Eksplorasi Data")

     # Plot for Question 1: Pengaruh Hari Libur
    # Calculate the mean rental count based on holiday
    holiday_workday_cnt = day_df.groupby("holiday")["cnt"].mean().reset_index()

    # Create a bar plot to visualize the effect of holiday on bike rentals
    plt.figure(figsize=(8, 6))
    sns.barplot(data=holiday_workday_cnt, x="holiday", y="cnt")

    # Set plot title and labels
    plt.title("Pengaruh Hari Libur Terhadap Jumlah Penyewaan Sepeda", fontsize=14)
    plt.xlabel("Hari Libur (0: Hari Kerja, 1: Hari Libur)", fontsize=12)
    plt.ylabel("Rata-rata Jumlah Penyewaan Sepeda", fontsize=12)

    # Add value annotations on bars
    for index, value in enumerate(holiday_workday_cnt['cnt']):
        plt.text(index, value, f"{value:.2f}", ha='center', va='bottom')

    # Replace plt.show() with st.pyplot()
    st.pyplot(plt)

    # Insights from Plot 1
    st.subheader("Kesimpulan Pertanyaan 1")
    st.write("""
    1. **Pengaruh Hari Libur**: Hari libur cenderung memiliki rata-rata jumlah penyewaan sepeda yang lebih tinggi dibandingkan dengan hari kerja.
    2. **Perbedaan Hari Kerja dan Hari Libur**: Rata-rata penyewaan pada hari libur menunjukkan lonjakan, menunjukkan preferensi penggunaan sepeda untuk bersantai.
    3. **Keterlibatan pada Hari Kerja**: Penyewaan pada hari kerja lebih rendah, menunjukkan penggunaan sepeda sebagai sarana transportasi harian.
    4. **Rekomendasi**: Optimalkan kampanye pemasaran dan penawaran khusus pada hari libur.
    """)

    # Plot for Question 2: Perbedaan pengguna kasual dan terdaftar
    day_df['total_rentals'] = day_df['casual'] + day_df['registered']
    daily_rentals = day_df.groupby('dteday').agg({'casual': 'sum', 'registered': 'sum'}).reset_index()
    daily_rentals['dteday'] = pd.to_datetime(daily_rentals['dteday'])

    plt.figure(figsize=(14, 7))
    sns.lineplot(data=daily_rentals, x='dteday', y='casual', label='Pengguna Kasual', color='blue')
    sns.lineplot(data=daily_rentals, x='dteday', y='registered', label='Pengguna Terdaftar', color='orange')
    plt.title('Perbandingan Jumlah Penyewaan Per Hari')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Penyewaan')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    st.pyplot(plt)

    # Insights from Plot 2
    st.subheader("Kesimpulan Pertanyaan 2")
    st.write("""
    1. **Dominasi Pengguna Terdaftar**: Pengguna terdaftar memiliki jumlah penyewaan yang lebih tinggi dan konsisten dibandingkan pengguna kasual.
    2. **Fluktuasi Penyewaan Kasual**: Penyewaan pengguna kasual menunjukkan fluktuasi yang lebih besar, terutama pada akhir pekan.
    3. **Pola Musiman**: Indikasi pola musiman terlihat dengan penyewaan meningkat pada bulan-bulan tertentu.
    4. **Keterlibatan Stabil**: Pengguna terdaftar menunjukkan keterlibatan yang lebih stabil, mencerminkan loyalitas.
    5. **Rekomendasi**: Tingkatkan pemasaran untuk pengguna kasual pada waktu tertentu untuk meningkatkan penyewaan.
    """)

else:
    st.write("Silakan unggah file hour.csv dan day.csv untuk melanjutkan.")
