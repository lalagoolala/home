# 홈페이지가 업데이트되지 않는 문제 해결

홈페이지에 변경사항을 적용했는데도 새롭게 보이지 않는 경우의 해결 방법입니다.

## 🔍 문제 원인

1. **브라우저 캐시** - 이전에 로드된 파일이 캐시되어 있음
2. **서버 캐시** - 배포 서버의 캐시 문제
3. **정적 파일 캐시** - CSS, JavaScript 파일이 캐시되어 있음
4. **CDN 캐시** - Bootstrap 같은 외부 라이브러리 캐시
5. **서버가 재시작되지 않음** - 새로운 코드가 아직 실행되지 않음

## 💻 해결 방법

### 1단계: 브라우저 캐시 클리어

#### Chrome/Edge
- `Ctrl + Shift + Delete` (Windows)
- `Cmd + Shift + Delete` (Mac)
- "Cached images and files" 선택
- "All time" 선택
- "Clear data" 클릭

#### Firefox
- `Ctrl + Shift + Delete` (Windows)
- `Cmd + Shift + Delete` (Mac)
- "Cache" 선택
- "Clear Now" 클릭

#### Safari
- 메뉴 → Preferences
- Advanced 탭 → "Show Develop menu in menu bar" 활성화
- Develop → Empty Caches

### 2단계: 강제 새로고침 (Hard Refresh)

- `Ctrl + F5` (Windows)
- `Cmd + Shift + R` (Mac)
- `Ctrl + Shift + R` (Linux)

또는
- `Ctrl + Shift + Delete` 후 캐시 클리어 후 페이지 새로고침

### 3단계: 배포 서버 재시작

#### Heroku의 경우

```bash
# 1. Heroku CLI 설치 (이미 설치한 경우 생략)
# Windows: choco install heroku
# Mac: brew install heroku
# Linux: curl https://cli-assets.heroku.com/install.sh | sh

# 2. Heroku에 로그인
heroku login

# 3. 앱 확인
heroku apps

# 4. 앱 재시작
heroku restart -a your-app-name

# 5. 실시간 로그 확인
heroku logs -a your-app-name --tail
```

#### Railway의 경우

1. [Railway 대시보드](https://railway.app)에 접속
2. 프로젝트 선택
3. "Deployments" 탭
4. 최신 배포 옆의 "..." 클릭
5. "Redeploy" 선택

#### PythonAnywhere의 경우

1. PythonAnywhere 대시보드 접속
2. "Web" 탭
3. 앱 선택
4. "Reload" 버튼 클릭

### 4단계: GitHub에서 재배포

```bash
# 최신 변경사항이 GitHub에 푸시되었는지 확인
git status

# 변경사항 추가
git add .

# 커밋
git commit -m "fix: 홈페이지 업데이트 안 되는 문제 해결"

# 푸시 (자동 배포 트리거)
git push origin main

# 또는 특정 브랜치에 푸시
git push origin your-branch-name
```

### 5단계: 파일 구조 확인

```bash
# 프로젝트 루트에서 확인
ls -la

# 다음 파일들이 있는지 확인:
# - app.py (메인 Flask 앱)
# - Procfile (배포 설정)
# - requirements.txt (패키지 목록)
# - templates/ (HTML 폴더)
# - static/ (CSS, JS 폴더)
```

### 6단계: 배포 로그 확인

#### Heroku 로그 확인

```bash
# 전체 로그
heroku logs -a your-app-name

# 실시간 로그 (꼬리 모드)
heroku logs -a your-app-name --tail

# 특정 앱의 최근 로그
heroku logs -a your-app-name -n 50

# 에러만 필터링
heroku logs -a your-app-name | grep ERROR
```

#### Railway 로그 확인

대시보드 → Deployments → 배포 선택 → "Logs" 탭

#### PythonAnywhere 로그 확인

Web 탭 → "Error log" 또는 "Server log" 확인

## 🔧 근본적인 해결 방법

### 1. app.py 캐시 설정 수정

```python
# 개발 환경
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # 캐시 비활성화

# 프로덕션 환경 (1시간 캐시)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 3600
```

### 2. HTML에 메타 태그 추가

```html
<!-- base.html <head> 섹션에 추가 -->
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
```

### 3. 정적 파일 버전 관리

```html
<!-- CSS 파일에 버전 추가 -->
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}?v={{ version }}">

<!-- JavaScript 파일에 버전 추가 -->
<script src="{{ url_for('static', filename='script.js') }}?v={{ version }}"></script>
```

### 4. 배포 전 확인 사항

- [ ] 모든 변경사항이 git에 커밋되었는가?
- [ ] GitHub에 푸시했는가?
- [ ] `requirements.txt`가 최신 패키지 버전을 포함하는가?
- [ ] `Procfile`이 올바른가?
- [ ] 환경 변수가 배포 플랫폼에 설정되어 있는가?

## 📋 체크리스트

홈페이지가 업데이트되지 않을 때 순서대로 시도해보세요:

- [ ] 1단계: 브라우저 캐시 클리어
- [ ] 2단계: 강제 새로고침
- [ ] 3단계: 배포 서버 재시작
- [ ] 4단계: GitHub에서 재배포
- [ ] 5단계: 파일 구조 확인
- [ ] 6단계: 배포 로그 확인

## 🆘 문제가 계속 발생하는 경우

### GitHub Issues에 보고

1. [Issues 페이지](https://github.com/yourusername/health-class-homepage/issues)에서 "New Issue" 클릭
2. 다음 정보 포함:
   - 무엇을 변경했는가?
   - 어디에 배포했는가? (Heroku, Railway 등)
   - 배포 로그의 오류 메시지
   - 예상한 결과 vs 실제 결과

### 배포 로그 수집

```bash
# Heroku의 경우
heroku logs -a your-app-name -n 100 > deployment.log
```

이 파일을 GitHub Issue에 첨부하면 문제 해결에 도움이 됩니다.

## 💡 팁

1. **Development 모드에서 테스트**
   ```bash
   python app.py
   ```
   로컬에서 변경사항이 제대로 작동하는지 먼저 확인하세요.

2. **브라우저 개발자 도구 활용**
   - `F12` 또는 `Ctrl + Shift + I`로 개발자 도구 열기
   - Network 탭에서 파일 로드 상태 확인
   - Console 탭에서 JavaScript 오류 확인

3. **배포 전 커밋 메시지 확인**
   ```bash
   git log --oneline -10
   ```
   최근 커밋이 제대로 푸시되었는지 확인하세요.

---

**여전히 문제가 있으신가요?** [Issues 페이지](https://github.com/yourusername/health-class-homepage/issues)에서 질문해주세요!
