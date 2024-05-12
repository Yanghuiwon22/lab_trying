import streamlit as st
import func_main

# 메인 페이지
st.title('전북대 농업생명과학대 호실 사용 현황')


# 사이드바
select_company = st.sidebar.selectbox(
    '확인하고 싶은 기관을 선택하세요',
    func_main.get_data()
)

# 상세 페이지
df = func_main.second_data()
tmp_df = df[df['사용기관명'] == select_company]

## 상세페이지 - 전체
if select_company == '전체':
    st.dataframe(df)
else:
    st.write(select_company)
    st.dataframe(tmp_df)




