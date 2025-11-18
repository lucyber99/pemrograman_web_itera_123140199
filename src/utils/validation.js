/**
 * Validasi input form buku
 * @param {Object} book - Object buku dengan properti title, author, status, imageUrl
 * @returns {Object} - Object dengan properti isValid dan errors
 */
export const validateBookInput = (book) => {
  const errors = {};

  // Validasi judul
  if (!book.title || book.title.trim() === '') {
    errors.title = 'Judul buku harus diisi';
  } else if (book.title.trim().length < 2) {
    errors.title = 'Judul buku minimal 2 karakter';
  } else if (book.title.trim().length > 100) {
    errors.title = 'Judul buku maksimal 100 karakter';
  }

  // Validasi penulis
  if (!book.author || book.author.trim() === '') {
    errors.author = 'Nama penulis harus diisi';
  } else if (book.author.trim().length < 2) {
    errors.author = 'Nama penulis minimal 2 karakter';
  } else if (book.author.trim().length > 50) {
    errors.author = 'Nama penulis maksimal 50 karakter';
  }

  // Validasi status
  const validStatuses = ['milik', 'baca', 'beli'];
  if (!book.status || !validStatuses.includes(book.status)) {
    errors.status = 'Status harus dipilih (milik, baca, atau beli)';
  }

  // Validasi URL gambar (opsional, jika diisi harus valid)
  if (book.imageUrl && book.imageUrl.trim() !== '') {
    const urlPattern = /^https?:\/\/.+/i;
    if (!urlPattern.test(book.imageUrl.trim())) {
      errors.imageUrl = 'URL gambar harus valid (http:// atau https://)';
    }
  }

  return {
    isValid: Object.keys(errors).length === 0,
    errors
  };
};

/**
 * Generate ID unik untuk buku baru
 * @returns {string} - ID unik
 */
export const generateId = () => {
  return Date.now().toString(36) + Math.random().toString(36).substr(2);
};
