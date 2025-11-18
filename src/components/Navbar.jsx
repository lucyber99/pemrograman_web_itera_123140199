import { Link } from 'react-router-dom';
import './Navbar.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-container">
        <Link to="/" className="navbar-logo">
          📚 Manajemen Buku
        </Link>
        <div className="navbar-menu">
          <Link to="/" className="navbar-link">
            Beranda
          </Link>
          <Link to="/add" className="navbar-link navbar-link-add">
            + Tambah Buku
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
