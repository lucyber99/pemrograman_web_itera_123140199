"""
Module untuk mengelola data mahasiswa
"""

# Data mahasiswa awal
mahasiswa_list = [
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


def get_all_mahasiswa():
    """Mengambil semua data mahasiswa"""
    return mahasiswa_list


def tambah_mahasiswa(mahasiswa_baru):
    """Menambah mahasiswa baru ke list"""
    mahasiswa_list.append(mahasiswa_baru)
    return True


def hapus_mahasiswa(nim):
    """Menghapus mahasiswa berdasarkan NIM"""
    global mahasiswa_list
    mahasiswa_list = [mhs for mhs in mahasiswa_list if mhs['nim'] != nim]


def cari_mahasiswa_by_nim(nim):
    """Mencari mahasiswa berdasarkan NIM"""
    for mhs in mahasiswa_list:
        if mhs['nim'] == nim:
            return mhs
    return None
