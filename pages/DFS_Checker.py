import streamlit as st

st.set_page_config(page_title="Digital Fatigue Syndrome Checker", layout="centered")


# ✅ Check login status
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.error("⚠️ You must login first to access the DFS Checker.")
    st.stop()

st.markdown(
    "<h1 style='text-align:center; color:#2E86C1;'>💻 Digital Fatigue Syndrome Checker</h1>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)
with col1:
    screen_time = st.slider("Daily Screen Time (hours)", 0, 16, 4)
    continuous_use = st.slider("Continuous Use (hours without break)", 0, 8, 2)
    breaks = st.slider("Number of Breaks per day", 0, 10, 2)
    sleep_hours = st.slider("Sleep Hours", 0, 12, 7)

with col2:
    headache = st.radio("Headache?", ["No", "Yes"], horizontal=True)
    eyestrain = st.radio("Eye Strain?", ["No", "Yes"], horizontal=True)
    neckpain = st.radio("Neck Pain?", ["No", "Yes"], horizontal=True)

if st.button("Check DFS Risk"):
    # Improved scoring logic for better accuracy
    risk_score = (
        screen_time * 3
        + continuous_use * 3
        - breaks * 2
        + (3 if headache == "Yes" else 0)
        + (3 if eyestrain == "Yes" else 0)
        + (3 if neckpain == "Yes" else 0)
        - sleep_hours * 2
    )

    # Updated thresholds for better prediction alignment
    if risk_score <= 8:
        st.success("✅ Predicted DFS Risk: Low")
        st.write("Your DFS risk is low. Keep maintaining healthy habits!")
    elif risk_score <= 15:
        st.warning("⚠️ Predicted DFS Risk: Medium")
        st.write("Moderate risk. Take frequent breaks and reduce screen time.")
    else:
        st.error("🚨 Predicted DFS Risk: High")
        st.write("High risk! Reduce screen exposure, take breaks, and ensure proper sleep.")
