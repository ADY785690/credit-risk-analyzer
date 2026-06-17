import streamlit as st

st.title("🏦 Credit Risk Analyzer")

income = st.number_input(
    "Annual Income (₹)",
    min_value=0,
    value=500000
)

loan = st.number_input(
    "Loan Amount (₹)",
    min_value=0,
    value=200000
)

credit_score = st.slider(
    "Credit Score",
    300,
    900,
    700
)

if st.button("Analyze Risk"):

    risk_score = (
        (loan / max(income,1))*100
    )

    if credit_score > 750 and risk_score < 50:
        st.success("✅ Low Credit Risk")

    elif credit_score > 650:
        st.warning("⚠ Medium Credit Risk")

    else:
        st.error("❌ High Credit Risk")

    st.metric(
        "Loan to Income Ratio %",
        round(risk_score,2)
    )
