import math
import matplotlib.pyplot as plt

# Definisikan Fungsi x(t)
def x(t, A):
    if -A/2 <= t <= A/2:
        return 1
    else:
        return 0

# Definisikan Fungsi Transformasi Fourier
def fourier_transform(x, A, w):
    integral_real = 0
    integral_imag = 0
    # Perbedaan Selisih t Untuk Integrasi Numerik
    delta_t = 0.0001  
    t_values = [i * delta_t for i in range(int(-A/delta_t), int(A/delta_t)+1)]

    for t in t_values:
        integral_real += x(t, A) * math.cos(-w * t)
        integral_imag += x(t, A) * math.sin(-w * t)

    return integral_real, integral_imag

A = 1
# Nilai Frekuensi w
w_values = [i * 0.001 for i in range(-10000, 10000)]

# Hitung Fourier Transform untuk tiap Frekuensi
ft_values = [fourier_transform(x, A, w) for w in w_values]

# Ekstrak FT untuk Integral Real
real_part = [ft[0] for ft in ft_values]

# Plot fungsi origin
plt.subplot(4, 1, 1)
t_values = [i * 0.001 for i in range(int(-A/0.001), int(A/0.001)+1)]
x_values = [x(t, A) for t in t_values]
plt.plot(t_values, x_values)
plt.title('Fungsi Origin x(t)')
plt.grid()

# Plot Fungsi Transformasi Fourier
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(w_values, real_part)
plt.title('Fungsi Transformasi Fourier X(w)')
plt.grid()

plt.tight_layout()
plt.show()

print ("Manual Graph & Source Code 1B")
print ("Hanin Ainussyamsi Prabowo")
print ("5009211036")