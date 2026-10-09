import streamlit as st
import pandas as pd
import pickle as pk
from datetime import date
import plotly.graph_objects as go
import plotly.express as px


# Load model and scaler
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

with open(BASE_DIR / "model.pkl", "rb") as file:
    model = pk.load(file)

with open(BASE_DIR / "scaler.pkl", "rb") as file:
    scaler = pk.load(file)

st.set_page_config(page_title="Loan Prediction", page_icon="🏦", layout="centered")
st.markdown("""
<style>

.stApp{
    background: linear-gradient(to right,#0f172a,#1e293b);
}

h1,h2,h3,p,label{
    color:white !important;
}

.stButton>button{
    width:100%;
    height:55px;
    border-radius:15px;
    font-size:20px;
    background:linear-gradient(90deg,#00c6ff,#8a2be2);
    color:white;
    border:none;
}

.stButton>button:hover{
    transform:scale(1.02);
}

</style>
""", unsafe_allow_html=True)

with st.sidebar:

    st.title("🏦 Loan AI")

    st.success("Smart Loan Approval Prediction")

    st.info("""
    Features

    ✅ AI Prediction
    ✅ Credit Analysis
    ✅ Risk Assessment
    ✅ Instant Approval Check
    """)
st.markdown("""
<h1 style='text-align:center;
color:white;
font-size:45px;
text-shadow:0px 0px 20px #00c6ff;'>

🏦 SMART LOAN APPROVAL PREDICTION APP 💰

</h1>
""", unsafe_allow_html=True)

st.markdown(
"<h4 style='text-align:center;color:#cbd5e1;'>AI Powered Banking & Credit Risk Analysis System</h4>",
unsafe_allow_html=True
)

# --- Personal Details ---
name = st.text_input('Enter your Name')

dob = st.date_input(
    'Enter your Date of Birth',
    value=date(2000,1,1),
    min_value=date(1950,1,1),
    max_value=date.today()
)

loan_type = st.selectbox(
    'Select Loan Type',
    ['Home Loan', 'Personal Loan', 'Education Loan', 'Car Loan',
     'Business Loan', 'Gold Loan', 'Agriculture Loan',
     'Credit Card Loan', 'Startup Loan']
)

st.divider()

# --- Loan Applicant Data (SLIDERS) ---
no_of_dep = st.slider('Enter No. of Dependents', 0, 10, 1)

grad = st.selectbox('Choose Education', ['Graduated', 'Not Graduated'])
self_emp = st.selectbox('Self Employed?', ['Yes', 'No'])

# Layout using columns for better UI
col1, col2 = st.columns(2)

with col1:
    Annual_Income = st.number_input(
    "💰 Annual Income (₹)",
    min_value=0,
    value=500000,
    step=10000
)
    Loan_Amount = st.number_input(
    "🏦 Loan Amount (₹)",
    min_value=0,
    value=100000,
    step=10000
)

with col2:
    Loan_Dur = st.slider('Loan Duration (Years)', 1, 30, 5)
    Cibil = st.slider('CIBIL Score', 300, 900, 650)
if Cibil >= 750:
    st.success("🟢 Excellent Credit Score")

elif Cibil >= 650:
    st.warning("🟠 Average Credit Score")

else:
    st.error("🔴 Poor Credit Score")
st.subheader("📊 Credit Score Analysis")

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=Cibil,

    title={'text':"CIBIL Score"},

    gauge={
        'axis':{'range':[300,900]},

        'steps':[
            {'range':[300,550],'color':'red'},
            {'range':[550,700],'color':'orange'},
            {'range':[700,900],'color':'green'}
        ],

        'bar':{'color':'white'}
    }
))

st.plotly_chart(fig, use_container_width=True)

Assets = st.number_input(
    "🏠 Total Assets Value (₹)",
    min_value=0,
    value=200000,
    step=50000
)
st.subheader("👤 Applicant Profile")

col1,col2,col3 = st.columns(3)

with col1:
    st.metric("💰 Income", f"₹{Annual_Income:,}")

with col2:
    st.metric("🏦 Loan", f"₹{Loan_Amount:,}")

with col3:
    st.metric("📈 CIBIL", Cibil)

col1,col2 = st.columns(2)

with col1:
    st.info(f"🏦 Loan Type : {loan_type}")

with col2:
    st.info(f"👨‍👩‍👧 Dependents : {no_of_dep}")

# --- Encode categorical data ---
grad_s = 0 if grad == 'Graduated' else 1
emp_s = 1 if self_emp == 'Yes' else 0

st.divider()

# --- Prediction ---
if st.button("🔍 Predict"):

    if name == "":
        st.warning("⚠️ Please enter your name")

    else:

        pred_data = pd.DataFrame(
            [[no_of_dep, grad_s, emp_s, Annual_Income, Loan_Amount, Loan_Dur, Cibil, Assets]],
            columns=[
                'no_of_dependents',
                'education',
                'self_employed',
                'income_annum',
                'loan_amount',
                'loan_term',
                'cibil_score',
                'Assets'
            ]
        )

        pred_data = scaler.transform(pred_data)

        pred_result = model.predict(pred_data)

        try:
            probability = model.predict_proba(pred_data)[0][1]
        except:
            probability = 0.80

        st.subheader(f"👤 Applicant: {name}")
        st.write(f"🎂 Date of Birth: {dob}")
        st.write(f"🏠 Loan Type: {loan_type}")

        st.subheader("🤖 AI Decision Analysis")

        st.progress(int(probability * 100))

        st.info(
            f"Approval Probability : {round(probability * 100, 2)}%"
        )

        if pred_result[0] == 1:

            st.balloons()

            st.success("""
🎉 Congratulations!

Your Loan Application has been Approved.
            """)

        else:

            st.error("""
❌ Loan Application Rejected

Suggestions:
• Improve CIBIL Score
• Increase Income
• Reduce Loan Amount
            """)
