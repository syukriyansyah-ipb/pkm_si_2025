import pandas as pd
import streamlit as st
import altair as alt

st.set_page_config(
    page_title="Laporan PKM SISTEM INFORMASI 2025",  # Judul halaman
    page_icon=":bar_chart:",           # Ikon (emoji atau path file)
    layout="wide",                     # Mengatur mode layout menjadi lebar
    initial_sidebar_state="collapsed"  # Menyembunyikan sidebar secara default
)

# Membaca CSV langsung dari URL
# presensi_sosialisasi = pd.read_excel('daftar_hadir_sosialisasi.xlsx')
# presensi_sosialisasi["Kelas"] = presensi_sosialisasi["Kelas"].str.replace(" ", "").str.upper()
# unique_counts = presensi_sosialisasi["Kelas"].value_counts().reset_index()
# unique_counts.columns = ["Kelas", "Jumlah"]


# kelas - pkm
data_pkm = pd.read_excel('daftar_pkm_2025.xlsx')


# Konten
st.markdown("""
### Selamat Datang di Portal Informasi PKM
Saat ini jumlah PKM yang terdaftar adalah sebanyak 20 buah.
Akses link berikut untuk pendaftaran, pedoman, dan bahan lainnya.
""")

# Fungsi untuk membuat card
def create_card_info(title, description, link, button_text):
    card_template = f"""
    <div style="border:1px solid #ddd; border-radius:8px; padding:16px; margin-bottom:16px; box-shadow:2px 2px 10px rgba(0,0,0,0.1) text-center;">
        <h3>{title}</h3>
        <p>{description}</p>
        <a href="{link}" target="_blank" style="text-decoration:none;">
            <button style="background-color:#4CAF50; color:white; padding:8px 16px; border:none; border-radius:4px; cursor:pointer;">
                {button_text}
            </button>
        </a>
    </div>
    """
    return card_template

# Fungsi untuk membuat card
def create_card(title, description, link, button_text):
    card_template = f"""
    <div style="border:1px solid #ddd; border-radius:8px; padding:16px; margin-bottom:16px; box-shadow:2px 2px 10px rgba(0,0,0,0.1) text-center;">
        <h3>{title}</h3>
        <p>{description}</p>
        <a href="{link}" target="_blank" style="text-decoration:none;">
            <button style="background-color:#4CAF50; color:white; padding:8px 16px; border:none; border-radius:4px; cursor:pointer;">
                {button_text}
            </button>
        </a>
    </div>
    """
    return card_template

card1, card2 = st.columns(2, gap='small')
with card1:
    # Card 1 - Link Pendaftaran
    st.markdown(create_card(
        title="Link Pendaftaran PKM",
        description="Daftarkan judul PKM Anda melalui tautan berikut.",
        link="https://forms.gle/UeqZyMUM5d2q14nM8",  # Ganti dengan URL pendaftaran
        button_text="Daftar Sekarang"
    ), unsafe_allow_html=True)

with card2:
    # Card 2 - Pedoman PKM
    st.markdown(create_card(
        title="Pedoman PKM",
        description="Akses panduan resmi PKM untuk mempersiapkan proposal Anda.",
        link="https://simbelmawa.kemdikbud.go.id/portal/penerimaan-proposal-pkm-2024/",  # Ganti dengan URL pedoman
        button_text="Lihat Pedoman"
    ), unsafe_allow_html=True)


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



