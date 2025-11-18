"""
Program Pengelolaan Data Nilai Mahasiswa - Modular Version
Main Entry Point
"""

from data_mahasiswa import get_all_mahasiswa, tambah_mahasiswa
from perhitungan import hitung_rata_rata_kelas, tentukan_grade
from pencarian import (
    cari_mahasiswa_tertinggi, 
    cari_mahasiswa_terendah, 
    filter_berdasarkan_grade
)
from tampilan import (
    tampilkan_data_tabel, 
    tampilkan_statistik, 
    tampilkan_detail_mahasiswa
)
from input_data import input_mahasiswa_baru, validasi_grade


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
                data = get_all_mahasiswa()
                tampilkan_data_tabel(data)
            
            elif pilihan == "2":
                mahasiswa_baru = input_mahasiswa_baru()
                if mahasiswa_baru:
                    tambah_mahasiswa(mahasiswa_baru)
                    print(f"\n✅ Data mahasiswa {mahasiswa_baru['nama']} berhasil ditambahkan!")
            
            elif pilihan == "3":
                data = get_all_mahasiswa()
                mhs_tertinggi = cari_mahasiswa_tertinggi(data)
                if mhs_tertinggi:
                    tampilkan_detail_mahasiswa(
                        mhs_tertinggi, 
                        "🏆 MAHASISWA DENGAN NILAI TERTINGGI"
                    )
            
            elif pilihan == "4":
                data = get_all_mahasiswa()
                mhs_terendah = cari_mahasiswa_terendah(data)
                if mhs_terendah:
                    tampilkan_detail_mahasiswa(
                        mhs_terendah, 
                        "📉 MAHASISWA DENGAN NILAI TERENDAH"
                    )
            
            elif pilihan == "5":
                grade_cari = input("Masukkan Grade yang dicari (A/B/C/D/E): ").strip().upper()
                if validasi_grade(grade_cari):
                    data = get_all_mahasiswa()
                    hasil = filter_berdasarkan_grade(data, grade_cari)
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
                data = get_all_mahasiswa()
                tampilkan_statistik(data)
            
            elif pilihan == "7":
                data = get_all_mahasiswa()
                rata_rata = hitung_rata_rata_kelas(data)
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
    print("="*50)
    print("PROGRAM PENGELOLAAN DATA NILAI MAHASISWA")
    print("Versi Modular - Python")
    print("="*50)
    menu_utama()
