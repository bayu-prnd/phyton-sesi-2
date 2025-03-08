def is_kabisat(tahun):
    if (tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0)):
        return True
    else:
        return False
    
# Menerima input tahun
tahun = int(input("masukan tahun: "))

# Mengecek apakah tahun tersebut kabisat atau bukan
if is_kabisat(tahun):
    print(f"{tahun} adalah tahun kabisat. ")
else:
    print(f"{tahun} bukan tahun kabisat. ")