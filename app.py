import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(page_title="Jaya Jaya Institut - Dropout Predictor", layout="wide")

# =========================
# LOAD MODEL
# =========================
@st.cache_resource
def load_model():
    model_path = os.path.join('model/model_logistic_regression.pkl')
    
    if not os.path.exists(model_path):
        st.error("File model tidak ditemukan di folder 'model/'.")
        st.stop()
        
    model = joblib.load(model_path)
    return model

model = load_model()

# =========================
# HEADER
# =========================
st.title("🎓 Student Dropout Prediction")
st.markdown("### Sistem Pendukung Keputusan Penanganan Mahasiswa")

# =========================
# INPUT FORM
# =========================
with st.form("prediction_form"):
    st.subheader("📝 Data Input Mahasiswa")
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Usia saat Pendaftaran", 10, 70, 20)
        gender = st.selectbox("Jenis Kelamin", [0, 1], format_func=lambda x: "Perempuan" if x==0 else "Laki-laki")
        scholarship = st.selectbox("Penerima Beasiswa", [0, 1], format_func=lambda x: "Tidak" if x==0 else "Ya")
        tuition = st.selectbox("UKT Lunas", [0, 1], format_func=lambda x: "Tidak" if x==0 else "Ya")
        debtor = st.selectbox("Memiliki Hutang", [0, 1], format_func=lambda x: "Tidak" if x==0 else "Ya")

    with col2:
        ipk_indo_1 = st.number_input("IPK Semester 1 (0-4)", 0.0, 4.0, 3.0)
        ipk_indo_2 = st.number_input("IPK Semester 2 (0-4)", 0.0, 4.0, 3.0)
        marital = st.selectbox("Status Pernikahan", [1,2,3,4,5,6])
        course = st.number_input("ID Program Studi", 1, 100, 33)

    submit = st.form_submit_button("Jalankan Prediksi")

# =========================
# PREDIKSI
# =========================
if submit:
    # Konversi IPK ke skala model
    gpa_sem1 = ipk_indo_1 * 5
    gpa_sem2 = ipk_indo_2 * 5

    # Feature Engineering
    financial_risk = 1 if (debtor == 1 and tuition == 0) else 0

    # =========================
    # DAFTAR KOLOM (HARUS SAMA DENGAN TRAINING)
    # =========================
    all_columns = [
        'Marital_status', 'Application_mode', 'Application_order', 'Course', 
        'Daytime_evening_attendance', 'Previous_qualification', 
        'Previous_qualification_grade', 'Nacionality', 'Mothers_qualification', 
        'Fathers_qualification', 'Mothers_occupation', 'Fathers_occupation', 
        'Admission_grade', 'Displaced', 'Educational_special_needs', 'Debtor', 
        'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder', 
        'Age_at_enrollment', 'International',
        'Curricular_units_1st_sem_credited', 
        'Curricular_units_1st_sem_enrolled', 
        'Curricular_units_1st_sem_evaluations', 
        'Curricular_units_1st_sem_approved', 
        'Curricular_units_1st_sem_grade', 
        'Curricular_units_1st_sem_without_evaluations', 
        'Curricular_units_2nd_sem_credited', 
        'Curricular_units_2nd_sem_enrolled', 
        'Curricular_units_2nd_sem_evaluations', 
        'Curricular_units_2nd_sem_approved', 
        'Curricular_units_2nd_sem_grade', 
        'Curricular_units_2nd_sem_without_evaluations', 
        'Unemployment_rate', 'Inflation_rate', 'GDP',
        'Total_Approved_Units', 'Grade_Trend', 
        'Academic_Success_Rate', 'Financial_High_Risk',
        'Parents_Edu_Level'
    ]

    # =========================
    # INPUT DEFAULT
    # =========================
    data = {col: 0 for col in all_columns}

    # =========================
    # UPDATE NILAI INPUT
    # =========================
    data.update({
        'Marital_status': marital,
        'Course': course,
        'Age_at_enrollment': age,
        'Gender': gender,
        'Scholarship_holder': scholarship,
        'Tuition_fees_up_to_date': tuition,
        'Debtor': debtor,
        'Curricular_units_1st_sem_grade': gpa_sem1,
        'Curricular_units_2nd_sem_grade': gpa_sem2,
        'Curricular_units_1st_sem_approved': int(gpa_sem1 >= 10),
        'Curricular_units_2nd_sem_approved': int(gpa_sem2 >= 10),
        'Financial_High_Risk': financial_risk
    })

    # =========================
    # FEATURE TAMBAHAN (ANTI ERROR)
    # =========================
    data['Total_Approved_Units'] = (
        data['Curricular_units_1st_sem_approved'] +
        data['Curricular_units_2nd_sem_approved']
    )

    data['Grade_Trend'] = gpa_sem2 - gpa_sem1

    data['Academic_Success_Rate'] = (gpa_sem1 + gpa_sem2) / 2

    data['Parents_Edu_Level'] = 0

    # =========================
    # PREDIKSI
    # =========================
    input_df = pd.DataFrame([data])[all_columns]

    try:
        prediction = model.predict(input_df)
        result = prediction[0]

        st.divider()
        st.subheader("📊 Hasil Prediksi")

        if result == 'Dropout':
            st.error(f"### ⚠️ {result} (Risiko Tinggi)")
            st.markdown("""
            **Rekomendasi:**
            - Konseling akademik
            - Bantuan finansial
            - Monitoring ketat
            """)
        else:
            st.success(f"### ✅ {result} (Aman)")
            st.markdown("""
            **Rekomendasi:**
            - Pertahankan performa
            - Program pengembangan
            """)

    except Exception as e:
        st.error(f"Terjadi error: {e}")
