import { useState } from 'react';
import './BookForm.css';

const BookForm = ({ initialData = {}, onSubmit, submitLabel = 'Simpan' }) => {
  const [formData, setFormData] = useState({
    title: initialData.title || '',
    author: initialData.author || '',
    status: initialData.status || 'milik',
    imageUrl: initialData.imageUrl || ''
  });

  const [errors, setErrors] = useState({});

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
    // Clear error untuk field yang sedang diubah
    if (errors[name]) {
      setErrors({
        ...errors,
        [name]: ''
      });
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    
    // Submit form
    const result = onSubmit(formData);
    
    // Jika ada errors, tampilkan
    if (result && !result.success && result.errors) {
      setErrors(result.errors);
    } else if (result && result.success) {
      // Clear form jika berhasil dan bukan edit mode
      if (!initialData.id) {
        setFormData({
          title: '',
          author: '',
          status: 'milik',
          imageUrl: ''
        });
      }
      setErrors({});
    }
  };

  return (
    <form onSubmit={handleSubmit} className="book-form">
      <div className="form-group">
        <label htmlFor="title">Judul Buku *</label>
        <input
          type="text"
          id="title"
          name="title"
          value={formData.title}
          onChange={handleChange}
          className={errors.title ? 'error' : ''}
          placeholder="Masukkan judul buku"
        />
        {errors.title && <span className="error-message">{errors.title}</span>}
      </div>

      <div className="form-group">
        <label htmlFor="author">Penulis *</label>
        <input
          type="text"
          id="author"
          name="author"
          value={formData.author}
          onChange={handleChange}
          className={errors.author ? 'error' : ''}
          placeholder="Masukkan nama penulis"
        />
        {errors.author && <span className="error-message">{errors.author}</span>}
      </div>

      <div className="form-group">
        <label htmlFor="status">Status *</label>
        <select
          id="status"
          name="status"
          value={formData.status}
          onChange={handleChange}
          className={errors.status ? 'error' : ''}
        >
          <option value="milik">Sudah Dimiliki</option>
          <option value="baca">Sedang Dibaca</option>
          <option value="beli">Ingin Dibeli</option>
        </select>
        {errors.status && <span className="error-message">{errors.status}</span>}
      </div>

      <div className="form-group">
        <label htmlFor="imageUrl">URL Gambar Cover (opsional)</label>
        <input
          type="url"
          id="imageUrl"
          name="imageUrl"
          value={formData.imageUrl}
          onChange={handleChange}
          className={errors.imageUrl ? 'error' : ''}
          placeholder="https://example.com/book-cover.jpg"
        />
        {errors.imageUrl && <span className="error-message">{errors.imageUrl}</span>}
        <span className="help-text">Masukkan URL gambar cover buku (opsional)</span>
      </div>

      <button type="submit" className="btn btn-primary btn-submit">
        {submitLabel}
      </button>
    </form>
  );
};

export default BookForm;
