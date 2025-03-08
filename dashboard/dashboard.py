import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('Dashboard Latihan Machine Learning_mc211d5y2136')

@st.cache_data 
def load_data():
    return pd.read_csv('Hour_day_df.csv')

df = load_data()

st.write('Berikut adalah dataset Hour_day_df:')
st.dataframe(df)

st.sidebar.header('Robby saidi prasetyo_mc211d5y2136')
selected_column = st.sidebar.selectbox('Pilih kolom untuk visualisasi:', df.columns)

st.subheader(f'Distribusi Kolom: {selected_column}')

fig, ax = plt.subplots()
sns.histplot(df[selected_column], bins=30, kde=True, ax=ax)
ax.set_title(f'Distribusi {selected_column}')
ax.set_xlabel(selected_column)
ax.set_ylabel('Frekuensi')

st.pyplot(fig)

if selected_column == 'cnt':
    st.subheader('Distribusi Jumlah Sewa Sepeda (cnt)')
    st.write('Berikut adalah distribusi jumlah sewa sepeda yang diaggregasi per hari:')
    
    
    fig_cnt, ax_cnt = plt.subplots()
    sns.barplot(df['cnt'], bins=30, kde=True, ax=ax_cnt)
    ax_cnt.set_title('Data Penyewaan Sepeda yang Diaggregasi per Hari (cnt)')
    ax_cnt.set_xlabel('Jumlah Sewa Sepeda')
    ax_cnt.set_ylabel('Frekuensi')
    
    # Tampilkan plot khusus untuk 'cnt'
    st.pyplot(fig_cnt)

if len(df.columns) > 1:
    st.sidebar.header('Scatter Plot')
    x_axis = st.sidebar.selectbox('Pilih sumbu X:', df.columns)
    y_axis = st.sidebar.selectbox('Pilih sumbu Y:', df.columns)
    
    st.subheader(f'Scatter Plot: {x_axis} vs {y_axis}')
    fig_scatter, ax_scatter = plt.subplots()
    sns.scatterplot(data=df, x=x_axis, y=y_axis, ax=ax_scatter)
    ax_scatter.set_title(f'{x_axis} vs {y_axis}')
    ax_scatter.set_xlabel(x_axis)
    ax_scatter.set_ylabel(y_axis)
    st.pyplot(fig_scatter)