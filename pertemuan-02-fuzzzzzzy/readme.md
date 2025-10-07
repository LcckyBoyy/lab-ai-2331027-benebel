## Penjelasan `tugas.ipynb` — Sistem Fuzzy Kontrol Intensitas Lampu

Notebook ini mendemonstrasikan penerapan logika fuzzy (Mamdani) menggunakan pustaka `scikit-fuzzy` untuk mengatur intensitas lampu berdasarkan dua input:

- Cahaya lingkungan (0–100)
- Jarak objek/sensor (0–100)

Output yang dihasilkan adalah tingkat intensitas lampu (0–100) beserta interpretasinya: MATI, REDUP, atau TERANG.

---

### Isi dan Alur Notebook

1. Import dan Setup

- `%matplotlib inline` untuk visualisasi di Jupyter.
- Import `numpy`, `matplotlib`, `scikit-fuzzy` (`skfuzzy`) dan modul kontrol (`skfuzzy.control as ctrl`).
- Penanganan opsional agar modul visualisasi `skfuzzy` mendeteksi `matplotlib` dengan benar.

2. Definisi Variabel Fuzzy

- Antecedent (input):
  - `cahaya`: 0–100
  - `jarak`: 0–100
- Consequent (output):
  - `lampu`: 0–100

3. Fungsi Keanggotaan (Membership Functions)

- Bentuk segitiga (`fuzz.trimf`):
  - `cahaya`: `gelap` [0, 0, 50], `sedang` [25, 50, 75], `terang` [50, 100, 100]
  - `jarak`: `dekat` [0, 0, 40], `sedang` [20, 50, 80], `jauh` [60, 100, 100]
  - `lampu`: `mati` [0, 0, 30], `redup` [20, 50, 80], `terang` [70, 100, 100]

4. Aturan Fuzzy (Rules)

- Jika `cahaya` gelap dan `jarak` dekat → `lampu` terang
- Jika `cahaya` gelap dan `jarak` jauh → `lampu` redup
- Jika `cahaya` sedang dan `jarak` dekat → `lampu` redup
- Jika `cahaya` terang → `lampu` mati

5. Sistem dan Simulasi

- Membangun `ControlSystem` dari aturan-aturan di atas dan menjalankan `ControlSystemSimulation`.

6. Contoh Input

- `cahaya = 70`
- `jarak = 5`

7. Hasil dan Interpretasi

- Menghitung output crisp `lampu` lalu menampilkan di konsol.
- Interpretasi:
  - `< 20` → MATI
  - `< 60` → REDUP
  - `>= 60` → TERANG

---

### Cara Menjalankan

1. Pastikan dependensi terpasang (direkomendasikan menggunakan virtual environment):

```powershell
# Dari folder root repo
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Buka VS Code dan jalankan notebook `tugas.ipynb`:

- Pastikan Kernel/Jupyter menggunakan interpreter dari `.venv` yang aktif.
- Jalankan sel dari atas ke bawah.

Catatan: Jika Anda hanya ingin memasang paket secara manual, paket inti yang dipakai adalah `numpy`, `matplotlib`, dan `scikit-fuzzy`.

---

### Eksperimen yang Disarankan

- Ubah nilai input `cahaya` dan `jarak` untuk melihat perubahan output.
- Sesuaikan bentuk/parameter membership function agar sesuai kebutuhan sistem nyata.
- Tambahkan atau modifikasi aturan untuk skenario yang lebih kompleks.

---

### Troubleshooting

- ModuleNotFoundError: `skfuzzy`
  - Pastikan environment aktif dan paket sudah terinstal: `pip install scikit-fuzzy`.
- Kernel tidak menampilkan paket yang sudah dipasang
  - Pilih ulang Python interpreter di VS Code ke `.venv` yang benar.
- Masalah visualisasi
  - Notebook sudah mencoba memuat ulang modul visualisasi `skfuzzy` jika `matplotlib` tidak terdeteksi; pastikan `matplotlib` terinstal.

---

### Lisensi

Konten ini untuk keperluan pembelajaran. Sesuaikan dan gunakan seperlunya dalam tugas atau proyek Anda.
