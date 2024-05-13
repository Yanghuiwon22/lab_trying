import streamlit as st
import func_main
import altair as alt

import pandas as pd
import numpy as np

# 사이드바
select_company = st.sidebar.selectbox(
    '확인하고 싶은 기관을 선택하세요',
    func_main.get_data()
)

st.write(func_main.get_data()[0])

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

    # 농업생명과학대 전체 호실 사용 현황
    x = func_main.get_data()[1:]
    y = func_main.group_area()
    df_group = pd.DataFrame({'사용기관명': x, '전용면적': y})

    chart = alt.Chart(df_group).mark_bar().encode(
        x=alt.X('전용면적', axis=alt.Axis(title='전용면적', titleFontSize=17, titleFontWeight='bold')),
        y=alt.Y('사용기관명', axis=alt.Axis(title='사용기관명', titleFontSize=17, titleFontWeight='bold'))  # y 축의 라벨 크기를 조절합니다.
    ).properties(
        height=alt.Step(30)  # 그래프의 높이를 조절합니다.
    )
    st.altair_chart(chart, use_container_width=True)

    # 학과/사업체 - 호실 사용 현황




    st.dataframe(df)

else:
    st.bar_chart(data=tmp_df, x='호실명', y='전용면적',) # color=None, width=0, height=0, use_container_width=True)

    st.dataframe(tmp_df)

#test



