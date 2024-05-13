import streamlit as st
import func_main
import altair as alt


# 사이드바
select_company = st.sidebar.selectbox(
    '확인하고 싶은 기관을 선택하세요',
    func_main.get_data()
)

# 메인 페이지
if select_company == '전체':
    spot = '전북대 농업생명과학대학'
else:
    spot = select_company
st.title(f'{spot} 호실 사용 현황')

# 상세 페이지
df = func_main.second_data()
tmp_df = df[df['사용기관명'] == select_company]


## 상세페이지 - 전체
if select_company == '전체':

    chart = alt.Chart(df).mark_bar().encode(
        x='전용면적',
        y=alt.Y('사용기관명', axis=alt.Axis(title='사용기관명', labelFontSize=14))  # y 축의 라벨 크기를 조절합니다.
    ).properties(
        height=alt.Step(30)  # 그래프의 높이를 조절합니다.
    )
    st.altair_chart(chart, use_container_width=True)

    st.dataframe(df)

else:
    st.bar_chart(data=tmp_df, x='호실명', y='전용면적',) # color=None, width=0, height=0, use_container_width=True)

    st.dataframe(tmp_df)

#test



