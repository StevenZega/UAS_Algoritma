class Huffman:
    def run(self, data):
        # Simplified Huffman algorithm for illustration
        freq = {}
        for char in data:
            freq[char] = freq.get(char, 0) + 1
        # Return a simplified frequency dictionary
        return freq
