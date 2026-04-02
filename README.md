# # 다국어 AI 감정 분석 시스템

🔗 **[사이트에서 직접 확인하기](https://share.streamlit.io/s26-30519-svg/ttt/main)**

## 목적
언어에 따른 AI 감정 분석 결과 차이를 분석한다.

## 기능
- 한국어, 영어, 소수언어 입력
- 감정 분석
- 결과 비교
- 편향 감지

## 결과
언어에 따라 서로 다른 결과가 나타나는 현상을 확인하였다.

## 배포 및 실행 안내

1. Streamlit Cloud(공개 URL)
   - https://share.streamlit.io/s26-30519-svg/ttt/main
   - 접근 오류(권한 없음) 시:
     - https://share.streamlit.io 에 로그인
     - 앱 페이지에서 Public 옵션 활성화 또는 필요한 사용자 추가
     - 재배포 후 표시된 URL로 접속

2. 로컬 실행 (다른 기기에서도 접속 가능)
   - `source .venv/bin/activate`
   - `streamlit run app.py --server.address 0.0.0.0 --server.port 8501`
   - 같은 네트워크에서 `http://<호스트_IP>:8501`

3. .venv 및 의존성 설치
   - `python3 -m venv .venv`
   - `pip install -r requirements.txt` 또는 `pip install streamlit transformers pandas`

4. 이슈 발생 시 확인
   - `streamlit run app.py` 터미널 로그
   - 코드스페이스/도커/로컬 여부
   - 포트 포워딩 여부 (8501)
