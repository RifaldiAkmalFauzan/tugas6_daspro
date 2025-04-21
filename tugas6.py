print("=" * 60)
print(" PROGRAM KONVERSI SKOR NILAI MAHASISWA ".center(60, "="))
print("=" * 60)
print("\n>> Ketik 'q' untuk keluar <<\n")

while True:
    skor_input = input(">> Masukkan skor (0-100): ").strip()
    
    if not skor_input:
        print("\nERROR: Input tidak boleh kosong!\n")
        continue
        
    if skor_input.lower() == 'q':
        print("\nProgram berhenti. Sampai jumpa!")
        break
        
    try:
        skor = float(skor_input)
        if 0 <= skor <= 100:
            print("\n" + " HASIL KONVERSI ".center(60, "="))
            if skor >= 90:
                print("[A] Skor {:.2f}: Nilai A".format(skor))
                print("Predikat: Dengan Pujian")
            elif skor >= 80:
                print("[B] Skor {:.2f}: Nilai B".format(skor))
                print("Predikat: Sangat Memuaskan")
            # ... (lanjutan kondisi lainnya)
            print("=" * 60 + "\n")
            break
        else:
            print("\nERROR: Skor harus 0-100!\n")
    except ValueError:
        print("\nERROR: Input harus angka (contoh: 75.5)!\n")