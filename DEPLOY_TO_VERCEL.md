# Deploy to Vercel - Quick Guide

## Prerequisites
✅ Vercel CLI is installed
✅ Local server tested successfully
✅ vercel.json configuration ready

## Step 1: Login to Vercel

```bash
vercel login
```

This will open your browser. Follow the authentication flow.

## Step 2: Set Environment Variables

You need to set these environment variables in Vercel:

### Required Variables:
```bash
GEMINI_API_KEY=your_gemini_api_key_here
SESSION_SECRET_KEY=your_random_secret_key_here
ADMIN_PASSWORD=your_admin_password_here
```

### Optional Variables (if using full RAG mode):
```bash
QDRANT_API_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.i_17XFcFgePIA3QwXtZgJ4Sgune8vtie6TSDwLcHG3o
QDRANT_CLUSTER_URL=https://dbdf8d97-4356-4b17-af69-1ebd8a201af6.europe-west3-0.gcp.cloud.qdrant.io
NEON_DATABASE_URL=your_postgres_connection_string
OPENAI_API_KEY=your_openai_api_key
```

## Step 3: Deploy

### Simple deployment:
```bash
vercel
```

### Production deployment:
```bash
vercel --prod
```

### Deploy with environment variables:
```bash
vercel --prod \
  -e GEMINI_API_KEY=your_key \
  -e SESSION_SECRET_KEY=$(openssl rand -hex 32) \
  -e ADMIN_PASSWORD=yourpassword
```

## Step 4: Set Environment Variables via Vercel Dashboard

1. Go to https://vercel.com/dashboard
2. Select your project
3. Click "Settings" > "Environment Variables"
4. Add the required variables:
   - `GEMINI_API_KEY`
   - `SESSION_SECRET_KEY` (generate with: `openssl rand -hex 32`)
   - `ADMIN_PASSWORD`

## Step 5: Verify Deployment

After deployment, Vercel will provide a URL like:
```
https://your-project.vercel.app
```

Test the endpoints:
- `https://your-project.vercel.app/` - Frontend
- `https://your-project.vercel.app/health` - Health check
- `https://your-project.vercel.app/docs` - API documentation

## How to Get API Keys

### GEMINI_API_KEY:
1. Go to https://makersuite.google.com/app/apikey
2. Create a new API key
3. Copy the key

### SESSION_SECRET_KEY:
Generate a random secret:
```bash
openssl rand -hex 32
```
OR
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### ADMIN_PASSWORD:
Choose a strong password for authentication.

## Troubleshooting

### Error: "Collection doesn't exist"
This is normal if you're not using the full RAG mode. The app will fall back to demo mode.

### Error: "Invalid Postgres connection"
Set NEON_DATABASE_URL or the app will skip database logging.

### Python version mismatch:
Vercel uses Python 3.9 by default. Our app works with Python 3.9+.

## Current Project Status

✅ Server running locally on http://localhost:8000
✅ Frontend HTML serving correctly
✅ Authentication system working
✅ Health check endpoint functional
✅ Vercel configuration (vercel.json) ready

## Quick Deploy Script

Run this single command after logging in:

```bash
vercel --prod
```

Then set environment variables in the Vercel dashboard.
