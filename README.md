# Aplikasi Manajemen Buku Pribadi

Aplikasi web untuk mengelola koleksi buku pribadi yang memungkinkan pengguna mencatat buku yang dimiliki, sedang dibaca, atau ingin dibeli.

## Fitur Utama

✅ **Manajemen Buku Lengkap**
- Tambah buku baru dengan judul, penulis, dan status
- Edit informasi buku yang sudah ada
- Hapus buku dari koleksi
- Data tersimpan otomatis di localStorage

✅ **Pencarian & Filter**
- Cari buku berdasarkan judul atau penulis dengan debounce
- Filter buku berdasarkan status (Semua, Sudah Dimiliki, Sedang Dibaca, Ingin Dibeli)
- Real-time search dengan performa optimal

✅ **UI/UX Modern**
- Desain responsif dan user-friendly
- Card-based layout untuk tampilan buku
- Status badge dengan color coding
- Smooth transitions dan hover effects

## Teknologi yang Digunakan

- **React 19** - Library UI dengan functional components
- **React Router DOM** - Navigasi multi-halaman (SPA)
- **Vite** - Build tool dan dev server yang cepat
- **Vitest** - Testing framework
- **React Testing Library** - Testing components
- **CSS3** - Styling dengan custom CSS

## Struktur Folder

```
src/
├── components/          # Komponen reusable
│   ├── BookCard.jsx     # Card untuk menampilkan buku
│   ├── BookForm.jsx     # Form untuk tambah/edit buku
│   ├── FilterButtons.jsx # Tombol filter status
│   ├── Navbar.jsx       # Navigation bar
│   └── SearchBar.jsx    # Input pencarian
├── contexts/            # Context API untuk state management
│   └── BooksContext.jsx # Global state untuk data buku
├── hooks/               # Custom React hooks
│   ├── useDebounce.js   # Hook untuk debouncing
│   └── useLocalStorage.js # Hook untuk localStorage
├── pages/               # Halaman aplikasi
│   ├── Home.jsx         # Halaman utama dengan daftar buku
│   ├── AddBook.jsx      # Halaman tambah buku
│   └── EditBook.jsx     # Halaman edit buku
├── tests/               # Unit tests
│   ├── BookCard.test.jsx
│   ├── FilterButtons.test.jsx
│   ├── SearchBar.test.jsx
│   ├── useDebounce.test.js
│   ├── useLocalStorage.test.js
│   └── validation.test.js
├── utils/               # Utility functions
│   └── validation.js    # Validasi input & helper functions
├── App.jsx              # Root component dengan routing
└── main.jsx             # Entry point
```

## Implementasi Persyaratan

### ✅ Fitur Dasar
- [x] Menambah buku baru (judul, penulis, status: milik/baca/beli)
- [x] Mengedit dan menghapus buku
- [x] Filter buku berdasarkan status
- [x] Pencarian buku

### ✅ Teknologi React
- [x] useState dan useEffect digunakan di berbagai komponen
- [x] 6+ komponen reusable (BookCard, BookForm, SearchBar, FilterButtons, Navbar, dll)
- [x] Context API untuk state management (BooksContext)
- [x] React Router untuk navigasi multi-halaman (Home, AddBook, EditBook)

### ✅ Penyimpanan
- [x] localStorage untuk menyimpan data buku
- [x] Custom hook useLocalStorage untuk abstraksi

### ✅ Persyaratan Teknis
- [x] Functional components dengan Hooks
- [x] 2 custom hooks (useLocalStorage, useDebounce)
- [x] 31 unit tests dengan React Testing Library ✅
- [x] Error handling untuk form input dengan validasi
- [x] Struktur folder modular dan terorganisir

## Instalasi dan Menjalankan

### Prasyarat
- Node.js (versi 16 atau lebih baru)
- npm atau yarn

### Langkah-langkah

1. **Install dependencies**
   ```bash
   npm install
   ```

2. **Jalankan development server**
   ```bash
   npm run dev
   ```
   Aplikasi akan berjalan di `http://localhost:5173`

3. **Build untuk production**
   ```bash
   npm run build
   ```

4. **Jalankan tests**
   ```bash
   npm test
   ```

5. **Jalankan tests dengan coverage**
   ```bash
   npm run test:coverage
   ```

## Cara Menggunakan

### Menambah Buku
1. Klik tombol **"+ Tambah Buku"** di navbar
2. Isi form dengan informasi buku:
   - Judul (minimal 2 karakter, maksimal 100)
   - Penulis (minimal 2 karakter, maksimal 50)
   - Status (Sudah Dimiliki / Sedang Dibaca / Ingin Dibeli)
3. Klik **"Tambah Buku"**

### Mencari Buku
- Gunakan search bar di halaman utama
- Ketik judul atau nama penulis
- Hasil pencarian akan muncul secara real-time dengan debounce 300ms

### Filter Buku
- Klik salah satu tombol filter:
  - **Semua** - Tampilkan semua buku
  - **Sudah Dimiliki** - Buku yang sudah dimiliki
  - **Sedang Dibaca** - Buku yang sedang dibaca
  - **Ingin Dibeli** - Buku yang ingin dibeli

### Edit Buku
1. Klik tombol **"Edit"** pada card buku
2. Ubah informasi yang diinginkan
3. Klik **"Perbarui Buku"**

### Hapus Buku
1. Klik tombol **"Hapus"** pada card buku
2. Konfirmasi penghapusan

## Validasi Form

Aplikasi memiliki validasi input yang ketat:

- **Judul**: Wajib diisi, minimal 2 karakter, maksimal 100 karakter
- **Penulis**: Wajib diisi, minimal 2 karakter, maksimal 50 karakter
- **Status**: Harus dipilih salah satu dari 3 opsi

Error message akan ditampilkan jika validasi gagal.

## Testing

Aplikasi memiliki **31 unit tests** yang mencakup:

1. **Validation Utils** (8 tests)
   - Validasi input buku (judul, penulis, status)
   - Generate ID unik

2. **useLocalStorage Hook** (5 tests)
   - Initialize dengan nilai awal
   - Load dari localStorage
   - Update localStorage
   - Handle objects/arrays
   - Handle invalid JSON

3. **useDebounce Hook** (4 tests)
   - Return nilai awal
   - Debounce value changes
   - Cancel previous debounce
   - Custom delay

4. **BookCard Component** (5 tests)
   - Render informasi buku
   - Status badges
   - Edit/Delete buttons
   - Link navigation

5. **SearchBar Component** (5 tests)
   - Render input
   - Display value
   - onChange callback
   - Custom placeholder
   - Search icon

6. **FilterButtons Component** (4 tests)
   - Render semua tombol
   - Highlight active filter
   - onClick callback
   - Jumlah tombol

Jalankan tests dengan: `npm test`

## Fitur Tambahan

- **Debounced Search**: Pencarian dengan delay 300ms untuk performa optimal
- **Responsive Design**: Tampilan optimal di berbagai ukuran layar
- **Status Color Coding**: 
  - 🟢 Hijau = Sudah Dimiliki
  - 🔵 Biru = Sedang Dibaca
  - 🟡 Kuning = Ingin Dibeli
- **Konfirmasi Hapus**: Dialog konfirmasi sebelum menghapus buku
- **Persistence**: Data tersimpan otomatis di localStorage

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Lisensi

MIT

---

**Catatan**: Aplikasi ini dibuat sebagai bagian dari tugas praktikum Pengembangan Aplikasi Web.
