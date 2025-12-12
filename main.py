import sys
# This syntax is for impor any function
from create import create_file 

def main():
    print("=== SISTEM FILE MINI ===")
    print("PANDUAN KOMAND:")
    print("\"mkdir <nama_file>\" - Membuat file baru (Isi default kosong)")
    print("\"cat\" - Membaca isi file")
    print("\"nano\" - Membuka teks editor nano untuk mengedit file")
    print("\"rm\" - Menghapus file") 
    print("\"exit\" - Keluar dari program")
    
    while True:
        try:
            # 1. Mengambil input user layaknya terminal
            # Contoh input: create data.txt
            command_input = input("\nuser@system:~$ ").strip().split()

            if not command_input:
                continue # Skip jika user cuma tekan enter

            perintah = command_input[0].lower() # Ambil kata pertama (misal: create)

            # --- LOGIKA CREATE ---
            if perintah == "mkdir":
                # Cek apakah user memasukkan nama file
                if len(command_input) < 2:
                    print("[INFO] Harap masukkan nama file. Contoh: create biodata.txt")
                else:
                    nama_file = command_input[1]
                    # Panggil fungsi dari file create.py
                    create_file(nama_file)

            # --- KELUAR ---
            elif perintah == "exit":
                print("Sistem dimatikan.")
                break
            
            # --- COMMAND TIDAK DIKENAL ---
            else:
                print(f"[INFO] Perintah '{perintah}' belum tersedia atau salah ketik.")

        except KeyboardInterrupt:
            # Menangani jika user tekan Ctrl+C
            print("\nThanks for using our system.")
            break

if __name__ == "__main__":
    main()