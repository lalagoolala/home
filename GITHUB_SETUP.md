# 🚀 GitHub에 홈페이지 업로드하기 (완벽 가이드)

## 문제점 분석

이전에 GitHub에 업로드하려고 했을 때 실패한 이유:
- ❌ **Firebase API 키가 코드에 하드코딩되어 있었음**
- ❌ **GitHub는 공개 저장소에 API 키를 업로드하지 못하도록 보안 차단**

## 해결 방법

이제 **환경 변수(Environment Variables)**를 사용하여 API 키를 보호합니다!

### ✅ 현재 상태
- 모든 Firebase 설정이 `.env` 파일에서 로드됨
- `.env` 파일은 `.gitignore`에 포함되어 있어 GitHub에 업로드되지 않음
- `.env.example` 파일에는 민감하지 않은 설정 형식만 포함됨 (이 파일은 GitHub에 올라감)

---

## 📋 Step-by-Step 가이드

### 1단계: 로컬 설정 완료 확인

아래 파일들이 프로젝트에 있는지 확인:
- ✅ `.env.example` (GitHub에 올라갈 파일 - 민감한 정보 제외)
- ✅ `.env` (로컬에만 있을 파일 - 실제 API 키 포함)
- ✅ `.gitignore` (`.env`를 제외하도록 설정)

### 2단계: `.env` 파일 설정

프로젝트 루트에 `.env` 파일을 생성하고 다음을 입력:

```bash
# Flask 설정
FLASK_ENV=development
FLASK_DEBUG=True
FLASK_APP=app.py

# 보안 (프로덕션에서 변경 필수!)
SECRET_KEY=your-secret-key-12345

# Firebase 설정 (https://console.firebase.google.com 에서 복사)
FIREBASE_API_KEY=AIzaSyAbrKzSRUq1_Qi15yzK3aYKhOLSlhSm-2k
FIREBASE_AUTH_DOMAIN=homepage-63d32.firebaseapp.com
FIREBASE_PROJECT_ID=homepage-63d32
FIREBASE_STORAGE_BUCKET=homepage-63d32.firebasestorage.app
FIREBASE_MESSAGING_SENDER_ID=515012802016
FIREBASE_APP_ID=1:515012802016:web:4c3db8588aa7f00df8a785
FIREBASE_DATABASE_URL=https://homepage-63d32-default-rtdb.firebaseio.com

# 서버
PORT=5000
```

### 3단계: Git에서 `.env` 제외 확인

이미 `.gitignore`에 `.env`가 추가되어 있습니다. 확인:

```bash
# 상태 확인 (`.env` 파일이 보이면 안됨)
git status
```

결과 예시:
```
On branch main
Changes not staged for commit:
  modified:   README.md
  modified:   app.py
  ...
Untracked files:
  .env.example
  templates/index.html
  ...

(`.env` 파일이 보이지 않으면 정상!)
```

### 4단계: GitHub에 업로드

```bash
# 변경사항 추가
git add .

# 커밋
git commit -m "Add health class homepage with secure environment setup"

# 업로드
git push origin main
```

### 5단계: 배포 시 환경 변수 설정

배포 플랫폼에서 환경 변수를 설정해야 합니다.

#### Heroku에서 설정하기:
```bash
heroku login
heroku create your-app-name
heroku config:set FIREBASE_API_KEY=AIzaSyAbrKzSRUq1_Qi15yzK3aYKhOLSlhSm-2k
heroku config:set FIREBASE_AUTH_DOMAIN=homepage-63d32.firebaseapp.com
heroku config:set FIREBASE_PROJECT_ID=homepage-63d32
heroku config:set FIREBASE_STORAGE_BUCKET=homepage-63d32.firebasestorage.app
heroku config:set FIREBASE_MESSAGING_SENDER_ID=515012802016
heroku config:set FIREBASE_APP_ID=1:515012802016:web:4c3db8588aa7f00df8a785
heroku config:set FIREBASE_DATABASE_URL=https://homepage-63d32-default-rtdb.firebaseio.com
heroku config:set SECRET_KEY=your-secret-key-production

git push heroku main
```

#### Railway에서 설정하기:
1. [Railway.app](https://railway.app)에 로그인
2. "New Project" → "Deploy from GitHub" 선택
3. 저장소 선택
4. "Environment" 탭 클릭
5. `.env` 파일의 모든 변수 입력
6. 자동으로 배포됨

---

## 🔒 보안 검사 리스트

GitHub에 업로드하기 전에 확인하세요:

- [ ] `.env` 파일이 `.gitignore`에 포함되어 있나요?
- [ ] `git status`에서 `.env` 파일이 보이지 않나요?
- [ ] `.env.example` 파일만 GitHub에 올라가나요?
- [ ] app.py에서 API 키가 환경 변수로 로드되나요?
- [ ] login.html과 signup.html에서 Firebase 설정이 `/api/firebase-config`에서 동적 로드되나요?

모두 "네"라면 **안전하게 GitHub에 업로드할 수 있습니다!** ✅

---

## 🎯 요약

### 이전 (위험함 ❌)
```python
# app.py에 하드코딩됨
firebaseConfig = {
  "apiKey": "AIzaSyAbrKzSRUq1_Qi15yzK3aYKhOLSlhSm-2k",  # 노출됨!
  ...
}
```

### 현재 (안전함 ✅)
```python
# 환경 변수에서 로드됨
firebaseConfig = {
  "apiKey": os.environ.get('FIREBASE_API_KEY'),  # .env 파일에서 로드
  ...
}
```

---

## 🚨 만약 실수로 API 키를 GitHub에 올렸다면?

1. **빠르게 Firebase 키 재생성**: [Firebase Console](https://console.firebase.google.com) → 설정 → 키 관리 → 새로운 키 생성
2. 코드에서 API 키 제거
3. Git 히스토리에서 제거 (BFG Repo-Cleaner 사용)
4. 다시 커밋 및 푸시

---

## 📚 더 알아보기

- [flask-dotenv 문서](https://python-dotenv.readthedocs.io/)
- [Firebase 보안 모범 사례](https://firebase.google.com/docs/projects/best-practices/security)
- [GitHub 보안 설정](https://docs.github.com/en/code-security)

---

## ✨ 이제 안전하게 개발하세요!

질문이 있으시면 이슈를 등록해주세요. 🚀
