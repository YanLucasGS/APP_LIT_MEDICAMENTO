import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='App AEDA',page_icon="bar_chart:")

st.markdown('# Esta é uma aplicação de análise exploratória')

file = st.file_uploader('Faça o uipload do arquivo do consumidor', type=['CSV'])
file2 = st.file_uploader('Faça o uipload do arquivo do governo', type=['CSV'])

if file:
    df_consumidor = pd.read_csv(file,sep=';',encoding='ISO-8859-1')
    st.dataframe(df_consumidor.head())

    
if file2:
    df_governo = pd.read_csv(file2,sep=';',encoding='ISO-8859-1')
    st.dataframe(df_governo.head())