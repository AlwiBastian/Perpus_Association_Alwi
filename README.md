# Perpus_Association_Alwi
Program ini merupakan implementasi sederhana dari sistem peminjaman buku di perpustakaan menggunakan konsep Association antara dua kelas utama, yaitu Book (Buku) dan LibraryMember (Anggota Perpustakaan). Setiap objek LibraryMember akan terkait dengan beberapa objek Book yang merupakan daftar buku yang dipinjam oleh anggota tersebut.

## Fungsi dan Fitur

### 1. Kelas Book:

#### Atribut:
- title (string): Judul buku.
- author (string): Penulis buku.
- is_available (bool): Status ketersediaan buku (True jika tersedia, False jika sedang dipinjam).

### 2. Kelas LibraryMember:

#### Atribut:
- name (string): Nama anggota perpustakaan.
- borrowed_books (list): Daftar objek Book yang dipinjam oleh anggota.

#### Metode:
- borrow_book(book): Meminjam buku dengan menambahkannya ke dalam daftar buku yang dipinjam oleh anggota.
- return_book(book): Mengembalikan buku dengan menghapusnya dari daftar buku yang dipinjam oleh anggota.
- display_borrowed_books(): Menampilkan daftar buku yang dipinjam oleh anggota beserta informasi detailnya, seperti judul, penulis, dan status ketersediaan.

## Contoh Penggunaan
Berikut adalah contoh penggunaan program:
1. Memasukkan nama anggota perpustakaan.
2. Memilih opsi dari menu yang tersedia:
- Opsi 1: Pinjam buku. Pengguna memilih buku yang ingin dipinjam.
- Opsi 2: Kembalikan buku. Pengguna memilih buku yang ingin dikembalikan.
- Opsi 3: Tampilkan buku yang dipinjam. Menampilkan daftar buku yang saat ini dipinjam oleh anggota.
- Opsi 0: Keluar. Menghentikan program.
