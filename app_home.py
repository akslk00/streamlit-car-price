import streamlit as st

def run_home_app():
    st.subheader('Welcome~~')
    st.text('이앱은 고객데이터와 자동차 구매데이터에 대한 내용입니다.')
    st.text('고객정보를 넣으면 차 구매 금액도 예측해줍니다')

    img_url ='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqEgiaW68Tsp6nGBbZtF1rHsahh2XXT7wW6w&usqp=CAU'
    st.image(img_url)
