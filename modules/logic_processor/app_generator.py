# /modules/logic_processor/app_generator.py
# Modul fungsional spesifik untuk pemrosesan generator kerangka web

from core.formalism_engine import FormalismEngine

def run_app_generator(name: str, app_type: str) -> str:
    """
    Fungsi antarmuka untuk memanggil mesin pembuat kerangka web.
    """
    engine = FormalismEngine(app_name=name, app_type=app_type)
    result = engine.generate_structure()
    
    if result["status"] == "success":
        return result["output_code"]
    else:
        raise RuntimeError(result["message"])
