class Euclid:
    def run(self, a, b):
        # Pastikan bahwa a dan b adalah integer
        a = int(a)
        b = int(b)
        
        # Algoritma Euclidean untuk GCD
        while b != 0:
            a, b = b, a % b
        
        return f"GCD is {a}"