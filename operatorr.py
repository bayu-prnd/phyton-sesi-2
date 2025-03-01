# menerima masukan dari pengguna
nilai_x = input("masukan nilai untuk x: ")
nilai_y = input("masukan nilai untuk y: ")

# mengubah input menjadi boolean
nilai_x_boolean = bool(nilai_x)
nilai_y_boolean = bool(nilai_y)

#menampikan hasil  konversnsi
print(f"nilai x = {nilai_x_boolean}, nilai y = {nilai_y_boolean}")

# x and ya
print(f"x and y: {nilai_x_boolean and nilai_y_boolean}")

# x or y
print(f"x or y: {nilai_x_boolean or nilai_y_boolean}")

# not x
print(f"not x: {not nilai_x_boolean}")

# x xor y
print(f"x xor y: {nilai_x_boolean != nilai_y_boolean}")