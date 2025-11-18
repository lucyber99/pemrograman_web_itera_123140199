import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import BookCard from '../components/BookCard';

const mockBook = {
  id: '1',
  title: 'Test Book',
  author: 'Test Author',
  status: 'milik',
  createdAt: new Date().toISOString()
};

const renderWithRouter = (component) => {
  return render(
    <BrowserRouter>
      {component}
    </BrowserRouter>
  );
};

describe('BookCard Component', () => {
  it('should render book information correctly', () => {
    renderWithRouter(
      <BookCard book={mockBook} onDelete={() => {}} />
    );

    expect(screen.getByText('Test Book')).toBeInTheDocument();
    expect(screen.getByText('Oleh: Test Author')).toBeInTheDocument();
    expect(screen.getByText('Sudah Dimiliki')).toBeInTheDocument();
  });

  it('should display correct status badge for "baca" status', () => {
    const bookBaca = { ...mockBook, status: 'baca' };
    
    renderWithRouter(
      <BookCard book={bookBaca} onDelete={() => {}} />
    );

    expect(screen.getByText('Sedang Dibaca')).toBeInTheDocument();
  });

  it('should display correct status badge for "beli" status', () => {
    const bookBeli = { ...mockBook, status: 'beli' };
    
    renderWithRouter(
      <BookCard book={bookBeli} onDelete={() => {}} />
    );

    expect(screen.getByText('Ingin Dibeli')).toBeInTheDocument();
  });

  it('should have Edit and Delete buttons', () => {
    renderWithRouter(
      <BookCard book={mockBook} onDelete={() => {}} />
    );

    expect(screen.getByRole('link', { name: /edit/i })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /hapus/i })).toBeInTheDocument();
  });

  it('should have correct edit link', () => {
    renderWithRouter(
      <BookCard book={mockBook} onDelete={() => {}} />
    );

    const editLink = screen.getByRole('link', { name: /edit/i });
    expect(editLink).toHaveAttribute('href', '/edit/1');
  });
});
