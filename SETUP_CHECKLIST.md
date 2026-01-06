# Setup Checklist - Run the Application

Follow this checklist to get your Physical AI Textbook RAG application running.

---

## Part 1: Get API Keys (15 minutes)

### OpenAI API Key
- [ ] Go to https://platform.openai.com/signup
- [ ] Create account (or sign in)
- [ ] Add payment method at https://platform.openai.com/account/billing/overview
- [ ] Add $5-$10 credit (you'll use ~$2 total)
- [ ] Go to https://platform.openai.com/api-keys
- [ ] Click "Create new secret key"
- [ ] Name it "Physical AI Textbook"
- [ ] **Copy the key** (starts with `sk-...`)
- [ ] Save it somewhere safe

### Qdrant Cloud
- [ ] Go to https://cloud.qdrant.io
- [ ] Sign up (email or GitHub/Google)
- [ ] Click "Create cluster"
- [ ] Name: `physical-ai-textbook`
- [ ] Select **Free tier**
- [ ] Choose region closest to you
- [ ] Click "Create"
- [ ] Wait for cluster to deploy (~30 seconds)
- [ ] **Copy Cluster URL** (https://xxx.qdrant.io:6333)
- [ ] **Copy API Key** (click "Show" to reveal)

### Neon Postgres
- [ ] Go to https://neon.tech
- [ ] Sign up (GitHub/Google recommended)
- [ ] Click "Create project"
- [ ] Name: `physical-ai-textbook`
- [ ] Select **Free tier**
- [ ] Click "Create"
- [ ] **Copy connection string** (postgresql://...)
- [ ] Save the password (shown only once!)

---

## Part 2: Create .env File (2 minutes)

- [ ] Navigate to `C:\Users\lenovo\Desktop\Hakathon_I\claude\`
- [ ] Create new file named `.env`
- [ ] Open `.env` in text editor
- [ ] Copy template from `.env.example`
- [ ] Replace with your actual API keys:
  - [ ] `OPENAI_API_KEY=sk-...`
  - [ ] `QDRANT_API_KEY=...`
  - [ ] `QDRANT_CLUSTER_URL=https://...`
  - [ ] `NEON_DATABASE_URL=postgresql://...`
- [ ] Save the file
- [ ] Verify file exists: `dir .env`

---

## Part 3: Install Dependencies (3 minutes)

Open Command Prompt:

- [ ] `cd C:\Users\lenovo\Desktop\Hakathon_I\claude`
- [ ] `python -m venv venv`
- [ ] `venv\Scripts\activate` (Windows)
- [ ] `pip install -r requirements.txt`
- [ ] Wait for installation to complete

---

## Part 4: Setup Database (2 minutes)

### Option A: Using psql command-line
- [ ] `set NEON_DATABASE_URL=your_connection_string`
- [ ] `psql %NEON_DATABASE_URL% < schema.sql`
- [ ] Verify: Should see "CREATE TABLE" messages

### Option B: Using Neon Dashboard
- [ ] Go to Neon dashboard
- [ ] Open your `physical-ai-textbook` project
- [ ] Click "SQL Editor"
- [ ] Open `schema.sql` in text editor
- [ ] Copy all contents
- [ ] Paste into SQL Editor
- [ ] Click "Run"
- [ ] Verify: Should see "Success" messages

---

## Part 5: Generate Embeddings (2 minutes)

- [ ] `python scripts\generate_embeddings.py`
- [ ] Wait for completion (~1-2 minutes)
- [ ] Verify output shows:
  - [ ] "Loaded 44 chunks"
  - [ ] "Created collection 'textbook_chunks'"
  - [ ] "Generating embeddings: 100%"
  - [ ] "✅ Embedding generation complete!"

---

## Part 6: Start the Server (1 minute)

- [ ] `cd rag_api`
- [ ] `python main.py`
- [ ] Verify output shows:
  - [ ] "Uvicorn running on http://0.0.0.0:8000"
- [ ] Server is now running! ✅

---

## Part 7: Test the Application (2 minutes)

Open a **new Command Prompt** (keep server running):

### Test 1: Health Check
- [ ] `curl http://localhost:8000/health`
- [ ] Should return: `{"status": "ok", "qdrant": "ok", "postgres": "ok"}`

### Test 2: Simple Query
```bash
curl -X POST http://localhost:8000/ask -H "Content-Type: application/json" -d "{\"question\": \"What is Physical AI?\"}"
```
- [ ] Should return answer with `[intro-sec1]` citation

### Test 3: Full Test Suite
- [ ] `python tests\test_queries.py`
- [ ] Should show: "50/50 tests passed"

### Test 4: Open API Docs
- [ ] Open browser: http://localhost:8000/docs
- [ ] Try interactive query using Swagger UI

---

## ✅ Success Criteria

Your application is working if:

- [x] Health endpoint returns `status: ok`
- [x] Queries return answers with citations `[citation-id]`
- [x] Out-of-scope questions are refused politely
- [x] Test suite passes 50/50 queries
- [x] API docs open in browser
- [x] Response time is < 3 seconds

---

## 🎉 You're Done!

**Congratulations!** Your Physical AI Textbook RAG application is running!

### What You Can Do Now:

1. **Ask questions** via API:
   - "What is ROS 2?"
   - "What is the reality gap?"
   - "How does VLA connect to ROS 2?"

2. **View statistics**: `curl http://localhost:8000/stats`

3. **Check query logs**: View in Neon Postgres dashboard

4. **Add Docusaurus frontend** (optional): See `DEPLOYMENT_GUIDE.md`

---

## Next Steps (Optional)

- [ ] Deploy to Docusaurus (Phase 4)
- [ ] Publish to GitHub Pages (Phase 5)
- [ ] Add user authentication
- [ ] Customize for your needs

---

## Need Help?

- **Detailed API key instructions**: See `API_KEYS_GUIDE.md`
- **Quick start**: See `QUICKSTART.md`
- **Full deployment guide**: See `DEPLOYMENT_GUIDE.md`
- **Troubleshooting**: See `SETUP_GUIDE.md`

---

**Total Time**: ~30 minutes from start to running application
**Total Cost**: ~$2 (OpenAI credits only)
