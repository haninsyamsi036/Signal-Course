# Signal Project 3

## Naive Implementation of Convolution
   ### Original Phyton Script 
    def convolve(Signal_1, Signal_2):
    #Hitung panjang sinyal yang dihasilkan
    length = len(Signal_1) + len(Signal_2) - 1
    # Inisialisasi sinyal yang dihasilkan dengan nol
    result = [0] * length
 
    #Lakukan operasi konvolusi
    for i in range(length):
        for j in range(len(Signal_1)):
            if i - j >= 0 and i - j < len(Signal_2):
                result[i] += Signal_1[j] * Signal_2[i - j]
    return result

    print ("Naive Impelementation of Convolution")
    print ("Hanin Ainussyamsi Prabowo")
    print ("5009211036")

    #Uji fungsi di atas dengan menggunakan dua sinyal
    Signal_1 = [1, 3, 5, 7]
    Signal_2 = [2, 4, 6, 8]
    result = convolve(Signal_1, Signal_2)
    print(result)
      
### Result      
![NaiveImplementation-Convolution](https://github.com/haninsyamsi036/Signal-Course/assets/144574915/a29529d5-8983-4aae-a799-f18ebe5de8d8)

### Description
Pada kode ini, fungsi `convolve` mengambil dua sinyal larik 1 dimensi sebagai masukan. Fungsi ini menghitung panjang sinyal yang dihasilkan dan menginisialisasinya dengan angka nol. Kemudian, fungsi ini melakukan operasi konvolusi dengan mengulangi elemen-elemen sinyal input dan mengalikannya bersama-sama. Hasil dari setiap perkalian ditambahkan ke posisi yang sesuai dalam sinyal yang dihasilkan. Terakhir, fungsi mengembalikan sinyal yang dihasilkan. Dalam kasus ini menggunakan dua sinyal dengan nilai integer. Sinyal yang dihasilkan dihitung dengan mengalikan dua sinyal input. Keluaran dari kode adalah sinyal yang dihasilkan.

Untuk memvalidasi hasilnya, saya menggunakan NumPy Convolve. Keluaran dari NumPy Convolve harus sama dengan keluaran dari fungsi `convolve`. Jika tidak sama, hal ini mengindikasikan adanya kesalahan dalam implementasi. Jika sinyal input tidak memiliki tipe yang sesuai, kode akan gagal.
