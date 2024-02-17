# import streamlit as st

# st.set_page_config(
#     page_icon=":star:", 
#     page_title="Problem Statement"
# )

# st.header("Problem Statement")

# # Objective: 

# st.markdown(
#     """
    
#     Developing a machine learning model to predict crop yields in Sub-Saharan Africa based on 
#     various factors such as weather patterns, soil quality, irrigation systems, and farming techniques. 
#     This will help farmers make informed decisions regarding crop planting and harvesting, 
#     which can improve food security, reduce waste, and increase income for farmers. Predicting crop 
#     yields in Sub-Saharan Africa.
    
#     """
# )


import streamlit as st

# Set page configuration
st.set_page_config(
    page_icon=":seedling:",
    page_title="Crop Yield Prediction"
)

# Page title and subtitle
st.title("Crop Yield Prediction")
st.markdown("Helping farmers make informed decisions for improved crop yields in Sub-Saharan Africa")

# Problem statement
st.header("Problem Statement")

st.markdown(
    """
    Agriculture plays a crucial role in Sub-Saharan Africa, where it supports livelihoods 
    and food security for a large portion of the population. However, farmers in this region 
    face numerous challenges, including unpredictable weather patterns, limited access to 
    resources, and varying soil conditions.

    The goal of this project is to develop an advanced machine learning model that can accurately 
    predict crop yields in Sub-Saharan Africa. By considering various factors such as historical 
    weather data, soil quality, irrigation systems, and farming techniques, the model will provide 
    valuable insights to farmers, empowering them to make informed decisions regarding crop 
    planting, resource allocation, and harvesting.

    This predictive model will enable farmers to optimize their agricultural practices, improve 
    food security, reduce waste, and increase income. By harnessing the power of data-driven 
    decision-making, we aim to contribute to sustainable agriculture and economic growth in 
    Sub-Saharan Africa.

    **Objectives:**
    - Develop a machine learning model for crop yield prediction
    - Gather and analyze historical weather data
    - Incorporate soil quality and irrigation system information
    - Consider the impact of farming techniques and practices
    - Provide an intuitive interface for farmers to access predictions

    **Expected Outcomes:**
    - Accurate predictions of crop yields for various regions in Sub-Saharan Africa
    - Insights into the key factors influencing crop productivity
    - Empowerment of farmers through data-driven decision-making
    - Improved resource allocation and increased income for farmers

    **Impact:**
    By leveraging advanced machine learning techniques and integrating diverse data sources, 
    this project aims to revolutionize agricultural practices in Sub-Saharan Africa. The 
    predictive model will enable farmers to anticipate crop yields, plan for potential challenges, 
    and maximize productivity. Ultimately, this will contribute to food security, poverty 
    reduction, and sustainable economic development in the region.

    """
)