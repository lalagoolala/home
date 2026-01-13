# 🔄 Heroku 재배포 및 캐시 초기화 가이드

## 문제
- GitHub에는 새 코드가 올라갔음
- 하지만 웹에서는 여전히 예전 홈페이지가 보임
- **원인**: Heroku 서버의 캐시 + 브라우저 캐시

## 해결 방법

### 방법 1: Heroku에서 직접 재배포 (추천 - 가장 간단)

```bash
# 1. Heroku 로그인
heroku login

# 2. 앱 이름 확인
heroku apps

# 3. 앱 재시작 (즉시 적용)
heroku restart -a your-app-name

# 4. 로그 확인 (문제가 있는지 확인)
heroku logs -a your-app-name --tail
```

**또는 한 줄로:**
```bash
heroku restart -a your-app-name
```

---

### 방법 2: Heroku에 강제 재배포

```bash
# 1. 최신 코드 확인 (Heroku는 git으로 배포됨)
git status

# 2. 변경사항 커밋 (이미 했다면 스킵)
git add .
git commit -m "Fix cache issue and improve homepage"

# 3. Heroku에 재배포 (강제 업데이트)
git push heroku main -f

# 4. 배포 확인
heroku logs -a your-app-name --tail
```

---

### 방법 3: 브라우저 캐시 초기화

배포 후 브라우저에서도 캐시를 지워야 합니다:

**Windows/Linux:**
- Chrome: `Ctrl + Shift + Delete`
- Firefox: `Ctrl + Shift + Delete`
- Edge: `Ctrl + Shift + Delete`

**macOS:**
- Chrome: `Cmd + Shift + Delete`
- Firefox: `Cmd + Shift + Delete`
- Safari: `Develop` → `Clear Caches`

**또는 강제 새로고침:**
- Windows/Linux: `Ctrl + F5`
- macOS: `Cmd + Shift + R`

---

### 방법 4: Railway를 사용 중인 경우

```bash
# Railway 대시보드 접속
# https://railway.app/dashboard

# 1. 프로젝트 선택
# 2. 환경 변수 확인 (FIREBASE 설정이 모두 있는지)
# 3. "Redeploy" 또는 "Deploy" 버튼 클릭
```

---

## ✅ 확인 사항

1. **app.py에 새로운 캐시 헤더 추가됨** ✅
   - `Cache-Control: no-cache, no-store, must-revalidate`
   - 이제 브라우저와 서버 모두에서 캐시를 하지 않음

2. **TEMPLATES_AUTO_RELOAD 활성화됨** ✅
   - Flask 템플릿이 항상 최신 버전으로 로드됨

3. **set_no_cache 데코레이터 추가됨** ✅
   - 모든 응답에 캐시 비활성화 헤더 추가

---

## 🔧 실행 단계별 설명

### 단계 1: Heroku 로그인
```bash
heroku login
```
- Heroku 웹사이트가 열리면 로그인
- 또는 API 키 입력

### 단계 2: 앱 이름 확인
```bash
heroku apps
```
출력 예:
```
=== Apps
your-health-app
```

### 단계 3: 앱 재시작
```bash
heroku restart -a your-health-app
```

### 단계 4: 로그 확인
```bash
heroku logs -a your-health-app --tail
```

---

## 🌐 웹에서 확인

1. **URL 방문**: `https://your-app-name.herokuapp.com`
2. **Ctrl+Shift+Delete (캐시 삭제)**
3. **Ctrl+F5 (강제 새로고침)**
4. **새 홈페이지 확인**

---

## 📊 무엇이 변경되었는가?

### app.py의 변경사항
```python
# 추가됨:
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.after_request
def set_no_cache(response):
    """모든 응답에 캐시 비활성화 헤더 추가"""
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate, public, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response
```

이제 다음이 보장됩니다:
- ✅ 브라우저에서 캐시하지 않음
- ✅ 프록시에서 캐시하지 않음
- ✅ Heroku에서도 캐시하지 않음
- ✅ 항상 최신 버전을 제공

---

## 💡 팁

- **Heroku 다시 배포하기**: `git push heroku main`
- **로그 실시간 보기**: `heroku logs -a your-app-name --tail`
- **환경 변수 확인**: `heroku config -a your-app-name`
- **앱 상태 확인**: `heroku ps -a your-app-name`

---

## 🚨 만약 여전히 안 된다면?

1. **Heroku 로그 확인**
   ```bash
   heroku logs -a your-app-name --tail
   ```
   에러가 보이는지 확인

2. **환경 변수 확인**
   ```bash
   heroku config -a your-app-name
   ```
   FIREBASE_API_KEY 등 모든 변수가 설정되어 있는지 확인

3. **앱 일시중지/재시작**
   ```bash
   heroku restart -a your-app-name
   ```

4. **아주 마지막 수단 - 재배포**
   ```bash
   git push heroku main -f
   ```

---

**완료되면 반드시 브라우저 캐시를 지우고 (Ctrl+Shift+Delete) 강제 새로고침 (Ctrl+F5)하세요!** 🚀
