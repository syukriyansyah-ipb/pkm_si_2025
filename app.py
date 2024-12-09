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
st.dataframe(data_pkm[['Bidang', 'Kelas', 'Pembimbing', 'Judul']], use_container_width=True)

col1, col2 = st.columns(2, gap='large')

with col1:
    
    class_unique_counts = data_pkm["Kelas"].value_counts().reset_index()
    class_unique_counts.columns = ["Kelas", "Jumlah"]
    # st.bar_chart(class_unique_counts.set_index("Kelas"))
    # Membuat bar chart dengan warna otomatis untuk setiap kelas
    bar_chart = alt.Chart(class_unique_counts).mark_bar().encode(
        x=alt.X("Kelas", sort="-y"),  # Sort berdasarkan jumlah
        y="Jumlah",
        color=alt.Color("Kelas", legend=None),  # Warna otomatis untuk setiap kelas
        tooltip=["Kelas", "Jumlah"]  # Tooltip interaktif
    ).properties(
        title="Jumlah PKM Per Kelas"
    )

    # Tampilkan bar chart di Streamlit
    st.altair_chart(bar_chart, use_container_width=True)


with col1:
    # st.subheader("Dosen Pendamping / PKM")
    dosen_unique_counts = data_pkm["Pembimbing"].value_counts().reset_index()
    dosen_unique_counts.columns = ["Pembimbing", "Jumlah"]
    # st.bar_chart(dosen_unique_counts.set_index("Pembimbing"))
    # Membuat bar chart dengan warna otomatis untuk setiap kelas
    dosen_bar_chart = alt.Chart(dosen_unique_counts).mark_bar().encode(
        x=alt.X("Pembimbing", sort="-y", axis=alt.Axis(labelAngle=-45) ),  # Sort berdasarkan jumlah
        y="Jumlah",
        color=alt.Color("Pembimbing", legend=None),  # Warna otomatis untuk setiap Pembimbing
        tooltip=["Pembimbing", "Jumlah"]  # Tooltip interaktif
    ).properties(
        title="Jumlah PKM Per Pembimbing"
    )

    # Tampilkan bar chart di Streamlit
    st.altair_chart(dosen_bar_chart, use_container_width=True)
    
with col2:
    # st.subheader("Bidang PKM")
    bidang_unique_counts = data_pkm["Bidang"].value_counts().reset_index()
    bidang_unique_counts.columns = ["Bidang", "Jumlah"]
    # st.bar_chart(bidang_unique_counts.set_index("Bidang"))
    bidang_bar_chart = alt.Chart(bidang_unique_counts).mark_bar().encode(
        x=alt.X("Bidang", sort="-y", axis=alt.Axis(labelAngle=-45) ),  # Sort berdasarkan jumlah
        y="Jumlah",
        color=alt.Color("Bidang", legend=None),  # Warna otomatis untuk setiap Bidang
        tooltip=["Bidang", "Jumlah"]  # Tooltip interaktif
    ).properties(
        title="Jumlah PKM Per Bidang"
    )

    # Tampilkan bar chart di Streamlit
    st.altair_chart(bidang_bar_chart, use_container_width=True)



