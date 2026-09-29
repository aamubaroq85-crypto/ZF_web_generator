# /core/formalism_engine.py
# Inti eksekusi logika dan rumusan utama Zuhri Formalism

import os
from core.validator import ParameterValidator

class FormalismEngine:
    def __init__(self, app_name: str, app_type: str):
        # Jalankan validasi ketat dari lapisan hulu
        ParameterValidator.validate_app_config(app_name, app_type)
        self.app_name = app_name.strip()
        self.app_type = app_type.strip()

    def generate_structure(self) -> dict:
        """
        Menghasilkan struktur kerangka deterministik berdasarkan aturan desain.
        """
        try:
            # Menggunakan standar warna dari DESIGN.md (Slate Dark & Sky Blue)
            primary_color = "#0F172A"
            accent_color = "#0284C7"
            bg_color = "#F8FAFC"

            if self.app_type == "webapp":
                html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>{self.app_name}</title>
    <style>
        body {{ background-color: {bg_color}; color: {primary_color}; font-family: 'Inter', sans-serif; margin: 0; padding: 40px; }}
        header {{ border-bottom: 2px solid {accent_color}; padding-bottom: 20px; }}
        h1 {{ color: {accent_color}; }}
    </style>
</head>
<body>
    <header>
        <h1>{self.app_name}</h1>
        <p>Sistem WebApp Deterministik - Zuhri Formalism Engine</p>
    </header>
    <main>
        <section>
            <h2>Modul Utama Aktif</h2>
            <p>Sistem berjalan normal di bawah koridor keamanan ZF_DK.</p>
        </section>
    </main>
</body>
</html>"""
            else:
                html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>{self.app_name} - Landing Page</title>
    <style>
        body {{ background-color: {bg_color}; color: {primary_color}; font-family: 'Inter', sans-serif; text-align: center; padding: 80px; }}
        .btn {{ background-color: {accent_color}; color: #FFFFFF; padding: 12px 24px; border-radius: 6px; text-decoration: none; display: inline-block; }}
    </style>
</head>
<body>
    <h1>Selamat Datang di {self.app_name}</h1>
    <p>Solusi digital profesional berbasis arsitektur formal terstruktur.</p>
    <a href="#" class="btn">Mulai Sekarang</a>
</body>
</html>"""

            return {
                "status": "success",
                "app_name": self.app_name,
                "type": self.app_type,
                "output_code": html_content
            }

        except Exception as e:
            # Penanganan error aman sesuai SECURITY.md
            return {
                "status": "error",
                "message": f"Kegagalan eksekusi pada FormalismEngine: {str(e)}"
            }
