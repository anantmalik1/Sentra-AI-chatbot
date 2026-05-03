---
title: Sentra AI Chatbot
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: docker
app_file: app.py
pinned: false
---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00ffc8,50:7c3aed,100:00b4ff&height=200&section=header&text=SENTRA%20AI&fontSize=80&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Cyberpunk%20Emotion%20Chatbot&descAlignY=60&descSize=20" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=700&size=24&pause=1000&color=00FFC8&center=true&vCenter=true&width=600&lines=🤖+Next+Gen+AI+Chatbot;⚡+3+Emotion+Modes;🎨+Cyberpunk+Neon+UI;🚀+Powered+by+Mistral+AI;💬+Live+on+Hugging+Face!" alt="Typing SVG" />

<br/>

<img src="https://img.shields.io/badge/STATUS-LIVE-00ffc8?style=for-the-badge&logo=statuspage&logoColor=black" />
<img src="https://img.shields.io/badge/MISTRAL_AI-000000?style=for-the-badge&logo=openai&logoColor=white" />
<img src="https://img.shields.io/badge/STREAMLIT-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
<img src="https://img.shields.io/badge/DOCKER-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
<img src="https://img.shields.io/badge/PYTHON-3.13-blue?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/LANGCHAIN-00A67E?style=for-the-badge&logo=chainlink&logoColor=white" />

<br/><br/>

<img src="https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif" width="700" style="border-radius: 20px;"/>

<br/><br/>

### 🌐 LIVE DEMO
[![LAUNCH APP](https://img.shields.io/badge/🚀_LAUNCH_SENTRA_AI-LIVE_NOW-00ffc8?style=for-the-badge&logoColor=black)](https://huggingface.co/spaces/anantmalik125/Sentra-AI-chatbot)
[![HUGGING FACE](https://img.shields.io/badge/🤗_HuggingFace-Space-FFD21E?style=for-the-badge)](https://huggingface.co/spaces/anantmalik125/Sentra-AI-chatbot)

</div>

---

## ⚡ WHAT IS SENTRA AI?

<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=Share+Tech+Mono&size=14&pause=2000&color=7c3aed&center=true&vCenter=true&width=700&lines=A+futuristic+AI+chatbot+that+adapts+its+personality+to+your+mood.;Switch+between+3+emotion+modes+in+real-time.;Built+with+Cyberpunk+UI+%2B+Mistral+AI." />
</div>

> 🌌 **Sentra AI** is not just a chatbot — it's an **emotion-driven AI experience**. Choose from 3 powerful personality modes and chat with an AI that truly matches your vibe. Built with a stunning Cyberpunk Neon UI, smooth animations, and Mistral AI under the hood.

---

## 🧠 AI EMOTION MODES

<div align="center">

| 😤 ANGRY MODE | 😂 FUNNY MODE | 😢 SAD MODE |
|:---:|:---:|:---:|
| ![Angry](https://img.shields.io/badge/MODE-ANGRY-ff4444?style=for-the-badge) | ![Funny](https://img.shields.io/badge/MODE-FUNNY-ffd700?style=for-the-badge) | ![Sad](https://img.shields.io/badge/MODE-SAD-6496ff?style=for-the-badge) |
| Aggressive & Impatient | Hilarious & Witty | Empathetic & Emotional |
| Zero patience, maximum fire 🔥 | Life's too short to be serious 🎭 | Feels every word with you 💙 |

</div>

---

## ✨ FEATURES

<div align="center">

```
╔══════════════════════════════════════════════════════════════════╗
║                      SENTRA AI FEATURES                         ║
╠══════════════════════════════════════════════════════════════════╣
║  🎨  Cyberpunk Neon Dark Theme      ⚡  Animated Backgrounds    ║
║  🧊  3D Card Hover Effects          💬  Live Chat Bubbles       ║
║  ✨  Fade-In Message Animation      📊  Live Status Bar         ║
║  🌌  Grid Overlay Visual FX         🔄  3 Emotion Mode Switch   ║
║  📱  Fully Responsive Design        🗑️  Clear Chat Feature      ║
║  🚀  HuggingFace Deployment         🔐  Secure API Key Handling ║
╚══════════════════════════════════════════════════════════════════╝
```

</div>

---

## 🛠️ TECH STACK

<div align="center">

<img src="https://skillicons.dev/icons?i=python,docker,git,vscode&theme=dark" />

<br/><br/>

| Layer | Technology | Purpose |
|:---:|:---:|:---:|
| 🐍 Language | Python 3.13 | Core runtime |
| 🖥️ Frontend | Streamlit | UI Framework |
| 🤖 AI Model | Mistral AI | Language Model |
| 🔗 Orchestration | LangChain | AI Pipeline |
| 🐳 Container | Docker | Deployment |
| ☁️ Hosting | Hugging Face | Cloud Platform |

</div>

---

## 🎨 UI PREVIEW

<div align="center">

<img src="https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif" width="600" style="border-radius:16px"/>

*Cyberpunk Neon UI with smooth animations, glowing cards, and live chat bubbles*

</div>

---

## 🚀 RUN LOCALLY

```bash
# Clone the repo
git clone https://huggingface.co/spaces/anantmalik125/Sentra-AI-chatbot
cd Sentra-AI-chatbot

# Install dependencies
pip install -r requirements.txt

# Setup environment
echo "MISTRAL_API_KEY=your_key_here" > .env

# Launch the app
streamlit run app.py
```

---

## 🐳 RUN WITH DOCKER

```bash
# Build image
docker build -t sentra-ai .

# Run container
docker run -p 8501:8501 -e MISTRAL_API_KEY=your_key_here sentra-ai

# Open browser → http://localhost:8501
```

---

## 📁 PROJECT STRUCTURE

```
Sentra-AI-chatbot/
│
├── 🐍  app.py              ← Main Streamlit application
├── 📦  requirements.txt    ← Python dependencies
├── 🐳  Dockerfile          ← Docker configuration
└── 📖  README.md           ← This file
```

---

## 🔑 ENVIRONMENT SETUP

<div align="center">

| Variable | Description | Required |
|:---:|:---:|:---:|
| `MISTRAL_API_KEY` | Your Mistral AI API key | ✅ YES |

</div>

> 🔗 Get your **FREE** API key at [console.mistral.ai](https://console.mistral.ai)
>
> 🤗 On Hugging Face: **Settings → Repository Secrets → Add** `MISTRAL_API_KEY`

---

## 📊 PROJECT STATS

<div align="center">

<img src="https://img.shields.io/badge/LINES_OF_CODE-663-7c3aed?style=for-the-badge" />
<img src="https://img.shields.io/badge/EMOTION_MODES-3-ff4444?style=for-the-badge" />
<img src="https://img.shields.io/badge/ANIMATIONS-INFINITE-ffd700?style=for-the-badge" />
<img src="https://img.shields.io/badge/VIBE-CYBERPUNK-00ffc8?style=for-the-badge" />

</div>

---

## 👨‍💻 AUTHOR

<div align="center">

**anantmalik125**

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&size=14&pause=1000&color=00FFC8&center=true&vCenter=true&width=400&lines=Building+cool+AI+projects+🚀;Follow+for+more+awesome+stuff+⭐" />

<br/>

[![HuggingFace](https://img.shields.io/badge/🤗_HuggingFace-anantmalik125-FFD21E?style=for-the-badge)](https://huggingface.co/anantmalik125)

</div>

---

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00b4ff,50:7c3aed,100:00ffc8&height=120&section=footer" width="100%"/>

<div align="center">

**Made with ❤️ + ☕ + 🤖 by anantmalik125**

*If you like this project, please ⭐ star it on Hugging Face!*

</div>
