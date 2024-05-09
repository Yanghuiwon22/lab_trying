import streamlit as st
import func_main

st.title('전북대 농업생명과학대 호실 사용 현')


st.sidebar.title('this is sidebar')
st.sidebar.text('체크박스에 표시될 문구')

# select_species 변수에 사용자가 선택한 값이 지정됩니다
select_company = st.sidebar.selectbox(
    '확인하고 싶은 기관을 선택하세요',
    [func_main.get_data()]
)

df = func_main.second_data()
# 원래 dataframe으로 부터 꽃의 종류가 선택한 종류들만 필터링 되어서 나오게 일시적인 dataframe을 생성합니다
tmp_df = df[df['사용기관명'] == select_company]
# 선택한 종의 맨 처음 5행을 보여줍니다
st.table(tmp_df)

st.write(func_main.second_data())

