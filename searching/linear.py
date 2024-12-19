class LinearSearch:
    def run(self, arr, target):
        for i, val in enumerate(arr):  # Iterasi melalui setiap elemen dalam array
            if val == target:   # Jika sama dengan target, kembalikan indeks elemen tersebut
                return i
        return -1  # Jika target tidak ditemukan, kembalikan -1
