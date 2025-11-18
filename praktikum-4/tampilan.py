"""
Module untuk menampilkan data dan UI
"""

from perhitungan import hitung_nilai_akhir, tentukan_grade, hitung_rata_rata_kelas
from pencarian import cari_mahasiswa_tertinggi, cari_mahasiswa_terendah


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


def tampilkan_detail_mahasiswa(mhs, judul="DETAIL MAHASISWA"):
    """
    Menampilkan detail satu mahasiswa
    """
    nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
    grade = tentukan_grade(nilai_akhir)
    
    print(f"\n{judul}:")
    print(f"   Nama: {mhs['nama']}")
    print(f"   NIM: {mhs['nim']}")
    print(f"   Nilai UTS: {mhs['nilai_uts']}")
    print(f"   Nilai UAS: {mhs['nilai_uas']}")
    print(f"   Nilai Tugas: {mhs['nilai_tugas']}")
    print(f"   Nilai Akhir: {nilai_akhir}")
    print(f"   Grade: {grade}")
