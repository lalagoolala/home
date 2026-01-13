# 🔴 GitHub Pages 빌드 오류 해결

## 문제
- GitHub Pages가 Flask 앱을 빌드하려고 시도
- Flask는 동적 웹 프레임워크라서 GitHub Pages에서 지원 안 됨
- **"pages build and deployment / build (dynamic)" - Failing**

## 원인
리포지토리가 GitHub Pages로 설정되어 있음

---

## ✅ 해결 방법

### 방법 1: GitHub Pages 비활성화 (추천)

1. **GitHub 리포지토리 → Settings 클릭**
2. **좌측 메뉴에서 "Pages" 클릭**
3. **"Build and deployment" 섹션에서**
   - Source: **"Deploy from a branch"** 선택 시 → **"None"** 선택
   - 또는 Source: **"GitHub Actions"** 선택 후 → **workflows 중 모두 제거**
4. **Save 클릭**

**결과**: GitHub Pages 빌드 오류 사라짐 ✅

---

### 방법 2: 리포지토리 설정 변경

1. **Settings → General**
2. **아래로 스크롤하여 "GitHub Pages" 섹션 찾기**
3. **"None"으로 변경**
4. **Save**

---

## 🚀 이제 어디에 배포할 것인가?

Flask 앱은 GitHub Pages가 아닌 다른 곳에 배포해야 합니다:

### ✅ 무료 배포 옵션 (추천)

**1. Heroku (가장 인기)**
```bash
git push heroku main
```
- 한 번 설정하면 자동 배포
- 무료 플랜 제공 (단, 약간의 제약)

**2. Railway (더 좋음)**
- GitHub와 연동하면 자동 배포
- 더 빠른 성능
- 무료 크레딧 제공

**3. Render**
- 무료 호스팅 제공
- 자동 배포 지원

**4. PythonAnywhere**
- Python 특화
- 무료 플랜 제공

---

## 📝 현재 상황

```
✅ 코드는 GitHub에 올라감 (문제 없음)
❌ GitHub Pages가 빌드 실패 (Flask 미지원)
→ 다른 배포 플랫폼 사용해야 함
```

---

## 🎯 다음 단계

1. **GitHub Pages 비활성화** (위의 방법 1 따라하기)
2. **Heroku/Railway 중 선택**
3. **배포 플랫폼에 앱 배포**

이렇게 하면 GitHub에 코드도 안전하게 올라가고, 
실제로 작동하는 웹사이트도 배포됩니다! 🚀
