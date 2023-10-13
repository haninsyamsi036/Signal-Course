import cmath

def my_fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = my_fft(x[0::2])
    odd = my_fft(x[1::2])
    T = [cmath.exp(-2j * cmath.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

def my_fft2d(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # FFT per baris
    for i in range(rows):
        matrix[i] = my_fft(matrix[i])

    # FFT per kolom
    for j in range(cols):
        col = [matrix[i][j] for i in range(rows)]
        col = my_fft(col)
        for i in range(rows):
            matrix[i][j] = col[i]

    return matrix

# Contoh penggunaan
input_matrix = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13,14]
]

print ("FFT 2D Graph and SourceCode")
print ("Hanin Ainussyamsi Prabowo")
print ("5009211036")