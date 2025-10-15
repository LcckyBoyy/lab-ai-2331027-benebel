## Prediksi Harga Smartphone — Pertemuan 03

Notebook dan artefak di folder ini membangun model regresi untuk memprediksi harga smartphone berdasarkan spesifikasi seperti penyimpanan, RAM, ukuran layar, kamera, baterai, dan merek. Dataset sumber ada di `data-smartphone.csv` pada folder yang sama.

### Struktur Folder

- `latihan.ipynb` — notebook utama: pembersihan data, EDA, pelatihan, evaluasi, dan prediksi contoh.
- `data-smartphone.csv` — dataset mentah.
- `smartphone_price_model.joblib` — model tersimpan (opsional; akan ada setelah Anda menyimpannya dari notebook atau sudah disediakan).
- `requirements.txt` — daftar dependensi untuk lingkungan pertemuan ini.

---

## Tujuan

- Membersihkan dan menyiapkan data smartphone untuk analisis.
- Eksplorasi data (EDA) untuk memahami distribusi dan hubungan antar fitur.
- Membangun model regresi (contoh: `LinearRegression` pada scikit-learn) dengan normalisasi fitur.
- Mengevaluasi performa model dengan MSE, MAE, RMSE, dan R².
- Menyediakan cara memuat model tersimpan dan melakukan prediksi cepat.

## Dataset & Pembersihan

- File: `pertemuan-03/data-smartphone.csv`
- Kolom yang digunakan (beberapa dibersihkan/diubah tipe):
  - `Price ($)` (string → int64): hapus simbol `$`, koma, spasi.
  - `Storage ` (string → int64): hapus `GB` dan spasi. (Perhatikan ada spasi di nama kolom sumber)
  - `RAM ` (string → int64): hapus `GB` dan spasi. (Perhatikan ada spasi di nama kolom sumber)
  - `Screen Size (inches)` (string → float): hapus teks seperti ` (unfolded)` dan ambil angka sebelum tanda `+`.
  - `Camera (MP)` (string → numerik): hapus `MP`, `3D`, huruf/spasi/tanda, pecah dengan `+`, konversi ke angka, ambil nilai maksimum.
  - `Battery Capacity (mAh)` (numerik)
  - `Brand` (kategorikal → one-hot encoding)
  - `Model` (umumnya di-drop sebelum pemodelan)

---

## Instalasi (Windows PowerShell)

Direkomendasikan menggunakan virtual environment lokal di folder repo.

```powershell
# Dari folder pertemuan-03
python -m venv .venv; .\.venv\Scripts\Activate.ps1

# Opsi A: install sesuai daftar dependensi folder ini
pip install -r .\requirements.txt

# Opsi B: install minimal paket yang diperlukan
pip install jupyter numpy pandas matplotlib seaborn scikit-learn
```

Catatan: `requirements.txt` di folder ini memuat paket lengkap (cukup besar). Jika hanya ingin menjalankan analisis dasar, opsi B biasanya sudah cukup.

---

## Cara Menjalankan Notebook

1. Pastikan file `data-smartphone.csv` ada di folder `pertemuan-03/`.

2. Buka `latihan.ipynb` di VS Code (Notebook) atau Jupyter Lab/Notebook, lalu pilih kernel Python dari `.venv` yang Anda aktifkan.

3. Jalankan sel-sel secara berurutan:
   - Pembersihan data harus dijalankan sebelum EDA.
   - Langkah scaling + split data harus dijalankan sebelum pelatihan model.
   - Jalankan evaluasi untuk melihat MSE/MAE/RMSE/R² dan plot.
   - (Opsional) Simpan model menjadi `.joblib` untuk dipakai ulang.

---

## Menggunakan Model Tersimpan (`.joblib`)

Jika `smartphone_price_model.joblib` berisi Pipeline (preprocessing + model), Anda bisa langsung memuat dan memprediksi:

```python
import joblib
import pandas as pd

# muat pipeline
pipe = joblib.load('pertemuan-03/smartphone_price_model.joblib')

# contoh satu baris data (sesuaikan kolom sesuai yang dipakai saat training)
sample = pd.DataFrame([
    {
        'Storage': 256,            # GB
        'RAM': 8,                  # GB
        'Screen Size (inches)': 6.8,
        'Camera (MP)': 108,
        'Battery Capacity (mAh)': 5000,
        'Brand': 'Apple'           # akan di-one-hot oleh pipeline jika sudah termasuk encoder
    }
])

pred = pipe.predict(sample)[0]
print(f"Prediksi harga (USD): {pred:.2f}")
```

Jika file `.joblib` hanya berisi model tanpa preprocessing, jalankan notebook untuk membangun kembali tahap preprocessing (encoder/scaler) dan pastikan urutan/skalanya sama sebelum memanggil `model.predict(...)`.

---

## Output yang Dihasilkan

- Metrik evaluasi: MSE, MAE, RMSE, R².
- Visualisasi: scatter Harga Asli vs Prediksi dengan garis referensi diagonal, dan (opsional) bar chart merek, boxplot, scatter fitur vs harga, heatmap korelasi.

---

## Troubleshooting

- KeyError pada kolom CSV:
  - Beberapa kolom punya spasi di akhir nama: `Storage `, `RAM `. Sesuaikan penanganannya di kode pembersihan.
- Paket tidak ditemukan saat import:
  - Pastikan `.venv` aktif dan dependensi terinstal. Ulangi aktivasi: `.\.venv\Scripts\Activate.ps1`.
- Versi scikit-learn/joblib berbeda saat memuat `.joblib`:
  - Jika muncul error unpickling/compatibility, jalankan ulang training di notebook lalu simpan ulang model.
- Plot tidak muncul:
  - Pastikan sel visualisasi dijalankan setelah data bersih dan tersedia.

---

## Ide Lanjutan

- Simpan pipeline lengkap (preprocessing + estimator) agar prediksi ulang lebih mudah dan konsisten.
- Coba model lain (Ridge/Lasso/RandomForest/XGBoost) dan lakukan tuning hyperparameter.
- Tambahkan validasi silang dan pipeline `sklearn.pipeline` yang terintegrasi.
