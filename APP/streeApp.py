import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
import os

classifier=pickle.load(open("C:/Users/deepa/streamlit/rudra1.pkl","rb"))
def welcome():
    return 'welcome all'
def prediction(anxiety_level,self_esteem,mental_health_history,depression,sleep_quality,academic_performance,study_load,future_career_concerns):
    prediction = classifier.predict(
        [[anxiety_level,self_esteem,mental_health_history,depression,sleep_quality,academic_performance,study_load,future_career_concerns]])
    print(prediction)
    return prediction
def main():
      # giving the webpage a title
    st.title("Stress Level Predictions")

    # here we define some of the front end elements of the web page like
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Streamlit StressLevel ML App </h1>
    </div>
    """

    # this line allows us to display the front end aspects we have
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)

    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction
    anxiety_level = st.number_input("anxiety_level" )
    self_esteem = st.number_input("self_esteem" )
    mental_health_history = st.number_input("Pmental_health_history" )
    depression = st.number_input("depression" )



    sleep_quality = st.number_input("sleep_quality" )


    academic_performance = st.number_input("academic_performance" )
    study_load = st.number_input("study_load" )


    future_career_concerns = st.number_input("future_career_concerns" )

    result =" "

    # the below line ensures that when the button called 'Predict' is clicked,
    # the prediction function defined above is called to make the prediction
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(anxiety_level,self_esteem,mental_health_history,depression,sleep_quality,academic_performance,study_load,future_career_concerns)

        st.success(result)

if __name__=='__main__':
    main()
