from pathlib import Path
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

ROOT = Path(__file__).resolve().parent
DATA = ROOT/'data'/'dataset_sintesis_mahasiswa_1000.csv'

st.set_page_config(page_title='Bedah Kasus 2 | Profil Mahasiswa', page_icon='🎓', layout='wide')

@st.cache_data
def load_data():
    return pd.read_csv(DATA)

df = load_data()

st.title('Bedah Kasus 2: Dashboard Profil Mahasiswa')
st.markdown('### Raka Ramadhan | NIM 241051016')
st.caption('Dataset sintesis 1.000 mahasiswa yang dibangun dari dua observasi awal pada soal. Data bersifat simulasi untuk pembelajaran.')

with st.sidebar:
    st.header('Filter')
    majors = st.multiselect('Jurusan', sorted(df['Jurusan'].unique()), default=sorted(df['Jurusan'].unique()))
    semesters = st.multiselect('Semester', sorted(df['Semester'].unique()), default=sorted(df['Semester'].unique()))
    ipk_range = st.slider('Rentang IPK', float(df['IPK'].min()), float(df['IPK'].max()), (float(df['IPK'].min()), float(df['IPK'].max())), step=0.01)
    age_range = st.slider('Rentang Usia', int(df['Usia'].min()), int(df['Usia'].max()), (int(df['Usia'].min()), int(df['Usia'].max())))

mask = (
    df['Jurusan'].isin(majors) &
    df['Semester'].isin(semesters) &
    df['IPK'].between(ipk_range[0], ipk_range[1]) &
    df['Usia'].between(age_range[0], age_range[1])
)
d = df.loc[mask].copy()
if d.empty:
    st.warning('Tidak ada data untuk filter yang dipilih.')
    st.stop()

# KPI
c1,c2,c3,c4 = st.columns(4)
c1.metric('Jumlah Mahasiswa', f"{len(d):,}".replace(',','.'))
c2.metric('Rata-rata IPK', f"{d['IPK'].mean():.2f}")
c3.metric('Rata-rata Usia', f"{d['Usia'].mean():.1f} tahun")
c4.metric('Rata-rata Semester', f"{d['Semester'].mean():.2f}")

# Tabs
tab1,tab2,tab3,tab4 = st.tabs(['Ringkasan','Analisis Numerik','Analisis Ordinal','Data & Metodologi'])

with tab1:
    st.subheader('Komposisi Jurusan')
    major = d.groupby('Jurusan', as_index=False).agg(Jumlah=('ID_Mahasiswa','count'), Rata2_IPK=('IPK','mean'))
    c1,c2 = st.columns(2)
    with c1:
        fig = px.bar(major, x='Jurusan', y='Jumlah', text_auto=True, title='Jumlah Mahasiswa menurut Jurusan', labels={'Jumlah':'Jumlah Mahasiswa'})
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig = px.pie(major, names='Jurusan', values='Jumlah', title='Proporsi Mahasiswa menurut Jurusan', hole=0.35)
        st.plotly_chart(fig, use_container_width=True)
    st.dataframe(major.style.format({'Jumlah':'{:,.0f}','Rata2_IPK':'{:.2f}'}), use_container_width=True, hide_index=True)

with tab2:
    st.subheader('Variabel Numerik: IPK dan Usia')
    c1,c2 = st.columns(2)
    with c1:
        fig = px.histogram(d, x='IPK', color='Jurusan', nbins=24, marginal='box', title='Distribusi IPK', labels={'IPK':'IPK'})
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig = px.histogram(d, x='Usia', color='Jurusan', nbins=max(5, d['Usia'].nunique()), marginal='box', title='Distribusi Usia', labels={'Usia':'Usia (tahun)'})
        st.plotly_chart(fig, use_container_width=True)
    fig = px.scatter(d, x='Usia', y='IPK', color='Jurusan', hover_data=['Semester','ID_Mahasiswa'], opacity=0.65, title='Hubungan Usia dan IPK', labels={'Usia':'Usia (tahun)','IPK':'IPK'})
    st.plotly_chart(fig, use_container_width=True)
    corr = d[['Semester','IPK','Usia']].corr()
    st.markdown('#### Matriks korelasi')
    st.dataframe(corr.style.format('{:.3f}'), use_container_width=True)
    st.info('Korelasi menunjukkan keterkaitan linear, bukan sebab-akibat. Karena data merupakan sintesis dari dua observasi, hasil korelasi terutama berfungsi sebagai bahan latihan analisis.')

with tab3:
    st.subheader('Variabel Ordinal: Semester')
    sem = d.groupby('Semester', as_index=False).agg(Jumlah=('ID_Mahasiswa','count'), Rata2_IPK=('IPK','mean'), Rata2_Usia=('Usia','mean'))
    fig = px.bar(sem, x='Semester', y='Jumlah', text_auto=True, title='Distribusi Mahasiswa berdasarkan Semester', labels={'Jumlah':'Jumlah Mahasiswa'})
    st.plotly_chart(fig, use_container_width=True)
    fig = px.line(sem, x='Semester', y='Rata2_IPK', markers=True, title='Rata-rata IPK menurut Semester', labels={'Rata2_IPK':'Rata-rata IPK','Semester':'Semester'})
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(sem.style.format({'Jumlah':'{:,.0f}','Rata2_IPK':'{:.2f}','Rata2_Usia':'{:.1f}'}), use_container_width=True, hide_index=True)

with tab4:
    st.subheader('Data Sintesis')
    st.download_button('⬇️ Download CSV hasil filter', d.to_csv(index=False).encode('utf-8-sig'), 'data_mahasiswa_hasil_filter.csv', 'text/csv')
    st.dataframe(d, use_container_width=True, hide_index=True)

    st.subheader('Metodologi Sintesis')
    st.markdown('''
**Data awal:** dua observasi, yaitu Sistem Informasi, semester 3, IPK 3,85, usia 20 tahun, serta Manajemen, semester 1, IPK 3,50, usia 19 tahun.

**Prosedur sintesis:**
1. Membuat 1.000 observasi dengan seed acak 42 agar dapat direplikasi.
2. Mempertahankan dua jurusan dari data awal.
3. Membuat semester sebagai variabel ordinal 1 sampai 8 dengan probabilitas berbeda yang berpusat pada pola kedua observasi.
4. Membuat usia berdasarkan semester dengan variasi acak terbatas.
5. Membuat IPK di sekitar nilai acuan dengan variasi individual dan batas 2,25 sampai 4,00.

**Batasan:** data sintesis bukan data mahasiswa aktual. Karena sumber hanya memiliki dua baris, distribusi populasi tidak dapat diestimasi secara empiris. Gunakan dataset ini untuk latihan statistik deskriptif, visualisasi, dan dashboard.
''')

st.divider()
st.caption('Raka Ramadhan | NIM 241051016 | Bedah Kasus 2')
