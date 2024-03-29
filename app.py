import os
import json
from matplotlib import container
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import streamlit as st

from inference import make_prediction

st.set_page_config(page_icon=":star:", page_title="Crop Yields ML",  layout="wide")

data_source = "./data/cleaned_dataset.csv" # Or google drive

@st.cache_data()
def get_data():
    data = pd.read_csv(data_source)
    return data
data = get_data()    
data = data.rename(columns={
    "county": "county", 
    "year": "year", 
    "area (HA)": "area", 
    "production (MT)": "production", 
    "yield (MT/HA)": "yield", 
    "crop": "crop"
})

counties = list(data["county"].unique())
crops = list(data["crop"].unique())
years = list(data["year"].unique())      

side_bar = st.sidebar
with side_bar:
    st.subheader("About this app")
    st.write("---")
    st.markdown(
    """
    ### Data Source
    
    Agricultural production data for counties in Kenya was used in this project. 
    Data was downloaded from the following site:
    [Kilimo Open Data](http://kilimodata.developlocal.org/dataset/?organization=crops).

    
    The project focuses on the following crops:
    
    * Maize
    * Rice
    * Wheat
    * Sorghum
    * Dry beans
    
    
    This app is built to help users do crop yield predictions hence plan or make informed decisions.
    """
    )

main_col, right_col = st.columns([5, 2])

with main_col:  
    st.title("Crop Yield Prediction Model")
    st.write("---")

    st.markdown(
        """
        Kenya is among the Sub-Saharan countries. Therefore, this projects focuses on production 
        data for regions in Kenya. The Project went throught some phase that include: 
        
        * :star: Data gathering
        * :star: Data exploration
        * :star: Data cleaning
        * :star: Model Input definition
        * :star: Model Output definition
        * :star: Model training
        * :star: Model evaluation
        * :star: Model deployment
        """
    )

    st.subheader("An overview of the structure of data used:")
    st.write("---")
    st.write(data.head(5))
    st.subheader("An overview of data visualizations done: ")
    st.write("---")
    
    st.bar_chart(data=data, x='crop', y='production', use_container_width=True)
    st.write(":chart: Line charts:")
    pivot_df = pd.pivot_table(data, values='production', index=['crop'], columns=['year'])
    fig, ax = plt.subplots()
    pivot_df.plot(kind='line', ax=ax, figsize=[15, 5])
    plt.ylabel('Production')
    st.pyplot(fig)

    st.write(":bar_chart: Bar charts:")
    grouped_df = data.groupby(['crop', 'year'])['production'].sum()
    fig, ax = plt.subplots()
    ax.set_title(f'Total production by crop', fontsize=5)
    grouped_df.groupby(['crop']).sum().plot(ax=ax, kind='bar', ylabel='Total Production', 
                                            legend=False, figsize=[15, 5])
    plt.ylabel('Production')
    st.pyplot(fig)

    st.write(":pie: Pie Charts")
    year = st.selectbox("Select Year", years, index=years.index(2016))
    grouped_df = data.groupby(['crop', 'year'])['production'].sum()
    fig, ax = plt.subplots()
    grouped_df.loc[:, year].plot(ax=ax, kind='pie', ylabel='', autopct='%1.1f%%', figsize=[10, 5])
    ax.set_title('Total Production by Crop in {}'.format(year), fontsize=5)
    st.pyplot(fig)

with right_col:
    st.header("Prediction Engine")
    st.write("---")
    selected_crop = st.selectbox("Crop", crops)
    selected_year = st.selectbox("Year", [2016 + i for i in range(10)])
    selected_county = st.selectbox("Region", counties)
    target_area = st.number_input("Area Units (HA)", step=1)
    st.write("---")
    production, yields = make_prediction({
        "county": selected_county, 
        "crop": selected_crop, 
        "year": selected_year, 
        "area": target_area
    })
    st.write("Model projection for {} {} county.".format(selected_year, selected_county))
    st.write("Production in Metric tons: ", production)
    st.write("Yields per unit area (MT/ HA): ", yields)
    st.write("---")
    st.write("The model uses the following features to make predictions:")
    st.write("---")
    st.write("County: ", selected_county)
    st.write("Crop: ", selected_crop)
    st.write("Year: ", selected_year)
    st.write("Area: ", target_area)
    st.write("---")

    st.write("---")
    st.write("Objective: ")
    st.write("Developing a machine learning model to predict crop yields in Sub-Saharan Africa based on various factors such as weather patterns, soil quality, irrigation systems, and farming techniques. This will help farmers make informed decisions regarding crop planting and harvesting, which can improve food security, reduce waste, and increase income for farmers. Predicting crop yields in Sub-Saharan Africa.")
    st.write("---")