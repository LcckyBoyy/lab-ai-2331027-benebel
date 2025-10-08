# Fuzzy Logic: Pengaturan Intensitas Lampu (`lampu.ipynb`)

Dokumen ini menjelaskan notebook `lampu.ipynb` yang mengatur intensitas lampu menggunakan logika fuzzy (scikit-fuzzy) berdasarkan dua masukan: tingkat cahaya lingkungan dan jarak objek. Notebook juga menghasilkan dataset contoh hasil inferensi ke file `dataset_fuzzy_lampu.csv`.

## Ringkasannya

- Masukan (input):
  - Cahaya (0–100)
  - Jarak (0–100)
- Keluaran (output):
  - Intensitas Lampu (0–100), beserta kategori: Rendah, Sedang, Tinggi
- Metode: Fuzzy Inference System (Mamdani) dengan fungsi keanggotaan (membership functions) dan basis aturan, defuzzifikasi menggunakan centroid.
- Artefak utama: `lampu.ipynb`, `dataset_fuzzy_lampu.csv`

## Data

- `dataset_fuzzy_lampu.csv` berisi contoh pasangan input dan hasil inferensi:
  - Kolom: `Cahaya`, `Jarak`, `Intensitas Lampu`, `Kategori Lampu`
  - Nilai contoh:
    - 51, 92 → 80.69 (Tinggi)
    - 82, 86 → 18.25 (Rendah)
    - 32, 75 → 62.52 (Sedang)

Catatan: Nilai input berada pada rentang 0–100. Output kontinu (0–100) dan juga dipetakan ke label kategori untuk memudahkan interpretasi.

## Desain Sistem Fuzzy (gambaran umum)

- Variabel input:
  - Cahaya: Rendah, Sedang, Tinggi (rentang semesta ~0–100)
  - Jarak: Dekat, Sedang, Jauh (rentang semesta ~0–100)
- Variabel output:
  - Intensitas Lampu: Rendah, Sedang, Tinggi (0–100)
- Fungsi keanggotaan: segitiga/trapesium standar pada rentang 0–100 (detail dan visualisasi ada di sel-sel plotting pada notebook).
- Basis aturan: kombinasi logis antara (Cahaya x Jarak) → Intensitas (contoh: jika Cahaya tinggi maka Intensitas cenderung rendah, dst). Aturan lengkap dapat dilihat/dimodifikasi pada sel “definisi aturan” di notebook.
- Defuzzifikasi: metode centroid untuk menghasilkan nilai intensitas akhir.

## Kebutuhan/Dependensi

Minimal paket yang digunakan oleh notebook:

- Python 3.10+
- jupyter
- numpy, pandas, matplotlib
- scikit-fuzzy

Repositori ini sudah menyediakan `requirements.txt` dengan pin versi. Anda bisa menggunakan itu untuk reproduksi persis (opsional).

Opsional (Windows PowerShell) untuk membuat environment dan instalasi:

```powershell
# (opsional) buat virtual environment
python -m venv .venv; .\.venv\Scripts\Activate.ps1

# instal minimal dependensi
pip install jupyter numpy pandas matplotlib scikit-fuzzy

# atau instal sesuai requirements yang disertakan
pip install -r requirements.txt
```

## Cara Menjalankan

1. Buka notebook `pertemuan-02-fuzzzzzzy/lampu.ipynb` di Jupyter/VS Code.
2. Jalankan sel-sel secara berurutan dari atas ke bawah.
3. Notebook akan:
   - Mendefinisikan semesta pembicaraan dan membership functions.
   - Menetapkan aturan fuzzy dan melakukan inferensi.
   - Mem-plot fungsi keanggotaan/hasil (jika diaktifkan di sel visualisasi).
   - Menyimpan hasil contoh ke `dataset_fuzzy_lampu.csv` (jika sel ekspor dijalankan).

## Hasil & Output

- File `dataset_fuzzy_lampu.csv` (contoh hasil inferensi kumpulan pasangan (Cahaya, Jarak)).
- Visualisasi membership dan/atau permukaan kontrol (plots) di output sel notebook.
- Nilai Intensitas Lampu kontinu serta label kategori:
  - Rendah ≈ nilai kecil (mis. ~15–30)
  - Sedang ≈ nilai menengah (mis. ~35–65)
  - Tinggi ≈ nilai besar (mis. ~70–85)

Rentang di atas bersifat indikatif berdasar sampel output; batas pasti mengikuti setup membership dan aturan pada notebook Anda.

## Kustomisasi

- Ubah bentuk/rentang membership di sel definisi variabel fuzzy untuk menyesuaikan domain (mis. ubah batas 0–100).
- Tambahkan/ubah aturan fuzzy pada sel basis aturan untuk mencerminkan logika yang diinginkan.
- Atur metode defuzzifikasi (default: centroid) di bagian inferensi jika diperlukan.

## Troubleshooting

- Jika grafik tidak muncul, pastikan sel plotting dijalankan setelah definisi membership.
- Jika paket tidak ditemukan, aktifkan environment yang benar dan jalankan instalasi dependensi.
- Jika `dataset_fuzzy_lampu.csv` tidak terbentuk, jalankan sel ekspor/penyimpanan di bagian akhir notebook.

---

Untuk contoh fuzzy lain dalam folder ini, lihat juga `fuzzy.ipynb`.
