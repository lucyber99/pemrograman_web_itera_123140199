import { useNavigate } from 'react-router-dom';
import { useBooks } from '../contexts/BooksContext';
import BookForm from '../components/BookForm';
import './AddBook.css';

const AddBook = () => {
  const navigate = useNavigate();
  const { addBook } = useBooks();

  const handleSubmit = (formData) => {
    const result = addBook(formData);
    
    if (result.success) {
      // Redirect ke home setelah berhasil menambahkan
      navigate('/', { 
        state: { message: `Buku "${result.book.title}" berhasil ditambahkan!` }
      });
    }
    
    return result;
  };

  return (
    <div className="add-book-page">
      <div className="add-book-container">
        <h1>Tambah Buku Baru</h1>
        <BookForm 
          onSubmit={handleSubmit}
          submitLabel="Tambah Buku"
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

export default AddBook;
