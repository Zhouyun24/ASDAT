print("Harga Rental 5000")

masuk = input("Jam Masuk (hh:mm) : ").split(":")
keluar = input("Jam Keluar (hh:mm) : ").split(":")

jam_m , menit_m = int(masuk[0]), int(masuk[1])
jamk_k , menit_k = int(keluar[0]), int(keluar[1])

lamaRental = (jamk_k * 60 + menit_k) - (jam_m * 60 + menit_m)
hargaRental = (lamaRental / 60) * 5000

lama_j = lamaRental // 60
lama_m = lamaRental % 60

print(f"Lama Rental : {lamaRental} menit ({lama_j} Jam {lama_m} Menit)")
print(f"Harga Rental : {hargaRental:.0f}")
