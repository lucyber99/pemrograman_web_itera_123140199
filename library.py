"""
Module yang berisi class Library untuk mengelola koleksi item perpustakaan.
"""

from typing import List, Optional
from library_item import LibraryItem


class Library:
    """
    Class Library untuk menyimpan dan mengelola koleksi item perpustakaan.
    Menerapkan encapsulation untuk melindungi data koleksi.
    """
    
    def __init__(self, name: str):
        """
        Constructor untuk Library.
        
        Args:
            name: Nama perpustakaan
        """
        self.__name = name  # Private attribute
        self.__items: List[LibraryItem] = []  # Private collection
        self.__total_borrowed = 0  # Private counter
    
    @property
    def name(self):
        """Getter untuk nama perpustakaan"""
        return self.__name
    
    @property
    def total_items(self):
        """Getter untuk total item di perpustakaan"""
        return len(self.__items)
    
    @property
    def available_items(self):
        """Getter untuk jumlah item yang tersedia"""
        return sum(1 for item in self.__items if item.is_available)
    
    @property
    def borrowed_items(self):
        """Getter untuk jumlah item yang dipinjam"""
        return sum(1 for item in self.__items if not item.is_available)
    
    def add_item(self, item: LibraryItem) -> bool:
        """
        Menambahkan item ke perpustakaan.
        
        Args:
            item: LibraryItem yang akan ditambahkan
            
        Returns:
            True jika berhasil, False jika gagal
        """
        if not isinstance(item, LibraryItem):
            print("Error: Item harus merupakan instance dari LibraryItem")
            return False
        
        self.__items.append(item)
        print(f"✓ Berhasil menambahkan {item.get_item_type()}: '{item.title}' (ID: {item.id})")
        return True
    
    def remove_item(self, item_id: int) -> bool:
        """
        Menghapus item dari perpustakaan berdasarkan ID.
        
        Args:
            item_id: ID item yang akan dihapus
            
        Returns:
            True jika berhasil, False jika gagal
        """
        for i, item in enumerate(self.__items):
            if item.id == item_id:
                removed_item = self.__items.pop(i)
                print(f"✓ Berhasil menghapus: '{removed_item.title}'")
                return True
        
        print(f"✗ Item dengan ID {item_id} tidak ditemukan")
        return False
    
    def display_all_items(self):
        """Menampilkan semua item di perpustakaan"""
        if not self.__items:
            print("\n📚 Perpustakaan masih kosong.")
            return
        
        print(f"\n{'='*80}")
        print(f"📚 DAFTAR ITEM DI {self.__name.upper()}")
        print(f"{'='*80}")
        print(f"Total Item: {self.total_items} | Tersedia: {self.available_items} | Dipinjam: {self.borrowed_items}")
        print(f"{'='*80}\n")
        
        # Group items by type
        books = [item for item in self.__items if item.get_item_type() == "Book"]
        magazines = [item for item in self.__items if item.get_item_type() == "Magazine"]
        
        if books:
            print("📖 BUKU:")
            print("-" * 80)
            for item in books:
                print(f"  {item}")
            print()
        
        if magazines:
            print("📰 MAJALAH:")
            print("-" * 80)
            for item in magazines:
                print(f"  {item}")
            print()
    
    def display_available_items(self):
        """Menampilkan item yang tersedia untuk dipinjam"""
        available = [item for item in self.__items if item.is_available]
        
        if not available:
            print("\n📚 Tidak ada item yang tersedia saat ini.")
            return
        
        print(f"\n{'='*80}")
        print(f"📗 ITEM TERSEDIA DI {self.__name.upper()}")
        print(f"{'='*80}\n")
        
        for item in available:
            print(f"  {item}")
        print()
    
    def search_by_title(self, title: str) -> List[LibraryItem]:
        """
        Mencari item berdasarkan judul.
        
        Args:
            title: Judul yang dicari (case-insensitive, partial match)
            
        Returns:
            List of LibraryItem yang cocok
        """
        results = [item for item in self.__items 
                  if title.lower() in item.title.lower()]
        
        self.__display_search_results(results, f"judul '{title}'")
        return results
    
    def search_by_id(self, item_id: int) -> Optional[LibraryItem]:
        """
        Mencari item berdasarkan ID.
        
        Args:
            item_id: ID item yang dicari
            
        Returns:
            LibraryItem jika ditemukan, None jika tidak
        """
        for item in self.__items:
            if item.id == item_id:
                print(f"\n🔍 Item ditemukan:")
                print(f"  {item}")
                print(f"\n📝 Deskripsi: {item.get_description()}\n")
                return item
        
        print(f"\n✗ Item dengan ID {item_id} tidak ditemukan.\n")
        return None
    
    def search_by_author(self, author: str) -> List[LibraryItem]:
        """
        Mencari item berdasarkan penulis/publisher.
        
        Args:
            author: Nama penulis/publisher yang dicari
            
        Returns:
            List of LibraryItem yang cocok
        """
        results = [item for item in self.__items 
                  if author.lower() in item.author.lower()]
        
        self.__display_search_results(results, f"penulis/publisher '{author}'")
        return results
    
    def __display_search_results(self, results: List[LibraryItem], search_term: str):
        """
        Private method untuk menampilkan hasil pencarian.
        
        Args:
            results: List hasil pencarian
            search_term: Term yang dicari
        """
        print(f"\n🔍 Hasil pencarian untuk {search_term}:")
        print("-" * 80)
        
        if not results:
            print("  Tidak ada item yang cocok.")
        else:
            print(f"  Ditemukan {len(results)} item:\n")
            for item in results:
                print(f"  {item}")
        print()
    
    def borrow_item(self, item_id: int) -> bool:
        """
        Meminjam item dari perpustakaan.
        
        Args:
            item_id: ID item yang akan dipinjam
            
        Returns:
            True jika berhasil, False jika gagal
        """
        item = self.search_by_id(item_id)
        if not item:
            return False
        
        if item.borrow():
            self.__total_borrowed += 1
            print(f"✓ Berhasil meminjam: '{item.title}'")
            return True
        else:
            print(f"✗ Item '{item.title}' sedang dipinjam.")
            return False
    
    def return_item(self, item_id: int) -> bool:
        """
        Mengembalikan item ke perpustakaan.
        
        Args:
            item_id: ID item yang akan dikembalikan
            
        Returns:
            True jika berhasil, False jika gagal
        """
        item = self.search_by_id(item_id)
        if not item:
            return False
        
        if item.return_item():
            print(f"✓ Berhasil mengembalikan: '{item.title}'")
            return True
        else:
            print(f"✗ Item '{item.title}' tidak sedang dipinjam.")
            return False
    
    def get_statistics(self):
        """Menampilkan statistik perpustakaan"""
        print(f"\n{'='*80}")
        print(f"📊 STATISTIK {self.__name.upper()}")
        print(f"{'='*80}")
        print(f"Total Item          : {self.total_items}")
        print(f"Item Tersedia       : {self.available_items}")
        print(f"Item Dipinjam       : {self.borrowed_items}")
        print(f"Total Peminjaman    : {self.__total_borrowed}")
        
        books = sum(1 for item in self.__items if item.get_item_type() == "Book")
        magazines = sum(1 for item in self.__items if item.get_item_type() == "Magazine")
        
        print(f"Jumlah Buku         : {books}")
        print(f"Jumlah Majalah      : {magazines}")
        print(f"{'='*80}\n")
    
    def __str__(self) -> str:
        """String representation dari Library"""
        return f"Perpustakaan {self.__name} - {self.total_items} item"
