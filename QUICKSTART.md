# Quick Start Guide - Run the Application in 10 Minutes

Follow these steps to get the RAG application running:

---

## Step 1: Get API Keys (5 minutes)

### 1.1 OpenAI API Key
1. Go to https://platform.openai.com/api-keys
2. Sign in or create account
3. Click "Create new secret key"
4. Copy the key (starts with `sk-...`)

### 1.2 Qdrant Cloud (Free Tier)
1. Go to https://cloud.qdrant.io
2. Sign up for free account
3. Create a new cluster (free tier)
4. Copy:
   - **API Key**
   - **Cluster URL** (e.g., https://xyz.qdrant.io)

### 1.3 Neon Postgres (Free Tier)
1. Go to https://neon.tech
2. Sign up for free account
3. Create new project: `physical_ai_textbook`
4. Copy the **Connection String** (starts with `postgresql://...`)

---

## Step 2: Quick Setup (5 minutes)

### 2.1 Install Dependencies

Open Command Prompt or PowerShell:

```bash
cd C:\Users\lenovo\Desktop\Hakathon_I\claude

# Create virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

### 2.2 Configure Environment

Create a file named `.env` in the `claude` folder with your API keys:

```env
# OpenAI
OPENAI_API_KEY=sk-your_actual_openai_key_here

# Qdrant Cloud
QDRANT_API_KEY=your_qdrant_api_key_here
QDRANT_CLUSTER_URL=https://your-cluster.qdrant.io

# Neon Postgres
NEON_DATABASE_URL=postgresql://user:password@host/physical_ai_textbook

# API Config (defaults are fine)
API_HOST=0.0.0.0
API_PORT=8000
LLM_MODEL=gpt-4
RAG_TOP_K=3
```

### 2.3 Set Up Database

```bash
# Set the database URL (replace with yours)
set NEON_DATABASE_URL=postgresql://user:password@host/physical_ai_textbook

# Run schema
psql %NEON_DATABASE_URL% < schema.sql
```

**Alternative if `psql` not installed:**
- Open Neon dashboard
- Go to SQL Editor
- Copy/paste content from `schema.sql`
- Click "Run"

### 2.4 Generate Embeddings

```bash
python scripts\generate_embeddings.py
```

This takes ~2 minutes and:
- Creates embeddings for all 44 chunks
- Uploads to Qdrant
- Stores metadata in Postgres

**Expected output:**
```
Loaded 44 chunks
Created collection 'textbook_chunks'
Generating embeddings: 100%
✅ Embedding generation complete!
```

---

## Step 3: Run the Server

```bash
cd rag_api
python main.py
```

**Expected output:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**Server is running!** ✅

---

## Step 4: Test It

Open a **new terminal** (keep server running):

### Test 1: Health Check

```bash
curl http://localhost:8000/health
```

Expected:
```json
{"status": "ok", "qdrant": "ok", "postgres": "ok"}
```

### Test 2: Ask a Question

```bash
curl -X POST http://localhost:8000/ask ^
  -H "Content-Type: application/json" ^
  -d "{\"question\": \"What is Physical AI?\"}"
```

Expected response with citation:
```json
{
  "answer": "Physical AI is intelligence deployed in the physical world... [intro-sec1]",
  "sources": [{"citation_id": "intro-sec1", ...}]
}
```

### Test 3: Run Full Test Suite

```bash
python tests\test_queries.py
```

Expected: 50/50 tests pass ✅

---

## Step 5: Use the API

### Open Interactive API Docs

Go to: http://localhost:8000/docs

This opens Swagger UI where you can:
- Test queries interactively
- See request/response schemas
- Try different questions

### Example Questions to Try

**Single Module:**
- "What is ROS 2?"
- "What is the reality gap?"
- "What is the VLA agent loop?"

**Cross-Module:**
- "How does VLA connect to ROS 2?"
- "How does simulation help with robot development?"

**Should Refuse:**
- "What is the best programming language?"
- "How do I install Python?"

---

## Troubleshooting

### "Module not found" error
```bash
# Activate virtual environment
venv\Scripts\activate
pip install -r requirements.txt
```

### "Connection refused" to Qdrant/Postgres
- Verify API keys in `.env`
- Check if services are active in dashboards

### Embeddings generation fails
- Check OpenAI API key
- Ensure you have API credits
- Script is idempotent - just re-run it

### Can't connect to port 8000
- Check if another app is using port 8000
- Change `API_PORT` in `.env` to 8001

---

## Success Checklist

Your application is working when:

- [x] `/health` returns `"status": "ok"`
- [x] Questions return answers with `[citation-id]`
- [x] Out-of-scope questions are refused
- [x] Test suite passes 50/50 queries
- [x] Response time is < 3 seconds

---

## What's Next?

**You're done!** The RAG application is running.

**Optional enhancements:**
- Add Docusaurus web interface (see `DEPLOYMENT_GUIDE.md`)
- Deploy to GitHub Pages
- Add user authentication

**Need help?** Check `SETUP_GUIDE.md` for detailed explanations.
