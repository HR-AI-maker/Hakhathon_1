# Deploy to Vercel - Step by Step

## ✅ Pre-Deployment Complete

All files are ready for deployment:
- ✅ Vercel configuration updated
- ✅ Frontend configured for production
- ✅ API requirements updated
- ✅ Environment variables defined

---

## 🚀 Deploy in 5 Minutes

### Step 1: Login to Vercel (1 minute)

Open a new terminal and run:

```bash
cd C:\Users\lenovo\Desktop\Hakathon_I\claude
npx vercel login
```

This will:
- Open your browser
- Ask you to sign in (use GitHub, GitLab, or Email)
- Automatically authenticate the CLI

### Step 2: Deploy (2 minutes)

After successful login, run:

```bash
npx vercel --prod --yes
```

You'll see:
```
Vercel CLI 50.1.3
Loading scopes…
Deploying to production…
Building…
Uploading…
✅ Production: https://your-app.vercel.app
```

**Copy your production URL!**

### Step 3: Set Environment Variables (2 minutes)

#### Option A: Via Dashboard (Recommended)

1. Go to https://vercel.com/dashboard
2. Click on your project
3. Go to **Settings** → **Environment Variables**
4. Add these variables:

| Name | Value | Where to Get |
|------|-------|--------------|
| `GEMINI_API_KEY` | Your Gemini API key | https://aistudio.google.com/app/apikey |
| `SESSION_SECRET_KEY` | Random 64-char hex string | Run: `python -c "import secrets; print(secrets.token_hex(32))"` |
| `ADMIN_PASSWORD` | Your admin password | Any secure password |

5. Click **Save**
6. Go to **Deployments** → Click **⋯** → **Redeploy**

#### Option B: Via CLI

```bash
# Set Gemini API key
npx vercel env add GEMINI_API_KEY production
# Paste your key when prompted

# Set session secret
npx vercel env add SESSION_SECRET_KEY production
# Paste generated secret

# Set admin password
npx vercel env add ADMIN_PASSWORD production
# Enter your password

# Redeploy to apply
npx vercel --prod
```

---

## 🎯 Quick Commands

### Deploy Now:
```bash
cd C:\Users\lenovo\Desktop\Hakathon_I\claude
npx vercel login
npx vercel --prod --yes
```

### Generate Session Secret:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### Get Gemini API Key:
Open: https://aistudio.google.com/app/apikey

---

## ✅ After Deployment

### Test Your Live App

1. **Open your Vercel URL** (e.g., https://physical-ai-textbook.vercel.app)
2. **You'll see the login page**
3. **Login with:**
   - Username: `demo`
   - Password: `demo123`
4. **Ask a question:** "What is Physical AI?"
5. **Get AI-powered answer** with citations!

### Verify Everything Works

- [ ] Can access the URL
- [ ] Login page loads
- [ ] Can login with demo/demo123
- [ ] Chatbot interface appears
- [ ] Can ask questions
- [ ] Get responses from Gemini
- [ ] Sources are cited
- [ ] Logout works

---

## 🔧 Troubleshooting

### "Login Failed"
```bash
# Clear Vercel auth and retry
npx vercel logout
npx vercel login
```

### "Build Failed"
- Check that all files are in the project directory
- Verify `vercel.json` exists
- Ensure `requirements.txt` is updated

### "Environment Variables Not Working"
- Go to Vercel Dashboard → Project → Settings → Environment Variables
- Verify all three variables are set
- Redeploy after adding variables

### "Chatbot Not Responding"
- Check that `GEMINI_API_KEY` is set correctly
- Verify it's a valid API key from Google AI Studio
- Check Vercel logs: `npx vercel logs`

### "Session Issues"
- Ensure `SESSION_SECRET_KEY` is set
- It should be a 64-character hex string
- Generate new one if needed

---

## 📊 What Gets Deployed

```
Vercel Production:
├── Frontend (Static)
│   └── index.html → Served at root
│
└── API (Serverless Python)
    ├── /auth/login
    ├── /auth/logout
    ├── /auth/status
    ├── /chat (authenticated)
    └── /ask (public)
```

**URLs:**
- Frontend: `https://your-app.vercel.app`
- API: `https://your-app.vercel.app/auth/*`
- Chatbot: `https://your-app.vercel.app/chat`

---

## 🎉 Success!

Once deployed and configured, you'll have:

✅ **Live authenticated chatbot**
✅ **Powered by Gemini AI**
✅ **Secure session-based auth**
✅ **Rate limiting active**
✅ **Professional UI**
✅ **Global CDN delivery**
✅ **Automatic HTTPS**
✅ **Free hosting** (on Vercel free tier)

**Your app is production-ready!**

---

## 📝 Commands Reference

```bash
# Initial deployment
npx vercel login
npx vercel --prod --yes

# Set environment variables
npx vercel env add GEMINI_API_KEY production
npx vercel env add SESSION_SECRET_KEY production
npx vercel env add ADMIN_PASSWORD production

# Redeploy after changes
npx vercel --prod

# View logs
npx vercel logs

# Check deployments
npx vercel ls

# Remove deployment
npx vercel remove [deployment-url]
```

---

## 🔑 Important Notes

1. **Keep your API keys secure** - Never commit `.env` to git
2. **Session secret is critical** - Generate a strong random key
3. **Free tier limits** - Vercel free tier has execution time limits
4. **Cold starts** - First request may take 1-2 seconds
5. **Gemini free tier** - 60 requests/minute

---

**Ready to deploy? Run the commands above!** 🚀
