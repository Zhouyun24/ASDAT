jamMasuk1 = int(input("Jam Masuk : "))
menitMasuk = int(input("Menit Masuk : "))
jamKeluar1 = int(input("Jam Keluar : "))
menitKeluar = int(input("Menit Keluar : "))
print("-"*30)
jamMasuk2 = jamMasuk1 * 60
jamKeluar2 = jamKeluar1 * 60
lamaRental = (jamKeluar2+menitKeluar)-(jamMasuk2 + menitMasuk)
biayaRental = 5000 *(lamaRental/60)
print(f"Lama rental : {lamaRental} ({jamMasuk1} Jam {menitMasuk} Menit)")
print(f"Biaya rental : {biayaRental}")