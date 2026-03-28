import streamlit as st
from utils import train_model, detect_login_risk

st.set_page_config(
    page_title="Intelligent Login Risk Analyzer",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 Intelligent Login Risk Analyzer")
st.markdown("""
Welcome to the **Intelligent Login Risk Analyzer**.

This application evaluates a login attempt using:
- rule-based risk scoring
- behavioral risk factors
- machine learning anomaly detection

It helps identify whether a login is:
- low risk
- medium risk
- high risk
- potentially anomalous
""")


st.markdown("---")

@st.cache_resource
def load_resources():
    model, training_columns = train_model()
    return model, training_columns

model, training_columns = load_resources()

left_col, right_col = st.columns([1, 1.2])

with left_col:
    st.subheader("Login Input")

    user = st.selectbox(
        "User",
        [f"user{i}" for i in range(1, 21)]
    )

    time_str = st.text_input("Login Time (HH:MM)", value="10:30")

    location = st.selectbox(
        "Location",
        ["Dhaka", "Sylhet", "Khulna", "Rajshahi", "Chittagong", "India", "USA", "UK", "Russia"]
    )

    device_or_browser = st.selectbox(
        "Device / Browser",
        ["Chrome", "Edge", "Firefox", "Mobile"]
    )

    status = st.selectbox(
        "Login Status",
        ["success", "failed"]
    )


if analyze_clicked:
    try:
        result = detect_login_risk(
            user=user,
            time_str=time_str,
            location=location,
            device_or_browser=device_or_browser,
            status=status,
            model=model,
            training_columns=training_columns
        )

        with right_col:
            st.subheader("Detection Result")

            st.info(
                f"Summary: This login attempt was classified as "
                f"**{result['risk_level']} risk** with a final decision of "
                f"**{result['final_decision']}**."
            )

            st.write(f"**User:** {result['user']}")
            st.write(f"**Time:** {result['time']}")
            st.write(f"**Hour:** {result['hour']}")
            st.write(f"**Location:** {result['location']}")
            st.write(f"**Device / Browser:** {result['device_or_browser']}")
            st.write(f"**Status:** {result['status']}")

            col1, col2 = st.columns(2)
            col3, col4 = st.columns(2)

            col1.metric("Risk Score / 10", result["risk_score"])
            col2.metric("Risk Level", result["risk_level"])
            col3.metric("Final Decision", result["final_decision"])
            col4.metric("Alert", "Yes" if result["alert"] else "No")

            st.write(f"**Model Output:** {result['model_anomaly_label']}")

            st.markdown("---")
            st.subheader("Risk Factors")

            if result["risk_factors"]:
                for factor in result["risk_factors"]:
                    st.warning(f"⚠️ {factor}")
            else:
                st.success("✅ No major risk factors detected")

            st.markdown("---")

            if result["risk_level"] == "High":
                st.error("🔴 High Risk Login Detected")
            elif result["risk_level"] == "Medium":
                st.warning("🟡 Medium Risk Login")
            else:
                st.success("🟢 Low Risk Login")

            if result["alert"]:
                st.error("🚨 Alert: Suspicious login detected")
            else:
                st.success("✅ No immediate alert triggered")

    except Exception as e:
        with right_col:
            st.error(f"Error: {e}")