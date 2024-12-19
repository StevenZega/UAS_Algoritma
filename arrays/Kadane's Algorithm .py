# Kadane's Algorithm: Mencari Jumlah Subarray Maksimum
def kadane_algorithm(self, arr):
    # Inisialisasi nilai saat ini dan nilai maksimum global
    max_current = max_global = arr[0]
    
    # Iterasi mulai dari elemen kedua hingga akhir array
    for i in range(1, len(arr)):
        # Menentukan nilai maksimum saat ini: antara elemen arr[i] atau penambahan elemen tersebut ke subarray sebelumnya
        max_current = max(arr[i], max_current + arr[i])
        
        # Memperbarui nilai maksimum global jika nilai saat ini lebih besar
        if max_current > max_global:
            max_global = max_current
    
    # Mengembalikan nilai subarray maksimum yang ditemukan
    return max_global
