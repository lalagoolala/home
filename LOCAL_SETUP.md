# 🚀 로컬 설정 및 실행 가이드

이 가이드를 따라 본인의 컴퓨터에서 프로젝트를 실행하고 개발할 수 있습니다.

## 📋 사전 요구사항

- **Python 3.8 이상** - [python.org에서 설치](https://www.python.org/downloads/)
- **Git** - [git-scm.com에서 설치](https://git-scm.com/)
- **코드 에디터** - VS Code, PyCharm 등

## 🔧 설치 및 실행

### 1단계: 저장소 복제

```bash
# GitHub에서 프로젝트 복제
git clone https://github.com/yourusername/health-class-homepage.git

# 프로젝트 폴더로 이동
cd health-class-homepage
```

### 2단계: 가상 환경 생성 및 활성화

#### Windows
```bash
# 가상 환경 생성
python -m venv venv

# 가상 환경 활성화
venv\Scripts\activate
```

#### Mac / Linux
```bash
# 가상 환경 생성
python3 -m venv venv

# 가상 환경 활성화
source venv/bin/activate
```

### 3단계: 패키지 설치

```bash
# pip 업그레이드 (선택사항)
pip install --upgrade pip

# requirements.txt에서 패키지 설치
pip install -r requirements.txt
```

### 4단계: 환경 변수 설정

`.env` 파일 생성 (`.env.example` 참고):

```bash
# Windows - Notepad로 생성
notepad .env

# Mac / Linux - nano로 생성
nano .env
```

파일 내용:
```
FLASK_ENV=development
SECRET_KEY=your_secret_key_here_change_this
```

### 5단계: 애플리케이션 실행

```bash
python app.py
```

또는 Windows에서:
```bash
python app.py
```

**출력 예시:**
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### 6단계: 브라우저에서 접속

브라우저를 열고 다음 주소로 접속:
```
http://localhost:5000
```

## 📁 프로젝트 구조

```
health-class-homepage/
├── app.py                      # Flask 메인 애플리케이션
├── wsgi.py                     # WSGI 진입점 (배포용)
├── requirements.txt            # Python 패키지 목록
├── Procfile                    # Heroku 배포 설정
├── runtime.txt                 # Python 버전 명시
├── .env.example                # 환경 변수 템플릿
├── .gitignore                  # Git 제외 파일 목록
├── .editorconfig               # 에디터 설정
│
├── templates/                  # HTML 템플릿
│   ├── base.html               # 기본 레이아웃
│   ├── index.html              # 홈 페이지
│   ├── login.html              # 로그인 페이지
│   ├── signup.html             # 회원가입 페이지
│   └── board.html              # 게시판 페이지
│
├── static/                     # 정적 파일
│   ├── css/                    # CSS 파일
│   └── js/                     # JavaScript 파일
│
├── .github/                    # GitHub 설정
│   ├── workflows/
│   │   └── deploy.yml          # 자동 배포 설정
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md
│       └── feature_request.md
│
└── docs/                       # 문서
    ├── README.md               # 프로젝트 설명서
    ├── CONTRIBUTING.md         # 기여 가이드
    ├── DEPLOYMENT.md           # 배포 가이드
    ├── TROUBLESHOOTING.md      # 문제 해결 가이드
    └── LOCAL_SETUP.md          # 로컬 설정 가이드
```

## 🔄 개발 워크플로우

### 변경사항 적용

```bash
# 파일 변경 후
git status                      # 변경사항 확인

git add .                       # 모든 변경사항 추가
# 또는 특정 파일만
git add filename.py

git commit -m "feat: 새로운 기능 추가"  # 커밋

git push origin main            # GitHub에 푸시
```

### 브랜치 생성 (새로운 기능 개발)

```bash
# 새 브랜치 생성
git checkout -b feature/my-feature

# 코드 작성 및 테스트
# ...

# 변경사항 커밋
git add .
git commit -m "feat: 새로운 기능"

# 브랜치 푸시
git push origin feature/my-feature

# GitHub에서 Pull Request 생성
```

## 🧪 로컬 테스트

### 회원가입 테스트

1. 브라우저에서 `http://localhost:5000/signup` 접속
2. 다음 정보 입력:
   - 이름: 테스트 사용자
   - 이메일: test@example.com
   - 학년 반 번호: 5학년 1반 1번
   - 비밀번호: testpass123
3. 회원가입 버튼 클릭

### 로그인 테스트

1. `http://localhost:5000/login` 접속
2. 위에서 가입한 이메일과 비밀번호 입력
3. 로그인 버튼 클릭

### 구글 로그인 테스트

1. 로그인/회원가입 페이지에서 구글 버튼 클릭
2. Google 로그인 팝업에서 테스트 계정으로 로그인

## 🐛 디버깅

### Flask Debug Toolbar 설정 (선택사항)

```bash
pip install flask-debugtoolbar
```

app.py에 추가:
```python
from flask_debugtoolbar import DebugToolbarExtension

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)
```

### 로그 확인

app.py에서 debug 출력 추가:
```python
@app.route('/')
def index():
    print("Index page accessed")  # 콘솔에 출력
    return render_template('index.html')
```

### 데이터베이스 확인

Firebase Console에서 실시간 데이터 확인:
1. [Firebase Console](https://console.firebase.google.com/)
2. 프로젝트 선택
3. Realtime Database 선택
4. 데이터 조회

## 🔒 환경 변수 관리

### 안전한 SECRET_KEY 생성

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

생성된 값을 `.env` 파일의 `SECRET_KEY`로 설정

## 📱 모바일 테스트

### 로컬 네트워크에서 접속

```bash
# 컴퓨터의 IP 주소 확인
ipconfig getifaddr en0  # Mac
ipconfig                # Windows

# 모바일에서 접속
# http://YOUR_IP_ADDRESS:5000
# 예: http://192.168.1.100:5000
```

## 🔌 외부 라이브러리 추가

새로운 패키지 설치 시:

```bash
# 패키지 설치
pip install package-name

# requirements.txt 업데이트
pip freeze > requirements.txt
```

## 🚨 자주 발생하는 문제

### "ModuleNotFoundError: No module named 'flask'"

해결:
```bash
# 가상 환경이 활성화되었는지 확인
which python  # Mac/Linux
where python  # Windows

# 패키지 재설치
pip install -r requirements.txt
```

### "Port 5000 already in use"

해결:
```bash
# 다른 포트 사용
python app.py --port 5001

# 또는 app.py 수정
app.run(port=5001)
```

### "Firebase authentication failed"

해결:
1. Firebase API Key 확인
2. 네트워크 연결 확인
3. Firebase 규칙 설정 확인

## 📚 학습 자료

- [Flask 공식 문서](https://flask.palletsprojects.com/)
- [Firebase 문서](https://firebase.google.com/docs)
- [Bootstrap 문서](https://getbootstrap.com/)
- [Python 공식 가이드](https://docs.python.org/3/)

## ✅ 다음 단계

1. **코드 이해하기** - `app.py`와 `templates/` 폴더의 파일 읽기
2. **기능 추가하기** - 새로운 기능 구현해보기
3. **배포하기** - Heroku, Railway 등에 배포
4. **피드백 공유하기** - 개선사항을 Issues에 등록

---

**도움이 필요하신가요?** [Issues 페이지](https://github.com/yourusername/health-class-homepage/issues)에서 질문해주세요!
