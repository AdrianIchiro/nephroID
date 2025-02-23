import streamlit as st

st.set_page_config(page_title="NephroID", page_icon="🩺", layout="centered")

def app():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("logo.png", width=300)

    # Judul aplikasi
    st.markdown("<h1 style='text-align: center; color: #4A90E2;'>Aplikasi NephroID</h1>", unsafe_allow_html=True)

    # Deskripsi aplikasi
    st.write("Selamat datang di aplikasi NephroID, solusi cerdas untuk prediksi dan analisis kesehatan ginjal!")
    
    st.markdown("---")

    st.subheader("👨‍💻 About Developer")

    col1, col2 = st.columns([1, 3])

    with col1:
        st.image("profile.jpg", width=150, caption="Adrian Fahren Setiawan", use_container_width=False)

    with col2:
        st.write("""
        **Nama:** Adrian Fahren Setiawan  
        **Email:** [adrianfahren10@gmail.com](mailto:adrianfahren10@gmail.com)  
        **LinkedIn:** [linkedin.com/in/adrian-fahren-setiawan](https://www.linkedin.com/in/adrian-fahren-setiawan-34a939278/)  
        **GitHub:** [github.com/AdrianIchiro](https://github.com/AdrianIchiro)  
        """)

    st.markdown("Create by Adrian")