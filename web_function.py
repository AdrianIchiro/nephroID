import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import streamlit as st

@st.cache()
def load_data():
    df = pd.read_csv('kidney-disease.csv')