def cek_angka(angka):
    # Menentukan angka 
    if angka > 0:
        return "positif"
    elif angka < 0:
        return "negatif"
    else:
        return "nol"
    
# Inpu angka dari pengguna
angka = float(input("masukan angka: "))

# Menentukan angka
hasil = cek_angka(angka)
print(f"angka {angka} adalah {hasil}. ")