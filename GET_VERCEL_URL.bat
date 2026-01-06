@echo off
REM Get Vercel deployment URL

echo ========================================
echo Get Your Vercel Deployment URL
echo ========================================
echo.

cd /d "%~dp0"

echo Logging in to Vercel...
npx vercel login

if errorlevel 1 (
    echo ERROR: Login failed
    pause
    exit /b 1
)

echo.
echo Fetching your deployments...
echo.
npx vercel ls

echo.
echo ========================================
echo Copy your production URL from above
echo ========================================
echo.
echo It should look like:
echo https://physical-ai-textbook-xyz.vercel.app
echo.
pause
