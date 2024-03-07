class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        self.__nim = nim
        self.__nama = nama
        self.angkatan = angkatan
        self.isMahasiswa = isMahasiswa

    def get_nim(self):
        return self.__nim

    def set_nim(self, nim):
        self.__nim = nim

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def info_mahasiswa(self):
        return f"NIM: {self.__nim}, Nama: {self.__nama}, Angkatan: {self.angkatan}, Mahasiswa: {self.isMahasiswa}"

    def status_mahasiswa(self):
        if self.isMahasiswa:
            return "Status: Mahasiswa"
        else:
            return "Status: Bukan Mahasiswa"

    def tahun_lulus(self):
        return 2024 - self.angkatan + 3


mahasiswa1 = Mahasiswa(nim="122140090", nama="Christopher", angkatan=2022)
mahasiswa2 = Mahasiswa(nim="12210091", nama="Rika", angkatan=2022)

mahasiswa1.set_nama("Christopher")
nim_mahasiswa1 = mahasiswa1.get_nim()

print(mahasiswa1.info_mahasiswa())
print(mahasiswa1.status_mahasiswa())
print(f"Tahun Lulus: {mahasiswa1.tahun_lulus()}")

print(mahasiswa2.info_mahasiswa())
print(mahasiswa2.status_mahasiswa())
print(f"Tahun Lulus: {mahasiswa2.tahun_lulus()}")
