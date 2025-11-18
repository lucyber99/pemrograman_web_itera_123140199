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


## 🎯 Konsep OOP yang Diterapkan

### 1. **Abstraction (Abstraksi)**

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


**Selamat belajar OOP dengan Python! 🐍**
