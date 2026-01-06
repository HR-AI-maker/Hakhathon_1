@echo off
REM Quick Vercel Deployment Script
REM Physical AI Textbook - Authenticated Chatbot

echo ========================================
echo Deploy to Vercel - Automated Script
echo ========================================
echo.

cd /d "%~dp0"

echo Step 1: Checking Vercel CLI...
npx vercel --version
if errorlevel 1 (
    echo ERROR: Vercel CLI not available
    echo Please install Node.js from https://nodejs.org
    pause
    exit /b 1
)

echo.
echo Step 2: Logging in to Vercel...
echo This will open your browser.
echo.
npx vercel login

if errorlevel 1 (
    echo ERROR: Login failed
    pause
    exit /b 1
)

echo.
echo Step 3: Deploying to production...
echo.
npx vercel --prod --yes

if errorlevel 1 (
    echo ERROR: Deployment failed
    echo Check the error message above
    pause
    exit /b 1
)

echo.
echo ========================================
echo Deployment Complete!
echo ========================================
echo.
echo Next Steps:
echo 1. Copy your production URL from above
echo 2. Go to https://vercel.com/dashboard
echo 3. Click on your project
echo 4. Go to Settings - Environment Variables
echo 5. Add these variables:
echo    - GEMINI_API_KEY (get from https://aistudio.google.com/app/apikey)
echo    - SESSION_SECRET_KEY (generate with: python -c "import secrets; print(secrets.token_hex(32))")
echo    - ADMIN_PASSWORD (your choice)
echo 6. Redeploy: npx vercel --prod
echo.
echo See DEPLOY_NOW.md for detailed instructions.
echo.
pause
