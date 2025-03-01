# Menerima input bilangan bulat a, b, dan c
a = int(input("masukan bilangan a: "))
b = int(input("masukan bilangan b: "))
c = int(input("masukan bilangan c: "))

# Memeriksa apakah semua kondisi terpenuhi
if (a > b or b > c) and (a % 2 == 0 and c % 2 != 0) and (b != c):
    print("kondisi terpenuhi")
else:
    print("kondisi tidak terpenuhi")
