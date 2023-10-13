import numpy as np
import matplotlib.pyplot as plt

def fft2d(x):
    N, M = x.shape
    if N <= 1 and M <= 1:
        return x
    else:
        # Membagi data menjadi bagian ganjil dan genap
        x_even_even = fft2d(x[::2, ::2])
        x_even_odd = fft2d(x[::2, 1::2])
        x_odd_even = fft2d(x[1::2, ::2])
        x_odd_odd = fft2d(x[1::2, 1::2])

        # Kombinasi hasilnya
        factor = np.exp(-2j * np.pi * np.arange(N) / N)[:, None]
        even_part = np.hstack([x_even_even + factor * x_even_odd, x_even_even - factor * x_even_odd])
        odd_part = np.hstack([x_odd_even + factor * x_odd_odd, x_odd_even - factor * x_odd_odd])
        factor = np.exp(-2j * np.pi * np.arange(M) / M)
        result = np.vstack([even_part + factor[:, None] * odd_part, even_part - factor[:, None] * odd_part])
        
        return result

# Buat sinyal tes 2D
A = 5
N = 64
M = 64
x = np.zeros((N, M))
x[N // 4: 3 * N // 4, M // 4: 3 * M // 4] = 1

# Tampilkan FFT 2D
X = fft2d(x)

# Gunakan NumPy untuk validasi
X_numpy = np.fft.fft2(x)

# Plot sinyal origin
plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.imshow(x, cmap='gray', extent=(0, N, 0, M))
plt.title('Sinyal Origin')

# Plot sinyal FFT 2D
plt.subplot(132)
plt.imshow(np.abs(X), cmap='inferno', extent=(0, N, 0, M))
plt.title('Sinyal FFT 2D')

# Plot sinyal NumPy FFT 2D untuk validasi
plt.subplot(133)
plt.imshow(np.abs(X_numpy), cmap='inferno', extent=(0, N, 0, M))
plt.title('Sinyal NumPy FFT 2D')

plt.tight_layout()
plt.show()

print ("FFT 2D Graph and SourceCode")
print ("Hanin Ainussyamsi Prabowo")
print ("5009211036")