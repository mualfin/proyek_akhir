import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from babel.numbers import format_currency
sns.set(style='dark')

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
    st.text('ini gambar 1')

with tab2:
    st.header("Pertanyaan 2")
    st.text('ini gambar 2')

