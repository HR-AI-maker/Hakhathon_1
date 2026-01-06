# 🚀 Deploy to Vercel - DO THIS NOW

## Quick Steps (2 minutes)

### Step 1: Open a new terminal/command prompt

Press `Win + R`, type `cmd`, press Enter

### Step 2: Navigate to project directory

```bash
cd C:\Users\lenovo\Desktop\Hakathon_I\claude
```

### Step 3: Login to Vercel

```bash
vercel login
```

This will:
1. Open your browser automatically
2. Ask you to sign in with GitHub, GitLab, Bitbucket, or Email
3. Authenticate the CLI

**Just click through the browser prompts - it takes 30 seconds!**

### Step 4: Deploy to Production

```bash
vercel --prod
```

The CLI will ask a few questions:
- **Set up and deploy?** → Press ENTER (Yes)
- **Which scope?** → Press ENTER (your account)
- **Link to existing project?** → Type `N` and press ENTER
- **What's your project's name?** → Type `physical-ai-chatbot` or press ENTER
- **In which directory is your code located?** → Press ENTER (./)
- **Want to override settings?** → Type `N` and press ENTER

### Step 5: Get Your Deployment URL

Vercel will show you a URL like:
```
https://physical-ai-chatbot-xxx.vercel.app
```

**Copy this URL!**

### Step 6: Set Environment Variables

Open the URL in your browser or go to:
https://vercel.com/dashboard

Then:
1. Click on your project
2. Go to **Settings** → **Environment Variables**
3. Add these three variables:

**GEMINI_API_KEY**
- Get from: https://makersuite.google.com/app/apikey
- Click "Create API Key"
- Copy and paste

**SESSION_SECRET_KEY**
- Run this in terminal:
  ```bash
  python -c "import secrets; print(secrets.token_hex(32))"
  ```
- Copy the output

**ADMIN_PASSWORD**
- Choose any password (e.g., `MySecurePass123!`)

4. Click **Save** for each variable

### Step 7: Redeploy (to apply env vars)

```bash
vercel --prod
```

### Step 8: Test Your Live App!

Visit your Vercel URL and test the chatbot!

---

## 🔥 Even Faster: One-Line Deploy

If you already have a Vercel account and are logged in:

```bash
vercel --prod
```

That's it!

---

## Need API Keys?

### Get Gemini API Key (FREE):
1. Go to https://makersuite.google.com/app/apikey
2. Sign in with Google
3. Click "Create API Key"
4. Copy the key

### Generate Session Secret:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

---

## Troubleshooting

**Error: "Not logged in"**
→ Run: `vercel login`

**Error: "No credentials found"**
→ Run: `vercel login` and complete browser auth

**Deployment stuck?**
→ Press Ctrl+C and run `vercel --prod` again

**Need help?**
→ Check deployment logs at https://vercel.com/dashboard
