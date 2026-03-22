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

Cakupan Proyek (Project Scope)
Proyek ini berfokus pada pengembangan sistem deteksi dini dan pemantauan keberlanjutan studi mahasiswa dengan cakupan kerja sebagai berikut:

1. Analisis dan Pemrosesan Data (Data Engineering)
Eksplorasi Data (EDA): Melakukan analisis mendalam terhadap dataset untuk mengidentifikasi korelasi antara faktor demografi, sosial-ekonomi, dan performa akademik terhadap status kelulusan.

    - Pembersihan Data: Menangani data yang hilang (missing values), inkonsistensi format, dan memastikan data siap untuk tahap pemodelan.

    - Rekayasa Fitur (Feature Engineering): Menciptakan fitur baru yang relevan secara bisnis, seperti:

    - Financial High Risk: Penggabungan status hutang dan pelunasan UKT untuk memetakan risiko ekonomi.

    - Academic Success Rate: Rasio keberhasilan unit mata kuliah yang diambil.

    - Grade Trend: Analisis fluktuasi nilai dari semester 1 ke semester 2.

2. Pengembangan Model Prediksi (Machine Learning)
Pemodelan: Mengimplementasikan algoritma Logistic Regression untuk melakukan klasifikasi tiga kelas (Dropout, Enrolled, Graduate).

    - Evaluasi Model: Mengukur performa model menggunakan metrik standar industri seperti Accuracy, Precision, Recall, dan F1-Score untuk memastikan prediksi yang handal.

    - Export Model: Menyimpan model yang telah dilatih ke dalam format .pkl menggunakan library Joblib agar dapat digunakan secara modular.

3. Pengembangan Prototype Aplikasi (Deployment)
Antarmuka Pengguna: Membangun dashboard interaktif menggunakan Streamlit.

    - Lokalisasi Input: Menyesuaikan standar penilaian akademik dengan Skala IPK Indonesia (0.00 - 4.00) untuk memudahkan penggunaan oleh staf institusi.

    - Sistem Rekomendasi: Mengintegrasikan logika bisnis ke dalam aplikasi yang memberikan saran tindakan strategis (seperti bantuan beasiswa atau kelas tambahan) berdasarkan hasil prediksi model.

    - Cloud Hosting: Melakukan publikasi aplikasi ke Streamlit Community Cloud sehingga dapat diakses secara publik melalui URL.
### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Setup environment:
```
conda create --name students_perfomance python=3.9
conda activate students_perfomance
pip install streamlit==1.32.0 pandas==2.2.2 scikit-learn==1.3.2 joblib==1.3.1 imbalanced-learn==0.11.0 scipy==1.10.1 numpy==1.24.4
pip install psycopg2
```

## Business Dashboard
1. SKS Lulus Berdasarkan Umur
   Grafik ini menunjukkan tren yang menarik: mahasiswa dengan usia yang lebih dewasa (Diatas 35 Tahun) cenderung memiliki rata-rata kelulusan SKS yang lebih
   tinggi dibandingkan mahasiswa yang lebih muda (18-19 Tahun).
   Insight Bisnis: Mahasiswa dewasa mungkin memiliki manajemen waktu atau motivasi yang lebih matang. Hal ini membuktikan bahwa usia bukan hambatan bagi performa
   akademik di institusi ini.

2. Distribusi Umur dan Total Mahasiswa
   Grafik ini memberikan gambaran volume populasi mahasiswa.
   Insight Bisnis: Mayoritas populasi mahasiswa terkonsentrasi di kelompok usia 18-19 Tahun (hampir 2.000 mahasiswa). Sementara itu, kelompok usia lainnya
   digabungkan dalam kategori "Lainnya", yang menunjukkan segmentasi pasar institusi didominasi oleh lulusan baru SMA.

3. Memiliki Hutang vs Tidak (Donut Chart)
   Ini adalah indikator risiko paling krusial untuk prediksi dropout.
   Insight Bisnis: Sebagian besar mahasiswa (88.6%) tidak memiliki hutang, namun ada 11.4% mahasiswa yang tercatat memiliki kendala finansial
   Rekomendasi: Angka 11.4% ini harus dimonitor secara ketat, karena berdasarkan analisis data science, status hutang seringkali menjadi pemicu utama mahasiswa
   memutuskan untuk berhenti studi (dropout).


## Menjalankan Sistem Machine Learning
Melalui Link Cloud Deployment : https://students-perfomance-kbsrld7hdruyutgkfpgcsz.streamlit.app/
```
conda activate students_perfomance
streamlit run app.py
```

## Conclusion
Mahasiswa yang memiliki status Debtor (Hutang) dan mereka yang tidak melakukan pembayaran Tuition Fees tepat waktu memiliki probabilitas dropout yang jauh lebih tinggi. Dari sisi akademik, performa pada Semester 1 merupakan indikator awal yang paling krusial; penurunan nilai yang drastis di awal semester berkorelasi kuat dengan keputusan mahasiswa untuk berhenti.

Dengan adanya sistem ini, institusi kini memiliki alat Deteksi Dini (Early Warning System) yang mampu memprediksi risiko dropout sebelum hal tersebut benar-benar terjadi.

  - Intervensi Finansial: Memberikan program cicilan atau bantuan beasiswa khusus bagi 11.4% mahasiswa yang terdeteksi sebagai Debtor berisiko tinggi.

  - Pendampingan Akademik: Melakukan konseling intensif bagi mahasiswa yang memiliki indeks prestasi rendah di Semester 1 untuk mencegah akumulasi kegagalan di semester berikutnya.

### Rekomendasi Action Items
- Memberikan program cicilan UKT yang lebih fleksibel atau skema "Dana Talangan" internal bagi mahasiswa yang terdeteksi sebagai Debtor namun memiliki performa akademik yang baik.
- Mengintegrasikan hasil prediksi model ke dalam sistem informasi akademik (SIAKAD). Staf dosen wali akan menerima notifikasi otomatis jika ada mahasiswa yang diprediksi "Dropout" berdasarkan nilai Semester 1 mereka.
- Meninjau kembali kriteria penerima beasiswa. Alihkan sebagian kuota beasiswa untuk mahasiswa yang secara akademik mampu (Graduate) namun secara finansial terancam (Debtor) agar mereka tidak berhenti di tengah jalan.
