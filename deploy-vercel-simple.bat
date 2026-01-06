@echo off
REM Simple Vercel Deployment Script
REM This script will guide you through deploying to Vercel

echo ========================================
echo Vercel Deployment for Physical AI RAG
echo ========================================
echo.

REM Check if Vercel CLI is installed
vercel --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Vercel CLI not installed!
    echo Please run: npm install -g vercel
    pause
    exit /b 1
)

echo Vercel CLI found!
echo.

REM Check if logged in
vercel whoami >nul 2>&1
if errorlevel 1 (
    echo You are not logged in to Vercel.
    echo Please run: vercel login
    echo.
    echo After logging in, run this script again.
    pause
    exit /b 1
)

echo Logged in successfully!
echo.

echo ========================================
echo IMPORTANT: Environment Variables
echo ========================================
echo.
echo Before deploying, make sure you have:
echo 1. GEMINI_API_KEY - Get from https://makersuite.google.com/app/apikey
echo 2. SESSION_SECRET_KEY - Generate with: openssl rand -hex 32
echo 3. ADMIN_PASSWORD - Choose a strong password
echo.
echo You can set these in Vercel Dashboard after deployment.
echo.

set /p CONTINUE="Continue with deployment? (Y/N): "
if /i not "%CONTINUE%"=="Y" (
    echo Deployment cancelled.
    pause
    exit /b 0
)

echo.
echo Deploying to Vercel...
echo.

REM Deploy to production
vercel --prod

echo.
echo ========================================
echo Deployment Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Go to https://vercel.com/dashboard
echo 2. Select your project
echo 3. Go to Settings -^> Environment Variables
echo 4. Add the required environment variables
echo 5. Redeploy if needed
echo.
echo Your app will be live at the URL shown above.
echo.

pause
