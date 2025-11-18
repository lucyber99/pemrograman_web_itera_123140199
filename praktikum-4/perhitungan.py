"""
Module untuk perhitungan nilai dan grade
"""


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
