class KMP:
    def run(self, text, pattern):
        lps = [0] * len(pattern)  # Tabel LPS
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            lps[i] = j  # Perbarui LPS

        result = []
        i = j = 0
        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1
            if j == len(pattern):  # Pola ditemukan
                result.append(i - j)
                j = lps[j - 1]
            elif i < len(text) and text[i] != pattern[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return result  # Kembalikan hasil
