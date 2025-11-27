# 🚀 Deployment Guide - YouTube Transcript Chatbot

This guide will help you deploy your RAG chatbot to Streamlit Cloud and get a public URL to share with your team.

## 📋 Prerequisites

1. **GitHub Account**: You need a GitHub account (free)
2. **Streamlit Cloud Account**: Sign up at [share.streamlit.io](https://share.streamlit.io) (free)
3. **OpenAI API Key**: Get one from [OpenAI Platform](https://platform.openai.com/api-keys)

---

## 🎯 Step-by-Step Deployment

### Step 1: Prepare Your Repository

1. **Create a `.env` file locally** (for testing, DON'T commit this):
   ```bash
   cp .env.example .env
   ```
   Then add your OpenAI API key to the `.env` file.

2. **Test locally first**:
   ```bash
   cd RAG/Project
   streamlit run main.py
   ```
   Make sure everything works before deploying!

### Step 2: Push to GitHub

1. **Add files to git**:
   ```bash
   git add RAG/Project/
   git commit -m "Add YouTube Transcript Chatbot"
   git push origin main
   ```

2. **Verify files are on GitHub**:
   - Go to your GitHub repository
   - Navigate to `RAG/Project/`
   - Ensure these files are present:
     - `main.py`
     - `Indexing.py`
     - `Retriver.py`
     - `Augmentation.py`
     - `Generation.py`
     - `requirements.txt`
     - `.env.example`

### Step 3: Deploy to Streamlit Cloud

1. **Go to Streamlit Cloud**:
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Click "Sign in with GitHub"

2. **Create New App**:
   - Click "New app" button
   - Select your repository
   - Set the following:
     - **Main file path**: `RAG/Project/main.py`
     - **App URL**: Choose a custom URL (e.g., `youtube-chatbot`)

3. **Configure Secrets**:
   - Before deploying, click "Advanced settings"
   - Add your secrets in the "Secrets" section:
   ```toml
   OPENAI_API_KEY = "your_actual_api_key_here"
   ```

4. **Deploy**:
   - Click "Deploy!"
   - Wait 2-5 minutes for deployment

### Step 4: Get Your Public URL

Once deployed, you'll get a URL like:
```
https://your-app-name.streamlit.app
```

Share this URL with your team! 🎉

---

## 🔧 Troubleshooting

### Common Issues:

1. **"ModuleNotFoundError"**
   - Solution: Check that all packages are in `requirements.txt`

2. **"OpenAI API key not found"**
   - Solution: Add `OPENAI_API_KEY` to Streamlit Cloud secrets

3. **App keeps restarting**
   - Solution: Check logs in Streamlit Cloud dashboard
   - Might be hitting memory limits (free tier: 1GB)

4. **FAISS index not saving**
   - This is expected! Indices are rebuilt per session
   - For production, consider adding cloud storage

### Resource Limits (Free Tier):

- **Memory**: 1GB RAM
- **CPU**: Shared
- **Apps**: Up to 3 public apps
- **Storage**: Ephemeral (temporary)

---

## 🎨 Customization Options

### Change App Name & URL:
1. Go to Streamlit Cloud dashboard
2. Click on your app
3. Go to Settings → General
4. Update "App name" or "App URL"

### Update App:
Just push to GitHub - app auto-redeploys!
```bash
git add .
git commit -m "Update chatbot"
git push
```

### Add Custom Domain (Pro):
Streamlit Cloud Pro allows custom domains like `chatbot.yourcompany.com`

---

## 📊 Monitoring

### View Logs:
1. Go to Streamlit Cloud dashboard
2. Click on your app
3. Click "Manage app" → "Logs"

### Track Usage:
- Streamlit Cloud shows visitor count
- Monitor OpenAI API usage at [platform.openai.com](https://platform.openai.com/usage)

---

## 💰 Cost Considerations

### Streamlit Cloud:
- **Free tier**: Perfect for demos and small teams
- **Pro tier** ($20/month): More resources, custom domains

### OpenAI API:
- **GPT-3.5-turbo**: ~$0.001 per 1K tokens
- **Embeddings**: ~$0.0001 per 1K tokens
- Budget $5-10 for testing, adjust based on usage

---

## 🔐 Security Best Practices

1. **Never commit `.env` file** - it's in `.gitignore`
2. **Use Streamlit secrets** for API keys
3. **Rotate API keys** if accidentally exposed
4. **Set OpenAI usage limits** to prevent surprises

---

## 📈 Next Steps

### For Production:
1. **Add cloud storage** for FAISS indices (S3/GCS)
2. **Implement caching** to avoid re-indexing
3. **Add authentication** if needed
4. **Monitor costs** and set alerts
5. **Upgrade to Pro** for better performance

### Optional Enhancements:
- Add video title display
- Support for video playlists
- Export chat history
- Multiple language support
- Custom branding

---

## 🆘 Need Help?

- **Streamlit Docs**: [docs.streamlit.io](https://docs.streamlit.io)
- **Streamlit Forum**: [discuss.streamlit.io](https://discuss.streamlit.io)
- **LangChain Docs**: [python.langchain.com](https://python.langchain.com)

---

## ✅ Quick Deployment Checklist

- [ ] Tested app locally
- [ ] Pushed code to GitHub
- [ ] Created Streamlit Cloud account
- [ ] Added OpenAI API key to secrets
- [ ] Deployed app
- [ ] Got public URL
- [ ] Shared with team
- [ ] Set up usage monitoring

---

**Your public URL will be**: `https://your-chosen-name.streamlit.app`

Happy deploying! 🚀
