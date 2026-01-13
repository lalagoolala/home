@echo off
REM Git 커밋 및 푸시 자동화 스크립트
REM 이 파일을 실행하면 모든 변경사항이 자동으로 GitHub에 업로드됩니다

setlocal enabledelayedexpansion

cd /d "c:\Users\cyh99\Documents\프로젝트"

echo ========================================
echo GitHub Pages 비활성화 - 최종 업로드
echo ========================================
echo.

echo [1/3] 변경사항 스테이징...
git add .
if errorlevel 1 (
    echo Error: git add 실패
    pause
    exit /b 1
)
echo 성공!
echo.

echo [2/3] 커밋 생성...
git commit -m "Disable GitHub Pages - use external deployment instead"
if errorlevel 1 (
    echo Error: git commit 실패
    pause
    exit /b 1
)
echo 성공!
echo.

echo [3/3] GitHub에 푸시...
git push origin main
if errorlevel 1 (
    echo Error: git push 실패
    echo GitHub 인증 정보를 확인하세요
    pause
    exit /b 1
)
echo 성공!
echo.

echo ========================================
echo 완료! GitHub에 업로드되었습니다
echo ========================================
echo.
echo 다음 단계:
echo 1. GitHub Settings → Pages로 이동
echo 2. Source를 "None"으로 변경
echo 3. Save 클릭
echo.
pause
