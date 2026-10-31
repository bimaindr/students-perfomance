import ssl

# Memaksa Python mengabaikan validasi sertifikat Windows yang korup
try:
    ssl._create_default_https_context = ssl._create_unverified_context
except AttributeError:
    pass

import os

import joblib
import pandas as pd
import streamlit as st

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(page_title="Jaya Jaya Institut - Dropout Predictor", layout="wide")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "model_decision_tree.pkl")

# Urutan kolom HARUS sama dengan saat training
ALL_COLUMNS = [
    'Marital_status', 'Application_mode', 'Application_order', 'Course',
    'Daytime_evening_attendance', 'Previous_qualification',
    'Previous_qualification_grade', 'Nacionality', 'Mothers_qualification',
    'Fathers_qualification', 'Mothers_occupation', 'Fathers_occupation',
    'Admission_grade', 'Displaced', 'Educational_special_needs', 'Debtor',
    'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder',
    'Age_at_enrollment', 'International',
    'Curricular_units_1st_sem_credited', 'Curricular_units_1st_sem_enrolled',
    'Curricular_units_1st_sem_evaluations', 'Curricular_units_1st_sem_approved',
    'Curricular_units_1st_sem_grade', 'Curricular_units_1st_sem_without_evaluations',
    'Curricular_units_2nd_sem_credited', 'Curricular_units_2nd_sem_enrolled',
    'Curricular_units_2nd_sem_evaluations', 'Curricular_units_2nd_sem_approved',
    'Curricular_units_2nd_sem_grade', 'Curricular_units_2nd_sem_without_evaluations',
    'Unemployment_rate', 'Inflation_rate', 'GDP',
    'Total_Approved_Units', 'Grade_Trend', 'Academic_Success_Rate',
    'Financial_High_Risk', 'Parents_Edu_Level',
]

# Label pilihan (kode dataset -> deskripsi)
MARITAL = {1: "1 - Single", 2: "2 - Married", 3: "3 - Widower",
           4: "4 - Divorced", 5: "5 - Facto union", 6: "6 - Legally separated"}
COURSES = {
    33: "33 - Biofuel Production Technologies",
    171: "171 - Animation and Multimedia Design",
    8014: "8014 - Social Service (evening)",
    9003: "9003 - Agronomy",
    9070: "9070 - Communication Design",
    9085: "9085 - Veterinary Nursing",
    9119: "9119 - Informatics Engineering",
    9130: "9130 - Equinculture",
    9147: "9147 - Management",
    9238: "9238 - Social Service",
    9254: "9254 - Tourism",
    9500: "9500 - Nursing",
    9556: "9556 - Oral Hygiene",
    9670: "9670 - Advertising and Marketing Management",
    9773: "9773 - Journalism and Communication",
    9853: "9853 - Basic Education",
    9991: "9991 - Management (evening)",
}
APP_MODES = {
    1: "1 - 1st phase - general contingent",
    2: "2 - Ordinance No. 612/93",
    5: "5 - 1st phase - special contingent (Azores)",
    7: "7 - Holders of other higher courses",
    10: "10 - Ordinance No. 854-B/99",
    15: "15 - International student (bachelor)",
    16: "16 - 1st phase - special contingent (Madeira)",
    17: "17 - 2nd phase - general contingent",
    18: "18 - 3rd phase - general contingent",
    26: "26 - Ordinance No. 533-A/99, item b2",
    27: "27 - Ordinance No. 533-A/99, item b3",
    39: "39 - Over 23 years old",
    42: "42 - Transfer",
    43: "43 - Change of course",
    44: "44 - Technological specialization diploma holders",
    51: "51 - Change of institution/course",
    53: "53 - Short cycle diploma holders",
    57: "57 - Change of institution/course (International)",
}


def yes_no(x):
    return "Ya" if x == 1 else "Tidak"


# =========================
# LOAD MODEL
# =========================
@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        st.error(f"File model tidak ditemukan: {MODEL_PATH}")
        st.stop()
    return joblib.load(MODEL_PATH)


model = load_model()

# =========================
# HEADER
# =========================
st.title("🎓 Student Dropout Prediction")
st.markdown("### Sistem Pendukung Keputusan Penanganan Mahasiswa")
st.caption("Isi seluruh data mahasiswa, lalu klik **Jalankan Prediksi**. "
           "Nilai default adalah contoh mahasiswa dengan performa baik.")

# =========================
# INPUT FORM
# =========================
with st.form("prediction_form"):

    st.subheader("👤 Data Pribadi & Pendaftaran")
    c1, c2, c3 = st.columns(3)
    with c1:
        marital = st.selectbox("Status Pernikahan", list(MARITAL), format_func=MARITAL.get)
        gender = st.selectbox("Jenis Kelamin", [0, 1],
                              format_func=lambda x: "Perempuan" if x == 0 else "Laki-laki")
        age = st.number_input("Usia saat Pendaftaran", 15, 80, 20)
        nacionality = st.number_input("Kode Kewarganegaraan", 1, 109, 1,
                                      help="1 = Portuguese (sesuai kode dataset)")
        international = st.selectbox("Mahasiswa Internasional", [0, 1], format_func=yes_no)
    with c2:
        course = st.selectbox("Program Studi", list(COURSES), index=list(COURSES).index(9254),
                              format_func=COURSES.get)
        app_mode = st.selectbox("Jalur Pendaftaran", list(APP_MODES), format_func=APP_MODES.get)
        app_order = st.number_input("Urutan Pilihan Pendaftaran (0-9)", 0, 9, 1)
        attendance = st.selectbox("Waktu Kuliah", [1, 0],
                                  format_func=lambda x: "Siang (Daytime)" if x == 1 else "Malam (Evening)")
        displaced = st.selectbox("Mahasiswa Perantau (Displaced)", [0, 1], index=1, format_func=yes_no)
    with c3:
        special_needs = st.selectbox("Kebutuhan Pendidikan Khusus", [0, 1], format_func=yes_no)
        prev_qual = st.number_input("Kode Kualifikasi Sebelumnya", 1, 43, 1)
        prev_qual_grade = st.number_input("Nilai Kualifikasi Sebelumnya (0-200)", 0.0, 200.0, 130.0)
        admission_grade = st.number_input("Nilai Masuk / Admission Grade (0-200)", 0.0, 200.0, 125.0)

    st.subheader("👪 Data Orang Tua")
    c1, c2 = st.columns(2)
    with c1:
        mothers_qual = st.number_input("Kode Kualifikasi Ibu", 1, 44, 1)
        mothers_occ = st.number_input("Kode Pekerjaan Ibu", 0, 195, 1)
    with c2:
        fathers_qual = st.number_input("Kode Kualifikasi Ayah", 1, 44, 1)
        fathers_occ = st.number_input("Kode Pekerjaan Ayah", 0, 195, 1)

    st.subheader("💰 Data Finansial")
    c1, c2, c3 = st.columns(3)
    with c1:
        debtor = st.selectbox("Memiliki Hutang", [0, 1], format_func=yes_no)
    with c2:
        tuition = st.selectbox("UKT Lunas / Up to Date", [1, 0], format_func=yes_no)
    with c3:
        scholarship = st.selectbox("Penerima Beasiswa", [1, 0], format_func=yes_no)

    st.subheader("📚 Performa Akademik Semester 1")
    c1, c2, c3 = st.columns(3)
    with c1:
        s1_credited = st.number_input("SKS Diakui (Credited) - Sem 1", 0, 30, 0)
        s1_enrolled = st.number_input("Mata Kuliah Diambil (Enrolled) - Sem 1", 0, 40, 6)
    with c2:
        s1_eval = st.number_input("Jumlah Evaluasi - Sem 1", 0, 60, 6)
        s1_approved = st.number_input("Mata Kuliah Lulus (Approved) - Sem 1", 0, 40, 6)
    with c3:
        s1_grade = st.number_input("Rata-rata Nilai Sem 1 (0-20)", 0.0, 20.0, 14.5)
        s1_noeval = st.number_input("Tanpa Evaluasi - Sem 1", 0, 20, 0)

    st.subheader("📚 Performa Akademik Semester 2")
    c1, c2, c3 = st.columns(3)
    with c1:
        s2_credited = st.number_input("SKS Diakui (Credited) - Sem 2", 0, 30, 0)
        s2_enrolled = st.number_input("Mata Kuliah Diambil (Enrolled) - Sem 2", 0, 40, 6)
    with c2:
        s2_eval = st.number_input("Jumlah Evaluasi - Sem 2", 0, 60, 6)
        s2_approved = st.number_input("Mata Kuliah Lulus (Approved) - Sem 2", 0, 40, 6)
    with c3:
        s2_grade = st.number_input("Rata-rata Nilai Sem 2 (0-20)", 0.0, 20.0, 15.0)
        s2_noeval = st.number_input("Tanpa Evaluasi - Sem 2", 0, 20, 0)

    st.subheader("📈 Kondisi Makroekonomi")
    c1, c2, c3 = st.columns(3)
    with c1:
        unemployment = st.number_input("Unemployment Rate (%)", -10.0, 30.0, 10.8, step=0.1)
    with c2:
        inflation = st.number_input("Inflation Rate (%)", -10.0, 30.0, 1.4, step=0.1)
    with c3:
        gdp = st.number_input("GDP", -10.0, 10.0, 1.74, step=0.01)

    submit = st.form_submit_button("Jalankan Prediksi", type="primary")

# =========================
# PREDIKSI
# =========================
if submit:
    # ---- Feature engineering (sama dengan saat training) ----
    total_approved = s1_approved + s2_approved
    total_enrolled = s1_enrolled + s2_enrolled
    grade_trend = s2_grade - s1_grade
    success_rate = total_approved / total_enrolled if total_enrolled > 0 else 0.0
    financial_risk = 1 if (debtor == 1 and tuition == 0) else 0
    parents_edu = (mothers_qual + fathers_qual) / 2

    data = {
        'Marital_status': marital,
        'Application_mode': app_mode,
        'Application_order': app_order,
        'Course': course,
        'Daytime_evening_attendance': attendance,
        'Previous_qualification': prev_qual,
        'Previous_qualification_grade': prev_qual_grade,
        'Nacionality': nacionality,
        'Mothers_qualification': mothers_qual,
        'Fathers_qualification': fathers_qual,
        'Mothers_occupation': mothers_occ,
        'Fathers_occupation': fathers_occ,
        'Admission_grade': admission_grade,
        'Displaced': displaced,
        'Educational_special_needs': special_needs,
        'Debtor': debtor,
        'Tuition_fees_up_to_date': tuition,
        'Gender': gender,
        'Scholarship_holder': scholarship,
        'Age_at_enrollment': age,
        'International': international,
        'Curricular_units_1st_sem_credited': s1_credited,
        'Curricular_units_1st_sem_enrolled': s1_enrolled,
        'Curricular_units_1st_sem_evaluations': s1_eval,
        'Curricular_units_1st_sem_approved': s1_approved,
        'Curricular_units_1st_sem_grade': s1_grade,
        'Curricular_units_1st_sem_without_evaluations': s1_noeval,
        'Curricular_units_2nd_sem_credited': s2_credited,
        'Curricular_units_2nd_sem_enrolled': s2_enrolled,
        'Curricular_units_2nd_sem_evaluations': s2_eval,
        'Curricular_units_2nd_sem_approved': s2_approved,
        'Curricular_units_2nd_sem_grade': s2_grade,
        'Curricular_units_2nd_sem_without_evaluations': s2_noeval,
        'Unemployment_rate': unemployment,
        'Inflation_rate': inflation,
        'GDP': gdp,
        'Total_Approved_Units': total_approved,
        'Grade_Trend': grade_trend,
        'Academic_Success_Rate': success_rate,
        'Financial_High_Risk': financial_risk,
        'Parents_Edu_Level': parents_edu,
    }

    input_df = pd.DataFrame([data])[ALL_COLUMNS]

    try:
        pred = model.predict(input_df)[0]
        proba = model.predict_proba(input_df)[0]
        classes = list(model.classes_)
        # Encoding model: 0 = Dropout, 1 = Graduate
        p_dropout = float(proba[classes.index(0)])
        p_graduate = float(proba[classes.index(1)])
        is_graduate = int(pred) == 1

        st.divider()
        st.subheader("📊 Hasil Prediksi")

        if is_graduate:
            st.success("### ✅ Graduate (Diprediksi Lulus)")
            st.markdown("""
            **Rekomendasi:**
            - Pertahankan performa akademik
            - Tawarkan program pengembangan (magang, riset, organisasi)
            """)
        else:
            st.error("### ⚠️ Dropout (Risiko Tinggi)")
            st.markdown("""
            **Rekomendasi:**
            - Konseling akademik segera
            - Bantuan finansial / keringanan UKT
            - Monitoring ketat setiap semester
            """)

        m1, m2 = st.columns(2)
        m1.metric("Probabilitas Graduate", f"{p_graduate:.1%}")
        m2.metric("Probabilitas Dropout", f"{p_dropout:.1%}")
        st.progress(p_graduate)

        with st.expander("Lihat fitur hasil perhitungan otomatis"):
            st.write({
                "Total_Approved_Units": total_approved,
                "Grade_Trend": round(grade_trend, 2),
                "Academic_Success_Rate": round(success_rate, 3),
                "Financial_High_Risk": financial_risk,
                "Parents_Edu_Level": parents_edu,
            })

    except Exception as e:
        st.error(f"Terjadi error: {e}")
