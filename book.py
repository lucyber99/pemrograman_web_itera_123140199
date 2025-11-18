"""
Module yang berisi class Book yang mewarisi dari LibraryItem.
"""

from library_item import LibraryItem


class Book(LibraryItem):
    """
    Class Book yang mewarisi dari LibraryItem.
    Merepresentasikan buku dalam perpustakaan.
    """
    
    def __init__(self, title: str, author: str, publication_year: int, 
                 isbn: str, pages: int, genre: str = "General"):
        """
        Constructor untuk Book.
        
        Args:
            title: Judul buku
            author: Penulis buku
            publication_year: Tahun publikasi
            isbn: ISBN buku
            pages: Jumlah halaman
            genre: Genre buku (default: General)
        """
        super().__init__(title, author, publication_year)
        self.__isbn = isbn  # Private attribute
        self._pages = pages  # Protected attribute
        self._genre = genre  # Protected attribute
    
    @property
    def isbn(self):
        """Getter untuk ISBN (read-only)"""
        return self.__isbn
    
    @property
    def pages(self):
        """Getter untuk jumlah halaman"""
        return self._pages
    
    @property
    def genre(self):
        """Getter untuk genre"""
        return self._genre
    
    # Implementasi abstract method dari parent class
    def get_item_type(self) -> str:
        """Mengembalikan tipe item yaitu Book"""
        return "Book"
    
    def get_description(self) -> str:
        """Mengembalikan deskripsi lengkap buku"""
        return (f"Buku '{self.title}' ditulis oleh {self.author}, "
                f"diterbitkan tahun {self._publication_year}. "
                f"Genre: {self._genre}, {self._pages} halaman. "
                f"ISBN: {self.__isbn}")
    
    # Override method dari parent class (Polymorphism)
    def get_info(self) -> str:
        """Override method get_info untuk menambahkan info spesifik Book"""
        base_info = super().get_info()
        return f"{base_info} | Genre: {self._genre} | {self._pages} hal | ISBN: {self.__isbn}"
    
    def __str__(self) -> str:
        """String representation dari Book object"""
        return f"[{self.get_item_type()}] {self.get_info()}"
