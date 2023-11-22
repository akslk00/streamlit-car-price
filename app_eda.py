import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

def run_eda_app():
    st.subheader('데이터 분석')

    st.text('전체 데이터프레임 확인하기')
    df=pd.read_csv('./data/Car_Purchasing_Data.csv')
    st.dataframe(df)

    st.text('기초통계 데이터 확인하기')
    if st.checkbox('통계 데이터 보기'):
         st.dataframe(df.describe())
    else:
         st.text('')

    st.text('최대/최소 데이터 확인하기')
    column_list=df.columns[4:]
    select_column=st.selectbox('컬럼을 선택하세요',column_list)
    st.text(select_column+'컬럼의 최소값')
    st.dataframe(df.loc[df[select_column]==df[select_column].min(),])
    st.text(select_column+'컬럼의 최대값')
    st.dataframe(df.loc[df[select_column]==df[select_column].max(),])


    fig1=plt.figure()
    df[select_column].hist(bins=20)
    st.pyplot(fig1)
