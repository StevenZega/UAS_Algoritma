class Kadane:
    def run(self, arr):
        # Inisialisasi nilai maksimum global dan lokal dengan elemen pertama array
        max_sum = current_sum = arr[0]
        for num in arr[1:]:  # Iterasi dimulai dari elemen kedua
            # Perbarui jumlah maksimum lokal (apakah menambahkan elemen baru atau mulai dari elemen baru)
            current_sum = max(num, current_sum + num)
            # Perbarui jumlah maksimum global jika diperlukan
            max_sum = max(max_sum, current_sum)
        return max_sum  # Kembalikan jumlah maksimum
