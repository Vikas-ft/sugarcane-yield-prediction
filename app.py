import streamlit as st
import pandas as pd
import pickle

# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(page_title="AI Yield Intelligence", layout="wide")

# ------------------------------
# ULTRA PREMIUM GLASS CSS
# ------------------------------
st.markdown("""
<style>

/* MAIN BACKGROUND */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

/* REMOVE WHITE BLOCK */
.block-container {
    padding-top: 2rem;
    background: transparent;
}

/* GLASS CARD */
.glass {
    background: rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    padding: 30px;
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    transition: 0.3s;
}

/* HOVER EFFECT */
.glass:hover {
    transform: scale(1.02);
}

/* TITLE */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: white;
}

/* SUBTITLE */
.subtitle {
    text-align: center;
    color: #cccccc;
    margin-bottom: 30px;
}

/* DROPDOWN STYLE */
div[data-baseweb="select"] > div {
    background: rgba(255,255,255,0.1) !important;
    border-radius: 10px !important;
    border: 1px solid rgba(255,255,255,0.3) !important;
}

/* BUTTON */
.stButton>button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 12px;
    height: 3.5em;
    width: 100%;
    font-size: 18px;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 15px #00c6ff;
}

/* RESULT BOX */
.result {
    background: rgba(255,255,255,0.08);
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    font-size: 22px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.2);
}

/* INFO BOX FIX */
.stAlert {
    background: rgba(255,255,255,0.1) !important;
    border-radius: 10px;
}

/* HIDE FOOTER */
footer {
    visibility: hidden;
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
# LAYOUT
# ------------------------------
col1, col2 = st.columns([1,1])

# ------------------------------
# LEFT PANEL
# ------------------------------
with col1:
    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.subheader("📍 Select District")

    district = st.selectbox("", sorted(data['District'].unique()))

    selected_row = data[data['District'] == district].iloc[0]
    avg_ndvi = selected_row['NDVI']

    st.markdown(f"<p style='color:#ccc;'>🌿 NDVI Value: <b>{avg_ndvi:.2f}</b></p>", unsafe_allow_html=True)

    predict = st.button("🚀 Generate Prediction")

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------
# RIGHT PANEL
# ------------------------------
with col2:
    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.subheader("📊 Prediction Output")

    if predict:
        input_data = pd.DataFrame([[avg_ndvi]], columns=['NDVI'])
        prediction = model.predict(input_data)

        st.markdown(f"""
        <div class="result">
            🌍 <b>{district}</b><br><br>
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
