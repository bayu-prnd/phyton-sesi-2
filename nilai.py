def cek_kelulusan(nilai_matematika, nilai_sains, nilai_bahasa_inggris):
    # Menghitung rata-rata nilai
    rata_rata = (nilai_matematika + nilai_sains + nilai_bahasa_inggris) / 3

    # Menghitung jumlah mata pelajaran yang nilainya di bawah 70
    mata_pelajaran_bawah_70 = sum(1 for nilai in [nilai_matematika, nilai_sains, nilai_bahasa_inggris] if nilai < 70)

    # Mengecek apakah ada nilai sempurna (100) pada salah satu mata pelajaran
    nilai_sempurna = 100 in [nilai_matematika, nilai_sains, nilai_bahasa_inggris]

    # Memeriksa apakah memenuhi kriteria kelulusan
    if rata_rata > 75 and mata_pelajaran_bawah_70 == 1 and nilai_sempurna:
        return "Anda lulus!"
    else:
        return "Anda tidak lulus."

# Input nilai untuk 3 mata pelajaran
nilai_matematika = float(input("Masukkan nilai Matematika: "))
nilai_sains = float(input("Masukkan nilai Sains: "))
nilai_bahasa_inggris = float(input("Masukkan nilai Bahasa Inggris: "))

# Mengecek kelulusan
hasil = cek_kelulusan(nilai_matematika, nilai_sains, nilai_bahasa_inggris)
print(hasil)
