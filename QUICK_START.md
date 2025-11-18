# Quick Start Guide - Sistem Manajemen Perpustakaan

## 🚀 Cara Cepat Menggunakan

### 1. Jalankan Demo
```bash
python demo.py
```

### 2. Jalankan Program Lengkap (Interaktif)
```bash
python main.py
```

## 📝 Contoh Penggunaan Kode

### Import Modules
```python
from library_item import LibraryItem
from book import Book
from magazine import Magazine
from library import Library
```

### Membuat Buku
```python
book = Book(
    title="Python Programming",
    author="John Smith",
    publication_year=2022,
    isbn="978-1234567890",
    pages=350,
    genre="Programming"
)
```

### Membuat Majalah
```python
magazine = Magazine(
    title="Tech Today",
    publisher="Tech Publications",
    publication_year=2024,
    issue_number=45,
    month="November",
    topic="Technology"
)
```

### Membuat Library dan Menambahkan Item
```python
lib = Library("Perpustakaan Universitas")
lib.add_item(book)
lib.add_item(magazine)
```

### Menampilkan Semua Item
```python
lib.display_all_items()
```

### Mencari Item
```python
# Cari berdasarkan judul
lib.search_by_title("Python")

# Cari berdasarkan ID
lib.search_by_id(1000)

# Cari berdasarkan author
lib.search_by_author("John")
```

### Meminjam dan Mengembalikan Item
```python
# Pinjam
lib.borrow_item(1000)

# Kembalikan
lib.return_item(1000)
```

### Menampilkan Statistik
```python
lib.get_statistics()
```

## 🔍 Mengakses Properties

### Book Properties
```python
print(book.id)           # ID (read-only)
print(book.title)        # Title
print(book.author)       # Author
print(book.isbn)         # ISBN (read-only)
print(book.pages)        # Pages
print(book.genre)        # Genre
print(book.is_available) # Status

# Mengubah title
book.title = "New Title"
```

### Magazine Properties
```python
print(magazine.id)            # ID (read-only)
print(magazine.title)         # Title
print(magazine.publisher)     # Publisher
print(magazine.issue_number)  # Issue number (read-only)
print(magazine.month)         # Month
print(magazine.topic)         # Topic
print(magazine.is_available)  # Status
```

### Library Properties
```python
print(lib.name)              # Library name
print(lib.total_items)       # Total items
print(lib.available_items)   # Available items
print(lib.borrowed_items)    # Borrowed items
```

## 💡 Tips

### 1. Polymorphism
```python
items = [book1, magazine1, book2]
for item in items:
    # Memanggil method yang sama tapi behavior berbeda
    print(item.get_item_type())
    print(item.get_description())
    print(item.get_info())
```

### 2. Validasi Otomatis
```python
try:
    book.title = ""  # Error! Title tidak boleh kosong
except ValueError as e:
    print(e)
```

### 3. Auto ID Generation
```python
# ID di-generate otomatis, dimulai dari 1000
book1 = Book(...)  # ID: 1000
book2 = Book(...)  # ID: 1001
book3 = Book(...)  # ID: 1002
```

### 4. Type Hints
```python
# Function dengan type hints
def process_item(item: LibraryItem) -> str:
    return item.get_info()
```

## 📚 File Structure

```
pertemuan 5/
├── library_item.py      # Abstract base class
├── book.py             # Book implementation
├── magazine.py         # Magazine implementation
├── library.py          # Library management
├── main.py             # Full demo (6 demos)
├── demo.py             # Quick demo
├── README.md           # Full documentation
├── KONSEP_OOP.md       # OOP concepts explained
├── CLASS_DIAGRAM.md    # Class diagram
└── QUICK_START.md      # This file
```

## 🎯 Demo Programs

### demo.py - Quick Demo
Menampilkan:
- ✅ Menambahkan item
- ✅ Menampilkan semua item
- ✅ Pencarian
- ✅ Peminjaman
- ✅ Polymorphism
- ✅ Statistik

**Runtime**: ~2 detik

### main.py - Full Interactive Demo
Menampilkan 6 demo lengkap:
1. Operasi Dasar Perpustakaan
2. Polymorphism
3. Operasi Pencarian
4. Peminjaman dan Pengembalian
5. Encapsulation dengan Property
6. Inheritance & Abstraction

**Runtime**: Interactive (tekan Enter untuk lanjut)

## ✅ Checklist Fitur

- [x] Abstract class dengan abstract methods
- [x] Minimal 2 subclass (Book, Magazine)
- [x] Implementasi abstract methods
- [x] Library class untuk manajemen
- [x] Encapsulation (private/protected)
- [x] Property decorator
- [x] Menambahkan item
- [x] Menampilkan daftar item
- [x] Mencari item (by title, ID, author)
- [x] Bonus: Peminjaman & pengembalian
- [x] Bonus: Statistik
- [x] Bonus: Type hints
- [x] Bonus: Comprehensive documentation

## 🐛 Troubleshooting

### Import Error
```python
# Pastikan semua file dalam satu direktori
# Jalankan dari direktori yang sama
cd "d:\Semester 5\Pengembangan Aplikasi Web\pertemuan 5"
python demo.py
```

### Module not found
```python
# Pastikan Python 3.7+ terinstall
python --version

# Jika pakai virtual environment, aktifkan dulu
# Windows:
.\venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate
```

## 📖 Dokumentasi Lengkap

Untuk dokumentasi lengkap, lihat:
- `README.md` - Dokumentasi utama dengan screenshot
- `KONSEP_OOP.md` - Penjelasan konsep OOP yang diterapkan
- `CLASS_DIAGRAM.md` - Diagram class lengkap

## 🎓 Pembelajaran

Program ini mendemonstrasikan:
1. **Abstraction** - LibraryItem as abstract base
2. **Inheritance** - Book & Magazine extends LibraryItem
3. **Encapsulation** - Private/protected with properties
4. **Polymorphism** - Same method, different behavior

---

**Happy Coding! 🚀**
