"""
Program Pengelolaan Data Nilai Mahasiswa
Fitur: CRUD data mahasiswa, hitung nilai akhir, grade, statistik
"""

# Data mahasiswa awal
data_mahasiswa = [
    {
        "nama": "Ahmad Fauzi",
        "nim": "2301010001",
        "nilai_uts": 85,
        "nilai_uas": 90,
        "nilai_tugas": 88
    },
    {
        "nama": "Siti Nurhaliza",
        "nim": "2301010002",
        "nilai_uts": 78,
        "nilai_uas": 82,
        "nilai_tugas": 80
    },
    {
        "nama": "Budi Santoso",
        "nim": "2301010003",
        "nilai_uts": 65,
        "nilai_uas": 70,
        "nilai_tugas": 68
    },
    {
        "nama": "Dewi Lestari",
        "nim": "2301010004",
        "nilai_uts": 92,
        "nilai_uas": 95,
        "nilai_tugas": 93
    },
    {
        "nama": "Eko Prasetyo",
        "nim": "2301010005",
        "nilai_uts": 55,
        "nilai_uas": 60,
        "nilai_tugas": 58
    }
]


def hitung_nilai_akhir(nilai_uts, nilai_uas, nilai_tugas):
    """
    Menghitung nilai akhir mahasiswa
    Formula: 30% UTS + 40% UAS + 30% Tugas
    """
    nilai_akhir = (0.3 * nilai_uts) + (0.4 * nilai_uas) + (0.3 * nilai_tugas)
    return round(nilai_akhir, 2)


def tentukan_grade(nilai_akhir):
    """
    Menentukan grade berdasarkan nilai akhir
    A: ≥80, B: ≥70, C: ≥60, D: ≥50, E: <50
    """
    if nilai_akhir >= 80:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 60:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    else:
        return "E"


def tampilkan_data_tabel(data_mahasiswa):
    """
    Menampilkan data mahasiswa dalam format tabel
    """
    if not data_mahasiswa:
        print("\n⚠️  Tidak ada data mahasiswa!")
        return
    
    print("\n" + "="*120)
    print(f"{'No':<4} {'Nama':<20} {'NIM':<12} {'UTS':<6} {'UAS':<6} {'Tugas':<6} {'Nilai Akhir':<12} {'Grade':<6}")
    print("="*120)
    
    for idx, mhs in enumerate(data_mahasiswa, 1):
        nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        grade = tentukan_grade(nilai_akhir)
        print(f"{idx:<4} {mhs['nama']:<20} {mhs['nim']:<12} {mhs['nilai_uts']:<6} "
              f"{mhs['nilai_uas']:<6} {mhs['nilai_tugas']:<6} {nilai_akhir:<12} {grade:<6}")
    
    print("="*120)


def cari_mahasiswa_tertinggi(data_mahasiswa):
    """
    Mencari mahasiswa dengan nilai tertinggi
    """
    if not data_mahasiswa:
        return None
    
    mahasiswa_tertinggi = None
    nilai_tertinggi = 0
    
    for mhs in data_mahasiswa:
        nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        if nilai_akhir > nilai_tertinggi:
            nilai_tertinggi = nilai_akhir
            mahasiswa_tertinggi = mhs.copy()
            mahasiswa_tertinggi['nilai_akhir'] = nilai_akhir
    
    return mahasiswa_tertinggi


def cari_mahasiswa_terendah(data_mahasiswa):
    """
    Mencari mahasiswa dengan nilai terendah
    """
    if not data_mahasiswa:
        return None
    
    mahasiswa_terendah = None
    nilai_terendah = 100
    
    for mhs in data_mahasiswa:
        nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        if nilai_akhir < nilai_terendah:
            nilai_terendah = nilai_akhir
            mahasiswa_terendah = mhs.copy()
            mahasiswa_terendah['nilai_akhir'] = nilai_akhir
    
    return mahasiswa_terendah


def input_mahasiswa_baru():
    """
    Input data mahasiswa baru
    """
    print("\n" + "="*50)
    print("INPUT DATA MAHASISWA BARU")
    print("="*50)
    
    try:
        nama = input("Nama Lengkap: ").strip()
        nim = input("NIM: ").strip()
        nilai_uts = float(input("Nilai UTS (0-100): "))
        nilai_uas = float(input("Nilai UAS (0-100): "))
        nilai_tugas = float(input("Nilai Tugas (0-100): "))
        
        # Validasi nilai
        if not (0 <= nilai_uts <= 100 and 0 <= nilai_uas <= 100 and 0 <= nilai_tugas <= 100):
            print("❌ Nilai harus antara 0-100!")
            return None
        
        mahasiswa_baru = {
            "nama": nama,
            "nim": nim,
            "nilai_uts": nilai_uts,
            "nilai_uas": nilai_uas,
            "nilai_tugas": nilai_tugas
        }
        
        return mahasiswa_baru
    
    except ValueError:
        print("❌ Input tidak valid! Nilai harus berupa angka.")
        return None


def filter_berdasarkan_grade(data_mahasiswa, grade_dicari):
    """
    Filter mahasiswa berdasarkan grade tertentu
    """
    hasil_filter = []
    
    for mhs in data_mahasiswa:
        nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        grade = tentukan_grade(nilai_akhir)
        
        if grade == grade_dicari.upper():
            mhs_copy = mhs.copy()
            mhs_copy['nilai_akhir'] = nilai_akhir
            mhs_copy['grade'] = grade
            hasil_filter.append(mhs_copy)
    
    return hasil_filter


def hitung_rata_rata_kelas(data_mahasiswa):
    """
    Menghitung rata-rata nilai kelas
    """
    if not data_mahasiswa:
        return 0
    
    total_nilai = 0
    for mhs in data_mahasiswa:
        nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        total_nilai += nilai_akhir
    
    rata_rata = total_nilai / len(data_mahasiswa)
    return round(rata_rata, 2)


def tampilkan_statistik(data_mahasiswa):
    """
    Menampilkan statistik kelas
    """
    if not data_mahasiswa:
        print("\n⚠️  Tidak ada data untuk ditampilkan!")
        return
    
    print("\n" + "="*50)
    print("STATISTIK KELAS")
    print("="*50)
    
    # Mahasiswa tertinggi
    mhs_tertinggi = cari_mahasiswa_tertinggi(data_mahasiswa)
    print(f"\n🏆 Nilai Tertinggi:")
    print(f"   Nama: {mhs_tertinggi['nama']}")
    print(f"   NIM: {mhs_tertinggi['nim']}")
    print(f"   Nilai Akhir: {mhs_tertinggi['nilai_akhir']}")
    print(f"   Grade: {tentukan_grade(mhs_tertinggi['nilai_akhir'])}")
    
    # Mahasiswa terendah
    mhs_terendah = cari_mahasiswa_terendah(data_mahasiswa)
    print(f"\n📉 Nilai Terendah:")
    print(f"   Nama: {mhs_terendah['nama']}")
    print(f"   NIM: {mhs_terendah['nim']}")
    print(f"   Nilai Akhir: {mhs_terendah['nilai_akhir']}")
    print(f"   Grade: {tentukan_grade(mhs_terendah['nilai_akhir'])}")
    
    # Rata-rata kelas
    rata_rata = hitung_rata_rata_kelas(data_mahasiswa)
    print(f"\n📊 Rata-rata Kelas: {rata_rata}")
    print(f"   Grade Rata-rata: {tentukan_grade(rata_rata)}")
    
    # Distribusi grade
    print(f"\n📈 Distribusi Grade:")
    grade_count = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
    for mhs in data_mahasiswa:
        nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        grade = tentukan_grade(nilai_akhir)
        grade_count[grade] += 1
    
    for grade, count in grade_count.items():
        persentase = (count / len(data_mahasiswa)) * 100
        print(f"   Grade {grade}: {count} mahasiswa ({persentase:.1f}%)")
    
    print("="*50)


def menu_utama():
    """
    Menu utama program
    """
    while True:
        print("\n" + "="*50)
        print("SISTEM PENGELOLAAN DATA NILAI MAHASISWA")
        print("="*50)
        print("1. Tampilkan Semua Data Mahasiswa")
        print("2. Tambah Data Mahasiswa Baru")
        print("3. Cari Mahasiswa Tertinggi")
        print("4. Cari Mahasiswa Terendah")
        print("5. Filter Berdasarkan Grade")
        print("6. Tampilkan Statistik Kelas")
        print("7. Hitung Rata-rata Kelas")
        print("0. Keluar")
        print("="*50)
        
        try:
            pilihan = input("Pilih menu (0-7): ").strip()
            
            if pilihan == "1":
                tampilkan_data_tabel(data_mahasiswa)
            
            elif pilihan == "2":
                mahasiswa_baru = input_mahasiswa_baru()
                if mahasiswa_baru:
                    data_mahasiswa.append(mahasiswa_baru)
                    print(f"\n✅ Data mahasiswa {mahasiswa_baru['nama']} berhasil ditambahkan!")
            
            elif pilihan == "3":
                mhs_tertinggi = cari_mahasiswa_tertinggi(data_mahasiswa)
                if mhs_tertinggi:
                    print("\n🏆 MAHASISWA DENGAN NILAI TERTINGGI:")
                    print(f"   Nama: {mhs_tertinggi['nama']}")
                    print(f"   NIM: {mhs_tertinggi['nim']}")
                    print(f"   Nilai Akhir: {mhs_tertinggi['nilai_akhir']}")
                    print(f"   Grade: {tentukan_grade(mhs_tertinggi['nilai_akhir'])}")
            
            elif pilihan == "4":
                mhs_terendah = cari_mahasiswa_terendah(data_mahasiswa)
                if mhs_terendah:
                    print("\n📉 MAHASISWA DENGAN NILAI TERENDAH:")
                    print(f"   Nama: {mhs_terendah['nama']}")
                    print(f"   NIM: {mhs_terendah['nim']}")
                    print(f"   Nilai Akhir: {mhs_terendah['nilai_akhir']}")
                    print(f"   Grade: {tentukan_grade(mhs_terendah['nilai_akhir'])}")
            
            elif pilihan == "5":
                grade_cari = input("Masukkan Grade yang dicari (A/B/C/D/E): ").strip().upper()
                if grade_cari in ["A", "B", "C", "D", "E"]:
                    hasil = filter_berdasarkan_grade(data_mahasiswa, grade_cari)
                    if hasil:
                        print(f"\n📋 MAHASISWA DENGAN GRADE {grade_cari}:")
                        for idx, mhs in enumerate(hasil, 1):
                            print(f"\n{idx}. {mhs['nama']} ({mhs['nim']})")
                            print(f"   Nilai Akhir: {mhs['nilai_akhir']}")
                    else:
                        print(f"\n⚠️  Tidak ada mahasiswa dengan grade {grade_cari}")
                else:
                    print("❌ Grade tidak valid!")
            
            elif pilihan == "6":
                tampilkan_statistik(data_mahasiswa)
            
            elif pilihan == "7":
                rata_rata = hitung_rata_rata_kelas(data_mahasiswa)
                print(f"\n📊 Rata-rata Nilai Kelas: {rata_rata}")
                print(f"   Grade: {tentukan_grade(rata_rata)}")
            
            elif pilihan == "0":
                print("\n👋 Terima kasih telah menggunakan program ini!")
                break
            
            else:
                print("❌ Pilihan tidak valid! Silakan pilih 0-7.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Program dihentikan oleh user.")
            break
        except Exception as e:
            print(f"\n❌ Terjadi kesalahan: {e}")


# Jalankan program
if __name__ == "__main__":
    menu_utama()
