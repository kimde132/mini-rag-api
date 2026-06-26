# Mini RAG API

FastAPI 기반 미니 RAG API 서버 학습 프로젝트입니다.

## 프로젝트 목표

이 프로젝트는 FastAPI를 활용해 AI 서비스의 기반이 되는 API 서버 구조를 학습하고, 최종적으로 문서 업로드, 임베딩, Vector DB 검색, LLM 답변 생성을 포함한 미니 RAG API 서버를 구현하는 것을 목표로 합니다.

현재 단계에서는 FastAPI의 기본 서버 실행, Health Check API, POST 요청, Request Body, Pydantic 입력값 검증을 학습합니다.

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

서버가 정상 실행되면 아래 주소로 접속할 수 있습니다.

```text
http://127.0.0.1:8000
```

## API 문서

서버 실행 후 아래 주소에서 Swagger API 문서를 확인할 수 있습니다.

```text
http://127.0.0.1:8000/docs
```

## API 목록

### Health Check API

서버가 정상적으로 실행 중인지 확인하는 API입니다.

```http
GET /health
```

응답 예시:

```json
{
  "status": "ok"
}
```

### Echo API

사용자가 보낸 메시지를 그대로 반환하는 테스트용 API입니다.
POST 요청, Request Body, Pydantic 입력값 검증을 학습하기 위해 작성했습니다.

```http
POST /echo
```

요청 예시:

```json
{
  "message": "안녕하세요"
}
```

응답 예시:

```json
{
  "message": "안녕하세요"
}
```

잘못된 요청 예시:

```json
{
  "msg": "안녕하세요"
}
```

위 요청은 서버가 기대하는 `message` 필드가 없기 때문에 `422 Unprocessable Entity` 에러가 발생합니다.

## 현재까지 학습한 내용

### FastAPI 기본 구조

```python
from fastapi import FastAPI

app = FastAPI()
```

`FastAPI()`를 통해 API 서버 애플리케이션 객체를 생성합니다.
이 객체에 `GET`, `POST` 등의 API 경로를 등록합니다.

### GET 요청

```python
@app.get("/health")
def health_check():
    return {"status": "ok"}
```

`GET` 요청은 주로 데이터를 조회하거나 서버 상태를 확인할 때 사용합니다.

### POST 요청

```python
@app.post("/echo")
def echo(request: EchoRequest):
    return {"message": request.message}
```

`POST` 요청은 사용자가 서버에 데이터를 보낼 때 사용합니다.

### Pydantic 입력값 검증

```python
from pydantic import BaseModel

class EchoRequest(BaseModel):
    message: str
```

Pydantic을 사용하면 사용자가 보낸 JSON 데이터의 구조와 타입을 검증할 수 있습니다.
위 코드에서는 `message` 필드가 반드시 있어야 하며, 문자열이어야 합니다.

## 현재 프로젝트 구조

```text
mini-rag-api/
├── main.py
├── requirements.txt
└── README.md
```

## 다음 학습 예정

* Response Model
* GET / POST 차이 정리
* Router 분리
* Request / Response 스키마 분리
* 에러 처리
* PostgreSQL 연동
* 파일 업로드 API
* RAG API 구조 설계
* Dockerfile 작성
* Docker Compose 구성
