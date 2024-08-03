import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from babel.numbers import format_currency
sns.set(style='dark')

all_df = pd.read_csv("all_data.csv")

st.title('Proyek Analisis Data :sparkles:')
st.write('Proyek ini disusun sebagai syarat untuk menyelesaikan kelas Belajar Analisis Data dengan Python Dicoding') 


st.header('Bike Sharing Dataset')
st.subheader('Pertanyaan Bisnis?')
st.write('1. Bagaimana performa permintaan sewa sepeda pada hari libur dan tidak libur?')
st.write('2. Apakah musim berpengaruh dalam permintaan sewa sepeda?')

st.header('Hasil Analisis')
tab1, tab2 = st.tabs(["Pertanyaan 1", "Pertanyaan 2"])

with tab1:
    st.subheader('Bagaimana performa permintaan sewa sepeda pada hari libur dan tidak libur?')
    st.image("holiday.png")

with tab2:
    st.subheader('Apakah musim berpengaruh dalam permintaan sewa sepeda?')
    st.image("season.png")

st.header('Kesimpulan')
left_column, right_column = st.columns(2)
with left_column:
    st.subheader('Pertanyaan 1')
    st.write('Grafik tersebut menunjukkan bahwa jumlah rata-rata penyewaan sepeda per hari lebih tinggi pada NOT HOLIDAY dibandingkan dengan HOLIDAY. Ini mengindikasikan bahwa sepeda lebih sering digunakan sebagai sarana transportasi untuk kegiatan sehari-hari atau bekerja pada NOT HOLIDAY. Untuk meningkatkan pendapatan, beberapa strategi dapat diterapkan, seperti memberikan diskon atau penawaran khusus pada HOLIDAY untuk menarik lebih banyak pelanggan, serta menyelenggarakan event atau aktivitas yang melibatkan penyewaan sepeda.')
with right_column:
    st.subheader('Pertanyaan 2')
    st.write('Grafik tersebut menunjukkan bahwa jumlah penyewaan sepeda terendah terjadi pada musim SPRING dan tertinggi pada musim FALL, dengan musim WINTER dan SUMMER berada di antara keduanya. Untuk meningkatkan pendapatan, beberapa strategi dapat diterapkan, seperti membuat promosi khusus dan event menarik di musim FALL, memastikan sepeda dalam kondisi baik dan memberikan penawaran paket langganan menarik di musim WINTER dan SUMMER, serta memaksimalkan potensi di musim FALL dengan menambah jumlah sepeda dan mempromosikannya melalui media sosial. Peningkatan layanan dan fasilitas sepanjang tahun juga penting untuk menjaga dan meningkatkan jumlah penyewaan sepeda')
