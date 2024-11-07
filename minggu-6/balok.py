p = int(input("Panjang : "))
l = int(input("Lebar : "))
t = int(input("Tinggi : "))
luas = 2 * p * l + 2 * p * t * 2 * l * t
volume = p * l * t
print("Luas Selimut Balok : %i" % (luas))
print("Luas Volume Balok : %i" % (volume))
print(f"Dimesi : {p} x {l} x {t}")
