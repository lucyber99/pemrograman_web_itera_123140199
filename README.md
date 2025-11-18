# Sistem Manajemen Perpustakaan Sederhana

Proyek ini adalah implementasi sistem manajemen perpustakaan sederhana menggunakan konsep **Object-Oriented Programming (OOP)** dalam Python. Sistem ini mendemonstrasikan penerapan konsep-konsep fundamental OOP seperti **Abstraction**, **Inheritance**, **Encapsulation**, dan **Polymorphism**.

## 📚 Deskripsi Program

Sistem Manajemen Perpustakaan ini memungkinkan pengelolaan koleksi item perpustakaan (buku dan majalah) dengan fitur-fitur dasar seperti:
- Menambahkan item baru ke perpustakaan
- Menampilkan daftar semua item
- Mencari item berdasarkan judul, ID, atau penulis
- Meminjam dan mengembalikan item
- Menampilkan statistik perpustakaan

## ✨ Fitur-Fitur Utama

### 1. **Manajemen Item Perpustakaan**
   - Menambahkan buku dan majalah ke koleksi
   - Menghapus item dari koleksi
   - Menampilkan semua item atau hanya item yang tersedia

### 2. **Sistem Pencarian**
   - Pencarian berdasarkan judul (partial match, case-insensitive)
   - Pencarian berdasarkan ID unik
   - Pencarian berdasarkan penulis/penerbit

### 3. **Sistem Peminjaman**
   - Meminjam item dari perpustakaan
   - Mengembalikan item yang dipinjam
   - Tracking status ketersediaan item

### 4. **Statistik Perpustakaan**
   - Total item di perpustakaan
   - Jumlah item tersedia vs dipinjam
   - Total peminjaman yang pernah terjadi
   - Breakdown berdasarkan tipe item (buku/majalah)

## 🏗️ Struktur Proyek

```
pertemuan 5/
├── library_item.py    # Abstract base class untuk semua item perpustakaan
├── book.py           # Class untuk buku (inherit dari LibraryItem)
├── magazine.py       # Class untuk majalah (inherit dari LibraryItem)
├── library.py        # Class untuk mengelola koleksi perpustakaan
├── main.py           # Program utama dengan demo lengkap semua fitur
├── demo.py           # Program demo singkat untuk screenshot
└── README.md         # Dokumentasi proyek
```

## 🎯 Konsep OOP yang Diterapkan

### 1. **Abstraction (Abstraksi)**
- **Abstract Class**: `LibraryItem` sebagai base class yang tidak bisa diinstansiasi langsung
- **Abstract Methods**: `get_item_type()` dan `get_description()` yang wajib diimplementasikan oleh subclass

```python
from abc import ABC, abstractmethod

class LibraryItem(ABC):
    @abstractmethod
    def get_item_type(self) -> str:
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        pass
```

### 2. **Inheritance (Pewarisan)**
- Class `Book` dan `Magazine` mewarisi dari `LibraryItem`
- Mewarisi atribut dan method dari parent class
- Mengimplementasikan abstract method yang wajib

```python
class Book(LibraryItem):
    def __init__(self, title, author, publication_year, isbn, pages, genre):
        super().__init__(title, author, publication_year)
        # ... additional attributes

class Magazine(LibraryItem):
    def __init__(self, title, publisher, publication_year, issue_number, month, topic):
        super().__init__(title, publisher, publication_year)
        # ... additional attributes
```

### 3. **Encapsulation (Enkapsulasi)**
- **Private attributes** (prefix `__`): `__id`, `__title`, `__isbn`, `__issue_number`
- **Protected attributes** (prefix `_`): `_author`, `_publication_year`, `_is_available`
- **Property decorators** untuk getter dan setter dengan validasi

```python
class LibraryItem(ABC):
    def __init__(self, title, author, publication_year):
        self.__id = LibraryItem._id_counter  # Private
        self.__title = title  # Private
        self._author = author  # Protected
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Title harus berupa string yang tidak kosong")
        self.__title = value
```

### 4. **Polymorphism (Polimorfisme)**
- Method overriding: `get_info()` di-override di subclass
- Method yang sama menghasilkan output berbeda sesuai tipe object
- Duck typing: Library dapat mengelola berbagai tipe item dengan interface yang sama

```python
# Parent class
class LibraryItem:
    def get_info(self):
        return f"[ID: {self.__id}] {self.__title} ..."

# Child class - Override
class Book(LibraryItem):
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} | Genre: {self._genre} ..."

# Polymorphic behavior
items = [book1, magazine1, book2]
for item in items:
    print(item.get_info())  # Memanggil method yang sesuai dengan tipe object
```

## 📋 Diagram Class

```
┌─────────────────────────┐
│   LibraryItem (ABC)     │
├─────────────────────────┤
│ - __id: int             │
│ - __title: str          │
│ # _author: str          │
│ # _publication_year: int│
│ # _is_available: bool   │
├─────────────────────────┤
│ + get_item_type()*      │
│ + get_description()*    │
│ + get_info()            │
│ + borrow()              │
│ + return_item()         │
└───────────┬─────────────┘
            │
      ┌─────┴─────┐
      │           │
┌─────▼──────┐ ┌──▼────────────┐
│   Book     │ │   Magazine    │
├────────────┤ ├───────────────┤
│ - __isbn   │ │ - __issue_num │
│ # _pages   │ │ # _month      │
│ # _genre   │ │ # _topic      │
├────────────┤ ├───────────────┤
│ Implements │ │ Implements    │
│ abstract   │ │ abstract      │
│ methods    │ │ methods       │
└────────────┘ └───────────────┘

┌──────────────────────────┐
│       Library            │
├──────────────────────────┤
│ - __name: str            │
│ - __items: List          │
│ - __total_borrowed: int  │
├──────────────────────────┤
│ + add_item()             │
│ + remove_item()          │
│ + display_all_items()    │
│ + search_by_title()      │
│ + search_by_id()         │
│ + borrow_item()          │
│ + return_item()          │
│ + get_statistics()       │
└──────────────────────────┘
```

**Keterangan:**
- `-` = Private attribute
- `#` = Protected attribute
- `+` = Public method
- `*` = Abstract method

## 🚀 Cara Menjalankan Program

### Prerequisites
- Python 3.7 atau lebih baru

### Langkah-langkah:

1. **Clone atau download repository ini**

2. **Navigasi ke direktori project**
   ```bash
   cd "pertemuan 5"
   ```

3. **Jalankan program demo lengkap** (dengan semua demonstrasi konsep OOP)
   ```bash
   python main.py
   ```
   Program akan menampilkan 6 demo interaktif:
   - Demo 1: Operasi Dasar Perpustakaan
   - Demo 2: Polymorphism
   - Demo 3: Operasi Pencarian
   - Demo 4: Peminjaman dan Pengembalian
   - Demo 5: Encapsulation dengan Property
   - Demo 6: Inheritance & Abstraction

4. **Atau jalankan demo singkat** (tanpa interaksi)
   ```bash
   python demo.py
   ```

## 📸 Screenshot Hasil Running Program

### 1. Menambahkan Item ke Perpustakaan
```
📚 Menambahkan Item ke Perpustakaan:
--------------------------------------------------------------------------------
✓ Berhasil menambahkan Book: 'Python Programming for Beginners' (ID: 1000)
✓ Berhasil menambahkan Book: 'Data Structures and Algorithms' (ID: 1001)
✓ Berhasil menambahkan Book: 'Clean Code' (ID: 1002)
✓ Berhasil menambahkan Magazine: 'Tech Today' (ID: 1003)
✓ Berhasil menambahkan Magazine: 'Science Monthly' (ID: 1004)
```

### 2. Menampilkan Semua Item
```
================================================================================
📚 DAFTAR ITEM DI PERPUSTAKAAN UNIVERSITAS
================================================================================
Total Item: 5 | Tersedia: 5 | Dipinjam: 0
================================================================================

📖 BUKU:
--------------------------------------------------------------------------------
  [Book] [ID: 1000] Python Programming for Beginners oleh John Smith (2022) - Tersedia | 
  Genre: Programming | 350 hal | ISBN: 978-1234567890
  [Book] [ID: 1001] Data Structures and Algorithms oleh Jane Doe (2021) - Tersedia | 
  Genre: Computer Science | 450 hal | ISBN: 978-0987654321
  [Book] [ID: 1002] Clean Code oleh Robert C. Martin (2008) - Tersedia | 
  Genre: Software Engineering | 464 hal | ISBN: 978-0132350884

📰 MAJALAH:
--------------------------------------------------------------------------------
  [Magazine] [ID: 1003] Tech Today oleh Tech Publications (2024) - Tersedia | 
  Edisi: #45 | Bulan: November | Topik: Technology
  [Magazine] [ID: 1004] Science Monthly oleh Science Press (2024) - Tersedia | 
  Edisi: #120 | Bulan: Oktober | Topik: Science
```

### 3. Pencarian Item
```
🔍 DEMO PENCARIAN
================================================================================

🔍 Hasil pencarian untuk judul 'Python':
--------------------------------------------------------------------------------
  Ditemukan 1 item:

  [Book] [ID: 1000] Python Programming for Beginners oleh John Smith (2022) - Tersedia | 
  Genre: Programming | 350 hal | ISBN: 978-1234567890
```

### 4. Peminjaman Item
```
📤 DEMO PEMINJAMAN
================================================================================
Meminjam buku dengan ID 1000:

🔍 Item ditemukan:
  [Book] [ID: 1000] Python Programming for Beginners oleh John Smith (2022) - Tersedia | 
  Genre: Programming | 350 hal | ISBN: 978-1234567890

✓ Berhasil meminjam: 'Python Programming for Beginners'

Status setelah peminjaman:
================================================================================
📗 ITEM TERSEDIA DI PERPUSTAKAAN UNIVERSITAS
================================================================================

  [Book] [ID: 1001] Data Structures and Algorithms oleh Jane Doe (2021) - Tersedia
  [Book] [ID: 1002] Clean Code oleh Robert C. Martin (2008) - Tersedia
  [Magazine] [ID: 1003] Tech Today oleh Tech Publications (2024) - Tersedia
  [Magazine] [ID: 1004] Science Monthly oleh Science Press (2024) - Tersedia
```

### 5. Demo Polymorphism
```
🔄 DEMO POLYMORPHISM - get_description()
================================================================================

Book: Python Programming for Beginners
→ Buku 'Python Programming for Beginners' ditulis oleh John Smith, diterbitkan tahun 2022. 
  Genre: Programming, 350 halaman. ISBN: 978-1234567890

Magazine: Tech Today
→ Majalah 'Tech Today' edisi 45, diterbitkan oleh Tech Publications pada November 2024. 
  Topik: Technology
```

### 6. Statistik Perpustakaan
```
================================================================================
📊 STATISTIK PERPUSTAKAAN UNIVERSITAS
================================================================================
Total Item          : 5
Item Tersedia       : 4
Item Dipinjam       : 1
Total Peminjaman    : 1
Jumlah Buku         : 3
Jumlah Majalah      : 2
================================================================================
```

## 💡 Penjelasan Fitur Encapsulation

Program ini menggunakan encapsulation dengan property decorator untuk melindungi data:

```python
# Private attribute dengan property decorator
@property
def title(self):
    """Getter untuk title"""
    return self.__title

@title.setter
def title(self, value: str):
    """Setter dengan validasi"""
    if not value or not isinstance(value, str):
        raise ValueError("Title harus berupa string yang tidak kosong")
    self.__title = value
```

**Keuntungan:**
- Data validation saat set nilai
- Read-only properties (hanya getter tanpa setter)
- Kontrol akses yang lebih baik
- Mencegah perubahan data yang tidak valid

## 🎓 Konsep Pembelajaran

### 1. **Abstract Base Class (ABC)**
Digunakan untuk mendefinisikan interface yang harus diimplementasikan oleh subclass.

### 2. **Class Variable**
`_id_counter` di LibraryItem untuk auto-increment ID secara otomatis.

### 3. **Property Decorator**
Membuat getter dan setter untuk kontrol akses attribute.

### 4. **Type Hints**
Menggunakan type hints untuk dokumentasi dan type checking.

### 5. **List Comprehension**
Digunakan untuk filtering dan searching item secara efisien.

### 6. **String Formatting**
Menggunakan f-strings untuk output yang rapi dan informatif.

## 📝 Catatan Penting

1. **ID Generation**: Setiap item mendapat ID unik secara otomatis dimulai dari 1000
2. **Validation**: Setter menggunakan validasi untuk memastikan data valid
3. **Protected vs Private**: 
   - Private (`__`): Tidak bisa diakses dari luar class
   - Protected (`_`): Konvensi untuk internal use, bisa diakses di subclass
4. **Abstract Methods**: Wajib diimplementasikan oleh semua subclass

## 🔧 Pengembangan Lebih Lanjut

Beberapa ide untuk pengembangan:
- [ ] Tambah tipe item lain (DVD, Journal, etc.)
- [ ] Implementasi database untuk persistent storage
- [ ] Sistem denda untuk keterlambatan pengembalian
- [ ] User authentication dan authorization
- [ ] GUI menggunakan Tkinter atau PyQt
- [ ] Export data ke CSV/JSON
- [ ] RESTful API dengan Flask/FastAPI

## 👨‍💻 Penulis

Dibuat sebagai tugas Pengembangan Aplikasi Web - Pertemuan 5

## 📄 Lisensi

Project ini dibuat untuk tujuan pembelajaran.

---

**Selamat belajar OOP dengan Python! 🐍**
