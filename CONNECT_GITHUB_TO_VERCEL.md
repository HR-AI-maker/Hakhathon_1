# 🔗 Connect GitHub to Vercel - Complete Guide

I'm pushing your code to GitHub right now!

Your GitHub repo: https://github.com/HR-AI-maker/Hakhathon_1

---

## 🚀 STEP-BY-STEP: Import GitHub Repo to Vercel

I just opened this page for you: https://vercel.com/new

---

### STEP 1: Import Git Repository

On the Vercel page you see:

┌─────────────────────────────────────────────┐
│  Import Git Repository                     │
│                                             │
│  GitHub    GitLab    Bitbucket             │
│                                             │
│  [Connect GitHub Account]                  │
└─────────────────────────────────────────────┘

**CLICK:** "GitHub" or "Connect GitHub Account"

---

### STEP 2: Authorize Vercel

A popup will appear asking to authorize Vercel:

- **CLICK:** "Authorize Vercel"
- GitHub may ask for your password - enter it
- Grant Vercel access to your repositories

---

###STEP 3: Select Your Repository

After authorization, you'll see a list of your repositories:

┌─────────────────────────────────────────────┐
│  Import Git Repository                      │
│  ┌─────────────────────────────────────┐   │
│  │ 🔍 Search repositories...           │   │
│  └─────────────────────────────────────┘   │
│                                             │
│  ☐ Hakhathon_1                   [Import]  │
│  ☐ other-repo-1                  [Import]  │
│  ☐ other-repo-2                  [Import]  │
└─────────────────────────────────────────────┘

Find "Hakhathon_1" and **CLICK "Import"**

---

### STEP 4: Configure Project

You'll see project configuration:

┌─────────────────────────────────────────────┐
│  Configure Project                           │
│                                              │
│  Project Name: hakhathon-1                   │
│  Framework Preset: Other                     │
│  Root Directory: ./                          │
│  Build Command: [leave empty]                │
│  Output Directory: [leave empty]             │
│                                              │
│  Environment Variables:                      │
│  [Add environment variables here]            │
└─────────────────────────────────────────────┘

**ADD ENVIRONMENT VARIABLES NOW:**

Click "Add" or expand "Environment Variables"

Add these 3 variables:

**Variable 1:**
```
Name: GEMINI_API_KEY
Value: [Your Gemini API key]
```

**Variable 2:**
```
Name: SESSION_SECRET_KEY
Value: 2ce8dab0bea856a5ee545c24302790a948db1dd50fd3fc8a43d19fe91cb7c612
```

**Variable 3:**
```
Name: ADMIN_PASSWORD
Value: [Your chosen password]
```

---

### STEP 5: Deploy!

After adding environment variables:

**CLICK:** "Deploy"

Vercel will:
1. Clone your GitHub repo
2. Build the project
3. Deploy it
4. Give you a live URL!

---

## ⏱️ DEPLOYMENT TIME

- First deployment: 2-3 minutes
- You'll see a progress screen
- When done, you'll see: "Congratulations!" with your URL

---

## 🎉 AFTER DEPLOYMENT

You'll get a URL like:
```
https://hakhathon-1-xyz123.vercel.app
```

**Test it:**
1. Click "Visit" or copy the URL
2. Open in browser
3. Login with: demo / demo123
4. Ask: "What is Physical AI?"
5. Get AI response!

---

## 🔄 AUTOMATIC DEPLOYMENTS

Now whenever you push to GitHub:
```bash
git add .
git commit -m "Update chatbot"
git push
```

Vercel will automatically redeploy! 🚀

---

## 📋 QUICK CHECKLIST

- [ ] Opened Vercel import page
- [ ] Connected GitHub account
- [ ] Selected Hakhathon_1 repository
- [ ] Added GEMINI_API_KEY
- [ ] Added SESSION_SECRET_KEY
- [ ] Added ADMIN_PASSWORD
- [ ] Clicked Deploy
- [ ] Got deployment URL
- [ ] Tested the app

---

## 🆘 TROUBLESHOOTING

**Can't find repository?**
→ Make sure code pushed to GitHub successfully
→ Check GitHub repo exists: https://github.com/HR-AI-maker/Hakhathon_1

**Deployment fails?**
→ Check environment variables are set
→ Verify vercel.json is in root directory
→ Check build logs for errors

**App not working?**
→ Make sure all 3 env vars are added
→ Redeploy after adding variables
→ Check app logs in Vercel dashboard

---

## 💡 PRO TIPS

1. **Bookmark your deployment URL**
2. **Enable automatic deployments from main branch**
3. **Set up custom domain later (optional)**
4. **Monitor deployments in Vercel dashboard**

---

Your GitHub repo is connected and Vercel is ready to deploy! 🎊
