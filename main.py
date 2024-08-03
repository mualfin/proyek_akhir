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
st.text('1. Bagaimana performa permintaan sewa sepeda pada hari libur dan tidak libur?')
st.text('2. Apakah musim berpengaruh dalam permintaan sewa sepeda?')

st.subheader('Hasil Analisis')
tab1, tab2 = st.tabs(["Pertanyaan 1", "Pertanyaan 2"])

with tab1:
    st.subheader('Bagaimana performa permintaan sewa sepeda pada hari libur dan tidak libur?')
    st.image("https://github.com/mualfin/asset/holiday.png")

with tab2:
    st.text('Apakah musim berpengaruh dalam permintaan sewa sepeda?')
    st.image("https://github.com/mualfin/asset/season.png")
