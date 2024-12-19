class QuickSelect:
    def quick_select(self, arr, left, right, k):
        arr = [int(x) for x in arr]  # Konversi elemen menjadi integer
        k = int(k)  # Pastikan k adalah integer

        if left == right:  # Hanya ada satu elemen
            return arr[left]

        pivot_index = self.partition(arr, left, right)  # Pisahkan array dengan pivot
        
        if k == pivot_index:  # Elemen ke-k ditemukan
            return arr[k]
        elif k < pivot_index:  # Cari di kiri pivot
            return self.quick_select(arr, left, pivot_index - 1, k)
        else:  # Cari di kanan pivot
            return self.quick_select(arr, pivot_index + 1, right, k)

    def partition(self, arr, left, right):
        pivot = arr[right]  # Pilih pivot
        i = left
        for j in range(left, right):  # Pisahkan berdasarkan pivot
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[right] = arr[right], arr[i]  # Tempatkan pivot
        return i  # Kembalikan indeks pivot

    def run(self, arr, k):
        arr = [int(x) for x in arr]  # Konversi elemen menjadi integer
        k = int(k)  # Pastikan k adalah integer
        if k < 1 or k > len(arr):  # Periksa validitas k
            raise ValueError(f"k harus berada dalam rentang 1 hingga {len(arr)}")
        return self.quick_select(arr, 0, len(arr) - 1, k - 1)  # Panggil quick_select
