"""
Program demo singkat untuk screenshot README.
"""

from book import Book
from magazine import Magazine
from library import Library


def main():
    """Fungsi utama untuk demo"""
    print("\n" + "="*80)
    print(" "*20 + "SISTEM MANAJEMEN PERPUSTAKAAN")
    print(" "*15 + "Demonstrasi Konsep OOP dengan Python")
    print("="*80)
    
    # Membuat instance Library
    lib = Library("Perpustakaan Universitas")
    
    # Menambahkan Buku
    print("\n📚 Menambahkan Item ke Perpustakaan:")
    print("-" * 80)
    
    book1 = Book("Python Programming for Beginners", "John Smith", 2022, 
                 "978-1234567890", 350, "Programming")
    book2 = Book("Data Structures and Algorithms", "Jane Doe", 2021, 
                 "978-0987654321", 450, "Computer Science")
    book3 = Book("Clean Code", "Robert C. Martin", 2008, 
                 "978-0132350884", 464, "Software Engineering")
    
    lib.add_item(book1)
    lib.add_item(book2)
    lib.add_item(book3)
    
    mag1 = Magazine("Tech Today", "Tech Publications", 2024, 45, "November", "Technology")
    mag2 = Magazine("Science Monthly", "Science Press", 2024, 120, "Oktober", "Science")
    
    lib.add_item(mag1)
    lib.add_item(mag2)
    
    # Menampilkan semua item
    lib.display_all_items()
    
    # Demo Pencarian
    print("\n🔍 DEMO PENCARIAN")
    print("="*80)
    lib.search_by_title("Python")
    
    # Demo Peminjaman
    print("\n📤 DEMO PEMINJAMAN")
    print("="*80)
    print("Meminjam buku dengan ID 1000:")
    lib.borrow_item(1000)
    
    print("\nStatus setelah peminjaman:")
    lib.display_available_items()
    
    # Demo Polymorphism
    print("\n🔄 DEMO POLYMORPHISM - get_description()")
    print("="*80)
    print(f"\n{book1.get_item_type()}: {book1.title}")
    print(f"→ {book1.get_description()}")
    print(f"\n{mag1.get_item_type()}: {mag1.title}")
    print(f"→ {mag1.get_description()}")
    
    # Statistik
    lib.get_statistics()
    
    print("\n" + "="*80)
    print(" "*28 + "DEMO SELESAI")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
