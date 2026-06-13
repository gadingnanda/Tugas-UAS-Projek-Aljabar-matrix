matriks = {
    "x": [[1,5], [9, 4]],
    "y": [[15, 26], [12, 38]],
    "p": [[40, 60], [27, 21]],
    "z": [[2, 19, 32], [44, 5, 6], [5, 40, 7]],
    "j": [[23, 6, 9], [19, 20, 5], [4, 12, 50]],
    "k": [[9, 8, 15], [7, 60, 4], [34, 77, 8]]
    
}

def tampilkan_matriks():
    print("DAFTAR MATRIKS :")
    for key, nilai in matriks.items():
        print(f"\nMatriks {key}:")
        for baris in nilai:
            print(baris)

def pilih_matriks():
    matrix = input("Pilih matriks (x/y/p/z/j/k) : ")
    if matrix not in matriks:
        print("Matriks tidak ditemukan!")
        return None
    return matrix

def tambah(A, B):
    hasil = []
    for i in range(len(A)):
        baris = []
        for j in range(len(A[0])):
            baris.append(A[i][j] + B[i][j])
        hasil.append(baris)
    return hasil

def kurang(A, B):
    hasil = []
    for i in range(len(A)):
        baris = []
        for j in range(len(A[0])):
            baris.append(A[i][j] - B[i][j])
        hasil.append(baris)
    return hasil

def kali(A, B):
    hasil = []
    for i in range(len(A)):
        baris = []
        for j in range(len(B[0])):
            total = 0
            for k in range(len(B)):
                total += A[i][k] * B[k][j]
            baris.append(total)
        hasil.append(baris)
    return hasil


def transpose(A):
    hasil = []
    for j in range(len(A[0])):
        baris = []
        for i in range(len(A)):
            baris.append(A[i][j])
        hasil.append(baris)
    return hasil


def determinan(A):
    if len(A) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]

    elif len(A) == 3:
        return (
            A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
            - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
        )