saldoAwal = int(input("Masukan Saldo : "))
bunga = int(input("Masukan Bunga : "))
jangkaWaktu = int(input("Masukan Jangka Waktu : "))
saldoAkhir = saldoAwal*(1+bunga/100)**jangkaWaktu
print("-"*30)
print(f"Saldo Akhir : {saldoAkhir:.0f}")

