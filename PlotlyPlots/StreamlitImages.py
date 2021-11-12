import streamlit as st
from PIL import Image
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

#Loading dataset

data = pd.read_csv(r'C:\Users\Natasha\Desktop\respiratory_disease_detection\notebooks\out2.csv')

#Previewing data
data.head()

header = st.container()
dataset = st.container()
features = st.container()
mode_training = st.container()


with header:
    st.title('Respiratory Disease Detection Project')
    st.text('This page contains visualizations on the analysis on the on Respiratory Disease Analysis')

with features:
    st.header('These are plots on the Respiratory Diseases within the dataset')


    img1 = Image.open("Figure_1.png")
    st.image(img1)
    st.markdown('* **Fig.1** Shows the Distribution of Respiratory Diseases within the dataset.')
    

    img3 = Image.open("Figure_3.png")
    st.image(img3)
    st.markdown('* **Fig.2** Shows the relationship between the rate of infections between both sexes.')
  

    img5 = Image.open("Figure_5.png")
    st.image(img5)
    st.markdown('* **Fig.3** Shows the distribution of infections per age.')

    link = '[Tableau](https://public.tableau.com/app/profile/natasha.gwena/viz/RespiratoryDiseaseDetectionAnalysis/Story3?publish=yes)'
    st.markdown(link, unsafe_allow_html=True)

    














