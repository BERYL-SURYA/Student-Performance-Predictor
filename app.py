import streamlit as st
import joblib
import pandas as pd
from src.pdf_report import generate_pdf

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("model/student_model.pkl")
encoder = joblib.load("model/label_encoder.pkl")
# Store prediction history
if "history" not in st.session_state:
    st.session_state.history = []
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# ============================
# Sidebar
# ============================

st.sidebar.title("🎓 Student Performance Predictor")

st.sidebar.markdown("---")

st.sidebar.header("📌 About")

st.sidebar.write("""
This application predicts a student's GPA using a Machine Learning model trained on academic and lifestyle factors.
""")

st.sidebar.markdown("---")

st.sidebar.header("🛠 Technologies")

st.sidebar.write("""
- Python
- Streamlit
- Pandas
- Scikit-learn
- Random Forest
""")

st.sidebar.markdown("---")

st.sidebar.header("👨‍💻 Developer")

st.sidebar.write("Beryl Surya")
st.markdown("""
<style>

.main {
    padding-top:20px;
}

h1{
    text-align:center;
    color:#1E88E5;
}

.stButton>button{
    width:100%;
    height:55px;
    border-radius:10px;
    background-color:#1E88E5;
    color:white;
    font-size:18px;
}

.stButton>button:hover{
    background-color:#1565C0;
}

</style>
""", unsafe_allow_html=True)
st.title("🎓 Student Performance Predictor")
st.write("Predict a student's GPA using Machine Learning.")

st.divider()
st.subheader("👨‍🎓 Student Details")

name = st.text_input("Student Name")

age = st.number_input(
    "Age",
    min_value=15,
    max_value=30,
    value=20
)

# -----------------------------
# User Inputs
# -----------------------------
study_hours = st.slider("Study Hours Per Day", 5.0, 10.0, 7.0)

extra_hours = st.slider("Extracurricular Hours Per Day", 0.0, 6.0, 2.0)

sleep_hours = st.slider("Sleep Hours Per Day", 3.0, 10.0, 7.0)

social_hours = st.slider("Social Hours Per Day", 0.0, 6.0, 2.0)

physical_hours = st.slider("Physical Activity Hours Per Day", 0.0, 8.0, 2.0)

stress = st.selectbox(
    "Stress Level",
    ["Low", "Moderate", "High"]
)

# Encode Stress Level
stress_encoded = encoder.transform([stress])[0]

# -----------------------------
# Prediction
# -----------------------------
# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict GPA"):

    input_data = pd.DataFrame({
        "Study_Hours_Per_Day": [study_hours],
        "Extracurricular_Hours_Per_Day": [extra_hours],
        "Sleep_Hours_Per_Day": [sleep_hours],
        "Social_Hours_Per_Day": [social_hours],
        "Physical_Activity_Hours_Per_Day": [physical_hours],
        "Stress_Level": [stress_encoded]
    })

    prediction = model.predict(input_data)[0]

    st.subheader("📊 Student Dashboard")

    st.write(f"### 👨‍🎓 Student : {name}")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🎯 GPA", round(prediction, 2))

    with col2:
        if prediction >= 3.7:
            performance = "Excellent"
        elif prediction >= 3.3:
            performance = "Very Good"
        elif prediction >= 2.7:
            performance = "Good"
        elif prediction >= 2.3:
            performance = "Average"
        else:
            performance = "Needs Improvement"

        st.metric("⭐ Performance", performance)

    with col3:
        st.metric("🔥 Stress", stress)

    st.subheader("📈 GPA Progress")

    progress = prediction / 4.0

    st.progress(progress)

    st.write(f"Current GPA: **{prediction:.2f} / 4.00**")

    

    st.divider()

    st.subheader("📝 Student Summary")

    st.info(f"""👨‍🎓 Student Name : {name}

    🎂 Age : {age}

    🔥 Stress Level : {stress}

    🎯 Predicted GPA : {prediction:.2f}

    ⭐ Performance : {performance}
    """)


    




    st.subheader("💡 Recommendations")

    if study_hours < 6:
        st.warning("📖 Increase your daily study hours.")

    if sleep_hours < 6:
        st.warning("😴 Get at least 7 hours of sleep.")

    if stress == "High":
        st.warning("🧘 Try reducing stress through exercise or meditation.")

    if physical_hours < 1:
        st.warning("🏃 Increase your physical activity.")

    if prediction >= 3.7:
        st.success("🎉 Excellent work! Keep maintaining your routine.")

    st.divider()

    st.subheader("📈 Feature Importance")

    st.image(
        "screenshots/feature_importance.png",
        caption="Feature Importance from Random Forest Model",
        use_container_width=True
    )

        # Save prediction history
    st.session_state.history.append({
        "Student": name,
        "Age": age,
        "Predicted GPA": round(prediction, 2),
        "Stress Level": stress
    })

    # Generate PDF
    pdf_file = generate_pdf(
        name,
        age,
        stress,
        prediction,
        performance
    )

    # Download PDF
    with open(pdf_file, "rb") as file:
        st.download_button(
            label="📄 Download Student Report",
            data=file,
            file_name="Student_Report.pdf",
            mime="application/pdf"
        )


st.divider()

st.subheader("📋 Prediction History")

if len(st.session_state.history) > 0:
    history_df = pd.DataFrame(st.session_state.history)
    st.dataframe(history_df, use_container_width=True)
else:
    st.info("No predictions made yet.")

if len(st.session_state.history) > 0:

    csv = history_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Prediction History",
        data=csv,
        file_name="prediction_history.csv",
        mime="text/csv"
    )




