"""
Module untuk pencarian dan filter data mahasiswa
"""

from perhitungan import hitung_nilai_akhir, tentukan_grade


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


def cari_mahasiswa_by_nama(data_mahasiswa, nama_cari):
    """
    Mencari mahasiswa berdasarkan nama (pencarian partial)
    """
    hasil = []
    nama_lower = nama_cari.lower()
    
    for mhs in data_mahasiswa:
        if nama_lower in mhs['nama'].lower():
            hasil.append(mhs)
    
    return hasil
