# 🚀 빠른 해결 가이드 (5분 안에 해결!)

## 문제
✗ GitHub에는 새 코드가 올라갔음  
✗ 웹에서는 여전히 예전 홈페이지 보임

## 원인
🔴 **캐시 문제** - 브라우저와 Heroku 서버 모두 오래된 버전을 캐싱하고 있음

---

## 🔧 즉시 해결하기 (3가지 방법)

### 👉 **가장 간단한 방법: Heroku 대시보드에서 클릭**

1. https://dashboard.heroku.com 접속
2. 앱 선택 (예: your-health-app)
3. 우측 상단 "More" → "Restart all dynos" 클릭
4. 1분 대기
5. 웹 새로고침 (Ctrl+F5)

---

### 👉 **방법 2: 터미널 명령어 (빠름)**

```powershell
# PowerShell에서 실행:
heroku login
heroku restart -a your-app-name
```

**your-app-name**을 Heroku 앱 이름으로 바꾸세요!

---

### 👉 **방법 3: 재배포 (가장 확실)**

```powershell
git add .
git commit -m "Fix cache and update homepage"
git push heroku main
```

---

## ✅ 확인 사항

```
✅ app.py에 새로운 캐시 설정 추가됨
✅ templates/index.html 개선됨  
✅ HEROKU_RESTART.md 가이드 생성됨
```

---

## 🌐 웹 확인

1. **브라우저 캐시 삭제**: Ctrl + Shift + Delete
2. **강제 새로고침**: Ctrl + F5
3. **새 홈페이지 확인** ✨

---

## 📱 Heroku 앱 이름 확인하기

앱 이름을 모르면:
```powershell
heroku apps
```

결과 예:
```
my-health-app
another-app
```

---

## 🎉 완료!

이제 새로운 보건 수업 홈페이지가 보일 것입니다! 🎊
