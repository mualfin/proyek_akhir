import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from babel.numbers import format_currency
sns.set(style='dark')

all_df = pd.read_csv("all_data.csv")

st.title('Proyek Analisis Data :sparkles:')
st.text('Proyek ini disusun sebagai syarat untuk menyelesaikan') 
st.text('kelas Belajar Analisis Data dengan Python Dicoding')

st.header('Bike Sharing Dataset')
st.subheader('Pertanyaan Bisnis?')
st.text('Bagaimana performa permintaan sewa sepeda pada hari libur dan tidak libur?')
st.text('Apakah musim berpengaruh dalam permintaan sewa sepeda?')

st.subheader('Hasil Analisis')
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

with tab1:
    st.header("Pertanyaan 1")
    st.subheader('Bagaimana performa permintaan sewa sepeda pada hari libur dan tidak libur?')

    all_df.holiday.replace((0,1), ('Not Holiday','Holiday'), inplace=True)
    all_df.groupby('holiday')['cnt'].mean().reset_index().sort_values("cnt")

    avg_holiday = day_df.groupby('holiday')['cnt'].mean().reset_index().sort_values("cnt")
    plt.figure(figsize=(8, 5))
    sns.barplot(x='holiday', y='cnt', data=avg_holiday, palette='Set2')

    plt.title('Performa Sewa Sepeda Per Hari')
    plt.xlabel('Hari Libur atau tidak')
    plt.ylabel('Jumlah Rata-Rata Penyewaan')

    plt.show()

with tab2:
    st.header("Pertanyaan 2")
    st.text('ini gambar 2')

