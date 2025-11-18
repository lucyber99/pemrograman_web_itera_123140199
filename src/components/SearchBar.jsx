import './SearchBar.css';

const SearchBar = ({ value, onChange, placeholder = 'Cari buku berdasarkan judul atau penulis...' }) => {
  return (
    <div className="search-bar">
      <input
        type="text"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder={placeholder}
        className="search-input"
      />
      <span className="search-icon">🔍</span>
    </div>
  );
};

export default SearchBar;
