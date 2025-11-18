import { createContext, useContext } from 'react';
import { useLocalStorage } from '../hooks/useLocalStorage';
import { validateBookInput, generateId } from '../utils/validation';

// Buat Context
const BooksContext = createContext();

// Custom hook untuk menggunakan context
export const useBooks = () => {
  const context = useContext(BooksContext);
  if (!context) {
    throw new Error('useBooks must be used within BooksProvider');
  }
  return context;
};

// Provider component
export const BooksProvider = ({ children }) => {
  const [books, setBooks] = useLocalStorage('books', []);

  /**
   * Tambah buku baru
   * @param {Object} bookData - Data buku (title, author, status, imageUrl)
   * @returns {Object} - { success: boolean, errors?: Object, book?: Object }
   */
  const addBook = (bookData) => {
    // Validasi input
    const validation = validateBookInput(bookData);
    if (!validation.isValid) {
      return { success: false, errors: validation.errors };
    }

    // Buat buku baru dengan ID dan timestamp
    const newBook = {
      id: generateId(),
      title: bookData.title.trim(),
      author: bookData.author.trim(),
      status: bookData.status,
      imageUrl: bookData.imageUrl?.trim() || '',
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString()
    };

    // Tambahkan ke state
    setBooks([...books, newBook]);
    return { success: true, book: newBook };
  };

  /**
   * Update buku yang sudah ada
   * @param {string} id - ID buku yang akan diupdate
   * @param {Object} updatedData - Data buku yang baru
   * @returns {Object} - { success: boolean, errors?: Object, book?: Object }
   */
  const updateBook = (id, updatedData) => {
    // Validasi input
    const validation = validateBookInput(updatedData);
    if (!validation.isValid) {
      return { success: false, errors: validation.errors };
    }

    // Cari dan update buku
    const updatedBooks = books.map(book => {
      if (book.id === id) {
        return {
          ...book,
          title: updatedData.title.trim(),
          author: updatedData.author.trim(),
          status: updatedData.status,
          imageUrl: updatedData.imageUrl?.trim() || '',
          updatedAt: new Date().toISOString()
        };
      }
      return book;
    });

    setBooks(updatedBooks);
    const updatedBook = updatedBooks.find(book => book.id === id);
    return { success: true, book: updatedBook };
  };

  /**
   * Hapus buku
   * @param {string} id - ID buku yang akan dihapus
   * @returns {boolean} - true jika berhasil
   */
  const deleteBook = (id) => {
    const filteredBooks = books.filter(book => book.id !== id);
    setBooks(filteredBooks);
    return true;
  };

  /**
   * Dapatkan buku berdasarkan ID
   * @param {string} id - ID buku
   * @returns {Object|null} - Object buku atau null
   */
  const getBookById = (id) => {
    return books.find(book => book.id === id) || null;
  };

  /**
   * Filter buku berdasarkan status
   * @param {string} status - Status buku (milik, baca, beli, atau 'all')
   * @returns {Array} - Array buku yang difilter
   */
  const filterBooksByStatus = (status) => {
    if (status === 'all') {
      return books;
    }
    return books.filter(book => book.status === status);
  };

  /**
   * Cari buku berdasarkan judul atau penulis
   * @param {string} query - Query pencarian
   * @returns {Array} - Array buku hasil pencarian
   */
  const searchBooks = (query) => {
    if (!query || query.trim() === '') {
      return books;
    }

    const lowerQuery = query.toLowerCase().trim();
    return books.filter(book => 
      book.title.toLowerCase().includes(lowerQuery) ||
      book.author.toLowerCase().includes(lowerQuery)
    );
  };

  // Value yang akan di-provide ke children
  const value = {
    books,
    addBook,
    updateBook,
    deleteBook,
    getBookById,
    filterBooksByStatus,
    searchBooks
  };

  return (
    <BooksContext.Provider value={value}>
      {children}
    </BooksContext.Provider>
  );
};
