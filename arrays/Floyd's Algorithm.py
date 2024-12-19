# Deteksi siklus menggunakan algoritma Floyd (Tortoise and Hare)
def floyds_cycle_detection(self, head):
    slow = head  # Pointer lambat
    fast = head  # Pointer cepat

    while fast and fast.next:  # Selama fast valid
        slow = slow.next  # Lambat maju 1 langkah
        fast = fast.next.next  # Cepat maju 2 langkah

        if slow == fast:  # Jika bertemu, ada siklus
            return True
    
    return False  # Tidak ada siklus
