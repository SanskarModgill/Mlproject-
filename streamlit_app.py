import streamlit as st
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="📚"
)

st.title("📚 Student Performance Predictor")
st.write("Enter the student's details to predict their performance.")

# Gender
gender = st.selectbox(
    "Gender",
    ["female", "male"]
)

# Race/Ethnicity
race_ethnicity = st.selectbox(
    "Race / Ethnicity",
    [
        "group A",
        "group B",
        "group C",
        "group D",
        "group E"
    ]
)

# Education
parental_level_of_education = st.selectbox(
    "Parental Level of Education",
    [
        "bachelor's degree",
        "some college",
        "master's degree",
        "associate's degree",
        "high school",
        "some high school"
    ]
)

# Lunch
lunch = st.selectbox(
    "Lunch",
    ["standard", "free/reduced"]
)

# Test preparation
test_preparation_course = st.selectbox(
    "Test Preparation Course",
    ["none", "completed"]
)

# Scores
reading_score = st.number_input(
    "Reading Score",
    min_value=0,
    max_value=100,
    value=50
)

writing_score = st.number_input(
    "Writing Score",
    min_value=0,
    max_value=100,
    value=50
)

# Prediction
if st.button("Predict Performance"):

    data = CustomData(
        gender=gender,
        race_ethnicity=race_ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=reading_score,
        writing_score=writing_score
    )

    pred_df = data.get_data_as_frame()

    predict_pipeline = PredictPipeline()

    results = predict_pipeline.predict(pred_df)

    st.success(
        f"Predicted Math Score: {results[0]:.2f}"
    )