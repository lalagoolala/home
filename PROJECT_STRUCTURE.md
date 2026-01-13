# 📚 프로젝트 인덱스

## 🗂️ 프로젝트 구조 안내

이 문서는 프로젝트의 전체 구조와 각 파일의 목적을 설명합니다.

### 핵심 애플리케이션 파일

```
app.py                          # Flask 메인 애플리케이션
```

- **용도**: Flask 웹 프레임워크의 메인 파일
- **주요 기능**: 
  - Flask 앱 초기화
  - 라우트(URL) 정의
  - Firebase 연동
  - 사용자 인증 관리

### 템플릿 폴더 (templates/)

```
templates/
├── base.html                   # 기본 레이아웃 템플릿
├── index.html                  # 홈페이지
├── login.html                  # 로그인 페이지
├── signup.html                 # 회원가입 페이지
└── board.html                  # 게시판 페이지
```

- **용도**: Flask Jinja2 템플릿
- **설명**: 모든 HTML 파일이 여기에 저장됨
- **구조**: base.html을 상속받아 일관된 스타일 유지

### 정적 파일 폴더 (static/)

```
static/
├── css/                        # CSS 파일 (향후 저장용)
└── js/                         # JavaScript 파일 (향후 저장용)
```

- **용도**: CSS, JavaScript, 이미지 등 정적 파일
- **현재 상태**: 구조만 생성됨 (향후 확장용)

### 설정 및 문서 파일

#### 필수 설정 파일

| 파일 | 설명 |
|------|------|
| `requirements.txt` | Python 패키지 의존성 |
| `.env` | 환경 변수 (git에 추가하지 않음) |
| `.env.example` | 환경 변수 예시 파일 |
| `.gitignore` | Git에서 제외할 파일 목록 |

#### 개발 도구 파일

| 파일 | 설명 |
|------|------|
| `.editorconfig` | 에디터 설정 (개발자 간 일관성) |
| `setup.cfg` | 패키지 설정 정보 |

#### 문서 파일

| 파일 | 설명 |
|------|------|
| `README.md` | 프로젝트 소개 및 설치 가이드 |
| `CONTRIBUTING.md` | 기여 가이드 |
| `CHANGELOG.md` | 버전 변경 이력 |
| `TODO.md` | 진행 상황 및 계획 |
| `LICENSE` | MIT 라이선스 |

#### GitHub 관련 파일

```
.github/
├── ISSUE_TEMPLATE/
│   ├── bug_report.md           # 버그 보고 템플릿
│   └── feature_request.md      # 기능 요청 템플릿
└── pull_request_template.md    # Pull Request 템플릿
```

### 레이아웃 레벨

```
프로젝트 루트
├── app.py (주 애플리케이션)
├── templates/ (HTML 템플릿)
├── static/ (CSS, JS, 이미지)
├── .github/ (GitHub 템플릿)
├── 설정 파일들 (.env, .gitignore, setup.cfg 등)
└── 문서 파일들 (README.md, CONTRIBUTING.md 등)
```

## 🚀 빠른 시작

### 1. 의존성 설치
```bash
pip install -r requirements.txt
```

### 2. 환경 변수 설정
```bash
# .env 파일 생성
cp .env.example .env
```

### 3. 애플리케이션 실행
```bash
python app.py
```

## 📝 파일별 상세 설명

### app.py
- **라인 1-11**: 라이브러리 import 및 초기화
- **라인 12-27**: Firebase 설정
- **라인 28-42**: 관리자 계정 생성 함수
- **라인 43-48**: 홈페이지 라우트
- **라인 49-75**: 회원가입 라우트 (POST/GET)
- **라인 76-102**: 로그인 라우트 (POST/GET)
- **라인 103-125**: 구글 로그인 처리
- **라인 126-130**: 로그아웃 라우트
- **라인 131-155**: 게시판 라우트

### base.html
- **헤더 섹션**: Bootstrap 및 폰트 로드
- **스타일 섹션**: 전체 디자인 CSS
- **네비게이션**: 헤더 메뉴
- **본문**: 각 페이지의 content 블록
- **푸터**: 저작권 정보

### templates/*.html
- 모든 페이지가 base.html을 상속
- `{% extends 'base.html' %}` 사용
- `{% block content %}...{% endblock %}` 내에 페이지별 컨텐츠

## 🔧 개발 팁

### 새로운 페이지 추가
1. `templates/` 폴더에 `new_page.html` 생성
2. `base.html`을 상속받기
3. `app.py`에서 라우트 정의

```python
@app.route('/new-page')
def new_page():
    return render_template('new_page.html')
```

### CSS 추가
1. `static/css/style.css` 생성 (아직 분리 안 됨)
2. `base.html`의 `<head>` 섹션에 링크 추가

### JavaScript 추가
1. `static/js/script.js` 생성 (아직 분리 안 됨)
2. `base.html`의 `</body>` 전에 스크립트 추가

## 📚 참고 자료

### 공식 문서
- [Flask 문서](https://flask.palletsprojects.com/)
- [Firebase 문서](https://firebase.google.com/docs)
- [Bootstrap 5 문서](https://getbootstrap.com/docs/5.0/)

### 코드 스타일
- Python: PEP 8 ([참고](https://www.python.org/dev/peps/pep-0008/))
- HTML/CSS: [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html)

## 🆘 문제 해결

### 포트 이미 사용 중
```bash
# Flask 기본 포트 변경
python -c "from app import app; app.run(port=8000)"
```

### Firebase 연결 오류
- Firebase 설정 정보 확인
- 인터넷 연결 확인
- 방화벽 설정 확인

### 템플릿을 찾을 수 없음
- `templates/` 폴더 존재 확인
- 파일명 대소문자 확인 (Linux에서는 대소문자 구별)

---

**마지막 업데이트**: 2024-01-13
