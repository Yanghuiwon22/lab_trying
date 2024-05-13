# docker 업로드
## 01 기본 세팅
1. Dockerfile 생성
  ```
  FROM python:3.8
  
  WORKDIR /usr/src/app
  
  COPY . /usr/src/app
  
  RUN pip install -r requirements.txt
  
  CMD ["streamlit", "run", "main.py"]
  ```

2. requirements.txt 생성
   ```
   streamlit
   pandas
   ```

3. docker-compse.yml 생성
   ```
   version: '3'
   
   services:
      streamlit:
        build: .
        ports:
          - "8501:8501"
        volumes:
          - ./main.py:/app/main.py
      ```
## 02 터미널 작업 + filezila
1. filezila 접속 ( 포트번호 22 )
2. 새 디렉토리 생성
3. 로컬 -> 서버 디렉토리로 파일 복사
4. 터미널에서 서버로 접속
5. 명령어 실행
   ```
   docker compose build
   ```
   ```
   docker compose up
   ```

# 그래프 그리기
## 가로형 그래프 그리기
![image](https://github.com/Yanghuiwon22/lab_trying/assets/127187225/e7da0008-ee02-4ea2-b879-3ebc04dfb287)
1. altair 라이브러리 사용
   ```
   pip install altair
   ```
2. 그래프를 위한 초기 데이터값 설정

   ```
       chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('전용면적', axis=alt.Axis(title='전용면적', titleFontSize=17, titleFontWeight='bold')),
        y=alt.Y('사용기관명', axis=alt.Axis(title='사용기관명', titleFontSize=17, titleFontWeight='bold'))  # y 축의 라벨 크기를 조절합니다.
    ).properties(
        height=alt.Step(30)  # 그래프의 높이를 조절합니다.
    )
   ```

      * mark_bar() : 바 차트를 그리는 함수
                 ==> 선 그래프를 그리고 싶다면 mark_line()
     * encode() : 시각적 속성을 매핑하는데 사용 
                   ==> x축, y축, 레이블 등
     * properties() :  차트의 속성을 설정하는데 사용
                   ==> 차트의 크기, 넓이 등
4. 그래프 그리기
   ```
   st.altair_chart(chart, use_container_width=True)
   ```
## 그래프 물결선(waveform)추가


   
