def knapsack_dp(capacity, weights, values, n):
    # Membuat tabel DP (K) untuk menyimpan hasil sub-masalah
    # Baris merepresentasikan item (0..n), Kolom merepresentasikan kapasitas (0..M)
    K = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
    
    # Membangun tabel K secara bottom-up
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i-1] <= w:
                # Max dari (Nilai barang ini + nilai sisa kapasitas) ATAU (Nilai tanpa barang ini)
                K[i][w] = max(values[i-1] + K[i-1][w-weights[i-1]], K[i-1][w])
            else:
                # Jika berat barang lebih besar dari kapasitas saat ini, jangan ambil
                K[i][w] = K[i-1][w]
    
    # Menemukan nilai maksimum
    max_value = K[n][capacity]
    
    # Backtracking untuk menemukan item mana yang dipilih
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if K[i][w] != K[i-1][w]:
            # Item i-1 dimasukkan
            selected_items.append(i) # Simpan nomor item (indeks 1-based)
            w -= weights[i-1]
            
    return max_value, selected_items

# DATA KASUS (Security Network Kit)
# Kapasitas Tas
M = 40 

# Data Item (Berat, Profit)
items = [
    (12, 60), # 1. Server Node
    (5, 40),  # 2. Forensic Laptop
    (8, 35),  # 3. Firewall
    (2, 20),  # 4. Net Tap
    (4, 25),  # 5. HDD Array
    (10, 15), # 6. UPS
    (3, 30),  # 7. Jammer
    (2, 18),  # 8. IoT Kit
    (5, 10),  # 9. Kabel
    (1, 5)    # 10. Cooling Pad
]

weights = [item[0] for item in items]
values = [item[1] for item in items]
n = len(items)

print("--- HASIL IMPLEMENTASI 0/1 KNAPSACK DP ---")
print(f"Kapasitas Maksimum: {M} kg")
print(f"Jumlah Item Tersedia: {n}")

max_profit, picked_indices = knapsack_dp(M, weights, values, n)

print(f"\nNilai Maksimum (Profit): {max_profit}")
print("Daftar Item Terpilih:")

total_weight = 0
picked_indices.sort()
for idx in picked_indices:
    real_idx = idx - 1
    w = weights[real_idx]
    v = values[real_idx]
    total_weight += w
    print(f"- Item {idx} (Berat: {w}, Nilai: {v})")

print(f"Total Berat: {total_weight} kg")