# 🚀 2단계: 로컬에서 Git 정리 및 업로드

## 🎯 지금 바로 하세요 (3가지 방법 - 가장 쉬운 순서)

---

## ✨ 방법 1: 자동 업로드 배치 파일 (가장 쉬움) 🎯

### Step 1: 배치 파일 실행
1. 윈도우 탐색기 열기
2. `c:\Users\cyh99\Documents\프로젝트` 폴더로 이동
3. **`git_upload.bat`** 파일 **더블클릭**
4. 검은 창이 떠서 자동으로 작업 완료 ✅

### 끝!

---

## 방법 2: Git Bash에서 직접 입력 (Git 설치되어 있으면)

### Step 1: Git Bash 열기
1. 프로젝트 폴더 열기
2. 빈 공간에서 우클릭
3. **"Git Bash Here"** 선택

### Step 2: 명령어 입력
```bash
git add .
git commit -m "Disable GitHub Pages - use external deployment"
git push origin main
```

---

## 방법 3: GitHub Desktop 사용 (가장 직관적)

1. https://desktop.github.com 다운로드 및 설치
2. GitHub Desktop 열기
3. "Add" → "Clone Repository..."
4. `lalagoola/home` 선택
5. "Current Branch" → 변경사항 확인
6. 좌측 상단 "Changes" 클릭
7. 모든 파일 체크 ✅
8. "Commit to main" 클릭
9. "Publish branch" 클릭

---

## ✅ 완료 확인

업로드 후:

1. https://github.com/lalagoola/home 방문
2. 파일들이 최신 상태인지 확인
3. **Settings → Pages**로 이동
4. **Source** → **"None"** 선택
5. **Save** 클릭

---

## 🎊 최종 체크리스트

```
✅ git add . 실행됨
✅ git commit 완료됨
✅ git push origin main 완료됨
✅ GitHub에 최신 파일 업로드됨
✅ GitHub Settings에서 Pages를 "None"으로 변경
```

모두 완료하면:

```
✅ Jekyll 빌드 오류 완전히 해결
✅ GitHub에 코드 안전하게 저장
✅ Railway/Heroku에서 배포 준비 완료
```

---

## 🚀 다음 단계: Railway에서 배포

```
1. https://railway.app 방문
2. GitHub 로그인
3. "New Project" → "Deploy from GitHub"
4. "lalagoola/home" 선택
5. 환경 변수 입력:
   - FIREBASE_API_KEY
   - FIREBASE_AUTH_DOMAIN
   - FIREBASE_PROJECT_ID
   - FIREBASE_STORAGE_BUCKET
   - FIREBASE_MESSAGING_SENDER_ID
   - FIREBASE_APP_ID
   - FIREBASE_DATABASE_URL
   - SECRET_KEY
6. Deploy! 🎉
```

---

**이제 정말 마지막입니다!** 🌟
