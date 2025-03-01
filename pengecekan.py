def cek_tipe_input(input1, input2, input3):
    if isinstance(input1, str) and isinstance(input2, int) and isinstance(input3, float):
        return "tipe input valid"
    else:
        return "tipe input tidak valid"
    
# kasus 1: data sesuai dengan yang diinginkan
print(cek_tipe_input("selamat datang", 123, 3.14))

# kasus 2: data pertama bukan string
print(cek_tipe_input(123, 123, 3.14))

#kaus 3: data kedua bukan integer
print(cek_tipe_input("selamat datang", "123", 3.14))

#kasus 4: data ketiga bukan float
print(cek_tipe_input("selamat datang", 123, "3.14"))