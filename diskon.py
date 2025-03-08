def hitung_total_bayar(total_belanja):
    if total_belanja > 100000:
        diskon = 0.10  # diskon 10%
    elif total_belanja > 50000:
        diskon = 0.05  # diskon 5%
    else:
        diskon = 0  # tidak ada diskon

    # menghitung total yang harus dibayar setelah diskon
    total_setelah_diskon = total_belanja - (total_belanja * diskon)

    return total_setelah_diskon, diskon

# Input total belanja dari pengguna
total_belanja = float(input("Masukkan total belanja: Rp "))

# Menghitung total yang harus dibayar dan besarnya diskon
total_bayar, diskon = hitung_total_bayar(total_belanja)

# Menampilkan hasil
if diskon > 0:
    print(f"Anda mendapatkan diskon sebesar {diskon * 100}%")
else:
    print("Anda tidak mendapatkan diskon.")

print(f"Total yang harus dibayar: Rp {total_bayar:.2f}")