class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

class LibraryMember:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            print(f"{self.name} berhasil meminjam buku {book.title}")
        else:
            print(f"{book.title} sedang dipinjam oleh anggota lain")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} mengembalikan buku {book.title}")
        else:
            print(f"{book.title} tidak ada dalam daftar buku yang dipinjam oleh {self.name}")

    def display_borrowed_books(self):
        print(f"Buku yang dipinjam oleh {self.name}:")
        if self.borrowed_books:
            for book in self.borrowed_books:
                print(f"Judul: {book.title}")
                print(f"Penulis: {book.author}")
                print(f"Ketersediaan: {'Tersedia' if book.is_available else 'Dipinjam'}")
                print()
        else:
            print("Tidak ada buku yang dipinjam")


def display_menu():
    print("|||-Menu Perpus-|||")
    print("1. Pinjam buku")
    print("2. Kembalikan buku")
    print("3. Tampilkan buku yang dipinjam")
    print("0. Keluar")


# Membuat objek LibraryMember
name = input("Masukkan nama anggota perpustakaan: ")
member1 = LibraryMember(name)

# Membuat objek Book
books = [
    Book("Pemrograman Berorientasi objek", "Margaret Mitchell"),
    Book("Pemrograman Web", "Jane Austen"),
    Book("Desain Perangkat Lunak", "Emily Bronte")
]

while True:
    display_menu()
    choice = input("Masukkan pilihan (0-3): ")

    if choice == '0':
        break

    elif choice == '1':
        print("||-Daftar Buku-||")
        for index, book in enumerate(books):
            print(f"{index+1}. {book.title} - {book.author}")

        book_choice = int(input("Masukkan nomor buku yang ingin dipinjam: ")) - 1

        if 0 <= book_choice < len(books):
            member1.borrow_book(books[book_choice])
        else:
            print("Pilihan tidak valid")

    elif choice == '2':
        if member1.borrowed_books:
            print("||-Buku yang Dipinjam-||")
            for index, book in enumerate(member1.borrowed_books):
                print(f"{index+1}. {book.title} - {book.author}")

            book_choice = int(input("Masukkan nomor buku yang ingin dikembalikan: ")) - 1

            if 0 <= book_choice < len(member1.borrowed_books):
                member1.return_book(member1.borrowed_books[book_choice])
            else:
                print("Pilihan tidak valid")
        else:
            print("Tidak ada buku yang dipinjam")

    elif choice == '3':
        member1.display_borrowed_books()

    else:
        print("Pilihan tidak valid")
