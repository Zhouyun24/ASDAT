total = int(input("Total Harus Dibayar : "))
bayar = int(input("Bayar : "))
print("-"*30)
kembalian = bayar - total
print(f"kembalian : {kembalian}")
print("Rincian")
rp50000 = kembalian // 50000
print(f"Rp. 50000 : {rp50000} lembar")
kembalian %= 50000
rp20000 = kembalian // 20000
print(f"Rp. 20000 : {rp20000} lembar")
kembalian %= 20000
rp10000 = kembalian // 10000
print(f"Rp. 10000 : {rp10000} lembar")
kembalian %= 10000
rp5000 = kembalian // 5000
print(f"Rp. 5000 : {rp5000} lembar")
kembalian %= 5000
rp2000 = kembalian // 2000
print(f"Rp. 2000 : {rp2000} lembar")
kembalian %= 2000
rp1000 = kembalian // 1000
print(f"Rp. 1000 : {rp1000} lembar")
kembalian %= 1000
