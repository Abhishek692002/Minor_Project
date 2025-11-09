# import streamlit as st

# st.set_page_config(page_title="Digital Fatigue Syndrome Checker", layout="centered")


# # ✅ Check login status
# if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
#     st.error("⚠️ You must login first to access the DFS Checker.")
#     st.stop()

# st.markdown(
#     "<h1 style='text-align:center; color:#2E86C1;'>💻 Digital Fatigue Syndrome Checker</h1>",
#     unsafe_allow_html=True
# )

# col1, col2 = st.columns(2)
# with col1:
#     screen_time = st.slider("Daily Screen Time (hours)", 0, 16, 4)
#     continuous_use = st.slider("Continuous Use (hours without break)", 0, 8, 2)
#     breaks = st.slider("Number of Breaks per day", 0, 10, 2)
#     sleep_hours = st.slider("Sleep Hours", 0, 12, 7)

# with col2:
#     headache = st.radio("Headache?", ["No", "Yes"], horizontal=True)
#     eyestrain = st.radio("Eye Strain?", ["No", "Yes"], horizontal=True)
#     neckpain = st.radio("Neck Pain?", ["No", "Yes"], horizontal=True)

# if st.button("Check DFS Risk"):
#     # Improved scoring logic for better accuracy
#     risk_score = (
#         screen_time * 3
#         + continuous_use * 3
#         - breaks * 2
#         + (3 if headache == "Yes" else 0)
#         + (3 if eyestrain == "Yes" else 0)
#         + (3 if neckpain == "Yes" else 0)
#         - sleep_hours * 2
#     )

#     # Updated thresholds for better prediction alignment
#     if risk_score <= 8:
#         st.success("✅ Predicted DFS Risk: Low")
#         st.write("Your DFS risk is low. Keep maintaining healthy habits!")
#     elif risk_score <= 15:
#         st.warning("⚠️ Predicted DFS Risk: Medium")
#         st.write("Moderate risk. Take frequent breaks and reduce screen time.")
#     else:
#         st.error("🚨 Predicted DFS Risk: High")
#         st.write("High risk! Reduce screen exposure, take breaks, and ensure proper sleep.")


# import streamlit as st

# st.set_page_config(page_title="Digital Fatigue Syndrome Checker", layout="centered")


# # ✅ Check login status
# if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
#     st.error("⚠️ You must login first to access the DFS Checker.")
#     st.stop()

# st.markdown(
#     "<h1 style='text-align:center; color:#2E86C1;'>💻 Digital Fatigue Syndrome Checker</h1>",
#     unsafe_allow_html=True
# )

# col1, col2 = st.columns(2)
# with col1:
#     screen_time = st.slider("Daily Screen Time (hours)", 0, 16, 4)
#     continuous_use = st.slider("Continuous Use (hours without break)", 0, 8, 2)
#     breaks = st.slider("Number of Breaks per day", 0, 10, 2)
#     sleep_hours = st.slider("Sleep Hours", 0, 12, 7)

# with col2:
#     headache = st.radio("Headache?", ["No", "Yes"], horizontal=True)
#     eyestrain = st.radio("Eye Strain?", ["No", "Yes"], horizontal=True)
#     neckpain = st.radio("Neck Pain?", ["No", "Yes"], horizontal=True)

# if st.button("Check DFS Risk"):
#     # Improved scoring logic for better accuracy
#     risk_score = (
#         screen_time * 3
#         + continuous_use * 3
#         - breaks * 2
#         + (3 if headache == "Yes" else 0)
#         + (3 if eyestrain == "Yes" else 0)
#         + (3 if neckpain == "Yes" else 0)
#         - sleep_hours * 2
#     )

#     # Updated thresholds for better prediction alignment
#     if risk_score <= 8:
#         st.success("✅ Predicted DFS Risk: Low")
#         st.write("Your DFS risk is low. Keep maintaining healthy habits!")
#     elif risk_score <= 15:
#         st.warning("⚠️ Predicted DFS Risk: Medium")
#         st.write("Moderate risk. Take frequent breaks and reduce screen time.")
#     else:
#         st.error("🚨 Predicted DFS Risk: High")
#         st.write("High risk! Reduce screen exposure, take breaks, and ensure proper sleep.")

import pandas as pd
import datetime
import os
import streamlit as st

st.set_page_config(
    page_title="Digital Fatigue Syndrome Checker", layout="centered")

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

# 🔹 Only run the risk calculation and saving if button clicked
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
    # if risk_score <= 8:
    #     fatigue_level = "Low"
    #     st.success("✅ Predicted DFS Risk: Low")
    #     st.write("Your DFS risk is low. Keep maintaining healthy habits!")
    # elif risk_score <= 15:
    #     fatigue_level = "Medium"
    #     st.warning("⚠️ Predicted DFS Risk: Medium")
    #     st.write("Moderate risk. Take frequent breaks and reduce screen time.")
    # else:
    #     fatigue_level = "High"
    #     st.error("🚨 Predicted DFS Risk: High")
    #     st.write(
    #         "High risk! Reduce screen exposure, take breaks, and ensure proper sleep.")

    if risk_score <= 8:
        fatigue_level = "Low"
        st.success("✅ Predicted DFS Risk: Low")

        st.markdown(
            """
        <div style='background-color:#D4EFDF; padding:10px; border-radius:10px;'>
        <h4 style='color:#196F3D;'>💡 Recommendation:</h4>
        <ul>
            <li>Maintain your healthy habits!</li>
            <li>Continue taking short breaks every hour.</li>
            <li>Keep your screen brightness moderate.</li>
            <li>Try to maintain 7–8 hours of sleep daily.</li>
        </ul>
        </div>
        """,
            unsafe_allow_html=True
        )

    elif risk_score <= 15:
        fatigue_level = "Medium"
        st.warning("⚠️ Predicted DFS Risk: Medium")

        st.markdown(
            """
        <div style='background-color:#FCF3CF; padding:10px; border-radius:10px;'>
        <h4 style='color:#9A7D0A;'>💡 Recommendation:</h4>
        <ul>
            <li>Take 10-minute breaks after every hour of screen time.</li>
            <li>Reduce continuous use and stretch regularly.</li>
            <li>Follow the 20-20-20 rule: Every 20 mins, look 20 feet away for 20 seconds.</li>
            <li>Maintain good posture and adjust your screen height.</li>
        </ul>
        </div>
        """,
            unsafe_allow_html=True
        )

    else:
        fatigue_level = "High"
        st.error("🚨 Predicted DFS Risk: High")

        st.markdown(
            """
        <div style='background-color:#F5B7B1; padding:10px; border-radius:10px;'>
        <h4 style='color:#922B21;'>💡 Recommendation:</h4>
        <ul>
            <li>Take an immediate 15–20 minute screen break.</li>
            <li>Perform eye relaxation exercises or blink often.</li>
            <li>Reduce your total daily screen time if possible.</li>
            <li>Ensure at least 7 hours of sleep tonight.</li>
            <li>If fatigue persists, consider consulting an eye specialist.</li>
        </ul>
        </div>
        """,
            unsafe_allow_html=True
        )

    # ---- Save result to history ----
    today = datetime.date.today()
    record = pd.DataFrame({
        "Date": [today],
        "Risk_Score": [risk_score],
        "Fatigue_Level": [fatigue_level]
    })

    # Append to CSV file (creates it if it doesn’t exist)
    if not os.path.exists("fatigue_history.csv"):
        record.to_csv("fatigue_history.csv", index=False)
    else:
        record.to_csv("fatigue_history.csv", mode='a',
                      header=False, index=False)

# ---- View past results ----
st.subheader("📊 View Your Fatigue History")
if st.button("View History"):
    if os.path.exists("fatigue_history.csv"):
        history = pd.read_csv("fatigue_history.csv")
        st.dataframe(history.tail(10))  # show last 10 entries
        st.line_chart(history["Risk_Score"])  # simple chart
    else:
        st.info("No history found yet. Run a fatigue check first.")


# ---- Clear history ----
if st.button("🗑️ Clear History"):
    if os.path.exists("fatigue_history.csv"):
        os.remove("fatigue_history.csv")
        st.success("✅ History cleared successfully.")
    else:
        st.info("No history file found to delete.")
# import streamlit as st

# st.set_page_config(page_title="Digital Fatigue Syndrome Checker", layout="centered")


# # ✅ Check login status
# if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
#     st.error("⚠️ You must login first to access the DFS Checker.")
#     st.stop()

# st.markdown(
#     "<h1 style='text-align:center; color:#2E86C1;'>💻 Digital Fatigue Syndrome Checker</h1>",
#     unsafe_allow_html=True
# )

# col1, col2 = st.columns(2)
# with col1:
#     screen_time = st.slider("Daily Screen Time (hours)", 0, 16, 4)
#     continuous_use = st.slider("Continuous Use (hours without break)", 0, 8, 2)
#     breaks = st.slider("Number of Breaks per day", 0, 10, 2)
#     sleep_hours = st.slider("Sleep Hours", 0, 12, 7)

# with col2:
#     headache = st.radio("Headache?", ["No", "Yes"], horizontal=True)
#     eyestrain = st.radio("Eye Strain?", ["No", "Yes"], horizontal=True)
#     neckpain = st.radio("Neck Pain?", ["No", "Yes"], horizontal=True)

# if st.button("Check DFS Risk"):
#     # Improved scoring logic for better accuracy
#     risk_score = (
#         screen_time * 3
#         + continuous_use * 3
#         - breaks * 2
#         + (3 if headache == "Yes" else 0)
#         + (3 if eyestrain == "Yes" else 0)
#         + (3 if neckpain == "Yes" else 0)
#         - sleep_hours * 2
#     )

#     # Updated thresholds for better prediction alignment
#     if risk_score <= 8:
#         st.success("✅ Predicted DFS Risk: Low")
#         st.write("Your DFS risk is low. Keep maintaining healthy habits!")
#     elif risk_score <= 15:
#         st.warning("⚠️ Predicted DFS Risk: Medium")
#         st.write("Moderate risk. Take frequent breaks and reduce screen time.")
#     else:
#         st.error("🚨 Predicted DFS Risk: High")
#         st.write("High risk! Reduce screen exposure, take breaks, and ensure proper sleep.")

import pandas as pd
import datetime
import os
import streamlit as st

st.set_page_config(
    page_title="Digital Fatigue Syndrome Checker", layout="centered")

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

# 🔹 Only run the risk calculation and saving if button clicked
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
    # if risk_score <= 8:
    #     fatigue_level = "Low"
    #     st.success("✅ Predicted DFS Risk: Low")
    #     st.write("Your DFS risk is low. Keep maintaining healthy habits!")
    # elif risk_score <= 15:
    #     fatigue_level = "Medium"
    #     st.warning("⚠️ Predicted DFS Risk: Medium")
    #     st.write("Moderate risk. Take frequent breaks and reduce screen time.")
    # else:
    #     fatigue_level = "High"
    #     st.error("🚨 Predicted DFS Risk: High")
    #     st.write(
    #         "High risk! Reduce screen exposure, take breaks, and ensure proper sleep.")

    if risk_score <= 8:
        fatigue_level = "Low"
        st.success("✅ Predicted DFS Risk: Low")

        st.markdown(
        """
        <div style='background-color:#D4EFDF; padding:10px; border-radius:10px;'>
        <h4 style='color:#196F3D;'>💡 Recommendation:</h4>
        <ul>
            <li>Maintain your healthy habits!</li>
            <li>Continue taking short breaks every hour.</li>
            <li>Keep your screen brightness moderate.</li>
            <li>Try to maintain 7–8 hours of sleep daily.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    elif risk_score <= 15:
        fatigue_level = "Medium"
        st.warning("⚠️ Predicted DFS Risk: Medium")

        st.markdown(
        """
        <div style='background-color:#FCF3CF; padding:10px; border-radius:10px;'>
        <h4 style='color:#9A7D0A;'>💡 Recommendation:</h4>
        <ul>
            <li>Take 10-minute breaks after every hour of screen time.</li>
            <li>Reduce continuous use and stretch regularly.</li>
            <li>Follow the 20-20-20 rule: Every 20 mins, look 20 feet away for 20 seconds.</li>
            <li>Maintain good posture and adjust your screen height.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    else:
        fatigue_level = "High"
        st.error("🚨 Predicted DFS Risk: High")

        st.markdown(
        """
        <div style='background-color:#F5B7B1; padding:10px; border-radius:10px;'>
        <h4 style='color:#922B21;'>💡 Recommendation:</h4>
        <ul>
            <li>Take an immediate 15–20 minute screen break.</li>
            <li>Perform eye relaxation exercises or blink often.</li>
            <li>Reduce your total daily screen time if possible.</li>
            <li>Ensure at least 7 hours of sleep tonight.</li>
            <li>If fatigue persists, consider consulting an eye specialist.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---- Save result to history ----
    today = datetime.date.today()
    record = pd.DataFrame({
        "Date": [today],
        "Risk_Score": [risk_score],
        "Fatigue_Level": [fatigue_level]
    })

    # Append to CSV file (creates it if it doesn’t exist)
    if not os.path.exists("fatigue_history.csv"):
        record.to_csv("fatigue_history.csv", index=False)
    else:
        record.to_csv("fatigue_history.csv", mode='a',
                      header=False, index=False)

# ---- View past results ----
st.subheader("📊 View Your Fatigue History")
if st.button("View History"):
    if os.path.exists("fatigue_history.csv"):
        history = pd.read_csv("fatigue_history.csv")
        st.dataframe(history.tail(10))  # show last 10 entries
        st.line_chart(history["Risk_Score"])  # simple chart
    else:
        st.info("No history found yet. Run a fatigue check first.")


# ---- Clear history ----
if st.button("🗑️ Clear History"):
    if os.path.exists("fatigue_history.csv"):
        os.remove("fatigue_history.csv")
        st.success("✅ History cleared successfully.")
    else:
        st.info("No history file found to delete.")