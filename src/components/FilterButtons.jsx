import './FilterButtons.css';

const FilterButtons = ({ activeFilter, onFilterChange }) => {
  const filters = [
    { value: 'all', label: 'Semua' },
    { value: 'milik', label: 'Sudah Dimiliki' },
    { value: 'baca', label: 'Sedang Dibaca' },
    { value: 'beli', label: 'Ingin Dibeli' }
  ];

  return (
    <div className="filter-buttons">
      {filters.map(filter => (
        <button
          key={filter.value}
          onClick={() => onFilterChange(filter.value)}
          className={`filter-btn ${activeFilter === filter.value ? 'active' : ''}`}
        >
          {filter.label}
        </button>
      ))}
    </div>
  );
};

export default FilterButtons;
