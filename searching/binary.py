class BinarySearch:
    def run(self, arr, target):
        target = int(target)
        
        # Mengubah setiap elemen dalam arr menjadi integer (jika arr berisi string atau nilai non-integer)
        arr = [int(x) for x in arr]

        # Inisialisasi variabel left dan right yang menunjukkan batas kiri dan kanan array
        left, right = 0, len(arr) - 1

        # Selama left tidak melewati right, lakukan pencarian
        while left <= right:
            # Tentukan indeks tengah dari array yang sedang diperiksa
            mid = (left + right) // 2
            
            # Jika elemen di tengah array sama dengan target, kembalikan posisi indeksnya
            if arr[mid] == target:
                return f"Target {target} found at index {mid}."
            
            # Jika elemen di tengah lebih kecil dari target, ubah batas kiri
            elif arr[mid] < target:
                left = mid + 1
            
            # Jika elemen di tengah lebih besar dari target, ubah batas kanan
            else:
                right = mid - 1
        
        # Jika pencarian selesai dan target tidak ditemukan, kembalikan pesan bahwa target tidak ada
        return f"Target {target} not found."



