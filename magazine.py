"""
Module yang berisi class Magazine yang mewarisi dari LibraryItem.
"""

from library_item import LibraryItem


class Magazine(LibraryItem):
    """
    Class Magazine yang mewarisi dari LibraryItem.
    Merepresentasikan majalah dalam perpustakaan.
    """
    
    def __init__(self, title: str, publisher: str, publication_year: int,
                 issue_number: int, month: str, topic: str = "General"):
        """
        Constructor untuk Magazine.
        
        Args:
            title: Judul majalah
            publisher: Penerbit majalah
            publication_year: Tahun publikasi
            issue_number: Nomor edisi
            month: Bulan publikasi
            topic: Topik majalah (default: General)
        """
        # Untuk magazine, author adalah publisher
        super().__init__(title, publisher, publication_year)
        self.__issue_number = issue_number  # Private attribute
        self._month = month  # Protected attribute
        self._topic = topic  # Protected attribute
    
    @property
    def issue_number(self):
        """Getter untuk issue number (read-only)"""
        return self.__issue_number
    
    @property
    def month(self):
        """Getter untuk month"""
        return self._month
    
    @property
    def topic(self):
        """Getter untuk topic"""
        return self._topic
    
    @property
    def publisher(self):
        """Getter untuk publisher (alias untuk author)"""
        return self._author
    
    # Implementasi abstract method dari parent class
    def get_item_type(self) -> str:
        """Mengembalikan tipe item yaitu Magazine"""
        return "Magazine"
    
    def get_description(self) -> str:
        """Mengembalikan deskripsi lengkap majalah"""
        return (f"Majalah '{self.title}' edisi {self.__issue_number}, "
                f"diterbitkan oleh {self._author} pada {self._month} {self._publication_year}. "
                f"Topik: {self._topic}")
    
    # Override method dari parent class (Polymorphism)
    def get_info(self) -> str:
        """Override method get_info untuk menambahkan info spesifik Magazine"""
        base_info = super().get_info()
        return f"{base_info} | Edisi: #{self.__issue_number} | Bulan: {self._month} | Topik: {self._topic}"
    
    def __str__(self) -> str:
        """String representation dari Magazine object"""
        return f"[{self.get_item_type()}] {self.get_info()}"
