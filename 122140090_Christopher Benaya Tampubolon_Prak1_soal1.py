batas_bawah = int(input("batas bawah : "))
batas_atas = int(input("batas atas : "))

if batas_bawah < 0 or batas_atas < 0:
    print("Batas bawah dan atas yang dimasukkan tidak boleh di bawah Nol.")
else:
    jumlah_ganjil = 0
    for bilangan in range(batas_bawah, batas_atas + 1):
        if bilangan % 2 != 0:
            jumlah_ganjil += 1

    print(f"Total: {jumlah_ganjil}")
