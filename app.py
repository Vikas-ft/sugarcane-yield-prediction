import streamlit as st
import pandas as pd
import pickle

# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(
    page_title="AI Yield Intelligence",
    layout="wide"
)

# ------------------------------
# PREMIUM CSS (GLASS UI)
# ------------------------------
st.markdown("""
<style>

/* Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

/* Glass Card */
.glass {
    background: rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    padding: 25px;
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    animation: fadeIn 1.5s ease-in-out;
}

/* Title */
.title {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    color: #ffffff;
    margin-bottom: 10px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #d1d1d1;
    margin-bottom: 30px;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 12px;
    height: 3.5em;
    width: 100%;
    font-size: 18px;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.05);
}

/* Result box */
.result {
    font-size: 24px;
    text-align: center;
    padding: 20px;
}

/* Animation */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

</style>
""", unsafe_allow_html=True)

# ------------------------------
# LOAD MODEL & DATA
# ------------------------------
model = pickle.load(open('yield_model.pkl', 'rb'))
data = pd.read_csv('TamilNadu_District_Avg_NDVI - TamilNadu_District_Avg_NDVI.csv')

# ------------------------------
# HEADER
# ------------------------------
st.markdown('<div class="title">🌾 AI Yield Intelligence Platform</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Satellite-driven crop analytics for Tamil Nadu</div>', unsafe_allow_html=True)

# ------------------------------
# LAYOUT (COLUMNS)
# ------------------------------
col1, col2 = st.columns([1,1])

# ------------------------------
# LEFT PANEL (INPUT)
# ------------------------------
with col1:
    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.subheader("📍 Select District")

    district = st.selectbox(
        "",
        sorted(data['District'].unique())
    )

    selected_row = data[data['District'] == district].iloc[0]
    avg_ndvi = selected_row['NDVI']

    st.write(f"🌿 NDVI Value: **{avg_ndvi:.2f}**")

    predict = st.button("🚀 Generate Prediction")

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------
# RIGHT PANEL (OUTPUT)
# ------------------------------
with col2:
    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.subheader("📊 Prediction Output")

    if predict:
        input_data = pd.DataFrame([[avg_ndvi]], columns=['NDVI'])
        prediction = model.predict(input_data)

        st.markdown(f"""
        <div class="result">
            🌍 District: <b>{district}</b><br><br>
            📈 NDVI: <b>{avg_ndvi:.2f}</b><br><br>
            🌾 Yield Prediction:<br>
            <b>{prediction[0]:.2f} tonnes/hectare</b>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.info("Click 'Generate Prediction' to see results")

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------
# FOOTER
# ------------------------------
st.markdown("""
<hr>
<center style="color:gray">
AI-Based Sugarcane Yield Prediction • Powered by Machine Learning & Satellite Data
</center>
""", unsafe_allow_html=True)
