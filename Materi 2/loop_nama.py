# Minta nama dari pengguna
nama = input("Siapa nama kamu? ")

# Contoh menggunakan for loop
print("\nContoh for loop:")

# Mengulang menampilkan nama sebanyak 5 kali
for i in range(5):
    print(f"{i+1}. {nama}")

# Contoh menggunakan while loop
print("\nContoh while loop:")

count = 0
while count < 5:
    print(f"{count+1}. {nama}")
    count += 1

print("\nPerulangan selesai!")
