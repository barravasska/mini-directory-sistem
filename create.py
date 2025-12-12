import os

def create_file(nama_file, isi_konten=""):
    # 1. Validate: if file already exist 
    if os.path.exists(nama_file):
        print(f"[ERROR] Gagal membuat file: '{nama_file}' sudah ada.")
        return False

    try:
        # 2. Execute: Create a new file
        with open(nama_file, 'w') as file:
            file.write(isi_konten)
        
        print(f"[SUKSES] File '{nama_file}' berhasil dibuat.")
        return True

    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan sistem: {e}")
        return False