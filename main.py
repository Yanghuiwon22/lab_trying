import streamlit as st
import func_main

st.title('전북대 농업생명과학대 호실 사용 현황')


st.sidebar.title('사업체별 확인')

# select_species 변수에 사용자가 선택한 값이 지정됩니다
select_company = st.sidebar.selectbox(
    '확인하고 싶은 기관을 선택하세요',
    func_main.get_data()
)

df = func_main.second_data()
tmp_df = df[df['사용기관명'] == select_company]

st.write(select_company)
st.dataframe(tmp_df)




