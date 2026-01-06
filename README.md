# Tugas Analisis & Implementasi Algoritma: 0/1 Knapsack Problem

Repositori ini berisi penyelesaian masalah optimasi **0/1 Knapsack Problem** menggunakan pendekatan algoritma **Dynamic Programming**. Proyek ini disusun untuk memenuhi tugas mata kuliah Analisis Algoritma.

## 📋 Deskripsi Masalah (Studi Kasus)
**Topik:** Network Forensics Kit Optimization

Seorang spesialis keamanan jaringan harus memilih peralatan forensik prioritas untuk dimasukkan ke dalam tas dengan **Kapasitas Maksimal 40 Kg**. Terdapat **10 Item** yang tersedia, masing-masing memiliki bobot (*weight*) dan nilai kegunaan (*profit*). Tujuannya adalah mendapatkan total profit maksimal tanpa melebihi kapasitas tas.

**Data Kasus:**
| No | Nama Item | Berat (kg) | Profit |
| :-- | :--- | :--- | :--- |
| 1 | High-Performance Server Node | 12 | 60 |
| 2 | Forensic Workstation Laptop | 5 | 40 |
| 3 | Hardware Firewall Appliance | 8 | 35 |
| 4 | Network Tap & Packet Analyzer | 2 | 20 |
| 5 | External HDD Array (Evidence) | 4 | 25 |
| 6 | UPS Unit (Portable) | 10 | 15 |
| 7 | Wireless Signal Jammer | 3 | 30 |
| 8 | IoT Analysis Kit | 2 | 18 |
| 9 | Kabel & Switch Kit | 5 | 10 |
| 10 | Cooling Pad & Accessories | 1 | 5 |

## 🚀 Pendekatan Algoritma
Solusi diimplementasikan menggunakan **Dynamic Programming (DP)** dengan karakteristik:
* **Time Complexity:** $O(n \times W)$
* **Metode:** Membangun tabel solusi secara *bottom-up* untuk menyimpan hasil sub-masalah, sehingga menjamin solusi optimal global.
* **Fitur Program:**
    * Menghitung Nilai Profit Maksimum.
    * Melacak item mana saja yang dipilih (Backtracking solusi).
    * Menampilkan total berat akhir.

## 🛠️ Cara Menjalankan Program
Pastikan Python sudah terinstal di komputer Anda.

1.  Clone repositori ini:
    ```bash
    git clone (https://github.com/EkoPrasetyoAdiNugroho/TUGAS-ANALISIS-IMPLEMENTASI-ALGORITMA)
    ```
2.  Masuk ke direktori project:
    ```bash
    cd kode
    ```
3.  Jalankan file Python:
    ```bash
    python SourceCode.py
    ```

## 👥 Anggota Kelompok
**Kelas:** 5 JK-A  
**Program Studi:** Informatika / Ilmu Komputer

1.  **Eko Prasetyo Adi Nugroho** (NIM: 105841114223)
2.  **Alamsyah Sahlan** (NIM: 105841114223)

---
**Catatan:**
Implementasi ini juga menyertakan analisis teoritis menggunakan *State Space Tree* (Pohon Ruang Status) untuk memvisualisasikan langkah pengambilan keputusan hingga Level 4.
