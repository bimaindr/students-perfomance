# WAJIB DI BARIS 1 & 2: Selesaikan urusan SSL sebelum import yang lain!
import ssl

def dummy_load_windows_certs(*args, **kwargs):
    pass

ssl.SSLContext.load_default_certs = dummy_load_windows_certs

# Baru setelah aman, kita import library Streamlit
import sys
from streamlit.web import cli as stcli

if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "app.py"]
    sys.exit(stcli.main())
