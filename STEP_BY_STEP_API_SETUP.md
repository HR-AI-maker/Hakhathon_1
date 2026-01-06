# 🔑 API Keys Setup - Complete Step-by-Step Guide

I'll walk you through getting each API key. Follow these steps carefully!

---

## 📍 **STEP 1: Get Gemini API Key (2 minutes)**

### What I Just Did For You:
✅ Opened the Gemini API page in your browser: https://aistudio.google.com/app/apikey

### What YOU Need to Do:

**1.1** Look at the browser window that just opened

**1.2** Sign in with your Google account (if not already signed in)

**1.3** You'll see a page titled "Get API Key" or "API Keys"

**1.4** Click the blue button that says **"Create API Key"**

**1.5** A popup will appear asking "Create API key in new project"
   - Click **"Create API key in new project"**
   - OR select an existing project if you have one

**1.6** Your API key will appear! It looks like this:
   ```
   AIzaSyABC123def456GHI789jkl012MNO345pqr678
   ```

**1.7** Click the **"Copy"** button next to the key

**1.8** Open the file: `YOUR_API_KEYS.txt` on your desktop

**1.9** Replace this line:
   ```
   GEMINI_API_KEY=PASTE_YOUR_KEY_HERE
   ```

   With:
   ```
   GEMINI_API_KEY=AIzaSy[your actual key here]
   ```

**✅ STEP 1 COMPLETE!** You now have your Gemini API Key!

---

## 📍 **STEP 2: Session Secret Key (Already Done!)**

### ✅ I Already Generated This For You!

Your SESSION_SECRET_KEY is:
```
2ce8dab0bea856a5ee545c24302790a948db1dd50fd3fc8a43d19fe91cb7c612
```

**Nothing to do here - just use this value when adding to Vercel!**

---

## 📍 **STEP 3: Choose Admin Password (30 seconds)**

### What YOU Need to Do:

**3.1** Think of a secure password for admin access

**Good password examples:**
- `MySecurePass2024!`
- `Hakathon@Physical2024`
- `Admin#AI2024!`

**3.2** Open the file: `YOUR_API_KEYS.txt`

**3.3** Replace this line:
   ```
   ADMIN_PASSWORD=YOUR_PASSWORD_HERE
   ```

   With your chosen password:
   ```
   ADMIN_PASSWORD=MySecurePass2024!
   ```

**✅ STEP 3 COMPLETE!** You chose your admin password!

---

## 📍 **STEP 4: Add Keys to Vercel (5 minutes)**

Now we add all three keys to your Vercel deployment.

### 4.1 Open Vercel Dashboard

**Option A:** Click this link:
- https://vercel.com/dashboard

**Option B:** I'll open it for you - just say "open vercel"

### 4.2 Find Your Project

- You'll see a list of projects
- Click on the one you just deployed (probably named "claude" or similar)

### 4.3 Go to Settings

- Click the **"Settings"** tab at the top

### 4.4 Open Environment Variables

- In the left sidebar, click **"Environment Variables"**

### 4.5 Add First Key - GEMINI_API_KEY

**Click the "Add New" button**, then:

```
Name: GEMINI_API_KEY
Value: [Paste the key you got from Google - starts with AIza...]
```

**Environment:** Check ALL THREE boxes:
- ✓ Production
- ✓ Preview
- ✓ Development

**Click "Save"**

### 4.6 Add Second Key - SESSION_SECRET_KEY

**Click "Add New" again**, then:

```
Name: SESSION_SECRET_KEY
Value: 2ce8dab0bea856a5ee545c24302790a948db1dd50fd3fc8a43d19fe91cb7c612
```

**Environment:** Check ALL THREE boxes:
- ✓ Production
- ✓ Preview
- ✓ Development

**Click "Save"**

### 4.7 Add Third Key - ADMIN_PASSWORD

**Click "Add New" again**, then:

```
Name: ADMIN_PASSWORD
Value: [Your chosen password from Step 3]
```

**Environment:** Check ALL THREE boxes:
- ✓ Production
- ✓ Preview
- ✓ Development

**Click "Save"**

**✅ STEP 4 COMPLETE!** All keys added to Vercel!

---

## 📍 **STEP 5: Redeploy (1 minute)**

The keys won't work until you redeploy!

### Option A: Using Command Line

Open Command Prompt and run:
```bash
cd C:\Users\lenovo\Desktop\Hakathon_I\claude
vercel --prod
```

### Option B: Using Vercel Dashboard

1. Still in your project, click **"Deployments"** tab
2. Find the most recent deployment
3. Click the three dots **"..."** on the right
4. Click **"Redeploy"**
5. Click **"Redeploy"** again to confirm

**✅ STEP 5 COMPLETE!** Your app is redeploying with the new keys!

---

## 📍 **STEP 6: Test Your App (2 minutes)**

Wait 1-2 minutes for the redeployment to complete, then:

### 6.1 Visit Your Vercel URL

Go to: `https://[your-project].vercel.app`

### 6.2 Test Login

- Username: `demo`
- Password: `demo123`
- Click "Login"

**You should successfully log in!**

### 6.3 Test Chatbot

Try asking:
- "What is Physical AI?"
- "What is ROS 2?"
- "Explain digital twins"

**You should get AI-powered responses!**

**✅ ALL DONE!** Your app is fully functional! 🎉

---

## 🎯 Quick Summary

Here's what we did:

1. ✅ Got Gemini API Key from Google
2. ✅ Used pre-generated Session Secret Key
3. ✅ Chose Admin Password
4. ✅ Added all 3 keys to Vercel Dashboard
5. ✅ Redeployed the application
6. ✅ Tested the live app

---

## 🚨 Troubleshooting

**Problem: Can't get Gemini API Key**
- Make sure you're signed in to Google
- Try this link: https://aistudio.google.com/app/apikey
- API is free with quota limits

**Problem: Keys not working after adding**
- Did you redeploy? (Step 5 is required!)
- Check all three environments are selected
- Wait 1-2 minutes after redeployment

**Problem: Login fails**
- Make sure SESSION_SECRET_KEY is added
- Check you redeployed after adding keys
- Try demo/demo123 credentials

**Problem: No AI responses**
- Verify GEMINI_API_KEY is correct
- Check you copied the entire key (starts with AIza)
- Make sure billing is enabled in Google Cloud (usually auto-enabled for free tier)

---

## 📞 Need More Help?

If you're stuck on any step, just tell me:
- "Help with step 1" (or whichever step)
- "Open Gemini page again"
- "How do I find Vercel dashboard"

I'm here to help! 🚀
