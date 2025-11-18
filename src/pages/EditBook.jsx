import { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useBooks } from '../contexts/BooksContext';
import BookForm from '../components/BookForm';
import './EditBook.css';

const EditBook = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const { getBookById, updateBook } = useBooks();
  const [book, setBook] = useState(null);
  const [notFound, setNotFound] = useState(false);

  useEffect(() => {
    const foundBook = getBookById(id);
    if (foundBook) {
      setBook(foundBook);
    } else {
      setNotFound(true);
    }
  }, [id, getBookById]);

  const handleSubmit = (formData) => {
    const result = updateBook(id, formData);
    
    if (result.success) {
      // Redirect ke home setelah berhasil update
      navigate('/', { 
        state: { message: `Buku "${result.book.title}" berhasil diperbarui!` }
      });
    }
    
    return result;
  };

  if (notFound) {
    return (
      <div className="edit-book-page">
        <div className="edit-book-container">
          <h1>Buku Tidak Ditemukan</h1>
          <p>Buku yang Anda cari tidak ada.</p>
          <button 
            onClick={() => navigate('/')} 
            className="btn btn-back"
          >
            Kembali ke Beranda
          </button>
        </div>
      </div>
    );
  }

  if (!book) {
    return (
      <div className="edit-book-page">
        <div className="edit-book-container">
          <p>Memuat...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="edit-book-page">
      <div className="edit-book-container">
        <h1>Edit Buku</h1>
        <BookForm 
          initialData={book}
          onSubmit={handleSubmit}
          submitLabel="Perbarui Buku"
        />
        <button 
          onClick={() => navigate('/')} 
          className="btn btn-back"
        >
          Kembali
        </button>
      </div>
    </div>
  );
};

export default EditBook;
