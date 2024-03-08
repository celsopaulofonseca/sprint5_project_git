import pandas as pd
import plotly_express as px
import streamlit as st

st.header('Dados sobre Veiculos')

car_data = pd.read_csv('vehicles.csv')
         
cria_histogram = st.checkbox('Criar histograma')
cria_scatter = st.checkbox('Criar gráfico de dispersão')

car_data = pd.read_csv('vehicles.csv')

# Check if the histogram checkbox is selected
if cria_histogram:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # Create a histogram
    fig_histogram = px.histogram(car_data, x="odometer")
     
    # Display an interactive Plotly chart for the histogram
    st.plotly_chart(fig_histogram, use_container_width=True)

# Check if the scatter plot checkbox is selected
if cria_scatter:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    
    # Create a scatter plot
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    
   # Display an interactive Plotly chart for the scatter plot
    st.plotly_chart(fig_scatter, use_container_width=True)