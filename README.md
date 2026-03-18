# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
Jaya Jaya Institut menghadapi tantangan besar dalam mempertahankan mahasiswa hingga lulus. Setiap mahasiswa yang dropout berarti:
-  Penurunan Reputasi angka kelulusan yang rendah dapat mempengaruhi akreditasi dan minat calon mahasiswa baru.
-  Banyak mahasiswa yang berhenti kuliah bukan karena kemampuan akademik, melainkan karena kendala ekonomi.

### Cakupan Proyek
Proyek ini mencakup pengembangan sistem prediksi dan pemantauan kelulusan mahasiswa yang terdiri dari beberapa tahapan utama:

1. Eksplorasi & Analisis Data (EDA)
  -  Melakukan pembersihan data (data cleaning) pada dataset mahasiswa Jaya Jaya Institut.

  -  Menganalisis korelasi antara faktor demografi, ekonomi, dan akademik terhadap status kelulusan.

  -  Visualisasi distribusi data untuk memahami karakteristik mahasiswa yang berisiko dropout.

2. Rekayasa Fitur (Feature Engineering)
  -  Pembuatan fitur baru untuk meningkatkan akurasi model, antara lain:

  -  Financial_High_Risk: Identifikasi risiko keuangan (gabungan status hutang dan pelunasan UKT).

  -  Academic_Success_Rate: Rata-rata tingkat keberhasilan unit mata kuliah.

  -  Grade_Trend: Analisis kenaikan atau penurunan nilai antar semester.

  -  Transformasi data (Encoding & Scaling) agar siap diproses oleh algoritma Machine Learning.

3. Pengembangan Model Prediksi
  -  Penerapan algoritma Logistic Regression (atau algoritma klasifikasi lainnya) untuk memprediksi status mahasiswa: Dropout, Enrolled, atau Graduate.

  -  Penanganan ketidakseimbangan data (class imbalance) menggunakan teknik seperti SMOTE (jika diperlukan).

  -  Evaluasi performa model menggunakan metrik Accuracy, Precision, Recall, dan F1-Score.

4. Pengembangan Prototype Aplikasi (Deployment)
  -  Membangun antarmuka berbasis web menggunakan Streamlit.

  -  Menyediakan fitur input data mahasiswa dengan standar IPK Indonesia (0.0 - 4.0).

  -  Sistem memberikan output berupa prediksi status beserta rekomendasi tindakan strategis bagi pihak kampus.

5. Dashboard Monitoring Business Intelligence
  -  Penyediaan dataset yang telah diproses untuk kebutuhan pelaporan manajemen.

  -  Pembuatan dashboard interaktif menggunakan Metabase (via Docker) untuk pemantauan tingkat tinggi (High-Level Monitoring).

  -  Visualisasi tren dropout berdasarkan kategori beasiswa dan risiko finansial.
### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Setup environment:
```
conda create --name students_perfomance python=3.9
conda activate students_perfomance
pip install numpy==1.24.4 scipy==1.10.1 scikit-learn==1.3.2 pandas==2.3.3 streamlit==1.50.0 joblib==1.3.1 imbalanced-learn==0.11.0
pip install greenlet
```

## Business Dashboard
Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```

```

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
#
