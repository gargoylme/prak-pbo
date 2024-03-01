pi = 3.14

def hitung_luas_dan_keliling_lingkaran(jari_jari):
    if jari_jari < 0:
        print("Jari-jari lingkaran tidak boleh negatif.")
    else:
        luas = pi * (jari_jari ** 2)
        keliling = 2 * pi * jari_jari

        print(f"Luas lingkaran: {luas}")
        print(f"Keliling lingkaran: {keliling}")

try:
    jari_jari = float(input("Masukkan jari-jari lingkaran: "))
    hitung_luas_dan_keliling_lingkaran(jari_jari)
except ValueError:
    print("Masukkan harus berupa angka.")
