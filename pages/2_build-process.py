import streamlit as st

# Set page configuration
st.set_page_config(
    page_icon=":wrench:",
    page_title="Build Process"
)

# Page title
st.header("Build Process")

st.markdown(
    """
    ### Data Source and Processing Stages
    - Data gathering was done from [Kilimo Open Data](http://kilimodata.developlocal.org/dataset/?organization=crops).
    - The following steps were performed for data processing and visualization:
        1. Downloaded CSV data formats for various crop production in Kenyan counties per year.
        2. Conducted data exploration to detect and filter out illegal and null values.
        3. Visualized the data to identify outliers.
        4. Defined model inputs and outputs based on priority.

    ### Model Training
    - TensorFlow/Keras API was used for its ease of application.
    - Built a sequential model that takes region, crop, area units, and year values as inputs and predicts production and yield per unit area as outputs.
    - Training involved the following steps:
        1. Tested both Mean Absolute Error (MAE) and Mean Squared Error (MSE) loss functions.
        2. Utilized Adam optimization algorithm.
        3. Employed a variety of evaluation metrics.
    - Evaluated the model on test data.

    ### Model Testing Phase

    ### UI/UX Design and Building
    - Streamlit was used as the basic framework.
    - Designed a user-friendly interface that displays all relevant information.
    - Prioritized ease of interaction with the model.

    ### Model Deployment
    - Deployed the model for final usage.

    """
)
