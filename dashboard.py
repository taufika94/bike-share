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
    st.write("Tabel dan visualisasi Hour Data", hour_df.head())
        
    # Convert date column (dteday) to datetime format
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

        
    # 1. User Distribution by Hour
    st.subheader("1. User Distribution by Hour")
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    sns.lineplot(x='hr', y='cnt', data=hour_df, ax=ax1, label='Total Users')
    sns.lineplot(x='hr', y='casual', data=hour_df, ax=ax1, label='Casual Users', linestyle='--')
    sns.lineplot(x='hr', y='registered', data=hour_df, ax=ax1, label='Registered Users', linestyle='--')
    ax1.set_title('Distribution of Users by Hour')
    ax1.set_xlabel('Hour of the Day')
    ax1.set_ylabel('Number of Users')
    ax1.legend()
    st.pyplot(fig1)

    # 2. User Distribution by Weekday
    st.subheader("2. User Distribution by Weekday")
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='weekday', y='cnt', data=hour_df, ax=ax2)
    ax2.set_title('Distribution of Total Users by Weekday')
    ax2.set_xlabel('Weekday (0 = Sunday, 6 = Saturday)')
    ax2.set_ylabel('Total Users')
    st.pyplot(fig2)

    # 3. Total Users by Weather Situation
    st.subheader("3. Total Users by Weather Situation")
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.barplot(x='weathersit', y='cnt', data=hour_df, ax=ax3)
    ax3.set_title('Total Users by Weather Situation')
    ax3.set_xlabel('Weather Situation (1 = Clear, 2 = Mist, 3 = Light Rain/Snow)')
    ax3.set_ylabel('Total Users')
    st.pyplot(fig3)

    # 4. Temperature vs Total Users
    st.subheader("4. Temperature vs Total Users")
    fig4, ax4 = plt.subplots(figsize=(12, 6))
    sns.scatterplot(x='temp', y='cnt', data=hour_df, ax=ax4)
    ax4.set_title('Temperature vs Total Users')
    ax4.set_xlabel('Temperature (normalized)')
    ax4.set_ylabel('Total Users')
    st.pyplot(fig4)

    # 5. Correlation Matrix
    st.subheader("5. Correlation Matrix")
    fig5, ax5 = plt.subplots(figsize=(12, 8))
    sns.heatmap(hour_df.corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=ax5)
    ax5.set_title('Correlation Matrix')
    st.pyplot(fig5)



    st.write("Tabel dan visualisasi Day Data", day_df.head())

    # Histogram of Total Bike Rentals
    st.subheader("Distribution of Total Bike Rentals (cnt)")
    plt.figure(figsize=(10, 6))
    sns.histplot(day_df['cnt'], bins=30, kde=True, color='blue')
    plt.title('Distribution of Total Bike Rentals (cnt)')
    plt.xlabel('Total Bike Rentals (cnt)')
    plt.ylabel('Frequency')
    st.pyplot(plt)  # Tampilkan plot

    # Boxplot of Bike Rentals by Season
    st.subheader("Boxplot of Bike Rentals by Season")
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='season', y='cnt', data=day_df, palette='Set2')
    plt.title('Boxplot of Bike Rentals by Season')
    plt.xlabel('Season')
    plt.ylabel('Total Bike Rentals (cnt)')
    plt.xticks(ticks=[0, 1, 2, 3], labels=['Spring', 'Summer', 'Fall', 'Winter'])
    st.pyplot(plt)  # Tampilkan plot

    # Scatter plot of Bike Rentals vs Temperature
    st.subheader("Bike Rentals (cnt) vs Temperature")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='temp', y='cnt', data=day_df, color='orange')
    plt.title('Bike Rentals (cnt) vs Temperature')
    plt.xlabel('Temperature (normalized)')
    plt.ylabel('Total Bike Rentals (cnt)')
    st.pyplot(plt)  # Tampilkan plot

    # Time series plot of Bike Rentals Over Time
    st.subheader("Total Bike Rentals Over Time")
    plt.figure(figsize=(12, 6))
    plt.plot(day_df['dteday'], day_df['cnt'], label='Total Bike Rentals', color='green')
    plt.title('Total Bike Rentals Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Bike Rentals (cnt)')
    plt.xticks(rotation=45)
    plt.legend()
    st.pyplot(plt)  # Tampilkan plot

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
