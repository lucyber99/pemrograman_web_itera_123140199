# Program Pengelolaan Data Nilai Mahasiswa

Program Python untuk mengelola data nilai mahasiswa dengan arsitektur modular.

## Struktur Modular

```
praktikum 4/
│
├── main.py                 # Entry point program
├── data_mahasiswa.py       # Module pengelolaan data
├── perhitungan.py          # Module perhitungan nilai & grade
├── pencarian.py            # Module pencarian & filter
├── tampilan.py             # Module UI/tampilan
├── input_data.py           # Module input & validasi
└── README.md              # Dokumentasi
```

## Deskripsi Module

### 1. `data_mahasiswa.py`
- Menyimpan data mahasiswa
- Fungsi CRUD dasar (Create, Read, Update, Delete)
- **Fungsi:**
  - `get_all_mahasiswa()` - Mengambil semua data
  - `tambah_mahasiswa()` - Menambah mahasiswa baru
  - `hapus_mahasiswa()` - Menghapus berdasarkan NIM
  - `cari_mahasiswa_by_nim()` - Cari berdasarkan NIM

### 2. `perhitungan.py`
- Perhitungan nilai akhir dan grade
- **Fungsi:**
  - `hitung_nilai_akhir()` - 30% UTS + 40% UAS + 30% Tugas
  - `tentukan_grade()` - Konversi nilai ke grade (A/B/C/D/E)
  - `hitung_rata_rata_kelas()` - Rata-rata nilai kelas

### 3. `pencarian.py`
- Pencarian dan filtering data
- **Fungsi:**
  - `cari_mahasiswa_tertinggi()` - Cari nilai tertinggi
  - `cari_mahasiswa_terendah()` - Cari nilai terendah
  - `filter_berdasarkan_grade()` - Filter by grade
  - `cari_mahasiswa_by_nama()` - Cari berdasarkan nama

### 4. `tampilan.py`
- Menampilkan data dan UI
- **Fungsi:**
  - `tampilkan_data_tabel()` - Format tabel lengkap
  - `tampilkan_statistik()` - Statistik kelas
  - `tampilkan_detail_mahasiswa()` - Detail satu mahasiswa

### 5. `input_data.py`
- Input dan validasi data
- **Fungsi:**
  - `input_mahasiswa_baru()` - Input data baru dengan validasi
  - `validasi_grade()` - Validasi input grade
  - `konfirmasi()` - Konfirmasi user action

### 6. `main.py`
- Entry point program
- Menu utama dan orchestration
- Mengintegrasikan semua module

## Cara Menjalankan

```bash
python main.py
```

## Fitur Program

1. ✅ Tampilkan semua data mahasiswa dalam tabel
2. ✅ Tambah data mahasiswa baru
3. ✅ Cari mahasiswa dengan nilai tertinggi
4. ✅ Cari mahasiswa dengan nilai terendah
5. ✅ Filter mahasiswa berdasarkan grade
6. ✅ Tampilkan statistik kelas lengkap
7. ✅ Hitung rata-rata nilai kelas

## Kriteria Grade

- **A**: ≥ 80
- **B**: ≥ 70
- **C**: ≥ 60
- **D**: ≥ 50
- **E**: < 50

## Formula Nilai Akhir

```
Nilai Akhir = (30% × UTS) + (40% × UAS) + (30% × Tugas)
```

## Keuntungan Arsitektur Modular

1. **Separation of Concerns** - Setiap module punya tanggung jawab spesifik
2. **Maintainability** - Mudah dipelihara dan diupdate
3. **Reusability** - Fungsi bisa digunakan ulang di project lain
4. **Testability** - Mudah untuk testing individual module
5. **Scalability** - Mudah menambah fitur baru
6. **Readability** - Code lebih mudah dibaca dan dipahami

## Pengembangan Lebih Lanjut

Untuk menambah fitur baru:
1. Buat module baru atau tambahkan fungsi di module yang sesuai
2. Import di `main.py`
3. Tambahkan menu baru di `menu_utama()`

## Requirements

- Python 3.6 atau lebih tinggi
- Tidak ada external dependencies
