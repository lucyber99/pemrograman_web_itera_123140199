import { describe, it, expect, vi } from 'vitest';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import SearchBar from '../components/SearchBar';

describe('SearchBar Component', () => {
  it('should render search input with placeholder', () => {
    render(<SearchBar value="" onChange={() => {}} />);

    const input = screen.getByPlaceholderText(/cari buku/i);
    expect(input).toBeInTheDocument();
  });

  it('should display the current value', () => {
    render(<SearchBar value="test query" onChange={() => {}} />);

    const input = screen.getByDisplayValue('test query');
    expect(input).toBeInTheDocument();
  });

  it('should call onChange when user types', async () => {
    const user = userEvent.setup();
    const mockOnChange = vi.fn();

    render(
      <SearchBar value="" onChange={mockOnChange} />
    );

    const input = screen.getByPlaceholderText(/cari buku/i);
    await user.type(input, 't');

    // Check that onChange was called
    expect(mockOnChange).toHaveBeenCalled();
    expect(mockOnChange).toHaveBeenCalledWith('t');
  });

  it('should accept custom placeholder', () => {
    render(
      <SearchBar 
        value="" 
        onChange={() => {}} 
        placeholder="Custom placeholder"
      />
    );

    expect(screen.getByPlaceholderText('Custom placeholder')).toBeInTheDocument();
  });

  it('should display search icon', () => {
    render(<SearchBar value="" onChange={() => {}} />);

    const icon = screen.getByText('🔍');
    expect(icon).toBeInTheDocument();
  });
});
