# Program utama daftar film.

from film.processing import KoleksiFilm
from film.validasi import DataFilmError

# Menampilkan pilihan yang tersedia.
def tampilkan_menu():
    print("\n===== APLIKASI DAFTAR FILM =====")
    print("1. Tambah film")
    print("2. Tampilkan semua film")
    print("3. Cari film berdasarkan ID")
    print("4. Cari film berdasarkan judul")
    print("5. Filter berdasarkan genre")
    print("6. Hapus film")
    print("7. Buat laporan")
    print("0. Keluar")

# Menjalankan menu dan memproses pilihan pengguna.
def jalankan_program():
    koleksi = KoleksiFilm()

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()

        try:
            if pilihan == "1":
                id_film = input("ID film: ").strip()
                judul = input("Judul film: ").strip()
                genre = input("Genre film: ").strip()
                tahun = int(input("Tahun rilis: "))

                sutradara = input(
                    "Nama sutradara (opsional): "
                ).strip()

                atribut = {}
                if sutradara:
                    atribut["sutradara"] = sutradara

                koleksi.tambah_film(
                    id_film=id_film,
                    judul=judul,
                    genre=genre,
                    tahun=tahun,
                    **atribut
                )

                print("Film berhasil ditambahkan.")

            elif pilihan == "2":
                daftar = koleksi.urutkan_film()

                if not daftar:
                    print("Belum ada film yang tersimpan.")
                else:
                    for film in daftar:
                        print(
                            f"{film.id_film} | {film.judul} | "
                            f"{film.genre} | {film.tahun}"
                        )

            elif pilihan == "3":
                id_film = input("Masukkan ID film: ").strip()
                film = koleksi.cari_film(id_film)

                if film is None:
                    print("Film tidak ditemukan.")
                else:
                    print(
                        f"Judul: {film.judul}\n"
                        f"Genre: {film.genre}\n"
                        f"Tahun: {film.tahun}"
                    )

                    if film.atribut.get("sutradara"):
                        print(
                            f"Sutradara: "
                            f"{film.atribut['sutradara']}"
                        )

            elif pilihan == "4":
                kata = input("Masukkan judul atau kata kunci: ")
                hasil = koleksi.cari_judul(kata)

                if hasil:
                    for film in hasil:
                        print(f"{film.judul} ({film.tahun})")
                else:
                    print("Film tidak ditemukan.")

            elif pilihan == "5":
                genre = input("Masukkan genre: ")
                hasil = koleksi.filter_genre(genre)

                if hasil:
                    for film in hasil:
                        print(f"{film.judul} - {film.genre}")
                else:
                    print("Tidak ada film dengan genre tersebut.")

            elif pilihan == "6":
                id_film = input("ID film yang akan dihapus: ")
                koleksi.hapus_film(id_film)
                print("Film berhasil dihapus.")

            elif pilihan == "7":
                print(koleksi.buat_laporan())
                print("Laporan disimpan di laporan.txt.")

            elif pilihan == "0":
                print("Program selesai.")
                break

            else:
                print("Pilihan tidak tersedia.")

        except ValueError:
            print("Input tahun harus berupa angka.")

        except DataFilmError as error:
            print("Terjadi kesalahan:", error)

        except OSError as error:
            print("Terjadi masalah pada file:", error)

# Program dijalankan hanya jika main.py dieksekusi langsung.
if __name__ == "__main__":
    jalankan_program()
  
