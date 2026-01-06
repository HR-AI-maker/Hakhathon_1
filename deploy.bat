@echo off
REM Deployment Script for Vercel
REM Physical AI Textbook RAG Application

echo ========================================
echo Physical AI Textbook - Vercel Deployment
echo ========================================
echo.

echo Step 1: Checking Vercel CLI...
npx vercel --version
if errorlevel 1 (
    echo ERROR: Could not run Vercel CLI
    echo Please install Node.js from https://nodejs.org
    pause
    exit /b 1
)

echo.
echo Step 2: Logging in to Vercel...
echo This will open your browser to authenticate.
echo.
npx vercel login

echo.
echo Step 3: Deploying to Vercel...
echo This will deploy your application to production.
echo.
npx vercel --prod

echo.
echo ========================================
echo Deployment Complete!
echo ========================================
echo.
echo Your application should now be live on Vercel.
echo Check the URL provided above to access your deployed app.
echo.
pause
