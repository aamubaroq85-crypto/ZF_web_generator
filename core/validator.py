# /core/validator.py
# Validasi parameter input sesuai kaidah Zuhri Formalism (Zero Assumption & Strict Types)

class ParameterValidator:
    @staticmethod
    def validate_app_config(app_name: str, app_type: str) -> bool:
        """
        Memastikan parameter nama aplikasi dan tipe valid sebelum diproses.
        Mencegah asumsi liar atau input kosong.
        """
        if not isinstance(app_name, str) or not app_name.strip():
            raise ValueError("Error Zuhri Formalism: Nama aplikasi tidak boleh kosong atau tidak valid.")
        
        allowed_types = ["webapp", "landing_page"]
        if app_type not in allowed_types:
            raise ValueError(f"Error Zuhri Formalism: Tipe aplikasi '{app_type}' tidak dikenali. Pilih antara: {allowed_types}")
            
        return True
