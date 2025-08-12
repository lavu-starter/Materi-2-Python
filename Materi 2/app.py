# Contoh menggunakan for loop
print("Contoh for loop:")

# for i in range(5): berarti i akan bernilai 0,1,2,3,4
for i in range(5):
    print(f"Ini adalah perulangan ke-{i}")

print("\nContoh while loop:")

# Contoh menggunakan while loop
count = 0  # variabel awal sebagai penghitung

# Selama count kurang dari 5, maka blok di bawah dijalankan terus
while count < 5:
    print(f"Ini adalah perulangan ke-{count}")
    count += 1  # menambahkan count sebanyak 1 setiap kali loop berjalan

print("\nPerulangan selesai!")
