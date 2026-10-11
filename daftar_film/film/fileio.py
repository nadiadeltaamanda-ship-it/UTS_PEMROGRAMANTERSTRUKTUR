# Mengatur penyimpanan data dan laporan film.

import os

FOLDER_PROYEK = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

FILE_DATA = os.path.join(FOLDER_PROYEK, "data_film.txt")
FILE_LAPORAN = os.path.join(FOLDER_PROYEK, "laporan.txt")

# Mode x membuat file baru tanpa menimpa file lama.
def siapkan_file():
    try:
        with open(FILE_DATA, "x", encoding="utf-8") as file:
            file.write("")
    except FileExistsError:
        pass

# Mode r digunakan untuk membaca data film.
def baca_film():
    siapkan_file()
    daftar = []

    try:
        with open(FILE_DATA, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                try:
                    bagian = baris.strip().split("|")

                    if len(bagian) != 4:
                        raise ValueError("Format data tidak sesuai.")

                    id_film, judul, genre, tahun = bagian

                    daftar.append({
                        "id_film": id_film,
                        "judul": judul,
                        "genre": genre,
                        "tahun": int(tahun)
                    })

                except (ValueError, TypeError):
                    # Baris rusak dilewati agar program tetap berjalan.
                    print(f"Baris data ke-{nomor} dilewati karena rusak.")

    except FileNotFoundError:
        print("File film belum ditemukan.")
        siapkan_file()

    return daftar

# Mode w menulis ulang seluruh data film.
def simpan_film(daftar_film):
    with open(FILE_DATA, "w", encoding="utf-8") as file:
        for film in daftar_film:
            file.write(
                f"{film.id_film}|{film.judul}|"
                f"{film.genre}|{film.tahun}\n"
            )

# Mode a menambahkan aktivitas ke laporan.
def tambah_log(pesan):
    with open(FILE_LAPORAN, "a", encoding="utf-8") as file:
        file.write(pesan + "\n")

# Mode w digunakan untuk menyimpan laporan terbaru.
def simpan_laporan(teks):
    with open(FILE_LAPORAN, "w", encoding="utf-8") as file:
        file.write(teks)

if __name__ == "__main__":
    print("Jumlah film:", len(baca_film()))
