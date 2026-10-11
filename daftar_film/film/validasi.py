# Memeriksa data film agar valid.

class DataFilmError(Exception):
    """Error khusus untuk data film yang tidak valid."""
    pass

def validasi_teks(teks, nama_field):
    if not isinstance(teks, str) or not teks.strip():
        raise DataFilmError(f"{nama_field} tidak boleh kosong.")

    return teks.strip()

def validasi_tahun(tahun):
    if isinstance(tahun, bool) or not isinstance(tahun, int):
        raise DataFilmError("Tahun harus berupa bilangan bulat.")

    if tahun < 1888 or tahun > 2100:
        raise DataFilmError("Tahun film tidak valid.")

    return tahun

def validasi_rating(rating):
    if isinstance(rating, bool) or not isinstance(rating, (int, float)):
        raise DataFilmError("Rating harus berupa angka.")

    if not 0 <= rating <= 10:
        raise DataFilmError("Rating harus antara 0 sampai 10.")

    return rating

def validasi_id(id_film):
    return validasi_teks(id_film, "ID film")

# Pengujian lokal modul validasi.
if __name__ == "__main__":
    assert validasi_teks("Interstellar", "Judul") == "Interstellar"
    assert validasi_tahun(2014) == 2014
    assert validasi_rating(8.7) == 8.7

    print("Pengujian validasi berhasil.")
