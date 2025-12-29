import time
import matplotlib.pyplot as plt

# ====================
# Faktorial Rekursif
# ====================
def faktorial_rekursif(n):
    if n <= 1:
        return 1
    return n * faktorial_rekursif(n - 1)

# ====================
# Faktorial Iteratif
# ====================
def faktorial_iteratif(n):
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil

# ====================
# Main Program
# ====================
n_max = int(input("Masukkan nilai n maksimum : "))
step = int(input("Masukkan step kenaikan n : "))
ulang = 100000  # pengulangan agar waktu terukur

data_n = []
waktu_iteratif = []
waktu_rekursif = []

print("\n n | Iteratif (ns) | Rekursif (ns)")
print("----------------------------------")

for n in range(step, n_max + 1, step):
    # Iteratif
    start = time.perf_counter_ns()
    for _ in range(ulang):
        faktorial_iteratif(n)
    end = time.perf_counter_ns()
    iter_ns = (end - start) // ulang

    # Rekursif
    start = time.perf_counter_ns()
    for _ in range(ulang):
        faktorial_rekursif(n)
    end = time.perf_counter_ns()
    rek_ns = (end - start) // ulang

    data_n.append(n)
    waktu_iteratif.append(iter_ns)
    waktu_rekursif.append(rek_ns)

    print(f"{n:2} | {iter_ns:12} | {rek_ns:12}")

# ====================
# Grafik
# ====================
plt.plot(data_n, waktu_iteratif, marker='o', label='Iteratif')
plt.plot(data_n, waktu_rekursif, marker='o', label='Rekursif')

plt.xlabel('Nilai n')
plt.ylabel('Waktu Eksekusi (ns)')
plt.title('Perbandingan Waktu Eksekusi Faktorial')
plt.legend()
plt.grid(True)

plt.show()
