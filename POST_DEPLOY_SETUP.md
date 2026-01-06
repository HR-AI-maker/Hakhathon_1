# 🔧 Post-Deployment Setup (REQUIRED)

After deploying to Vercel, you MUST set environment variables for the app to work properly.

## Step 1: Go to Vercel Dashboard

https://vercel.com/dashboard

## Step 2: Select Your Project

Click on the project you just deployed (e.g., "physical-ai-chatbot")

## Step 3: Add Environment Variables

Go to: **Settings** → **Environment Variables**

### Add These 3 Variables:

#### 1. GEMINI_API_KEY

**How to get it:**
1. Visit: https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Click "Create API Key" or "Get API Key"
4. Copy the key (starts with "AI...")

**In Vercel:**
- Name: `GEMINI_API_KEY`
- Value: Paste your Gemini API key
- Environment: Check all (Production, Preview, Development)
- Click "Save"

#### 2. SESSION_SECRET_KEY

**How to generate:**

Option A - Using Python:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Option B - Using PowerShell:
```powershell
-join ((48..57) + (97..102) | Get-Random -Count 64 | % {[char]$_})
```

Option C - Use this random value:
```
a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6
```

**In Vercel:**
- Name: `SESSION_SECRET_KEY`
- Value: Paste the generated secret
- Environment: Check all
- Click "Save"

#### 3. ADMIN_PASSWORD

**Choose a strong password** (e.g., `MyApp2024!Secure`)

**In Vercel:**
- Name: `ADMIN_PASSWORD`
- Value: Your chosen password
- Environment: Check all
- Click "Save"

## Step 4: Redeploy

After adding environment variables:

**Option A - In Dashboard:**
1. Go to "Deployments" tab
2. Click the three dots (...) on the latest deployment
3. Click "Redeploy"
4. Check "Use existing Build Cache"
5. Click "Redeploy"

**Option B - From CLI:**
```bash
vercel --prod
```

## Step 5: Test Your App

Visit your Vercel URL (e.g., `https://your-app.vercel.app`)

You should see:
- ✅ Login page loads
- ✅ Can login with demo credentials (demo/demo123)
- ✅ Can ask questions to the chatbot
- ✅ Get responses from Gemini AI

---

## 🎯 Quick Reference

| Variable | Where to Get | Example |
|----------|--------------|---------|
| GEMINI_API_KEY | https://makersuite.google.com/app/apikey | AIza... |
| SESSION_SECRET_KEY | `python -c "import secrets; print(secrets.token_hex(32))"` | a1b2c3d4... |
| ADMIN_PASSWORD | Your choice | MySecure123! |

---

## 🔍 Troubleshooting

**App shows errors?**
→ Check you added all 3 environment variables
→ Redeploy after adding variables

**Can't generate SESSION_SECRET_KEY?**
→ Just use any random 32+ character string

**Gemini API not working?**
→ Verify your API key at https://makersuite.google.com/app/apikey
→ Make sure billing is enabled (free tier available)

**Login not working?**
→ Try demo credentials: `demo` / `demo123`
→ Check ADMIN_PASSWORD is set if using admin login

---

## 📊 Verification Checklist

After setup, verify these endpoints work:

1. `https://your-app.vercel.app/` → Frontend loads ✅
2. `https://your-app.vercel.app/health` → Shows status ✅
3. `https://your-app.vercel.app/docs` → API docs ✅
4. Login with demo/demo123 → Works ✅
5. Ask "What is Physical AI?" → Get response ✅

---

## 🎉 You're Done!

Your Physical AI chatbot is now live and accessible from anywhere!

Share your deployment URL with others to let them use the chatbot.
