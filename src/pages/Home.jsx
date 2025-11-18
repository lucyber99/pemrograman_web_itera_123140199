import { useState, useEffect } from 'react';
import { useBooks } from '../contexts/BooksContext';
import { useDebounce } from '../hooks/useDebounce';
import BookCard from '../components/BookCard';
import SearchBar from '../components/SearchBar';
import FilterButtons from '../components/FilterButtons';
import { sampleBooks } from '../data/sampleBooks';
import './Home.css';

const Home = () => {
  const { books, deleteBook, filterBooksByStatus, searchBooks } = useBooks();
  const [searchQuery, setSearchQuery] = useState('');
  const [activeFilter, setActiveFilter] = useState('all');
  const [displayBooks, setDisplayBooks] = useState([]);

  // Debounce search query
  const debouncedSearchQuery = useDebounce(searchQuery, 300);

  useEffect(() => {
    // Filter berdasarkan status
    let filtered = filterBooksByStatus(activeFilter);

    // Filter berdasarkan search query
    if (debouncedSearchQuery.trim() !== '') {
      filtered = filtered.filter(book => 
        book.title.toLowerCase().includes(debouncedSearchQuery.toLowerCase()) ||
        book.author.toLowerCase().includes(debouncedSearchQuery.toLowerCase())
      );
    }

    setDisplayBooks(filtered);
  }, [debouncedSearchQuery, activeFilter, books, filterBooksByStatus]);

  const handleDelete = (id) => {
    deleteBook(id);
  };

  const loadSampleData = () => {
    if (window.confirm('Apakah Anda ingin memuat 6 buku contoh dengan gambar?')) {
      // Merge dengan data yang ada
      const existingIds = books.map(b => b.id);
      const newSamples = sampleBooks.filter(sample => !existingIds.includes(sample.id));
      if (newSamples.length > 0) {
        const updatedBooks = [...books, ...newSamples];
        window.localStorage.setItem('books', JSON.stringify(updatedBooks));
        window.location.reload();
      } else {
        alert('Data contoh sudah dimuat sebelumnya!');
      }
    }
  };

  return (
    <div className="home-page">
      <div className="home-header">
        <h1>Koleksi Buku Saya</h1>
        <p className="book-count">Total: {displayBooks.length} buku</p>
        {books.length === 0 && (
          <button onClick={loadSampleData} className="btn-load-sample">
            📚 Muat Data Contoh
          </button>
        )}
      </div>

      <div className="home-controls">
        <SearchBar 
          value={searchQuery}
          onChange={setSearchQuery}
        />
        <FilterButtons 
          activeFilter={activeFilter}
          onFilterChange={setActiveFilter}
        />
      </div>

      {displayBooks.length === 0 ? (
        <div className="empty-state">
          <p className="empty-message">
            {searchQuery || activeFilter !== 'all' 
              ? 'Tidak ada buku yang sesuai dengan pencarian atau filter.'
              : 'Belum ada buku. Tambahkan buku pertama Anda!'}
          </p>
        </div>
      ) : (
        <div className="books-grid">
          {displayBooks.map(book => (
            <BookCard 
              key={book.id} 
              book={book} 
              onDelete={handleDelete}
            />
          ))}
        </div>
      )}
    </div>
  );
};

export default Home;
