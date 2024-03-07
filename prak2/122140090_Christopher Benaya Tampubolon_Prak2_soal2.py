def log_method_call(method):
    def wrapper(self, *args, **kwargs):
        print(f"{self.jabatan}: Memanggil method {method.__name__}")
        result = method(self, *args, **kwargs)
        print(f"{self.jabatan}: Selesai memanggil method {method.__name__}")
        return result
    return wrapper

class Karyawan:
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan
        print(f"{self.jabatan} {self.nama} bergabung.")

    @log_method_call
    def bekerja(self):
        print(f"{self.jabatan} {self.nama}: Sedang bekerja.")

    @log_method_call
    def istirahat(self):
        print(f"{self.jabatan} {self.nama}: Sedang istirahat.")

    @log_method_call
    def __del__(self):
        print(f"{self.jabatan} {self.nama} keluar.")


manajer = Karyawan("Christopher", "Manajer")
pegawai = Karyawan("Christopher", "Pegawai")


manajer.bekerja()
pegawai.bekerja()
manajer.istirahat()


del manajer
del pegawai
