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
   
