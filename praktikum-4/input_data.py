"""
Module untuk input dan validasi data
"""


def input_mahasiswa_baru():
    """
    Input data mahasiswa baru
    """
    print("\n" + "="*50)
    print("INPUT DATA MAHASISWA BARU")
    print("="*50)
    
    try:
        nama = input("Nama Lengkap: ").strip()
        if not nama:
            print("❌ Nama tidak boleh kosong!")
            return None
            
        nim = input("NIM: ").strip()
        if not nim:
            print("❌ NIM tidak boleh kosong!")
            return None
            
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
    except KeyboardInterrupt:
        print("\n❌ Input dibatalkan.")
        return None


def validasi_grade(grade):
    """
    Validasi input grade
    """
    return grade.upper() in ["A", "B", "C", "D", "E"]


def konfirmasi(pesan):
    """
    Meminta konfirmasi user
    """
    while True:
        jawaban = input(f"{pesan} (y/n): ").strip().lower()
        if jawaban in ['y', 'yes', 'ya']:
            return True
        elif jawaban in ['n', 'no', 'tidak']:
            return False
        else:
            print("❌ Input tidak valid! Masukkan y atau n.")
