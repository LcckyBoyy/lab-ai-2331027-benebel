# Prediksi Harga Smartphone (`kelas.ipynb`)

Notebook ini membangun model regresi linear untuk memprediksi harga smartphone berdasarkan spesifikasi seperti penyimpanan, RAM, ukuran layar, kamera, baterai, dan merek. Dataset sumber ada di `data-smartphone.csv` pada folder yang sama.

## Tujuan

- Membersihkan dan menyiapkan data smartphone untuk analisis.
- Eksplorasi data (EDA) untuk memahami distribusi dan hubungan antar fitur.
- Membangun model `LinearRegression` (scikit-learn) dengan normalisasi fitur.
- Mengevaluasi performa model dengan MSE, MAE, RMSE, dan R².
- Menyediakan fungsi praktis untuk memprediksi harga berdasarkan spesifikasi yang diberikan.

## Dataset

- File: `pertemuan-03/data-smartphone.csv`
- Kolom yang digunakan (beberapa dibersihkan/diubah tipe):
  - `Price ($)` (string → int64): hapus simbol `$`, koma, spasi.
  - `Storage ` (string → int64): hapus `GB` dan spasi. (Perhatikan ada spasi di nama kolom sumber)
  - `RAM ` (string → int64): hapus `GB` dan spasi. (Perhatikan ada spasi di nama kolom sumber)
  - `Screen Size (inches)` (string → float): hapus teks seperti ` (unfolded)` dan ambil angka sebelum tanda `+`.
  - `Camera (MP)` (string → int64): hapus `MP`, `3D`, huruf/spasi/tanda, pecah dengan `+`, konversi ke angka, ambil nilai maksimum.
  - `Battery Capacity (mAh)` (numeric)
  - `Brand` (kategorikal → one-hot encoding)
  - `Model` (di-drop sebelum pemodelan)

## Alur Notebook

1. Load data (`pandas.read_csv`).
2. Pemeriksaan awal: dimensi, tipe data, nilai hilang, duplikasi.
3. Pembersihan kolom string → numerik (lihat bagian Dataset di atas).
4. EDA (opsional namun tersedia di notebook):
   - Distribusi merek (`value_counts` + bar chart)
   - Boxplot per fitur per `Brand`
   - Scatter `Price ($)` vs fitur numerik (dengan hue `Brand`)
   - Heatmap korelasi fitur numerik
5. Pra-pemrosesan:
   - Drop `Model`
   - One-Hot Encoding `Brand` → `Brand_Apple`, `Brand_Samsung`, dst.
   - Skala fitur dengan `MinMaxScaler` (hanya X/fitur, bukan target)
6. Split data: `train_test_split(test_size=0.3, random_state=42)`
7. Pelatihan model: `LinearRegression()`
8. Evaluasi: MSE, MAE, RMSE, R² + scatter plot Harga Asli vs Prediksi
9. Prediksi contoh: membuat `new_data` dan memprediksi harga
10. Fungsi utilitas `predict_phone_price(...)` untuk prediksi mudah

## Dependensi

Minimal paket yang diperlukan:

- Python 3.10+
- jupyter
- numpy, pandas
- matplotlib, seaborn
- scikit-learn

Anda juga dapat memakai `requirements.txt` di root repo untuk lingkungan yang persis.

### Instalasi cepat (Windows PowerShell)

```powershell
# (opsional) buat virtual environment
python -m venv .venv; .\.venv\Scripts\Activate.ps1

# instal minimal dependensi
pip install jupyter numpy pandas matplotlib seaborn scikit-learn

# atau gunakan requirements yang disertakan di repo (opsional)
pip install -r ..\requirements.txt
```

## Cara Menjalankan

1. Pastikan file `data-smartphone.csv` ada di folder `pertemuan-03/`.
2. Buka `pertemuan-03/kelas.ipynb` di Jupyter/VS Code.
3. Jalankan sel-sel dari atas ke bawah:
   - Bagian pembersihan data harus dijalankan sebelum EDA.
   - Bagian scaling + split harus dijalankan sebelum pelatihan model.
   - Jalankan sel evaluasi untuk melihat metrik dan plot.
   - Jalankan sel prediksi contoh atau pakai fungsi utilitas di bawah.

## Fungsi Prediksi

Notebook menyediakan fungsi berikut untuk prediksi cepat:

```python
predict_phone_price(
    brand="Apple",     # salah satu dari Brand_*
    storage=256,        # GB
    ram=8,              # GB
    camera=108,         # MP (nilai maksimum jika multi-kamera)
    screen_size=6.8,    # inches
    battery=5000        # mAh
)
```

Fungsi akan:

- Menyusun baris data dengan one-hot brand sesuai pilihan.
- Menerapkan skala yang sama (scaler yang sudah fit pada data latih).
- Mengembalikan prediksi harga dalam USD dan menampilkannya.

## Output yang Dihasilkan

- Metrik evaluasi (dicetak di output sel):
  - MSE, MAE, RMSE, R²
- Visualisasi:
  - Scatter Harga Asli vs Prediksi dengan garis diagonal referensi
  - (Opsional) Bar chart merek, boxplot, scatter fitur vs harga, heatmap korelasi

## Catatan & Troubleshooting

- Jika plot tidak muncul, pastikan sel matplotlib/seaborn dijalankan setelah data siap.
- Jika terjadi `KeyError` pada kolom, cek kembali nama kolom di CSV (beberapa memiliki spasi di akhir: `Storage `, `RAM `).
- Pastikan menjalankan sel pembersihan `Camera (MP)` sebelum konversi ke int agar formatnya konsisten.
- Untuk prediksi menggunakan fungsi, jalankan terlebih dahulu sel yang melatih model dan mendefinisikan `scaler`, `x`, `brand_list`, dan `predict_phone_price`.

## Ide Pengembangan Lanjutan

- Simpan model dan scaler (joblib) untuk inferensi di luar notebook.
- Coba model lain (Ridge/Lasso/RandomForest/XGBoost) dan lakukan tuning hyperparameter.
- Tambahkan validasi silang dan pipeline preprocessing terintegrasi (`sklearn.pipeline`).
