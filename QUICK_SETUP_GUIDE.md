# ⚡ Quick Setup Guide - Your Deployment is Live!

## 🎯 What You Just Deployed

Your **Physical AI & Humanoid Robotics Chatbot** is now live on Vercel!

**Features:**
- ✅ Authenticated login system
- ✅ AI-powered chatbot using Gemini
- ✅ RAG (Retrieval-Augmented Generation) with textbook content
- ✅ Beautiful modern UI
- ✅ Rate limiting and session management

---

## 🔧 CRITICAL: Add Environment Variables (Do This Now!)

Your app won't work properly until you add these 3 environment variables.

### Quick Steps:

1. **Open Vercel Dashboard**
   - Go to: https://vercel.com/dashboard
   - Click on your deployed project

2. **Navigate to Environment Variables**
   - Click "Settings" tab
   - Click "Environment Variables" in left sidebar

3. **Add Variable #1: GEMINI_API_KEY**
   ```
   Name: GEMINI_API_KEY
   Value: [Get from https://makersuite.google.com/app/apikey]
   Environments: ✓ Production ✓ Preview ✓ Development
   ```

   **How to get Gemini API Key:**
   - Visit: https://makersuite.google.com/app/apikey
   - Sign in with Google
   - Click "Create API Key" or "Get API Key"
   - Copy the key (starts with "AIza...")
   - Paste in Vercel

4. **Add Variable #2: SESSION_SECRET_KEY**
   ```
   Name: SESSION_SECRET_KEY
   Value: 83b78d36fa45ad95284cedd463917efaf3f8088c0c49a59e39e836f1daedc01e
   Environments: ✓ Production ✓ Preview ✓ Development
   ```
   *(Already generated for you - just copy/paste)*

5. **Add Variable #3: ADMIN_PASSWORD**
   ```
   Name: ADMIN_PASSWORD
   Value: [Choose your own secure password]
   Environments: ✓ Production ✓ Preview ✓ Development
   ```
   *(Example: MySecurePass2024!)*

6. **Click "Save" for each variable**

---

## 🔄 Redeploy to Apply Changes

After adding environment variables:

**Option A - Using CLI:**
```bash
cd C:\Users\lenovo\Desktop\Hakathon_I\claude
vercel --prod
```

**Option B - Using Dashboard:**
1. Go to "Deployments" tab
2. Find latest deployment
3. Click three dots (⋯)
4. Click "Redeploy"
5. Confirm

---

## ✅ Test Your Live App

### 1. Visit Your Vercel URL
Your app is deployed at: `https://[your-project-name].vercel.app`

### 2. Test Login
- **Demo Credentials:**
  - Username: `demo`
  - Password: `demo123`

### 3. Test Chatbot
Try asking:
- "What is Physical AI?"
- "What is ROS 2?"
- "What is a digital twin?"
- "How does VLA work?"

### 4. Verify Endpoints
- Frontend: `https://[your-url].vercel.app/`
- Health Check: `https://[your-url].vercel.app/health`
- API Docs: `https://[your-url].vercel.app/docs`

---

## 🎯 Success Checklist

After completing the steps above, verify:

- [ ] Added GEMINI_API_KEY to Vercel
- [ ] Added SESSION_SECRET_KEY to Vercel
- [ ] Added ADMIN_PASSWORD to Vercel
- [ ] Redeployed the app
- [ ] Frontend loads successfully
- [ ] Can login with demo/demo123
- [ ] Can ask questions and get AI responses
- [ ] Health endpoint shows "ok" status

---

## 🔍 Troubleshooting

**Problem: "GEMINI_API_KEY not configured"**
→ Make sure you added the key and redeployed

**Problem: Can't login**
→ Check SESSION_SECRET_KEY is set
→ Try demo/demo123 credentials

**Problem: No AI responses**
→ Verify GEMINI_API_KEY is valid
→ Check you have Gemini API access

**Problem: App shows errors**
→ Check deployment logs in Vercel dashboard
→ Verify all 3 env vars are set
→ Redeploy after adding variables

---

## 📊 Your Deployment Info

**Project Files:**
- Frontend: `/frontend/index.html`
- Backend API: `/rag_api/main.py`
- Configuration: `/vercel.json`

**Endpoints:**
- `/` - Frontend UI
- `/auth/login` - Login endpoint
- `/auth/logout` - Logout endpoint
- `/auth/status` - Check auth status
- `/chat` - Authenticated chatbot (requires login)
- `/health` - Health check
- `/docs` - API documentation

**Tech Stack:**
- Frontend: HTML/CSS/JavaScript
- Backend: FastAPI (Python)
- AI: Google Gemini 1.5 Flash
- Hosting: Vercel
- Auth: Session-based with cookies

---

## 🎉 You're All Set!

Once you've added the environment variables and redeployed, your chatbot will be fully functional and accessible to anyone with the URL!

**Share your deployment URL with others to let them try the chatbot!**

---

## 📞 Need Help?

- Vercel Docs: https://vercel.com/docs
- Gemini API: https://ai.google.dev/docs
- Project Files: Check the documentation in your project folder
