nama = input("Nama Barang : ")
harga = int(input("Harga  : Rp. "))
qty = int(input("Qty      : "))
print("-"*30)
subtotal = harga * qty
diskon = 0.20 *subtotal
total = subtotal - diskon
print(f"Sub Total	: Rp. {subtotal:10.0f}")
print(f"Diskon (20%)	: Rp. {diskon:10.0f}")
print(f"Total 		: Rp. {total:10.0f}")