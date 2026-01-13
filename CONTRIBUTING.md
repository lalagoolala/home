# 기여 가이드

이 프로젝트에 기여해주셔서 감사합니다! 다음은 기여 방법에 대한 가이드입니다.

## 🤝 기여 방법

### 1. Fork 및 Clone
```bash
# 1. GitHub에서 이 저장소를 Fork합니다
# 2. 로컬에 Clone합니다
git clone https://github.com/yourusername/health-class-homepage.git
cd health-class-homepage
```

### 2. 브랜치 생성
```bash
# 새로운 기능 브랜치를 생성합니다
git checkout -b feature/your-feature-name

# 버그 수정 브랜치를 생성합니다
git checkout -b fix/bug-fix-name
```

### 3. 변경 사항 구현
- 코드를 작성합니다
- 변경 사항을 테스트합니다
- 필요시 문서를 업데이트합니다

### 4. Commit
```bash
# 변경 사항을 커밋합니다
git add .
git commit -m "feat: 기능 설명" # 또는 "fix: 버그 설명"
```

### 5. Push 및 Pull Request
```bash
# 브랜치를 원격 저장소에 Push합니다
git push origin feature/your-feature-name

# GitHub에서 Pull Request를 생성합니다
```

## 📋 Commit 메시지 규칙

커밋 메시지는 다음 형식을 따라주세요:

```
<타입>: <제목>

<본문>

<footer>
```

### 타입
- `feat`: 새로운 기능
- `fix`: 버그 수정
- `docs`: 문서 업데이트
- `style`: 코드 스타일 변경 (기능 변화 없음)
- `refactor`: 코드 리팩토링
- `perf`: 성능 개선
- `test`: 테스트 추가 또는 수정
- `chore`: 빌드 및 설정 변경

### 예시
```
feat: 사용자 프로필 페이지 추가

사용자가 자신의 프로필을 확인하고 수정할 수 있는 페이지를 추가했습니다.

- 프로필 조회 기능
- 프로필 수정 기능
- 프로필 삭제 기능
```

## 💻 코드 스타일

### Python
- PEP 8을 따릅니다
- 들여쓰기는 4칸입니다
- 라인 길이는 최대 79자입니다

### HTML/CSS/JavaScript
- 들여쓰기는 2칸입니다
- 의미있는 클래스명을 사용합니다
- 주석은 명확하고 간결하게 작성합니다

## 🧪 테스트

변경 사항을 제출하기 전에 다음을 확인하세요:

1. 로컬에서 앱이 정상 실행되는지 확인
2. 새로운 기능의 경우 수동 테스트 수행
3. 기존 기능이 여전히 작동하는지 확인

## 📚 개발 환경 설정

```bash
# 1. 가상 환경 생성
python -m venv venv

# 2. 가상 환경 활성화
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 3. 패키지 설치
pip install -r requirements.txt

# 4. 앱 실행
python app.py
```

## 📖 문서

- README.md를 변경하는 경우 명확하고 자세하게 작성해주세요
- 새로운 기능을 추가하는 경우 사용 방법을 문서화해주세요
- 코드가 복잡한 경우 주석으로 설명해주세요

## 🐛 버그 보고

버그를 발견하면 [이슈 템플릿](.github/ISSUE_TEMPLATE/bug_report.md)을 사용하여 보고해주세요.

## ✨ 기능 제안

새로운 기능을 제안하려면 [기능 요청 템플릿](.github/ISSUE_TEMPLATE/feature_request.md)을 사용해주세요.

## 📝 라이선스

이 프로젝트에 기여하는 것은 MIT 라이선스에 동의하는 것입니다.

## 🙏 감사합니다

이 프로젝트에 기여해주셔서 정말 감사합니다! 여러분의 도움으로 더 좋은 프로젝트가 될 것입니다.

---

**질문이 있으신가요?** [이슈](https://github.com/yourusername/health-class-homepage/issues)를 통해 문의해주세요!
