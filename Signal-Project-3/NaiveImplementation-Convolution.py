import matplotlib.pyplot as plt
import numpy as np

def convolve(Signal_1, Signal_2):
    # Hitung panjang sinyal yang dihasilkan
    length = len(Signal_1) + len(Signal_2) - 1
    # Inisialisasi sinyal yang dihasilkan dengan nol
    result = [0] * length
 
    # Lakukan operasi konvolusi
    for i in range(length):
        for j in range(len(Signal_1)):
            if i - j >= 0 and i - j < len(Signal_2):
                result[i] += Signal_1[j] * Signal_2[i - j]
    return result
# Uji fungsi di atas dengan menggunakan dua sinyal
Signal_1 = [1, 3, 5]
Signal_2 = [2, 4, 6]
result = convolve(Signal_1, Signal_2)
print(result)
# Validasi hasilnya menggunakan NumPy Convolve
np_result = np.convolve(Signal_1, Signal_2)
print(np_result)
# Plot hasil dari fungsi konvolusi
plt.plot(Signal_1, label='Signal 1')
plt.plot(Signal_2, label='Signal 2')
plt.plot(result, label='Convolution Result')
plt.plot(np_result, label='NumPy Convolution Result')
plt.legend()
plt.show()