# Mini RAG API

FastAPI 기반 미니 RAG API 서버 학습 프로젝트입니다.

## 실행 방법

### 1. 가상환경 생성

```bash
python -m venv venv
```
### 2. 가상환경 실행

Git Bash:
```bash
source venv/Scripts/activate
```
PowerShell:
```bash
.\venv\Scripts\Activate.ps1
```
### 3. 패키지 설치
```bash
pip install -r requirements.txt
```
### 4. 서버 실행
```bash
uvicorn main:app --reload
```
### API 목록
Health Check
```bash
GET /health
```

응답 예시:
```bash
{
  "status": "ok"
}
```
API 문서

서버 실행 후 아래 주소에서 확인합니다.

http://127.0.0.1:8000/docs

---