# 🏥 5학년 보건수업 홈페이지

> 초등학교 5학년 학생 및 학부모를 위한 **친화적이고 예쁜 보건 수업 홈페이지**

[![Python 3.x](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![Flask 2.3](https://img.shields.io/badge/Flask-2.3-green)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## ✨ 주요 특징

### 👨‍👩‍👧‍👦 사용자 친화적 디자인
- 🎨 **밝고 예쁜 컬러** - 5학년 학생들이 좋아하는 오렌지, 파랑, 보라색 조화
- 📱 **반응형 디자인** - 모든 기기에서 완벽하게 표시
- ✨ **부드러운 애니메이션** - 인터랙티브한 사용자 경험
- 🎉 **재미있는 이모지** - 친근하고 즐거운 느낌

### 🔐 안전한 계정 관리
- 📝 **회원가입** - 이름, 학년 반 번호, 비밀번호로 가입
- 🔐 **로그인** - 안전한 세션 기반 로그인
- 🔑 **구글 로그인** - Firebase 인증으로 간편한 구글 계정 연동
- ✅ **입력 검증** - 모든 입력값에 대한 검증
- 🛡️ **환경 변수 보안** - API 키는 환경 변수에서 로드하므로 GitHub에 안전하게 올릴 수 있음

### 📢 정보 공유
- **공지사항** - 보건 선생님의 중요한 소식 공유
- **질의응답** - 학생들의 건강 관련 질문과 답변
- **보안된 세션** - 로그인한 사용자 정보 안전 보관
- **건강 팁** - 홈페이지에 건강 생활 팁 표시

## 🛠 기술 스택

| 분류 | 기술 |
|------|------|
| **Backend** | Flask 2.3 |
| **Database** | Firebase Realtime Database |
| **Authentication** | Firebase Authentication (구글 로그인) |
| **Frontend** | HTML5, Bootstrap 5, JavaScript |
| **Fonts** | Noto Sans KR, Jua (구글 폰트) |
| **Configuration** | python-dotenv (환경 변수 관리) |

## 📋 설치 및 실행

### 1. 필수 사항
- Python 3.7 이상
- Git

### 2. 저장소 복제
```bash
git clone https://github.com/yourusername/health-class-homepage.git
cd health-class-homepage
```

### 3. 가상 환경 생성 (권장)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. 의존성 설치
```bash
pip install -r requirements.txt
```

### 5. 환경 변수 설정 (.env 파일 생성)
`.env.example` 파일을 참고하여 `.env` 파일을 생성합니다:

```bash
# Windows/macOS/Linux
cp .env.example .env
```

그 후 `.env` 파일을 열어서 아래 정보를 입력합니다:

```text
# Flask 환경 설정
FLASK_ENV=development
FLASK_DEBUG=True
FLASK_APP=app.py

# 보안 설정 (프로덕션에서는 반드시 변경하세요!)
SECRET_KEY=your-secret-key-change-this-in-production

# Firebase 설정 (https://console.firebase.google.com 에서 획득)
FIREBASE_API_KEY=your_firebase_api_key
FIREBASE_AUTH_DOMAIN=your_firebase_auth_domain
FIREBASE_PROJECT_ID=your_firebase_project_id
FIREBASE_STORAGE_BUCKET=your_firebase_storage_bucket
FIREBASE_MESSAGING_SENDER_ID=your_firebase_messaging_sender_id
FIREBASE_APP_ID=your_firebase_app_id
FIREBASE_DATABASE_URL=your_firebase_database_url

# 서버 설정
PORT=5000
```

**⚠️ 주의**: `.env` 파일은 `.gitignore`에 포함되어 있으므로 GitHub에 업로드되지 않습니다. 배포 시에만 서버의 환경 변수로 이 값들을 설정하면 됩니다.

### 6. 애플리케이션 실행
```bash
python app.py
```

브라우저에서 `http://localhost:5000` 으로 접속하세요! 🎉

## 📁 프로젝트 구조

```
health-class-homepage/
├── app.py                      # Flask 메인 애플리케이션
├── wsgi.py                     # WSGI 진입점 (배포용)
├── requirements.txt            # Python 패키지 의존성
├── .env.example                # 환경 변수 예제 (github에 올리는 파일)
├── .env                        # 환경 변수 (git에 추가하지 마세요 ✗)
├── .gitignore                  # Git 제외 파일 목록
├── README.md                   # 프로젝트 설명서
├── LICENSE                     # MIT 라이선스
├── Procfile                    # Heroku 배포 설정
├── runtime.txt                 # Python 버전 명시 (배포용)
├── templates/                  # HTML 템플릿
│   ├── base.html               # 기본 레이아웃 (네비게이션, 스타일)
│   ├── index.html              # 홈 페이지
│   ├── login.html              # 로그인 페이지
│   ├── signup.html             # 회원가입 페이지
│   └── board.html              # 게시판 페이지
├── static/                     # 정적 파일
│   ├── css/                    # CSS 파일
│   └── js/                     # JavaScript 파일
└── 깃허브최적화용/             # GitHub에 올릴 때 참고하는 파일들
```

## 🔑 주요 기능 설명

### 🏠 홈페이지 (`/`)
- 보건수업 홈페이지 안내
- 공지사항 및 질의응답 링크
- 건강 생활 팁 표시
- 미로그인 사용자용 회원가입/로그인 유도
- 로그인한 사용자에게 환영 메시지 표시

### 📝 회원가입 (`/signup`)
- 이름, 학년 반 번호, 비밀번호 입력
- 중복 아이디 확인
- 구글 계정 연동 가입 옵션
- 입력 검증

### 🔐 로그인 (`/login`)
- 아이디(이메일)와 비밀번호로 로그인
- 구글 계정 로그인 옵션
- 에러 메시지 표시
- 회원가입 링크 제공

### 📢 게시판 (`/board/<type>`)
- **공지사항** (`/board/notice`) - 보건 선생님의 공지사항
- **질의응답** (`/board/qna`) - 학생들의 질문과 답변

### 🚪 로그아웃 (`/logout`)
- 현재 세션 종료

## 🔒 보안 사항

✅ **안전한 설정:**
- 비밀번호는 6자 이상이어야 하며 Firebase에 저장됨
- 세션 기반 인증으로 사용자 정보 보호
- 구글 로그인은 Firebase OAuth 2.0을 사용하여 안전함
- **API 키는 환경 변수에서 로드되므로 GitHub에 노출되지 않음**
- `.env` 파일은 `.gitignore`에 포함되어 있음

⚠️ **주의사항:**
- `.env` 파일에는 민감한 정보(Firebase 키, SECRET_KEY)가 포함됨
- **`.env` 파일은 절대 Git에 커밋하지 마세요** (`.gitignore`에 추가됨)
- 배포 시 서버의 환경 변수 설정에서 `.env` 파일의 값들을 입력해야 함

## 🌐 GitHub에 안전하게 업로드하기

이 프로젝트는 환경 변수를 사용하여 민감한 정보를 보호하므로 **GitHub에 안전하게 업로드할 수 있습니다!**

### 1단계: `.gitignore` 확인
프로젝트 루트의 `.gitignore` 파일에 다음이 포함되어 있는지 확인합니다:
```
.env
.env.local
__pycache__/
venv/
```

### 2단계: `.env.example` 파일 제공
민감한 정보 없이 필요한 환경 변수 형식만 포함한 `.env.example` 파일이 있습니다. 이 파일은 GitHub에 올라갑니다.

### 3단계: GitHub에 업로드
```bash
# 변경사항 확인 (`.env` 파일이 포함되지 않아야 함)
git status

# 커밋 및 푸시
git add .
git commit -m "Add health class homepage"
git push origin main
```

### 4단계: 배포 시 환경 변수 설정
배포 플랫폼 (Heroku, Railway, 등)의 대시보드에서:
1. "Environment Variables" 또는 "Config Vars" 섹션 찾기
2. `.env` 파일의 모든 변수를 입력하기

## 🚀 배포 방법 (무료 호스팅)

이제 GitHub에서 안전하게 코드를 공유할 수 있습니다! 다음 플랫폼에서 무료로 배포 가능합니다:

### Heroku 배포 (권장 - 무료)
```bash
# 1. Heroku 로그인
heroku login

# 2. Heroku 앱 생성
heroku create your-app-name

# 3. 환경 변수 설정
heroku config:set FIREBASE_API_KEY=your_key
heroku config:set FIREBASE_AUTH_DOMAIN=your_domain
# ... (모든 환경 변수 설정)

# 4. 배포
git push heroku main
```

### Railway 배포 (추천)
1. [Railway.app](https://railway.app)에 GitHub 계정으로 로그인
2. "New Project" → "Deploy from GitHub"
3. 저장소 선택
4. Environment 탭에서 `.env` 파일의 변수들 입력
5. 자동으로 배포됨

### PythonAnywhere 배포
1. [PythonAnywhere.com](https://www.pythonanywhere.com)에 가입
2. "Web" 탭에서 Flask 앱 생성
3. GitHub에서 코드 클론
4. Web 설정에서 환경 변수 입력
5. Reload 버튼 클릭

자세한 배포 가이드는 [DEPLOYMENT.md](DEPLOYMENT.md)를 참고하세요.

## 👥 사용자 가이드

### 학생들을 위해
1. **회원가입**: 이름과 학년 반 번호를 입력하고 가입합니다
2. **로그인**: 아이디와 비밀번호로 로그인합니다
3. **공지사항 확인**: 보건 선생님의 중요한 소식을 확인합니다
4. **질문하기**: 궁금한 점을 질의응답 게시판에 남깁니다

### 학부모들을 위해
- 자녀의 건강 정보와 학교 공지사항을 한곳에서 확인할 수 있습니다
- 구글 계정으로 간편하게 로그인 가능합니다

## 📝 라이선스

이 프로젝트는 [MIT 라이선스](LICENSE)를 따릅니다.

## 🤝 기여 가이드

1. Fork 한 후 기능 브랜치를 생성합니다 (`git checkout -b feature/AmazingFeature`)
2. 변경사항을 커밋합니다 (`git commit -m 'Add some AmazingFeature'`)
3. 브랜치에 Push 합니다 (`git push origin feature/AmazingFeature`)
4. Pull Request를 생성합니다

## 🆘 문제 해결

### 홈페이지가 업데이트되지 않는 경우

1. **브라우저 캐시 클리어**: `Ctrl + Shift + Delete` (Windows) 또는 `Cmd + Shift + Delete` (Mac)
2. **강제 새로고침**: `Ctrl + F5` (Windows) 또는 `Cmd + Shift + R` (Mac)
3. **배포 서버 재시작**: 
   - Heroku: `heroku restart -a your-app-name`
   - Railway: 대시보드에서 "Redeploy" 클릭

### ".env 파일을 찾을 수 없다" 오류
- `.env.example` 파일을 `.env`로 복사하고 정보를 입력했는지 확인
- 로컬 개발 시: `copy .env.example .env` (Windows) 또는 `cp .env.example .env` (Mac/Linux)

### Firebase 연결 오류
- `.env` 파일의 Firebase 설정이 올바른지 확인
- [Firebase Console](https://console.firebase.google.com)에서 프로젝트 설정 다시 확인
- DATABASE_URL이 정확하게 입력되었는지 확인

자세한 해결 방법은 [TROUBLESHOOTING.md](TROUBLESHOOTING.md)를 참고하세요.

## 💻 로컬 설정 및 실행

로컬 환경에서 개발하려면 [LOCAL_SETUP.md](LOCAL_SETUP.md)를 따르세요.

## 📧 문의 및 피드백

문제가 생기거나 개선 사항이 있으시면 [이슈](https://github.com/yourusername/health-class-homepage/issues)를 등록해주세요.

## 🎓 학습 자료

이 프로젝트는 다음 기술들을 학습하는 데 도움이 됩니다:
- Flask 웹 프레임워크
- Firebase 데이터베이스 및 인증
- HTML/CSS/JavaScript
- Bootstrap 프레임워크
- 반응형 웹 디자인
- 환경 변수와 보안

## 🌟 개발 로드맵

- [ ] 게시글 작성 기능
- [ ] 파일 업로드 기능
- [ ] 댓글 기능
- [ ] 공지사항 카테고리 분류
- [ ] 검색 기능
- [ ] 사용자 프로필 페이지
- [ ] 알림 기능
- [ ] 다크 모드 지원

---

**만든이**: [Your Name]  
**마지막 업데이트**: 2024년 1월  
**GitHub**: https://github.com/yourusername/health-class-homepage