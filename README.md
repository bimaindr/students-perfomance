# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
Masalah utama yang dihadapi Jaya Jaya Institut adalah jumlah mahasiswa yang tidak menyelesaikan studinya (dropout). Hal ini berdampak langsung pada:

  - Stabilitas Finansial: Kehilangan pendapatan berkelanjutan dari uang kuliah tunggal (UKT).

  - Efisiensi Sumber Daya: Kursi kosong di kelas yang seharusnya bisa diisi oleh mahasiswa aktif, membuat alokasi dosen dan fasilitas menjadi tidak optimal.

Pihak manajemen kampus selama ini cenderung bersifat reaktif. Mereka baru menyadari mahasiswa bermasalah ketika mahasiswa tersebut sudah berhenti membayar UKT atau tidak muncul di kelas selama satu semester.

Masalah: Tidak adanya sistem peringatan dini (early warning system) yang dapat memprediksi risiko dropout sebelum hal itu benar-benar terjadi.

### Cakupan Proyek
Gemini berkata
Berikut adalah rumusan Cakupan Proyek (Project Scope) yang terstruktur untuk laporan akhir Anda. Bagian ini mendefinisikan batasan teknis dan operasional dari solusi yang Anda bangun untuk Jaya Jaya Institut.

📋 Cakupan Proyek (Project Scope)
Proyek ini berfokus pada pengembangan sistem deteksi dini dan pemantauan keberlanjutan studi mahasiswa dengan cakupan kerja sebagai berikut:

1. Analisis dan Pemrosesan Data (Data Engineering)
Eksplorasi Data (EDA): Melakukan analisis mendalam terhadap dataset untuk mengidentifikasi korelasi antara faktor demografi, sosial-ekonomi, dan performa akademik terhadap status kelulusan.

Pembersihan Data: Menangani data yang hilang (missing values), inkonsistensi format, dan memastikan data siap untuk tahap pemodelan.

Rekayasa Fitur (Feature Engineering): Menciptakan fitur baru yang relevan secara bisnis, seperti:

Financial High Risk: Penggabungan status hutang dan pelunasan UKT untuk memetakan risiko ekonomi.

Academic Success Rate: Rasio keberhasilan unit mata kuliah yang diambil.

Grade Trend: Analisis fluktuasi nilai dari semester 1 ke semester 2.

2. Pengembangan Model Prediksi (Machine Learning)
Pemodelan: Mengimplementasikan algoritma Logistic Regression untuk melakukan klasifikasi tiga kelas (Dropout, Enrolled, Graduate).

Evaluasi Model: Mengukur performa model menggunakan metrik standar industri seperti Accuracy, Precision, Recall, dan F1-Score untuk memastikan prediksi yang handal.

Export Model: Menyimpan model yang telah dilatih ke dalam format .pkl menggunakan library Joblib agar dapat digunakan secara modular.

3. Pengembangan Prototype Aplikasi (Deployment)
Antarmuka Pengguna: Membangun dashboard interaktif menggunakan Streamlit.

Lokalisasi Input: Menyesuaikan standar penilaian akademik dengan Skala IPK Indonesia (0.00 - 4.00) untuk memudahkan penggunaan oleh staf institusi.

Sistem Rekomendasi: Mengintegrasikan logika bisnis ke dalam aplikasi yang memberikan saran tindakan strategis (seperti bantuan beasiswa atau kelas tambahan) berdasarkan hasil prediksi model.

Cloud Hosting: Melakukan publikasi aplikasi ke Streamlit Community Cloud sehingga dapat diakses secara publik melalui URL.
### Persiapan

Sumber data: ....

Setup environment:
```

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
