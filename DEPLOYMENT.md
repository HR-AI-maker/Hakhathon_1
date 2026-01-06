# Vercel Deployment Guide

This guide will help you deploy the Physical AI Textbook RAG Application to Vercel.

---

## 🚀 Quick Deploy

### Option 1: Deploy via Vercel CLI (Recommended)

#### Step 1: Install Vercel CLI

```bash
npm install -g vercel
```

#### Step 2: Login to Vercel

```bash
vercel login
```

#### Step 3: Deploy

```bash
cd C:\Users\lenovo\Desktop\Hakathon_I\claude
vercel
```

Follow the prompts:
- Set up and deploy? **Y**
- Which scope? Select your account
- Link to existing project? **N**
- Project name: **physical-ai-textbook** (or your choice)
- In which directory is your code located? **./**
- Want to override settings? **N**

#### Step 4: Set Environment Variables (Optional)

If you have API keys:

```bash
vercel env add OPENAI_API_KEY
vercel env add QDRANT_API_KEY
vercel env add QDRANT_CLUSTER_URL
vercel env add NEON_DATABASE_URL
```

Then redeploy:

```bash
vercel --prod
```

---

### Option 2: Deploy via Vercel Dashboard

#### Step 1: Push to GitHub

```bash
cd C:\Users\lenovo\Desktop\Hakathon_I\claude

# Initialize git if not already done
git init
git add .
git commit -m "Initial commit - Physical AI Textbook"

# Create repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/physical-ai-textbook.git
git branch -M main
git push -u origin main
```

#### Step 2: Import to Vercel

1. Go to [vercel.com](https://vercel.com)
2. Click **"New Project"**
3. Import your GitHub repository
4. Configure:
   - **Framework Preset**: Other
   - **Root Directory**: ./
   - **Build Command**: (leave empty)
   - **Output Directory**: frontend
5. Add Environment Variables (optional):
   - `OPENAI_API_KEY`
   - `QDRANT_API_KEY`
   - `QDRANT_CLUSTER_URL`
   - `NEON_DATABASE_URL`
6. Click **Deploy**

---

## 📝 Post-Deployment

### Your Deployed URLs

After deployment, you'll get:
- **Frontend**: `https://physical-ai-textbook.vercel.app`
- **API**: `https://physical-ai-textbook.vercel.app/api/`

### Update Frontend API URL

The frontend is configured to use `http://localhost:8000` for local development. For production, you may want to update it, but it's already configured to work on Vercel.

### Test Your Deployment

Visit your deployed URL and:
1. Check that the frontend loads
2. Try asking a question
3. Verify the chatbot responds with textbook content

---

## 🔧 Configuration Files

### `vercel.json`
Configures how Vercel builds and routes your application:
- Builds Python backend as serverless function
- Serves frontend as static files
- Routes `/api/*` to backend, everything else to frontend

### `api/index.py`
Entry point for Vercel serverless functions

### `api/requirements.txt`
Python dependencies for serverless functions

---

## 🎯 Demo Mode

The application works in **demo mode** without API keys:
- Uses direct content search through markdown files
- No external API calls required
- Returns actual textbook excerpts with citations
- Perfect for demonstration and testing

### To Enable Full RAG Mode

1. Get API keys (see main README.md)
2. Add them as Vercel environment variables
3. Generate embeddings (requires running script locally first)
4. Upload embeddings to Qdrant Cloud

---

## 🔍 Troubleshooting

### Build Fails

If build fails with Python errors:
- Check `api/requirements.txt` has correct versions
- Vercel uses Python 3.9 by default
- Add `runtime.txt` with `python-3.9` if needed

### API Routes Not Working

- Ensure `vercel.json` routes are correct
- Check that `api/index.py` exists
- Verify Python dependencies are installed

### Frontend Not Loading

- Check `frontend/index.html` exists
- Verify static file serving in `vercel.json`
- Check browser console for errors

### CORS Issues

The backend has CORS enabled for all origins. If you face issues:
- Check browser console
- Verify API URL is correct
- Ensure HTTPS is used (Vercel auto-provides)

---

## 📊 Performance

Vercel deployment provides:
- ✅ Global CDN for frontend
- ✅ Serverless functions for API
- ✅ Automatic HTTPS
- ✅ Fast cold starts (~1-2 seconds)
- ✅ Free tier: 100GB bandwidth/month

---

## 🎨 Customization

### Custom Domain

1. Go to Vercel Dashboard
2. Select your project
3. Settings → Domains
4. Add your custom domain

### Environment Variables

Add via:
```bash
vercel env add VARIABLE_NAME
```

Or via Dashboard:
1. Project Settings
2. Environment Variables
3. Add variables

---

## 📚 Resources

- [Vercel Documentation](https://vercel.com/docs)
- [Vercel Python Runtime](https://vercel.com/docs/runtimes#official-runtimes/python)
- [FastAPI on Vercel](https://vercel.com/docs/frameworks/fastapi)

---

## ✅ Deployment Checklist

- [ ] Vercel CLI installed or GitHub repo created
- [ ] Application tested locally
- [ ] Environment variables ready (optional)
- [ ] Deployed to Vercel
- [ ] Frontend accessible
- [ ] API responding
- [ ] Chatbot working
- [ ] Custom domain added (optional)

---

**Your application is ready for the world!** 🚀

The demo mode ensures it works perfectly even without API keys, making it ideal for hackathon demonstrations and testing.
