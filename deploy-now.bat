@echo off
echo ========================================
echo DEPLOYING TO VERCEL - AUTOMATED
echo ========================================
echo.
echo This script will:
echo 1. Login to Vercel (opens browser)
echo 2. Deploy your app to production
echo 3. Show you the live URL
echo.
echo Press any key to start...
pause >nul

echo.
echo Step 1/2: Logging in to Vercel...
echo.
echo A browser window will open.
echo Please complete the authentication.
echo.

REM Login to Vercel
call vercel login

REM Check if login was successful
vercel whoami >nul 2>&1
if errorlevel 1 (
    echo.
    echo ERROR: Login failed or was cancelled.
    echo Please try again: vercel login
    pause
    exit /b 1
)

echo.
echo ✅ Login successful!
echo.
echo ========================================
echo Step 2/2: Deploying to Production...
echo ========================================
echo.

REM Deploy to production
call vercel --prod --yes

echo.
echo ========================================
echo 🎉 DEPLOYMENT COMPLETE!
echo ========================================
echo.
echo Next steps:
echo 1. Copy the deployment URL shown above
echo 2. Go to https://vercel.com/dashboard
echo 3. Click on your project
echo 4. Go to Settings -^> Environment Variables
echo 5. Add these variables:
echo    - GEMINI_API_KEY (get from https://makersuite.google.com/app/apikey)
echo    - SESSION_SECRET_KEY (generate with: python -c "import secrets; print(secrets.token_hex(32))")
echo    - ADMIN_PASSWORD (choose a password)
echo 6. Redeploy: vercel --prod
echo.
echo Your app is LIVE! 🚀
echo.
pause
