# /app.py
# Antarmuka Pengguna Utama (Streamlit) - Zuhri Formalism Generator WebApp

import streamlit as st
from modules.logic_processor.app_generator import run_app_generator

# Konfigurasi Halaman sesuai DESIGN.md (Tema & Estetika)
st.set_page_config(
    page_title="Zuhri Formalism WebApp Generator",
    page_icon="⚡",
    layout="centered"
)

# Styling CSS Kustom (Token Warna: #0F172A, #0284C7, #F8FAFC)
st.markdown("""
    <style>
    .main {
        background-color: #F8FAFC;
        color: #0F172A;
    }
    .stButton>button {
        background-color: #0284C7;
        color: white;
        border-radius: 6px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #0369A1;
    }
    </style>
""", unsafe_allow_html=True)

# Judul Utama Aplikasi
st.title("⚡ Zuhri Formalism WebApp Generator")
st.markdown("Sistem pembuat kerangka aplikasi web deterministik di bawah koridor **ZF_DK**.")
st.markdown("---")

# Formulir Input Pengguna
with st.form("generator_form"):
    st.subheader("Konfigurasi Parameter Aplikasi")
    app_name_input = st.text_input("Nama Aplikasi / Proyek", value="Aa Baroq Digital App")
    app_type_input = st.selectbox("Pilih Tipe Struktur", options=["webapp", "landing_page"])
    
    submitted = st.form_submit_button("Hasilkan Kerangka (Generate)")

# Eksekusi Logika Berdasarkan Input
if submitted:
    try:
        # Memanggil modul pemrosesan formal
        generated_code = run_app_generator(name=app_name_input, app_type=app_type_input)
        
        st.success("✨ Kerangka berhasil dihasilkan secara deterministik!")
        
        # Menampilkan Pratinjau Hasil Kode HTML
        st.subheader("Pratinjau Kode HTML:")
        st.code(generated_code, language="html")
        
        # Opsi Unduh Berkas
        st.download_button(
            label="Unduh Berkas HTML",
            data=generated_code,
            file_name="index.html",
            mime="text/html"
        )
        
    except Exception as e:
        # Penanganan error aman sesuai SECURITY.md
        st.error(f"Terjadi kesalahan validasi sistem: {str(e)}")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748B;'>Aa Baroq Applied Technologies — Zuhri Formalism Engine</p>", unsafe_allow_html=True)
