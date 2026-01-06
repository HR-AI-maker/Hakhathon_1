@echo off
REM Quick script to set environment variables in Vercel

echo ========================================
echo Set Environment Variables in Vercel
echo ========================================
echo.

cd /d "%~dp0"

echo Your environment variable values:
echo.
echo 1. SESSION_SECRET_KEY (copy this):
echo    cadc2ec4da43cdd879441eb22b96c93f05dacd1f22b5a6ba58aee1c0260c17d3
echo.
echo 2. GEMINI_API_KEY (get from browser):
echo    Opening Google AI Studio...
start https://aistudio.google.com/app/apikey
echo.
echo 3. ADMIN_PASSWORD (your choice):
echo    Example: MySecurePass123
echo.
echo ========================================
echo.
echo Choose your method:
echo.
echo 1. Via Dashboard (Recommended - Easy)
echo 2. Via CLI (Advanced)
echo.
choice /c 12 /n /m "Enter 1 or 2: "

if errorlevel 2 goto CLI
if errorlevel 1 goto DASHBOARD

:DASHBOARD
echo.
echo Opening Vercel Dashboard...
start https://vercel.com/dashboard
echo.
echo ========================================
echo Follow these steps in the browser:
echo ========================================
echo.
echo 1. Click on your project (physical-ai-textbook)
echo 2. Click "Settings" tab
echo 3. Click "Environment Variables" in sidebar
echo 4. Click "Add Variable" button
echo.
echo Add these 3 variables:
echo.
echo Variable 1:
echo   Key: GEMINI_API_KEY
echo   Value: [paste from Google AI Studio tab]
echo   Environment: Production (check the box)
echo   Click Save
echo.
echo Variable 2:
echo   Key: SESSION_SECRET_KEY
echo   Value: cadc2ec4da43cdd879441eb22b96c93f05dacd1f22b5a6ba58aee1c0260c17d3
echo   Environment: Production (check the box)
echo   Click Save
echo.
echo Variable 3:
echo   Key: ADMIN_PASSWORD
echo   Value: [your choice - e.g., MySecurePass123]
echo   Environment: Production (check the box)
echo   Click Save
echo.
echo 5. Go to "Deployments" tab
echo 6. Click the three dots (...) on latest deployment
echo 7. Click "Redeploy"
echo 8. Wait for deployment to complete
echo.
echo ========================================
pause
goto END

:CLI
echo.
echo Setting variables via CLI...
echo.

echo Setting GEMINI_API_KEY...
echo Paste your Gemini API key when prompted:
npx vercel env add GEMINI_API_KEY production
echo.

echo Setting SESSION_SECRET_KEY...
echo Paste: cadc2ec4da43cdd879441eb22b96c93f05dacd1f22b5a6ba58aee1c0260c17d3
npx vercel env add SESSION_SECRET_KEY production
echo.

echo Setting ADMIN_PASSWORD...
echo Enter your chosen admin password:
npx vercel env add ADMIN_PASSWORD production
echo.

echo Redeploying...
npx vercel --prod
echo.

echo ========================================
echo Done!
echo ========================================
pause
goto END

:END
echo.
echo See VERCEL_ENV_SETUP.md for detailed instructions.
echo.
