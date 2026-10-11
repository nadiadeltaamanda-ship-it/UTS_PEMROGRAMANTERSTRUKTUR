# Mengelola koleksi film menggunakan class dan fungsi.

from film import fileio, validasi

# Menyimpan informasi satu film.
class Film:
    def __init__(self, id_film, judul, genre, tahun, **atribut):
        self.id_film = validasi.validasi_id(id_film)
        self.judul = validasi.validasi_teks(judul, "Judul")
        self.genre = validasi.validasi_teks(genre, "Genre")
        self.tahun = validasi.validasi_tahun(tahun)
        self.atribut = atribut

# Mengelola seluruh koleksi film.
class KoleksiFilm:
    def __init__(self):
        self.daftar_film = []

        for data in fileio.baca_film():
            try:
                self.daftar_film.append(Film(**data))
            except validasi.DataFilmError as error:
                print("Data film dilewati:", error)
    
    # Mencari film berdasarkan ID.
    def cari_film(self, id_film):
        for film in self.daftar_film:
            if film.id_film == id_film:
                return film

        return None

    # **kwargs menerima atribut tambahan, misalnya sutradara.
    def tambah_film(self, id_film, judul, genre, tahun, **atribut):
        if self.cari_film(id_film) is not None:
            raise validasi.DataFilmError("ID film sudah digunakan.")

        film_baru = Film(
            id_film=id_film,
            judul=judul,
            genre=genre,
            tahun=tahun,
            **atribut
        )

        self.daftar_film.append(film_baru)
        self.simpan()

        fileio.tambah_log(f"Film ditambahkan: {film_baru.judul}")

        return film_baru
      
    # Menghapus film berdasarkan ID.
    def hapus_film(self, id_film):
        film = self.cari_film(id_film)

        if film is None:
            raise validasi.DataFilmError("Film tidak ditemukan.")

        self.daftar_film.remove(film)
        self.simpan()

        fileio.tambah_log(f"Film dihapus: {film.judul}")
      
    # Mencari judul yang mengandung kata tertentu.
    def cari_judul(self, kata_kunci):
        kata_kunci = kata_kunci.lower()

        return [
            film for film in self.daftar_film
            if kata_kunci in film.judul.lower()
        ]

    # lambda mengurutkan film berdasarkan judul.
    def urutkan_film(self):
        return sorted(
            self.daftar_film,
            key=lambda film: film.judul.lower()
        )

    # Memfilter film berdasarkan genre.
    def filter_genre(self, genre):
        return list(
            filter(
                lambda film: film.genre.lower() == genre.lower(),
                self.daftar_film
            )
        )

    # *args memungkinkan pencarian satu atau beberapa tahun.
    def film_berdasarkan_tahun(self, *tahun):
        if not tahun:
            return self.urutkan_film()

        return [
            film for film in self.daftar_film
            if film.tahun in tahun
        ]
      
    # **kwargs menerima daftar genre yang ingin dianalisis.
    def ringkasan_genre(self, **genre_dicari):
        hasil = {}

        for label, genre in genre_dicari.items():
            hasil[label] = len(self.filter_genre(genre))

        return hasil

    # Menyimpan seluruh perubahan ke file.
    def simpan(self):
        fileio.simpan_film(self.daftar_film)

    # Membuat laporan daftar film.
    def buat_laporan(self):
        baris = ["===== LAPORAN DAFTAR FILM ====="]

        for film in self.urutkan_film():
            baris.append(
                f"{film.id_film} | {film.judul} | "
                f"{film.genre} | {film.tahun}"
            )

        baris.append(f"Total film: {len(self.daftar_film)}")

        laporan = "\n".join(baris) + "\n"
        fileio.simpan_laporan(laporan)

        return laporan

# Pengujian lokal sederhana.
if __name__ == "__main__":
    koleksi = KoleksiFilm()
    assert isinstance(koleksi.daftar_film, list)

    print("Modul processing berhasil dijalankan.")
