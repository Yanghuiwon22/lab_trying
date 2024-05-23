import streamlit as st
import func_main
import altair as alt

import pandas as pd
import numpy as np

def draw_barchart(data):
    chart = alt.Chart(data).mark_bar().encode(
        x=alt.X('sum(전용면적)', axis=alt.Axis(title='전용면적', titleFontSize=17, titleFontWeight='bold')),
        y=alt.Y('사용기관명', sort='-x', axis=alt.Axis(title='사용기관명', titleFontSize=17, titleFontWeight='bold')),
        color=alt.Color('공간용도구분:N', legend=alt.Legend(title='공간용도구분'))
    ).properties(
        height=alt.Step(30)
    ).configure_axis(
        labelFontSize=10
    )
    st.altair_chart(chart, use_container_width=True)


# 데이터 전처리
csv_output = pd.read_csv('./output/output.csv')
csv_department = pd.read_csv('./output/output_department.csv')
csv_business = pd.read_csv('./output/output_bisiness.csv')

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


# 상세페이지 - 전체
if select_company == '전체':

    # 농업생명과학대 전체 호실 사용 현황
    total_df = csv_output[['사용기관명', '전용면적', '공간용도구분']]

    draw_barchart(total_df)
    # 학과/사업체 - 호실 사용 현황

    draw_barchart(csv_department)

    draw_barchart(csv_business)


    st.dataframe(df)

else:
    st.bar_chart(data=tmp_df, x='호실명', y='전용면적',) # color=None, width=0, height=0, use_container_width=True)

    st.dataframe(tmp_df)

#test



