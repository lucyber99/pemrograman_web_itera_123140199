"""
Program utama untuk demonstrasi Sistem Manajemen Perpustakaan.
Mendemonstrasikan penggunaan konsep OOP: Inheritance, Encapsulation, Polymorphism, dan Abstraction.
"""

from book import Book
from magazine import Magazine
from library import Library


def print_header(text: str):
    """Helper function untuk print header"""
    print(f"\n{'='*80}")
    print(f"  {text}")
    print(f"{'='*80}\n")


def demo_basic_operations():
    """Demo operasi dasar perpustakaan"""
    print_header("DEMO 1: OPERASI DASAR PERPUSTAKAAN")
    
    # Membuat instance Library
    lib = Library("Perpustakaan Universitas")
    
    # Membuat beberapa buku
    print("📚 Menambahkan Buku ke Perpustakaan:")
    print("-" * 80)
    book1 = Book(
        title="Python Programming for Beginners",
        author="John Smith",
        publication_year=2022,
        isbn="978-1234567890",
        pages=350,
        genre="Programming"
    )
    lib.add_item(book1)
    
    book2 = Book(
        title="Data Structures and Algorithms",
        author="Jane Doe",
        publication_year=2021,
        isbn="978-0987654321",
        pages=450,
        genre="Computer Science"
    )
    lib.add_item(book2)
    
    book3 = Book(
        title="Web Development with Django",
        author="Robert Johnson",
        publication_year=2023,
        isbn="978-1122334455",
        pages=500,
        genre="Web Development"
    )
    lib.add_item(book3)
    
    # Membuat beberapa majalah
    print("\n📰 Menambahkan Majalah ke Perpustakaan:")
    print("-" * 80)
    mag1 = Magazine(
        title="Tech Today",
        publisher="Tech Publications",
        publication_year=2024,
        issue_number=45,
        month="November",
        topic="Technology"
    )
    lib.add_item(mag1)
    
    mag2 = Magazine(
        title="Science Monthly",
        publisher="Science Press",
        publication_year=2024,
        issue_number=120,
        month="Oktober",
        topic="Science"
    )
    lib.add_item(mag2)
    
    # Menampilkan semua item
    lib.display_all_items()
    
    # Menampilkan statistik
    lib.get_statistics()


def demo_polymorphism():
    """Demo konsep polymorphism"""
    print_header("DEMO 2: POLYMORPHISM - get_description() untuk tipe berbeda")
    
    lib = Library("Demo Library")
    
    book = Book(
        title="Clean Code",
        author="Robert C. Martin",
        publication_year=2008,
        isbn="978-0132350884",
        pages=464,
        genre="Software Engineering"
    )
    
    magazine = Magazine(
        title="National Geographic",
        publisher="National Geographic Society",
        publication_year=2024,
        issue_number=11,
        month="November",
        topic="Nature & Science"
    )
    
    lib.add_item(book)
    lib.add_item(magazine)
    
    # Polymorphism: method yang sama dipanggil pada object berbeda
    print("\n🔍 Memanggil get_description() pada berbagai tipe item:")
    print("-" * 80)
    
    items = [book, magazine]
    for item in items:
        print(f"\n{item.get_item_type()}: {item.title}")
        print(f"  → {item.get_description()}")


def demo_search_operations():
    """Demo operasi pencarian"""
    print_header("DEMO 3: OPERASI PENCARIAN")
    
    lib = Library("Search Demo Library")
    
    # Menambahkan beberapa item
    lib.add_item(Book("Python Basics", "Alice Wong", 2020, "111", 300, "Programming"))
    lib.add_item(Book("Python Advanced", "Bob Lee", 2021, "222", 400, "Programming"))
    lib.add_item(Book("Java Programming", "Charlie Brown", 2019, "333", 350, "Programming"))
    lib.add_item(Magazine("Python Weekly", "Tech Media", 2024, 50, "November", "Programming"))
    lib.add_item(Magazine("Developer's Digest", "Dev Publications", 2024, 25, "Oktober", "Technology"))
    
    # Pencarian berdasarkan judul
    print("🔍 Pencarian berdasarkan judul 'Python':")
    lib.search_by_title("Python")
    
    # Pencarian berdasarkan ID
    print("\n🔍 Pencarian berdasarkan ID (1001):")
    lib.search_by_id(1001)
    
    # Pencarian berdasarkan author
    print("\n🔍 Pencarian berdasarkan author 'Bob':")
    lib.search_by_author("Bob")


def demo_borrow_return():
    """Demo peminjaman dan pengembalian"""
    print_header("DEMO 4: PEMINJAMAN DAN PENGEMBALIAN ITEM")
    
    lib = Library("Borrow Demo Library")
    
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "444", 180, "Fiction")
    book2 = Book("1984", "George Orwell", 1949, "555", 328, "Fiction")
    
    lib.add_item(book1)
    lib.add_item(book2)
    
    print("\n📋 Status Awal:")
    lib.display_available_items()
    
    # Meminjam item
    print("\n📤 Meminjam buku dengan ID 1000:")
    print("-" * 80)
    lib.borrow_item(1000)
    
    print("\n📋 Status Setelah Peminjaman:")
    lib.display_available_items()
    
    # Coba pinjam lagi item yang sama
    print("\n📤 Mencoba meminjam buku yang sama lagi:")
    print("-" * 80)
    lib.borrow_item(1000)
    
    # Mengembalikan item
    print("\n📥 Mengembalikan buku dengan ID 1000:")
    print("-" * 80)
    lib.return_item(1000)
    
    print("\n📋 Status Setelah Pengembalian:")
    lib.display_available_items()
    
    lib.get_statistics()


def demo_encapsulation():
    """Demo konsep encapsulation dengan property"""
    print_header("DEMO 5: ENCAPSULATION - Property Decorator")
    
    book = Book(
        title="Design Patterns",
        author="Gang of Four",
        publication_year=1994,
        isbn="978-0201633612",
        pages=395,
        genre="Software Engineering"
    )
    
    print("📖 Demonstrasi Encapsulation dengan Property:")
    print("-" * 80)
    
    # Mengakses private attribute melalui property (getter)
    print(f"ID (read-only)     : {book.id}")
    print(f"Title (read-write) : {book.title}")
    print(f"ISBN (read-only)   : {book.isbn}")
    print(f"Author             : {book.author}")
    print(f"Pages              : {book.pages}")
    print(f"Genre              : {book.genre}")
    
    # Mencoba mengubah title melalui property setter
    print("\n✏️  Mengubah title melalui property setter:")
    print("-" * 80)
    old_title = book.title
    book.title = "Design Patterns: Elements of Reusable Object-Oriented Software"
    print(f"Title lama: {old_title}")
    print(f"Title baru: {book.title}")
    
    # Validasi pada setter
    print("\n❌ Mencoba set title dengan nilai invalid:")
    print("-" * 80)
    try:
        book.title = ""
    except ValueError as e:
        print(f"Error tertangkap: {e}")
    
    print("\n💡 Catatan: ID dan ISBN adalah read-only (hanya getter, tidak ada setter)")
    print("   Atribut __id dan __isbn bersifat private dan dilindungi dari akses langsung.")


def demo_inheritance_abstraction():
    """Demo inheritance dan abstraction"""
    print_header("DEMO 6: INHERITANCE & ABSTRACTION")
    
    print("📚 Demonstrasi Inheritance dan Abstract Method:")
    print("-" * 80)
    
    book = Book("The Pragmatic Programmer", "Andrew Hunt", 1999, "666", 320, "Programming")
    magazine = Magazine("Code Magazine", "Code Press", 2024, 100, "November", "Programming")
    
    # Menampilkan inheritance chain
    print("\n🔗 Inheritance Chain:")
    print(f"Book class hierarchy    : {Book.__mro__}")
    print(f"Magazine class hierarchy: {Magazine.__mro__}")
    
    # Abstract methods yang di-implement
    print("\n✅ Abstract Methods Implementation:")
    print("-" * 80)
    print(f"\nBook.get_item_type():")
    print(f"  → {book.get_item_type()}")
    
    print(f"\nMagazine.get_item_type():")
    print(f"  → {magazine.get_item_type()}")
    
    print(f"\nBook.get_description():")
    print(f"  → {book.get_description()}")
    
    print(f"\nMagazine.get_description():")
    print(f"  → {magazine.get_description()}")
    
    # Demonstrasi bahwa tidak bisa membuat instance dari abstract class
    print("\n\n❌ Mencoba membuat instance dari abstract class LibraryItem:")
    print("-" * 80)
    try:
        from library_item import LibraryItem
        # Ini akan error karena LibraryItem adalah abstract class
        item = LibraryItem("Test", "Test Author", 2024)
    except TypeError as e:
        print(f"Error: {e}")
        print("✓ Abstract class tidak bisa di-instantiate secara langsung!")


def main():
    """Fungsi utama untuk menjalankan semua demo"""
    print("\n")
    print("="*80)
    print(" "*20 + "SISTEM MANAJEMEN PERPUSTAKAAN")
    print(" "*15 + "Demonstrasi Konsep OOP dengan Python")
    print("="*80)
    
    # Jalankan semua demo
    demo_basic_operations()
    input("\n>>> Tekan Enter untuk melanjutkan ke demo berikutnya...")
    
    demo_polymorphism()
    input("\n>>> Tekan Enter untuk melanjutkan ke demo berikutnya...")
    
    demo_search_operations()
    input("\n>>> Tekan Enter untuk melanjutkan ke demo berikutnya...")
    
    demo_borrow_return()
    input("\n>>> Tekan Enter untuk melanjutkan ke demo berikutnya...")
    
    demo_encapsulation()
    input("\n>>> Tekan Enter untuk melanjutkan ke demo berikutnya...")
    
    demo_inheritance_abstraction()
    
    print("\n")
    print("="*80)
    print(" "*25 + "DEMO SELESAI")
    print(" "*15 + "Terima kasih telah menggunakan program ini!")
    print("="*80)
    print()


if __name__ == "__main__":
    main()
