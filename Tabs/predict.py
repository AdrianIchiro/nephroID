import streamlit as st
from web_function import predict

def app(df, x, y):
    st.title("🔍 Prediksi Penyakit Ginjal")
    st.markdown("---")
    
    # Styling dengan card-like UI
    st.markdown(
        """
        <style>
        .stTextInput>div>div>input {
            border-radius: 10px;
            padding: 10px;
        }
        .stButton>button {
            border-radius: 10px;
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            font-size: 16px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)
    
    with col1:
        bp = st.text_input('💉 Tekanan Darah (bp)')
        sg = st.text_input('🔬 Specific Gravity (sg)')
        al = st.text_input('🧪 Albumin (al)')
        su = st.text_input('🍬 Gula Urin (su)')
        rbc = st.text_input('🩸 Sel Darah Merah (rbc)')
        pc = st.text_input('🦠 Sel Pipih (pc)')
        pcc = st.text_input('🔍 Sel Pus (pcc)')
        ba = st.text_input('🦠 Bakteri (ba)')
    
    with col2:
        bgr = st.text_input('🔬 Glukosa Darah (bgr)')
        bu = st.text_input('💊 Urea Darah (bu)')
        sc = st.text_input('🧬 Serum Creatinine (sc)')
        sod = st.text_input('⚡ Sodium (sod)')
        pot = st.text_input('🥔 Potassium (pot)')
        hemo = st.text_input('🩸 Hemoglobin (hemo)')
        pcv = st.text_input('🧫 Packed Cell Volume (pcv)')
        wc = st.text_input('🦠 Sel Darah Putih (wc)')
    
    with col3:
        rc = st.text_input('🩸 Sel Darah Merah (rc)')
        htn = st.text_input('⚠️ Hipertensi (htn)')
        dm = st.text_input('🩸 Diabetes (dm)')
        cad = st.text_input('❤️ Penyakit Jantung (cad)')
        appet = st.text_input('🍽️ Nafsu Makan (appet)')
        pe = st.text_input('🤰 Edema Kehamilan (pe)')
        ane = st.text_input('🩸 Anemia (ane)')
    
    features = [bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane]
    
    if st.button('🔮 Prediksi'):
        prediction, score = predict(x, y, features)
        
        st.markdown("---")
        st.success("Prediksi sukses!")
        
        if prediction == 1:
            st.error("⚠️ Rentan terhadap penyakit ginjal!")
        else:
            st.success("✅ Aman dari penyakit ginjal")
        
        st.info(f"🧠 Model yang digunakan memiliki tingkat akurasi {score * 100:.2f}%")
