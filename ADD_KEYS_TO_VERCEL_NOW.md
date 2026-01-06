# 🔑 Add Your API Keys to Vercel - Follow These Steps

I just opened Vercel Dashboard for you: https://vercel.com/dashboard

---

## 📋 **YOUR 3 KEYS (Copy These):**

### Key 1: GEMINI_API_KEY
```
The key you just got from Google (starts with AIza...)
```

### Key 2: SESSION_SECRET_KEY
```
2ce8dab0bea856a5ee545c24302790a948db1dd50fd3fc8a43d19fe91cb7c612
```

### Key 3: ADMIN_PASSWORD
```
Choose any password - Example: MySecure2024!
```

---

## 🎯 **STEP-BY-STEP INSTRUCTIONS:**

### Step 1: Find Your Project
- Look at the browser I just opened
- You'll see your project listed (probably named "claude")
- **CLICK ON IT**

### Step 2: Go to Settings
- At the top of the page, click the **"Settings"** tab

### Step 3: Open Environment Variables
- On the left sidebar, click **"Environment Variables"**

### Step 4: Add GEMINI_API_KEY

Click the **"Add New"** button (or "Add Another" if you see it)

Fill in:
```
Key: GEMINI_API_KEY
Value: [Paste your Gemini API key here - the one starting with AIza]
```

**IMPORTANT:** Under "Environment", check ALL THREE boxes:
- ✓ Production
- ✓ Preview
- ✓ Development

Click **"Save"**

---

### Step 5: Add SESSION_SECRET_KEY

Click **"Add New"** again

Fill in:
```
Key: SESSION_SECRET_KEY
Value: 2ce8dab0bea856a5ee545c24302790a948db1dd50fd3fc8a43d19fe91cb7c612
```

**IMPORTANT:** Check ALL THREE boxes:
- ✓ Production
- ✓ Preview
- ✓ Development

Click **"Save"**

---

### Step 6: Add ADMIN_PASSWORD

Click **"Add New"** again

Fill in:
```
Key: ADMIN_PASSWORD
Value: [Your chosen password - e.g., MySecure2024!]
```

**IMPORTANT:** Check ALL THREE boxes:
- ✓ Production
- ✓ Preview
- ✓ Development

Click **"Save"**

---

## ✅ **Verification Checklist**

After adding all keys, you should see 3 environment variables listed:
- [ ] GEMINI_API_KEY
- [ ] SESSION_SECRET_KEY
- [ ] ADMIN_PASSWORD

Each should show: "Production, Preview, Development"

---

## 🔄 **NEXT STEP: Redeploy**

After adding all 3 keys, you MUST redeploy!

**Option A - Command Line:**
```bash
cd C:\Users\lenovo\Desktop\Hakathon_I\claude
vercel --prod
```

**Option B - Vercel Dashboard:**
1. Click "Deployments" tab at the top
2. Find the latest deployment
3. Click the three dots "..." on the right
4. Click "Redeploy"
5. Confirm by clicking "Redeploy" again

---

## 🎉 **After Redeployment**

Wait 1-2 minutes, then test your app:
1. Visit your Vercel URL
2. Login with: demo / demo123
3. Ask the chatbot: "What is Physical AI?"
4. You should get an AI response!

---

## 📝 **Visual Guide**

Here's what the Environment Variables page looks like:

```
╔══════════════════════════════════════════════════╗
║  Settings > Environment Variables                 ║
╠══════════════════════════════════════════════════╣
║                                                   ║
║  [Add New]                                        ║
║                                                   ║
║  ┌─────────────────────────────────────────────┐ ║
║  │ GEMINI_API_KEY                              │ ║
║  │ AIzaSy••••••••••••••••••                    │ ║
║  │ Production, Preview, Development            │ ║
║  └─────────────────────────────────────────────┘ ║
║                                                   ║
║  ┌─────────────────────────────────────────────┐ ║
║  │ SESSION_SECRET_KEY                          │ ║
║  │ 2ce8da••••••••••••••••••                    │ ║
║  │ Production, Preview, Development            │ ║
║  └─────────────────────────────────────────────┘ ║
║                                                   ║
║  ┌─────────────────────────────────────────────┐ ║
║  │ ADMIN_PASSWORD                              │ ║
║  │ ••••••••••                                  │ ║
║  │ Production, Preview, Development            │ ║
║  └─────────────────────────────────────────────┘ ║
║                                                   ║
╚══════════════════════════════════════════════════╝
```

---

## ❓ **Need Help?**

Just tell me:
- "I'm on the Vercel dashboard" - I'll guide you from there
- "I added all keys" - I'll help you redeploy
- "I'm stuck on step X" - I'll walk you through it
