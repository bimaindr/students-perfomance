import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Jaya Jaya Institut - Dropout Predictor", layout="wide")

# --- LOAD MODEL & ENCODER ---
@st.cache_resource
def load_model():
    model_path = os.path.join('model', 'model_logistic_regression.pkl')
    le_path = os.path.join('model', 'label_encoder.pkl')
    
    if not os.path.exists(model_path):
        st.error(f"File model tidak ditemukan di folder 'model/'.")
        st.stop()
        
    model = joblib.load(model_path)
    le = joblib.load(le_path)
    return model, le

try:
    model, le = load_model()
except Exception as e:
    st.error(f"Terjadi kesalahan saat memuat model: {e}")
    st.stop()

# --- HEADER ---
st.title("🎓 Student Dropout Prediction")
st.markdown("### Sistem Pendukung Keputusan Penanganan Mahasiswa")

# --- INPUT FORM ---
with st.form("prediction_form"):
    st.subheader("📝 Data Input Mahasiswa")
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Usia saat Pendaftaran", min_value=10, max_value=70, value=20)
        gender = st.selectbox("Jenis Kelamin", options=[0, 1], format_func=lambda x: "Perempuan" if x==0 else "Laki-laki")
        scholarship = st.selectbox("Penerima Beasiswa", options=[0, 1], format_func=lambda x: "Tidak" if x==0 else "Ya")
        tuition = st.selectbox("UKT/Biaya Kuliah Lunas", options=[0, 1], format_func=lambda x: "Tidak" if x==0 else "Ya")
        debtor = st.selectbox("Memiliki Tunggakan Hutang", options=[0, 1], format_func=lambda x: "Tidak" if x==0 else "Ya")

    with col2:
        ipk_indo_1 = st.number_input("IPK Semester 1 (Skala 0.0 - 4.0)", min_value=0.0, max_value=4.0, value=3.0)
        ipk_indo_2 = st.number_input("IPK Semester 2 (Skala 0.0 - 4.0)", min_value=0.0, max_value=4.0, value=3.0)
        marital = st.selectbox("Status Pernikahan", options=[1, 2, 3, 4, 5, 6], help="1: Lajang, 2: Menikah, dst.")
        course = st.number_input("ID Program Studi (Course ID)", min_value=1, value=33)

    submit = st.form_submit_button("Jalankan Prediksi & Rekomendasi")

# --- LOGIKA PREDIKSI ---
if submit:
    # KONVERSI: Indonesia (4.0) -> Model (20.0)
    gpa_sem1 = ipk_indo_1 * 5
    gpa_sem2 = ipk_indo_2 * 5
    
    # Feature Engineering
    financial_risk = 1 if (debtor == 1 and tuition == 0) else 0
    academic_rate = (gpa_sem1 + gpa_sem2) / 2

    # 1. Daftar Kolom Lengkap
    all_columns = [
        'Marital_status', 'Application_mode', 'Application_order', 'Course', 
        'Daytime_evening_attendance', 'Previous_qualification', 
        'Previous_qualification_grade', 'Nacionality', 'Mothers_qualification', 
        'Fathers_qualification', 'Mothers_occupation', 'Fathers_occupation', 
        'Admission_grade', 'Displaced', 'Educational_special_needs', 'Debtor', 
        'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder', 
        'Age_at_enrollment', 'International', 'Curricular_units_1st_sem_credited', 
        'Curricular_units_1st_sem_enrolled', 'Curricular_units_1st_sem_evaluations', 
        'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade', 
        'Curricular_units_1st_sem_without_evaluations', 'Curricular_units_2nd_sem_credited', 
        'Curricular_units_2nd_sem_enrolled', 'Curricular_units_2nd_sem_evaluations', 
        'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade', 
        'Curricular_units_2nd_sem_without_evaluations', 'Unemployment_rate', 
        'Inflation_rate', 'GDP', 'Total_Approved_Units', 'Grade_Trend', 
        'Academic_Success_Rate', 'Financial_High_Risk', 'Parents_Edu_Level'
    ]

    # 2. Inisialisasi & Update Dict
    full_input_dict = {col: 0 for col in all_columns}
    full_input_dict.update({
        'Marital_status': marital, 'Course': course, 'Age_at_enrollment': age,
        'Gender': gender, 'Scholarship_holder': scholarship,
        'Tuition_fees_up_to_date': tuition, 'Debtor': debtor,
        'Curricular_units_1st_sem_grade': gpa_sem1,
        'Curricular_units_2nd_sem_grade': gpa_sem2,
        'Curricular_units_1st_sem_approved': int(gpa_sem1 >= 10), 
        'Curricular_units_2nd_sem_approved': int(gpa_sem2 >= 10),
        'Academic_Success_Rate': academic_rate,
        'Financial_High_Risk': financial_risk
    })

    # 3. Prediksi
    input_df = pd.DataFrame([full_input_dict])[all_columns]

    try:
        prediction = model.predict(input_df)
        result = le.inverse_transform(prediction)[0] if not isinstance(prediction[0], (str, np.str_)) else prediction[0]
        
        # --- TAMPILAN HASIL & REKOMENDASI ---
        st.divider()
        st.subheader("📊 Hasil Analisis & Rekomendasi Strategis")
        
        if result == 'Dropout':
            st.error(f"### Prediksi Status: **{result}** (Risiko Tinggi)")
            st.markdown("""
            **Rekomendasi Tindakan:**
            1. **Intervensi Finansial:** Segera hubungi mahasiswa untuk mendiskusikan skema cicilan jika terdapat tunggakan UKT.
            2. **Mentoring Akademik:** Tugaskan Dosen Pembimbing Akademik (DPA) untuk melakukan sesi konseling terkait rendahnya nilai semester.
            3. **Early Warning System:** Masukkan data mahasiswa ke dalam daftar prioritas pemantauan ketat.
            """)
        elif result == 'Enrolled':
            st.warning(f"### Prediksi Status: **{result}** (Perlu Pantauan)")
            st.markdown("""
            **Rekomendasi Tindakan:**
            1. **Monitoring Berkala:** Pantau kehadiran dan keaktifan mahasiswa di kelas pada semester berjalan.
            2. **Peer Support:** Sarankan mahasiswa untuk bergabung dalam kelompok belajar atau asisten praktikum.
            3. **Evaluasi KRS:** Pastikan beban SKS yang diambil tidak terlalu berat untuk meningkatkan performa nilai.
            """)
        else:
            st.success(f"### Prediksi Status: **{result}** (Aman)")
            st.markdown("""
            **Rekomendasi Tindakan:**
            1. **Pertahankan Prestasi:** Berikan apresiasi atau informasi mengenai peluang beasiswa prestasi lebih lanjut.
            2. **Program Akselerasi:** Tawarkan program pengayaan atau magang di industri mitra.
            3. **Duta Mahasiswa:** Mahasiswa berpotensi menjadi mentor bagi rekan mahasiswa lainnya yang berisiko.
            """)

    except Exception as e:
        st.error(f"Terjadi kesalahan teknis: {e}")