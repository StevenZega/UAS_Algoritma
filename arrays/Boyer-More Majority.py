class BoyerMoore:
    def run(self, text, pattern):
        # Mengambil panjang dari pola (pattern) dan teks (text)
        m, n = len(pattern), len(text)
        
        # Jika panjang pola lebih besar dari teks, tidak ada kemungkinan ditemukan, kembalikan list kosong
        if m > n:
            return []
        
        def build_bad_char_table(pattern):
            # Membuat tabel Bad Character untuk algoritma Boyer-Moore
            table = {}
            for i in range(m):
                table[pattern[i]] = i  # Simpan posisi terakhir dari setiap karakter dalam pola
            return table
        
        def boyer_moore(text, pattern):
            # Fungsi utama algoritma Boyer-Moore untuk mencari pola dalam teks
            table = build_bad_char_table(pattern)  # Bangun tabel Bad Character
            i = 0  # Indeks untuk teks
            result = []  # List untuk menyimpan posisi indeks yang cocok dengan pola
            while i <= n - m:
                j = m - 1  # Mulai pengecekan dari karakter terakhir pola
                while j >= 0 and pattern[j] == text[i + j]:
                    # Cek apakah karakter dalam pola dan teks cocok
                    j -= 1
                if j < 0:
                    # Jika seluruh pola cocok, simpan posisi indeks i ke dalam result
                    result.append(i)
                    i += m  # Geser pola sepanjang panjang pola
                else:
                    # Jika tidak cocok, geser pola berdasarkan tabel Bad Character
                    i += max(1, j - table.get(text[i + j], -1))
            return result
        
        # Kembalikan hasil dari pencarian pola dalam teks
        return boyer_moore(text, pattern)
