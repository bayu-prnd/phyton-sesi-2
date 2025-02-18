def luas_persegi(a, b):
  result = a * b
  print(result)
luas_persegi(8, 8)

def uang_kembalian(total_belanja, uang_yang_dibayarkan):
  result = uang_yang_dibayarkan - total_belanja
  print(result)
uang_kembalian(20000, 35000)

def kalkulator(a, b):
  pertambahan = a + b
  pengurangan = a - b
  perkalian = a * b
  pembagian = a / b
  print(pertambahan, pengurangan, perkalian, pembagian)
kalkulator(8, 8)

def diskon(bayar, diskon):
  result = bayar * diskon
  print(result)
diskon(45000, 20/100)

def keuntungan(harga_jual, modal):
  result = harga_jual - modal
  print(f"modal = {modal}, harga jual = {harga_jual}, keuntungan = {result}")
keuntungan(3000000, 2500000)

buah = "semangka"
harga = 15000 

def ubah_nilai(a, b): 
  buah = a
  harga = b
  print(buah, harga)
  
ubah_nilai("melon", 17000)

def rata_rata(*args):
  list_data = []
  for data in args:
    list_data.append(data)

  total = sum(list_data[:3])
  rata_rata = total / 3

  return rata_rata

print(rata_rata(15, 11, 10))

def luas_keliling_segitiga(sa, sb, sc, alas, tinggi):
   luas = 1/2 * alas * tinggi
   keliling = sa + sb +sc

   print(f"luas = {luas} dan keliling = {keliling}")

luas_keliling_segitiga(3, 7, 5, 13, 15)