"""
Module yang berisi abstract class LibraryItem sebagai base class untuk semua item perpustakaan.
"""

from abc import ABC, abstractmethod
from datetime import datetime


class LibraryItem(ABC):
    """
    Abstract base class untuk semua item di perpustakaan.
    Menerapkan konsep abstraction dan encapsulation.
    """
    
    # Class variable untuk generate ID otomatis
    _id_counter = 1000
    
    def __init__(self, title: str, author: str, publication_year: int):
        """
        Constructor untuk LibraryItem.
        
        Args:
            title: Judul item
            author: Penulis/pembuat item
            publication_year: Tahun publikasi
        """
        self.__id = LibraryItem._id_counter  # Private attribute
        LibraryItem._id_counter += 1
        self.__title = title  # Private attribute
        self._author = author  # Protected attribute
        self._publication_year = publication_year  # Protected attribute
        self._is_available = True  # Protected attribute
        self._borrowed_date = None
    
    # Property decorator untuk encapsulation
    @property
    def id(self):
        """Getter untuk ID (read-only)"""
        return self.__id
    
    @property
    def title(self):
        """Getter untuk title"""
        return self.__title
    
    @title.setter
    def title(self, value: str):
        """Setter untuk title dengan validasi"""
        if not value or not isinstance(value, str):
            raise ValueError("Title harus berupa string yang tidak kosong")
        self.__title = value
    
    @property
    def author(self):
        """Getter untuk author"""
        return self._author
    
    @property
    def is_available(self):
        """Getter untuk status ketersediaan"""
        return self._is_available
    
    @abstractmethod
    def get_item_type(self) -> str:
        """
        Abstract method yang harus diimplementasikan oleh subclass.
        Mengembalikan tipe item (Book, Magazine, dll).
        """
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        """
        Abstract method yang harus diimplementasikan oleh subclass.
        Mengembalikan deskripsi lengkap item.
        """
        pass
    
    def borrow(self):
        """Method untuk meminjam item"""
        if not self._is_available:
            return False
        self._is_available = False
        self._borrowed_date = datetime.now()
        return True
    
    def return_item(self):
        """Method untuk mengembalikan item"""
        if self._is_available:
            return False
        self._is_available = True
        self._borrowed_date = None
        return True
    
    def get_info(self) -> str:
        """
        Method umum untuk mendapatkan informasi item.
        Menerapkan polymorphism karena akan di-override di subclass.
        """
        status = "Tersedia" if self._is_available else "Dipinjam"
        return f"[ID: {self.__id}] {self.__title} oleh {self._author} ({self._publication_year}) - {status}"
    
    def __str__(self) -> str:
        """String representation dari object"""
        return self.get_info()
