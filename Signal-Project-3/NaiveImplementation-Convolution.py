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

print ("Naive Impelementation of Convolution")
print ("Hanin Ainussyamsi Prabowo")
print ("5009211036")

# Uji fungsi di atas dengan menggunakan dua sinyal
Signal_1 = [1, 3, 5, 7]
Signal_2 = [2, 4, 6, 8]
result = convolve(Signal_1, Signal_2)
print(result)