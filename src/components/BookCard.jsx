import { Link } from 'react-router-dom';
import { useState } from 'react';
import './BookCard.css';

const BookCard = ({ book, onDelete }) => {
  const [imageError, setImageError] = useState(false);

  const handleDelete = () => {
    if (window.confirm(`Apakah Anda yakin ingin menghapus buku "${book.title}"?`)) {
      onDelete(book.id);
    }
  };

  const getStatusLabel = (status) => {
    const labels = {
      'milik': 'Sudah Dimiliki',
      'baca': 'Sedang Dibaca',
      'beli': 'Ingin Dibeli'
    };
    return labels[status] || status;
  };

  const getStatusClass = (status) => {
    return `status-badge status-${status}`;
  };

  const handleImageError = () => {
    setImageError(true);
  };

  const getPlaceholderImage = () => {
    return `https://via.placeholder.com/150x200/4a5568/ffffff?text=${encodeURIComponent(book.title.substring(0, 20))}`;
  };

  return (
    <div className="book-card">
      <div className="book-card-image">
        {book.imageUrl && !imageError ? (
          <img 
            src={book.imageUrl} 
            alt={`Cover ${book.title}`}
            onError={handleImageError}
            className="book-cover"
          />
        ) : (
          <div className="book-cover-placeholder">
            <div className="placeholder-icon">📚</div>
            <div className="placeholder-title">{book.title}</div>
          </div>
        )}
      </div>
      <div className="book-card-content">
        <div className="book-card-header">
          <h3 className="book-title">{book.title}</h3>
          <span className={getStatusClass(book.status)}>
            {getStatusLabel(book.status)}
          </span>
        </div>
        <p className="book-author">Oleh: {book.author}</p>
        <div className="book-card-actions">
          <Link to={`/edit/${book.id}`} className="btn btn-edit">
            Edit
          </Link>
          <button onClick={handleDelete} className="btn btn-delete">
            Hapus
          </button>
        </div>
      </div>
    </div>
  );
};

export default BookCard;
