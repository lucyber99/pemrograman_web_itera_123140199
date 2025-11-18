import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import FilterButtons from '../components/FilterButtons';

describe('FilterButtons Component', () => {
  it('should render all filter buttons', () => {
    render(
      <FilterButtons 
        activeFilter="all" 
        onFilterChange={() => {}} 
      />
    );

    expect(screen.getByText('Semua')).toBeInTheDocument();
    expect(screen.getByText('Sudah Dimiliki')).toBeInTheDocument();
    expect(screen.getByText('Sedang Dibaca')).toBeInTheDocument();
    expect(screen.getByText('Ingin Dibeli')).toBeInTheDocument();
  });

  it('should highlight active filter', () => {
    render(
      <FilterButtons 
        activeFilter="milik" 
        onFilterChange={() => {}} 
      />
    );

    const activeButton = screen.getByText('Sudah Dimiliki');
    expect(activeButton).toHaveClass('active');
  });

  it('should call onFilterChange when button is clicked', async () => {
    const user = userEvent.setup();
    let selectedFilter = 'all';
    const handleFilterChange = (filter) => {
      selectedFilter = filter;
    };

    render(
      <FilterButtons 
        activeFilter={selectedFilter} 
        onFilterChange={handleFilterChange} 
      />
    );

    const bacaButton = screen.getByText('Sedang Dibaca');
    await user.click(bacaButton);

    expect(selectedFilter).toBe('baca');
  });

  it('should render 4 filter buttons', () => {
    render(
      <FilterButtons 
        activeFilter="all" 
        onFilterChange={() => {}} 
      />
    );

    const buttons = screen.getAllByRole('button');
    expect(buttons).toHaveLength(4);
  });
});
