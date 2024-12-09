import pandas as pd
import streamlit as st
import altair as alt

st.set_page_config(
    page_title="Laporan PKM SI 2025",  # Judul halaman
    page_icon=":bar_chart:",           # Ikon (emoji atau path file)
    layout="wide",                     # Mengatur mode layout menjadi lebar
    initial_sidebar_state="collapsed"  # Menyembunyikan sidebar secara default
)

# Membaca CSV langsung dari URL
presensi_sosialisasi = pd.read_excel('daftar_hadir_sosialisasi.xlsx')
presensi_sosialisasi["Kelas"] = presensi_sosialisasi["Kelas"].str.replace(" ", "").str.upper()
unique_counts = presensi_sosialisasi["Kelas"].value_counts().reset_index()
unique_counts.columns = ["Kelas", "Jumlah"]


# kelas - pkm
data_pkm = pd.read_excel('daftar_pkm_2025.xlsx')

st.header("STATISTIK PKM SISFOR 2025")
st.subheader('Daftar PKM')
st.dataframe(data_pkm[['Bidang', 'Kelas', 'Pembimbing']], use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.header("Kehadiran Sosialisasi")
    st.bar_chart(unique_counts.set_index("Kelas"))
    
with col2:
    st.header("Jumlah PKM Per Kelas")
    
    class_unique_counts = data_pkm["Kelas"].value_counts().reset_index()
    class_unique_counts.columns = ["Kelas", "Jumlah"]
    st.bar_chart(class_unique_counts.set_index("Kelas"))

with col1:
    st.header("Dosen Pendamping / PKM")
    dosen_unique_counts = data_pkm["Pembimbing"].value_counts().reset_index()
    dosen_unique_counts.columns = ["Pembimbing", "Jumlah"]
    st.bar_chart(dosen_unique_counts.set_index("Pembimbing"))
    
with col2:
    st.header("Bidang PKM")
    bidang_unique_counts = data_pkm["Bidang"].value_counts().reset_index()
    bidang_unique_counts.columns = ["Bidang", "Jumlah"]
    st.bar_chart(bidang_unique_counts.set_index("Bidang"))



