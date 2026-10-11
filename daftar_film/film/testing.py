# Pengujian otomatis untuk program daftar film.

import unittest
import tempfile
import os
from unittest.mock import patch

from film.processing import KoleksiFilm
from film.validasi import DataFilmError

class TestKoleksiFilm(unittest.TestCase):

    # Menggunakan file sementara agar data asli tidak terganggu.
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.file_data = os.path.join(self.folder.name, "data.txt")
        self.file_laporan = os.path.join(
            self.folder.name, "laporan.txt"
        )

        self.patch_data = patch("film.fileio.FILE_DATA", self.file_data)
        self.patch_laporan = patch(
            "film.fileio.FILE_LAPORAN", self.file_laporan
        )

        self.patch_data.start()
        self.patch_laporan.start()

        with open(self.file_data, "w", encoding="utf-8") as file:
            file.write("")

        self.koleksi = KoleksiFilm()

    def tearDown(self):
        self.patch_data.stop()
        self.patch_laporan.stop()
        self.folder.cleanup()

    def test_tambah_film(self):
        film = self.koleksi.tambah_film(
            "F001", "Interstellar", "Sci-Fi", 2014
        )
        self.assertEqual(film.judul, "Interstellar")

    def test_cari_film(self):
        self.koleksi.tambah_film(
            "F001", "Interstellar", "Sci-Fi", 2014
        )
        film = self.koleksi.cari_film("F001")

        self.assertIsNotNone(film)
        self.assertEqual(film.tahun, 2014)

    def test_hapus_film(self):
        self.koleksi.tambah_film(
            "F001", "Interstellar", "Sci-Fi", 2014
        )
        self.koleksi.hapus_film("F001")

        self.assertEqual(len(self.koleksi.daftar_film), 0)

    def test_filter_genre(self):
        self.koleksi.tambah_film(
            "F001", "Interstellar", "Sci-Fi", 2014
        )
        self.koleksi.tambah_film(
            "F002", "The Notebook", "Romance", 2004
        )

        hasil = self.koleksi.filter_genre("Sci-Fi")
        self.assertEqual(len(hasil), 1)

    def test_tahun_film(self):
        self.koleksi.tambah_film(
            "F001", "Interstellar", "Sci-Fi", 2014
        )
        self.koleksi.tambah_film(
            "F002", "The Batman", "Action", 2022
        )

        hasil = self.koleksi.film_berdasarkan_tahun(2014, 2022)
        self.assertEqual(len(hasil), 2)

# Menjalankan seluruh pengujian.
if __name__ == "__main__":
    unittest.main()
  
