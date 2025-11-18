import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { BooksProvider } from './contexts/BooksContext';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import AddBook from './pages/AddBook';
import EditBook from './pages/EditBook';
import './App.css';

function App() {
  return (
    <Router>
      <BooksProvider>
        <div className="app">
          <Navbar />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/add" element={<AddBook />} />
            <Route path="/edit/:id" element={<EditBook />} />
          </Routes>
        </div>
      </BooksProvider>
    </Router>
  );
}

export default App;
