# Setting Environment Variables in Vercel

## ✅ Your Generated Values

### 1. SESSION_SECRET_KEY (Generated)
```
cadc2ec4da43cdd879441eb22b96c93f05dacd1f22b5a6ba58aee1c0260c17d3
```
**Copy this entire string!**

### 2. GEMINI_API_KEY (You need to get this)
Get your FREE Gemini API key from Google:
👉 https://aistudio.google.com/app/apikey

### 3. ADMIN_PASSWORD (Your choice)
Choose any secure password for the admin account.
Example: `MySecurePass123!`

---

## 🎯 Method 1: Via Vercel Dashboard (Recommended - Easiest)

### Step-by-Step Guide:

#### Step 1: Go to Vercel Dashboard
1. Open: https://vercel.com/dashboard
2. You should see your deployed project listed

#### Step 2: Click Your Project
- Look for "physical-ai-textbook" or similar name
- Click on it

#### Step 3: Go to Settings
1. Click **Settings** tab (top navigation)
2. Click **Environment Variables** in the left sidebar

#### Step 4: Add GEMINI_API_KEY
1. Click **Add Variable** button
2. Fill in:
   - **Key:** `GEMINI_API_KEY`
   - **Value:** (paste your Gemini API key from Google AI Studio)
   - **Environments:** Check ✅ **Production**
3. Click **Save**

#### Step 5: Add SESSION_SECRET_KEY
1. Click **Add Variable** button again
2. Fill in:
   - **Key:** `SESSION_SECRET_KEY`
   - **Value:** `cadc2ec4da43cdd879441eb22b96c93f05dacd1f22b5a6ba58aee1c0260c17d3`
   - **Environments:** Check ✅ **Production**
3. Click **Save**

#### Step 6: Add ADMIN_PASSWORD
1. Click **Add Variable** button again
2. Fill in:
   - **Key:** `ADMIN_PASSWORD`
   - **Value:** (your chosen admin password)
   - **Environments:** Check ✅ **Production**
3. Click **Save**

#### Step 7: Redeploy
1. Go to **Deployments** tab
2. Find your latest deployment
3. Click the **⋯** (three dots) menu
4. Click **Redeploy**
5. Wait 1-2 minutes for deployment to complete

---

## 🎯 Method 2: Via Vercel CLI (Advanced)

If you prefer command line:

### Step 1: Set GEMINI_API_KEY
```bash
npx vercel env add GEMINI_API_KEY production
```
When prompted, paste your Gemini API key

### Step 2: Set SESSION_SECRET_KEY
```bash
npx vercel env add SESSION_SECRET_KEY production
```
When prompted, paste: `cadc2ec4da43cdd879441eb22b96c93f05dacd1f22b5a6ba58aee1c0260c17d3`

### Step 3: Set ADMIN_PASSWORD
```bash
npx vercel env add ADMIN_PASSWORD production
```
When prompted, enter your chosen password

### Step 4: Redeploy
```bash
npx vercel --prod
```

---

## 🔑 How to Get Gemini API Key (FREE)

### Quick Steps:

1. **Go to Google AI Studio:**
   👉 https://aistudio.google.com/app/apikey

2. **Sign in with Google Account**
   - Use any Gmail account
   - Accept terms of service

3. **Create API Key:**
   - Click **"Create API Key"** button
   - Choose **"Create API key in new project"**
   - Your key will be generated instantly

4. **Copy the Key:**
   - It starts with `AIza...`
   - Click copy button
   - Keep it safe!

5. **Add to Vercel:**
   - Use the dashboard method above
   - Paste in `GEMINI_API_KEY` field

**Cost:** FREE tier includes:
- 60 requests per minute
- 1,500 requests per day
- Perfect for testing and demos!

---

## ✅ Verification Checklist

After adding all environment variables and redeploying:

- [ ] GEMINI_API_KEY is set in Vercel
- [ ] SESSION_SECRET_KEY is set in Vercel
- [ ] ADMIN_PASSWORD is set in Vercel
- [ ] All three are marked for "Production" environment
- [ ] You clicked "Redeploy" after adding variables
- [ ] Deployment completed successfully (green checkmark)

---

## 🧪 Test Your Deployment

Once redeployed with environment variables:

1. **Open your Vercel URL**
   Example: `https://physical-ai-textbook-abc123.vercel.app`

2. **You should see the login page**
   - If you see an error, check environment variables

3. **Login with demo credentials:**
   - Username: `demo`
   - Password: `demo123`

4. **Test the chatbot:**
   - Ask: "What is Physical AI?"
   - You should get an AI-generated answer
   - Answer should include citations like [intro-...]

5. **Verify Gemini is working:**
   - The answer should be detailed and well-formatted
   - Not just keywords (that would be demo mode)
   - Should feel like AI-generated content

---

## 🐛 Troubleshooting

### "GEMINI_API_KEY not configured" error

**Solution:**
1. Verify the key is added in Vercel dashboard
2. Check it's set for "Production" environment
3. Make sure you redeployed after adding it
4. Key should start with `AIza`

### "Session expired" or auth issues

**Solution:**
1. Verify SESSION_SECRET_KEY is set
2. It should be exactly: `cadc2ec4da43cdd879441eb22b96c93f05dacd1f22b5a6ba58aee1c0260c17d3`
3. Redeploy after setting it
4. Clear browser cookies and try again

### Deployment succeeds but chatbot doesn't work

**Solution:**
1. Open browser console (F12)
2. Check for error messages
3. Verify all 3 environment variables are set
4. Check Vercel logs: `npx vercel logs`
5. Make sure you redeployed AFTER adding variables

### "Invalid API key" from Gemini

**Solution:**
1. Verify your Gemini API key is correct
2. Make sure it's not expired
3. Check quota hasn't been exceeded
4. Generate a new key if needed

---

## 📱 Quick Reference

### Your Values:

```
SESSION_SECRET_KEY=cadc2ec4da43cdd879441eb22b96c93f05dacd1f22b5a6ba58aee1c0260c17d3

GEMINI_API_KEY=<get from https://aistudio.google.com/app/apikey>

ADMIN_PASSWORD=<your choice>
```

### Important URLs:

- **Vercel Dashboard:** https://vercel.com/dashboard
- **Get Gemini Key:** https://aistudio.google.com/app/apikey
- **Vercel Docs:** https://vercel.com/docs/environment-variables

---

## 🎯 Summary - What You Need To Do

1. ✅ **SESSION_SECRET_KEY is already generated above** - just copy it
2. 🔑 **Get GEMINI_API_KEY** from https://aistudio.google.com/app/apikey
3. 🔒 **Choose ADMIN_PASSWORD** - any secure password
4. 📋 **Go to Vercel Dashboard** → Your Project → Settings → Environment Variables
5. ➕ **Add all three variables** (see Step-by-Step Guide above)
6. 🔄 **Redeploy** - Deployments tab → ⋯ → Redeploy
7. ✅ **Test** - Open your URL and login!

---

**Need help?** Check the troubleshooting section or the detailed step-by-step guide above!
