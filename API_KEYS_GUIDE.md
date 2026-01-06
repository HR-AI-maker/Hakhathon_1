# API Keys Setup Guide - Step by Step

This guide walks you through getting all API keys needed to run the Physical AI Textbook RAG application.

**Total Time**: ~15 minutes
**Cost**: $0 (all free tiers available)

---

## 1. OpenAI API Key (5 minutes)

### What You Need:
- OpenAI account
- Payment method (credit card)
- Minimum $5 credit recommended

### Step-by-Step:

#### 1.1 Create OpenAI Account

1. Go to: https://platform.openai.com/signup
2. Click "Sign up"
3. Choose sign-up method:
   - Email + password, OR
   - Continue with Google, OR
   - Continue with Microsoft
4. Verify your email if using email signup

#### 1.2 Add Payment Method

**Important**: OpenAI requires a payment method even for API usage.

1. After logging in, go to: https://platform.openai.com/account/billing/overview
2. Click "Add payment method"
3. Enter your credit card details
4. Add initial credit (minimum $5 recommended)
   - For this project, you'll use approximately $0.50-$2.00 total

#### 1.3 Generate API Key

1. Go to: https://platform.openai.com/api-keys
2. Click "+ Create new secret key"
3. Name it: `Physical AI Textbook` (or any name you prefer)
4. **IMPORTANT**: Copy the key immediately (starts with `sk-...`)
   - You won't be able to see it again!
   - Save it somewhere safe temporarily

**Your OpenAI API key looks like:**
```
sk-proj-aBcDeFgHiJkLmNoPqRsTuVwXyZ1234567890AbCdEfGhIjKlMnOpQrStUvWxYz
```

✅ **You now have your OpenAI API key!**

---

## 2. Qdrant Cloud API Key & Cluster URL (4 minutes)

### What You Need:
- Email address
- No payment method required (free tier)

### Step-by-Step:

#### 2.1 Create Qdrant Cloud Account

1. Go to: https://cloud.qdrant.io
2. Click "Get Started" or "Sign Up"
3. Sign up with:
   - Email + password, OR
   - Continue with GitHub, OR
   - Continue with Google
4. Verify your email

#### 2.2 Create a Cluster

1. After logging in, you'll see the dashboard
2. Click "Create cluster" or "+ New cluster"
3. Configure cluster:
   - **Name**: `physical-ai-textbook`
   - **Cloud Provider**: Choose any (AWS/GCP/Azure)
   - **Region**: Choose closest to you
   - **Configuration**: Select **Free tier** (1 GB RAM, 0.5 CPU)
4. Click "Create"
5. Wait ~30 seconds for cluster to deploy

#### 2.3 Get API Key and Cluster URL

1. Once cluster is created, click on it
2. You'll see:
   - **Cluster URL**: `https://xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.us-east-1-0.aws.cloud.qdrant.io:6333`
   - **API Key**: Click "Show" or "Copy" to reveal
3. Copy both:
   - **Cluster URL** (the full HTTPS URL)
   - **API Key** (random string)

**Your Qdrant credentials look like:**
```
QDRANT_CLUSTER_URL=https://abc12345-1234-5678-9abc-def012345678.us-east-1-0.aws.cloud.qdrant.io:6333

QDRANT_API_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.abc123def456
```

✅ **You now have your Qdrant credentials!**

---

## 3. Neon Postgres Connection String (4 minutes)

### What You Need:
- Email address
- No payment method required (free tier)

### Step-by-Step:

#### 3.1 Create Neon Account

1. Go to: https://neon.tech
2. Click "Sign up" or "Get started"
3. Sign up with:
   - GitHub (recommended), OR
   - Google, OR
   - Email
4. No email verification needed for GitHub/Google signup

#### 3.2 Create a Project

1. After logging in, click "Create a project" or "+ New project"
2. Configure project:
   - **Project name**: `physical-ai-textbook`
   - **Postgres version**: Use default (latest)
   - **Region**: Choose closest to you
   - **Compute size**: Use default (Free tier: 0.25 vCPU, 1 GB RAM)
3. Click "Create project"
4. Wait ~10 seconds for project to be created

#### 3.3 Get Connection String

1. After project is created, you'll see a connection details page
2. Look for "Connection string" or "Connection details"
3. You'll see options for different connection methods:
   - **Direct connection** (choose this)
   - Pooled connection
   - Serverless driver
4. Copy the connection string

**Important**: The connection string includes a password that's only shown once!

**Your Neon connection string looks like:**
```
postgresql://username:password@ep-cool-meadow-123456.us-east-2.aws.neon.tech/neondb?sslmode=require
```

Components:
- `username`: Your database username (usually same as project name)
- `password`: Auto-generated password (copy it now!)
- `ep-cool-meadow-123456.us-east-2.aws.neon.tech`: Your database host
- `neondb`: Default database name

**Alternative way to find it:**
1. Click on your project in the dashboard
2. Go to "Connection details" tab
3. Copy the full connection string

✅ **You now have your Neon connection string!**

---

## 4. Create Your `.env` File (2 minutes)

Now that you have all three credentials, create your `.env` file:

### 4.1 Create the File

1. Navigate to: `C:\Users\lenovo\Desktop\Hakathon_I\claude\`
2. Create a new file named `.env` (exactly, with the dot at the start)
   - In Windows: Right-click → New → Text Document → Rename to `.env`
   - Or use any text editor: File → Save As → `.env`

### 4.2 Add Your Credentials

Copy this template and replace with your actual values:

```env
# OpenAI API Configuration
OPENAI_API_KEY=sk-proj-YOUR_ACTUAL_OPENAI_KEY_HERE

# Qdrant Cloud Configuration
QDRANT_API_KEY=YOUR_ACTUAL_QDRANT_API_KEY_HERE
QDRANT_CLUSTER_URL=https://your-actual-cluster-url.aws.cloud.qdrant.io:6333

# Neon Postgres Configuration
NEON_DATABASE_URL=postgresql://username:password@your-host.aws.neon.tech/neondb?sslmode=require

# API Configuration (these defaults are fine)
API_HOST=0.0.0.0
API_PORT=8000
API_DEBUG=false

# RAG Configuration (these defaults are fine)
RAG_TOP_K=3
RAG_MIN_CONFIDENCE=0.7
RAG_MAX_CHUNKS_PER_MODULE=2

# Model Configuration (these defaults are fine)
EMBEDDING_MODEL=text-embedding-ada-002
EMBEDDING_DIMENSION=1536
LLM_MODEL=gpt-4
LLM_TEMPERATURE=0.2
LLM_MAX_TOKENS=500
```

### 4.3 Verify Your `.env` File

Your final `.env` should look something like this (with your real credentials):

```env
OPENAI_API_KEY=sk-proj-aBcDeFgHiJkLmNoPqRsTuVwXyZ1234567890AbCdEfGhIjKlMnOpQrStUvWxYz
QDRANT_API_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.abc123
QDRANT_CLUSTER_URL=https://abc12345-1234-5678-9abc-def012345678.us-east-1-0.aws.cloud.qdrant.io:6333
NEON_DATABASE_URL=postgresql://physical_ai_user:Xy9Zq2Wp5Mn@ep-cool-meadow-123456.us-east-2.aws.neon.tech/neondb?sslmode=require
API_HOST=0.0.0.0
API_PORT=8000
LLM_MODEL=gpt-4
RAG_TOP_K=3
```

**Save the file!**

---

## 5. Verify Your Setup (1 minute)

### 5.1 Check File Exists

Open Command Prompt:
```bash
cd C:\Users\lenovo\Desktop\Hakathon_I\claude
dir .env
```

You should see the `.env` file listed.

### 5.2 Check File Contents (Optional)

```bash
type .env
```

Verify it shows your API keys (be careful not to share this publicly!).

---

## ✅ Setup Complete!

You now have all three API keys configured!

**What you have:**
- ✅ OpenAI API key for GPT-4 and embeddings
- ✅ Qdrant Cloud cluster for vector database
- ✅ Neon Postgres database for metadata
- ✅ `.env` file with all credentials

**Next steps:**
1. Install Python packages: `pip install -r requirements.txt`
2. Setup database: Run `schema.sql` on Neon
3. Generate embeddings: `python scripts\generate_embeddings.py`
4. Start server: `python rag_api\main.py`

See `QUICKSTART.md` for detailed next steps!

---

## 💰 Cost Breakdown

### Free Tier Limits:

**OpenAI** (Pay-as-you-go):
- Embedding generation: ~44 chunks × $0.0001 = **~$0.004**
- GPT-4 queries: ~50 test queries × $0.03 = **~$1.50**
- **Total estimated**: $1.50-$2.00 for initial setup + testing

**Qdrant Cloud** (Free tier):
- 1 GB RAM, 0.5 CPU
- Enough for 100,000+ vectors
- **Cost**: $0 (free forever)

**Neon Postgres** (Free tier):
- 0.25 vCPU, 1 GB RAM
- 3 GB storage
- **Cost**: $0 (free forever)

**Total cost to run this project**: ~$2 (one-time for embeddings + testing)

---

## 🔒 Security Notes

**IMPORTANT**:
- Never commit `.env` to git (it's already in `.gitignore`)
- Never share your API keys publicly
- Rotate keys if accidentally exposed
- Monitor usage on each platform dashboard

**To rotate keys:**
- OpenAI: https://platform.openai.com/api-keys → Delete old → Create new
- Qdrant: Dashboard → Settings → Regenerate API key
- Neon: Dashboard → Settings → Reset password

---

## ❓ Troubleshooting

### OpenAI Issues

**"Insufficient quota"**
- Add more credit: https://platform.openai.com/account/billing/overview
- Check usage: https://platform.openai.com/usage

**"Invalid API key"**
- Verify key starts with `sk-`
- Check for extra spaces in `.env`
- Regenerate key if needed

### Qdrant Issues

**"Connection refused"**
- Verify cluster is running (green status in dashboard)
- Check cluster URL includes `:6333` port
- Ensure URL starts with `https://`

**"Unauthorized"**
- Verify API key is correct
- Try regenerating API key

### Neon Issues

**"Password authentication failed"**
- Get fresh connection string from dashboard
- Ensure password wasn't truncated
- Check for special characters in password (may need URL encoding)

**"Connection timeout"**
- Check if database is active (might be in sleep mode)
- Go to dashboard and wake it up

---

## 🎯 Ready to Run!

Once you have your `.env` file configured, you're ready to run the application!

See `QUICKSTART.md` for the next steps.
