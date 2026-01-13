# 배포 가이드

이 문서는 5학년 보건수업 홈페이지를 다양한 플랫폼에 배포하는 방법을 설명합니다.

## 🚀 배포 플랫폼 선택

### 1. Heroku (권장)
가장 간단한 배포 방법입니다.

#### 준비물
- [Heroku 계정](https://www.heroku.com) (무료)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- Git 설치

#### 배포 단계

```bash
# 1. Heroku에 로그인
heroku login

# 2. Heroku 앱 생성
heroku create your-app-name

# 3. 환경 변수 설정 (선택사항)
heroku config:set SECRET_KEY="your_secret_key"

# 4. 배포
git push heroku main
# 또는 main이 아닌 경우
git push heroku YOUR_BRANCH:main

# 5. 앱 확인
heroku open

# 6. 로그 확인
heroku logs --tail
```

### 2. Railway
현대적이고 사용하기 쉬운 배포 플랫폼입니다.

#### 배포 단계

1. [Railway.app](https://railway.app)에 접속하여 GitHub로 로그인
2. "New Project" 클릭
3. "Deploy from GitHub repo" 선택
4. 저장소 선택
5. 자동으로 `Procfile`과 `requirements.txt`를 인식합니다
6. 배포 완료!

### 3. PythonAnywhere
클라우드 기반 Python 호스팅입니다.

#### 배포 단계

1. [PythonAnywhere](https://www.pythonanywhere.com) 가입
2. Web 탭에서 "Add a new web app"
3. Manual configuration 선택
4. Python 3.11 선택
5. Git에서 코드 복제:
```bash
git clone https://github.com/yourusername/health-class-homepage.git
```
6. WSGI 설정 파일에서 경로 설정
7. 배포 완료!

### 4. Google Cloud Run
서버리스 배포로 비용 효율적입니다.

#### 준비물
- Google Cloud 계정
- [gcloud CLI](https://cloud.google.com/sdk/install)

#### 배포 단계

```bash
# 1. 프로젝트 설정
gcloud config set project YOUR_PROJECT_ID

# 2. Cloud Run에 배포
gcloud run deploy health-class-homepage \
  --source . \
  --platform managed \
  --region asia-northeast1

# 3. URL 확인
# 배포 후 표시되는 URL로 접속
```

## 🔧 배포 전 체크리스트

- [ ] `.env` 파일이 `.gitignore`에 포함되어 있는가?
- [ ] `requirements.txt`가 모든 의존성을 포함하고 있는가?
- [ ] `Procfile`이 올바르게 설정되어 있는가?
- [ ] Firebase 설정이 환경 변수로 관리되는가?
- [ ] 디버그 모드가 비활성화되어 있는가?

## ⚙️ 프로덕션 환경 설정

### Flask 설정

```python
# app.py
if os.environ.get('FLASK_ENV') == 'production':
    app.config['DEBUG'] = False
else:
    app.config['DEBUG'] = True
```

### 환경 변수 설정

배포 플랫폼에서 다음의 환경 변수를 설정하세요:

```
SECRET_KEY=your_secret_key_here
FLASK_ENV=production
```

### HTTPS/SSL 설정

대부분의 플랫폼이 자동으로 HTTPS를 제공합니다. 추가 설정은 필요 없습니다.

## 🔒 보안 권장사항

1. **SECRET_KEY 변경**
   - 강력한 무작위 문자열 생성:
   ```python
   import secrets
   print(secrets.token_hex(32))
   ```

2. **Firebase 규칙 설정**
   - Firebase Console에서 Database Rules 설정
   - 인증된 사용자만 접근 가능하도록 설정

3. **환경 변수 관리**
   - 민감한 정보는 환경 변수로 관리
   - `.env` 파일은 git에 포함하지 않기

## 🆘 배포 후 문제 해결

### 페이지가 업데이트되지 않음

```bash
# 캐시 클리어 (Heroku의 경우)
heroku restart

# 또는 특정 dyno 재시작
heroku ps:restart web
```

### 정적 파일이 로드되지 않음

1. `static/` 폴더가 존재하는지 확인
2. Flask 앱의 `static_folder` 설정 확인
3. 배포 로그에서 오류 메시지 확인

### 데이터베이스 연결 오류

1. Firebase 설정 확인
2. 네트워크 연결 확인
3. Firebase Rules가 올바르게 설정되어 있는지 확인

## 📊 배포 후 모니터링

### Heroku의 경우

```bash
# 실시간 로그 확인
heroku logs --tail

# 메트릭 확인
heroku logs --ps=web

# 에러만 필터링
heroku logs --grep "ERROR"
```

### Railway의 경우

- 대시보드에서 실시간 로그 확인
- Metrics 탭에서 성능 모니터링

## 📝 자동 배포 설정 (CI/CD)

### GitHub Actions를 사용한 자동 배포

`.github/workflows/deploy.yml` 파일 생성:

```yaml
name: Deploy to Heroku

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Heroku
        uses: akhileshns/heroku-deploy@v3.12.12
        with:
          heroku_api_key: ${{ secrets.HEROKU_API_KEY }}
          heroku_app_name: "your-app-name"
          heroku_email: "your-email@example.com"
```

## ✅ 배포 완료 후 테스트

1. 사이트에 접속하여 정상 작동 확인
2. 회원가입/로그인 테스트
3. 구글 로그인 테스트
4. 게시판 기능 테스트
5. 모바일 반응형 확인

---

**도움이 필요하신가요?** [Issues 페이지](https://github.com/yourusername/health-class-homepage/issues)에서 질문해주세요!
