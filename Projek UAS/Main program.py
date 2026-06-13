import Gading066 as Gi

def perhitungan():
    print("\nPilih perhitungan matriks :")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    pilihan = input("Pilih operasi : ")

    nilai1 = Gi.pilih_matriks()
    if nilai1 is None:
        return
    nilai2 = Gi.pilih_matriks()
    if nilai2 is None:
        return

    A = Gi.matriks[nilai1]
    B = Gi.matriks[nilai2]

    if pilihan == "1":
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            print("Penjumlahan hanya dapat dilakukan pada matriks dengan ordo yang sama!")
            return
        hasil = Gi.tambah(A, B)
        simbol = "+"

    elif pilihan == "2":
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            print("Pengurangan hanya dapat dilakukan pada matriks dengan ordo yang sama!")
            return
        hasil = Gi.kurang(A, B)
        simbol = "-"

    elif pilihan == "3":
        if len(A[0]) != len(B):
            print("Perkalian matriks tidak dapat dilakukan!")
            return
        hasil = Gi.kali(A, B)
        simbol = "×"

    else:
        print("Pilihan tidak valid!")
        return
    
    print(f"\nMatriks {nilai1}:")
    for baris in A:
        print(baris)
    print(f"\nMatriks {nilai2}:")
    for baris in B:
        print(baris)
    print(f"\nHasil {nilai1} {simbol} {nilai2}:")
    for baris in hasil:
        print(baris)


def transpose_matriks():
    print("\nTranspose Matriks")
    nilai = Gi.pilih_matriks()
    if nilai is None:
        return

    hasil = Gi.transpose(Gi.matriks[nilai])
    print(f"\nMatriks {nilai}:")
    for baris in Gi.matriks[nilai]:
        print(baris)
    print(f"\nHasil transpose matriks {nilai}:")
    for baris in hasil:
        print(baris)


def determinan_matriks():
    print("\nNilai Determinan Matriks :")
    nilai = Gi.pilih_matriks()
    if nilai is None:
        return

    det = Gi.determinan(Gi.matriks[nilai])
    print(f"\nMatriks {nilai}:")
    for baris in Gi.matriks[nilai]:
        print(baris)
    print(f"\nNilai determinan matriks {nilai} = {det}")


def menu():
    Gi.tampilkan_matriks()
    while True:
        print("\nMENU :")
        print("1. Perhitungan Matriks")
        print("2. Transpose Matriks")
        print("3. Nilai Determinan Matriks")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            perhitungan()
        elif pilihan == "2":
            transpose_matriks()
        elif pilihan == "3":
            determinan_matriks()
        elif pilihan == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")
menu()