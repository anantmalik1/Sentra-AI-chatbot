import streamlit as st
import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

# ─── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MoodBot AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── CUSTOM CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;600&family=Share+Tech+Mono&display=swap');

/* ── GLOBAL RESET ── */
* { box-sizing: border-box; margin: 0; padding: 0; }

html, body, .stApp {
    background: #020209 !important;
    color: #e0e0ff !important;
    font-family: 'Rajdhani', sans-serif !important;
}

/* ── ANIMATED BACKGROUND ── */
.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background:
        radial-gradient(ellipse 80% 50% at 20% 10%, rgba(0,255,200,0.07) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 80% 80%, rgba(120,0,255,0.08) 0%, transparent 60%),
        radial-gradient(ellipse 50% 60% at 50% 50%, rgba(0,100,255,0.04) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
    animation: bgPulse 8s ease-in-out infinite alternate;
}

@keyframes bgPulse {
    0%   { opacity: 0.6; }
    100% { opacity: 1; }
}

/* Grid overlay */
.stApp::after {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
        linear-gradient(rgba(0,255,200,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,255,200,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
}

/* ── HEADER ── */
.hero-header {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
    position: relative;
    z-index: 10;
}

.hero-title {
    font-family: 'Orbitron', monospace;
    font-size: clamp(2.2rem, 5vw, 3.8rem);
    font-weight: 900;
    letter-spacing: 0.12em;
    background: linear-gradient(135deg, #00ffc8, #00b4ff, #a855f7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    filter: drop-shadow(0 0 30px rgba(0,255,200,0.4));
    animation: titleGlow 3s ease-in-out infinite alternate;
}

@keyframes titleGlow {
    0%   { filter: drop-shadow(0 0 20px rgba(0,255,200,0.3)); }
    100% { filter: drop-shadow(0 0 50px rgba(168,85,247,0.5)); }
}

.hero-subtitle {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.9rem;
    color: rgba(0,255,200,0.6);
    letter-spacing: 0.3em;
    margin-top: 0.5rem;
    text-transform: uppercase;
}

/* ── DIVIDER ── */
.neon-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #00ffc8, #a855f7, transparent);
    margin: 1rem 0 2rem;
    animation: dividerFlow 4s linear infinite;
    background-size: 200% 100%;
}
@keyframes dividerFlow {
    0%   { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}

/* ── MODE CARDS ── */
.mode-section-title {
    font-family: 'Orbitron', monospace;
    font-size: 0.75rem;
    letter-spacing: 0.35em;
    color: rgba(0,255,200,0.5);
    text-align: center;
    text-transform: uppercase;
    margin-bottom: 1.2rem;
}

.mode-cards-row {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
    margin-bottom: 2rem;
    position: relative;
    z-index: 10;
}

.mode-card {
    flex: 1;
    min-width: 180px;
    max-width: 220px;
    padding: 1.4rem 1rem;
    border-radius: 16px;
    cursor: pointer;
    border: 1px solid transparent;
    position: relative;
    overflow: hidden;
    transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
    text-align: center;
}

.mode-card::before {
    content: '';
    position: absolute;
    inset: 0;
    opacity: 0;
    transition: opacity 0.3s ease;
    border-radius: 16px;
}

.mode-card:hover { transform: translateY(-6px) scale(1.03); }

/* Angry card */
.mode-card.angry {
    background: linear-gradient(135deg, rgba(255,50,50,0.08), rgba(200,0,0,0.12));
    border-color: rgba(255,80,80,0.3);
    box-shadow: 0 4px 30px rgba(255,50,50,0.1);
}
.mode-card.angry:hover {
    border-color: rgba(255,80,80,0.8);
    box-shadow: 0 8px 40px rgba(255,50,50,0.3), inset 0 0 20px rgba(255,50,50,0.05);
}
.mode-card.angry.selected {
    border-color: #ff5050;
    box-shadow: 0 0 30px rgba(255,80,80,0.5), 0 0 60px rgba(255,50,50,0.2);
    background: linear-gradient(135deg, rgba(255,50,50,0.2), rgba(200,0,0,0.2));
}

/* Funny card */
.mode-card.funny {
    background: linear-gradient(135deg, rgba(255,200,0,0.08), rgba(255,150,0,0.12));
    border-color: rgba(255,200,0,0.3);
    box-shadow: 0 4px 30px rgba(255,200,0,0.1);
}
.mode-card.funny:hover {
    border-color: rgba(255,200,0,0.8);
    box-shadow: 0 8px 40px rgba(255,200,0,0.3), inset 0 0 20px rgba(255,200,0,0.05);
}
.mode-card.funny.selected {
    border-color: #ffd700;
    box-shadow: 0 0 30px rgba(255,215,0,0.5), 0 0 60px rgba(255,200,0,0.2);
    background: linear-gradient(135deg, rgba(255,200,0,0.2), rgba(255,150,0,0.2));
}

/* Sad card */
.mode-card.sad {
    background: linear-gradient(135deg, rgba(100,150,255,0.08), rgba(50,100,200,0.12));
    border-color: rgba(100,150,255,0.3);
    box-shadow: 0 4px 30px rgba(100,150,255,0.1);
}
.mode-card.sad:hover {
    border-color: rgba(100,150,255,0.8);
    box-shadow: 0 8px 40px rgba(100,150,255,0.3), inset 0 0 20px rgba(100,150,255,0.05);
}
.mode-card.sad.selected {
    border-color: #6496ff;
    box-shadow: 0 0 30px rgba(100,150,255,0.5), 0 0 60px rgba(100,150,255,0.2);
    background: linear-gradient(135deg, rgba(100,150,255,0.2), rgba(50,100,200,0.2));
}

.mode-emoji { font-size: 2.4rem; margin-bottom: 0.5rem; display: block; }
.mode-name {
    font-family: 'Orbitron', monospace;
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    margin-bottom: 0.3rem;
}
.angry  .mode-name { color: #ff8080; }
.funny  .mode-name { color: #ffd700; }
.sad    .mode-name { color: #96b4ff; }

.mode-desc {
    font-size: 0.75rem;
    color: rgba(200,200,255,0.5);
    line-height: 1.4;
}

.selected-badge {
    position: absolute;
    top: 8px; right: 8px;
    font-size: 0.6rem;
    font-family: 'Share Tech Mono', monospace;
    letter-spacing: 0.1em;
    padding: 2px 6px;
    border-radius: 4px;
    background: rgba(0,255,200,0.15);
    color: #00ffc8;
    border: 1px solid rgba(0,255,200,0.4);
}

/* ── CHAT CONTAINER ── */
.chat-wrapper {
    position: relative;
    z-index: 10;
    max-width: 800px;
    margin: 0 auto;
    padding: 0 1rem;
}

.chat-container {
    background: rgba(5, 8, 25, 0.8);
    border: 1px solid rgba(0,255,200,0.1);
    border-radius: 20px;
    padding: 1.5rem;
    min-height: 350px;
    max-height: 460px;
    overflow-y: auto;
    backdrop-filter: blur(20px);
    box-shadow: 0 0 60px rgba(0,0,0,0.5), inset 0 1px 0 rgba(0,255,200,0.05);
    scroll-behavior: smooth;
}

/* Scrollbar */
.chat-container::-webkit-scrollbar { width: 4px; }
.chat-container::-webkit-scrollbar-track { background: transparent; }
.chat-container::-webkit-scrollbar-thumb {
    background: rgba(0,255,200,0.3);
    border-radius: 2px;
}

/* ── MESSAGES ── */
.msg {
    display: flex;
    gap: 0.8rem;
    margin-bottom: 1.2rem;
    animation: msgFadeIn 0.4s ease forwards;
    opacity: 0;
}

@keyframes msgFadeIn {
    from { opacity: 0; transform: translateY(12px); }
    to   { opacity: 1; transform: translateY(0); }
}

.msg.user  { flex-direction: row-reverse; }

.msg-avatar {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1rem;
    flex-shrink: 0;
    border: 1px solid rgba(255,255,255,0.1);
}

.msg.user .msg-avatar {
    background: linear-gradient(135deg, #00ffc8, #00b4ff);
    box-shadow: 0 0 15px rgba(0,255,200,0.3);
}
.msg.bot .msg-avatar {
    background: linear-gradient(135deg, #a855f7, #6366f1);
    box-shadow: 0 0 15px rgba(168,85,247,0.3);
}

.msg-bubble {
    max-width: 72%;
    padding: 0.85rem 1.1rem;
    border-radius: 16px;
    font-size: 0.92rem;
    line-height: 1.6;
    position: relative;
}

.msg.user .msg-bubble {
    background: linear-gradient(135deg, rgba(0,255,200,0.12), rgba(0,180,255,0.12));
    border: 1px solid rgba(0,255,200,0.25);
    border-top-right-radius: 4px;
    color: #d0fff5;
}

.msg.bot .msg-bubble {
    background: linear-gradient(135deg, rgba(168,85,247,0.1), rgba(99,102,241,0.1));
    border: 1px solid rgba(168,85,247,0.2);
    border-top-left-radius: 4px;
    color: #e0d0ff;
}

.msg-time {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.6rem;
    color: rgba(200,200,255,0.3);
    margin-top: 0.3rem;
    text-align: right;
}
.msg.user .msg-time { text-align: left; }

/* ── TYPING INDICATOR ── */
.typing-indicator {
    display: flex;
    gap: 0.8rem;
    margin-bottom: 1.2rem;
    align-items: center;
}
.typing-dots {
    display: flex;
    gap: 4px;
    align-items: center;
    padding: 0.7rem 1rem;
    background: rgba(168,85,247,0.1);
    border: 1px solid rgba(168,85,247,0.2);
    border-radius: 16px;
    border-top-left-radius: 4px;
}
.typing-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #a855f7;
    animation: typingBounce 1.4s ease-in-out infinite;
}
.typing-dot:nth-child(2) { animation-delay: 0.2s; }
.typing-dot:nth-child(3) { animation-delay: 0.4s; }

@keyframes typingBounce {
    0%, 60%, 100% { transform: translateY(0); opacity: 0.4; }
    30%            { transform: translateY(-6px); opacity: 1; }
}

/* ── EMPTY STATE ── */
.empty-state {
    text-align: center;
    padding: 3rem 1rem;
    color: rgba(200,200,255,0.2);
}
.empty-state .empty-icon { font-size: 3rem; margin-bottom: 1rem; }
.empty-state p {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.8rem;
    letter-spacing: 0.15em;
}

/* ── INPUT AREA ── */
.input-area {
    margin-top: 1rem;
    position: relative;
    z-index: 10;
    max-width: 800px;
    margin: 1rem auto 0;
    padding: 0 1rem;
}

/* Override Streamlit's text input */
.stTextInput > div > div {
    background: rgba(5,8,25,0.9) !important;
    border: 1px solid rgba(0,255,200,0.2) !important;
    border-radius: 14px !important;
    color: #e0e0ff !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 1rem !important;
    padding: 0.6rem 1rem !important;
    transition: border-color 0.3s, box-shadow 0.3s !important;
    backdrop-filter: blur(10px) !important;
}
.stTextInput > div > div:focus-within {
    border-color: rgba(0,255,200,0.6) !important;
    box-shadow: 0 0 20px rgba(0,255,200,0.15) !important;
}
.stTextInput input { color: #e0e0ff !important; background: transparent !important; }
.stTextInput input::placeholder { color: rgba(200,200,255,0.25) !important; }
.stTextInput label { display: none !important; }

/* ── BUTTONS ── */
.stButton > button {
    width: 100% !important;
    padding: 0.7rem 1rem !important;
    border-radius: 12px !important;
    font-family: 'Orbitron', monospace !important;
    font-size: 0.75rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.1em !important;
    border: 1px solid rgba(0,255,200,0.4) !important;
    background: linear-gradient(135deg, rgba(0,255,200,0.08), rgba(0,180,255,0.08)) !important;
    color: #00ffc8 !important;
    transition: all 0.3s ease !important;
    cursor: pointer !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, rgba(0,255,200,0.2), rgba(0,180,255,0.2)) !important;
    box-shadow: 0 0 25px rgba(0,255,200,0.25) !important;
    transform: translateY(-1px) !important;
    border-color: rgba(0,255,200,0.8) !important;
}

/* ── STATUS BAR ── */
.status-bar {
    max-width: 800px;
    margin: 1rem auto 0;
    padding: 0 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.65rem;
    color: rgba(200,200,255,0.3);
    letter-spacing: 0.1em;
    position: relative;
    z-index: 10;
}

.status-dot {
    display: inline-block;
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #00ffc8;
    margin-right: 6px;
    animation: statusPulse 2s ease-in-out infinite;
    box-shadow: 0 0 8px rgba(0,255,200,0.6);
}
@keyframes statusPulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50%       { opacity: 0.4; transform: scale(0.8); }
}

.mode-indicator {
    padding: 2px 10px;
    border-radius: 20px;
    font-size: 0.65rem;
    letter-spacing: 0.1em;
}
.mode-angry  { background: rgba(255,80,80,0.15);  color: #ff8080; border: 1px solid rgba(255,80,80,0.3);  }
.mode-funny  { background: rgba(255,215,0,0.15);  color: #ffd700; border: 1px solid rgba(255,215,0,0.3);  }
.mode-sad    { background: rgba(100,150,255,0.15); color: #96b4ff; border: 1px solid rgba(100,150,255,0.3); }
.mode-none   { background: rgba(200,200,255,0.05); color: rgba(200,200,255,0.3); border: 1px solid rgba(200,200,255,0.1); }

/* ── CLEAR BUTTON AREA ── */
.clear-area {
    max-width: 800px;
    margin: 0.5rem auto 2rem;
    padding: 0 1rem;
    text-align: right;
}

/* hide streamlit branding */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 0 !important; padding-bottom: 0 !important; }
</style>
""", unsafe_allow_html=True)

# ─── SESSION STATE ────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "mode" not in st.session_state:
    st.session_state.mode = None
if "mode_name" not in st.session_state:
    st.session_state.mode_name = None
if "last_sent" not in st.session_state:
    st.session_state.last_sent = ""
if "input_key" not in st.session_state:
    st.session_state.input_key = 0

# ─── HEADER ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-header">
  <div class="hero-title">MOODBOT AI</div>
  <div class="hero-subtitle">⚡ Adaptive Emotion Engine · Powered by Mistral</div>
</div>
<div class="neon-divider"></div>
""", unsafe_allow_html=True)

# ─── MODE SELECTION ───────────────────────────────────────────────────────────
st.markdown('<div class="mode-section-title">◈ SELECT YOUR AI PERSONA ◈</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

def card_html(mode_class, emoji, name, desc, selected):
    badge = '<span class="selected-badge">● ACTIVE</span>' if selected else ''
    sel   = ' selected' if selected else ''
    return f"""
    <div class="mode-card {mode_class}{sel}">
      {badge}
      <span class="mode-emoji">{emoji}</span>
      <div class="mode-name">{name}</div>
      <div class="mode-desc">{desc}</div>
    </div>
    """

with c1:
    st.markdown(card_html("angry","😤","ANGRY MODE","Aggressive & impatient responses. Zero patience, maximum fire.", st.session_state.mode_name=="angry"), unsafe_allow_html=True)
    if st.button("⚡ ACTIVATE ANGRY", key="angry_btn"):
        st.session_state.mode = "You are an angry AI agent. You respond aggressively and impatiently. Use strong language and show frustration."
        st.session_state.mode_name = "angry"
        st.session_state.messages = []
        st.rerun()

with c2:
    st.markdown(card_html("funny","😂","FUNNY MODE","Jokes, puns & humor in every reply. Life's too short to be serious.", st.session_state.mode_name=="funny"), unsafe_allow_html=True)
    if st.button("🎭 ACTIVATE FUNNY", key="funny_btn"):
        st.session_state.mode = "You are a hilarious AI agent. You respond with humor, jokes, puns, and wit. Make every response entertaining."
        st.session_state.mode_name = "funny"
        st.session_state.messages = []
        st.rerun()

with c3:
    st.markdown(card_html("sad","😢","SAD MODE","Deeply empathetic & emotional. Feels every word with you.", st.session_state.mode_name=="sad"), unsafe_allow_html=True)
    if st.button("💙 ACTIVATE SAD", key="sad_btn"):
        st.session_state.mode = "You are a sad, empathetic AI agent. You respond with deep understanding, melancholy, and emotional sensitivity."
        st.session_state.mode_name = "sad"
        st.session_state.messages = []
        st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# ─── STATUS BAR ───────────────────────────────────────────────────────────────
mode_labels = {
    "angry": ('<span class="mode-indicator mode-angry">😤 ANGRY MODE</span>', "READY"),
    "funny": ('<span class="mode-indicator mode-funny">😂 FUNNY MODE</span>', "READY"),
    "sad":   ('<span class="mode-indicator mode-sad">😢 SAD MODE</span>',   "READY"),
    None:    ('<span class="mode-indicator mode-none">NO MODE SELECTED</span>', "IDLE"),
}
mode_badge, status_txt = mode_labels.get(st.session_state.mode_name, mode_labels[None])
msg_count = len([m for m in st.session_state.messages if isinstance(m, HumanMessage)])

st.markdown(f"""
<div class="status-bar">
  <span><span class="status-dot"></span>MOODBOT v2.0 · {status_txt}</span>
  {mode_badge}
  <span>MSGS: {msg_count:03d}</span>
</div>
""", unsafe_allow_html=True)

# ─── CHAT DISPLAY ─────────────────────────────────────────────────────────────
import datetime

def render_messages():
    chat_html = '<div class="chat-container" id="chatbox">'

    if not st.session_state.messages or all(isinstance(m, SystemMessage) for m in st.session_state.messages):
        chat_html += """
        <div class="empty-state">
          <div class="empty-icon">🤖</div>
          <p>SELECT A MODE ABOVE AND START CHATTING</p>
        </div>"""
    else:
        for msg in st.session_state.messages:
            if isinstance(msg, SystemMessage):
                continue
            now = datetime.datetime.now().strftime("%H:%M")
            if isinstance(msg, HumanMessage):
                chat_html += f"""
                <div class="msg user">
                  <div class="msg-avatar">👤</div>
                  <div>
                    <div class="msg-bubble">{msg.content}</div>
                    <div class="msg-time">{now}</div>
                  </div>
                </div>"""
            elif isinstance(msg, AIMessage):
                bot_emoji = {"angry":"😤","funny":"😂","sad":"😢"}.get(st.session_state.mode_name, "🤖")
                chat_html += f"""
                <div class="msg bot">
                  <div class="msg-avatar">{bot_emoji}</div>
                  <div>
                    <div class="msg-bubble">{msg.content}</div>
                    <div class="msg-time">{now}</div>
                  </div>
                </div>"""

    chat_html += '</div>'
    return chat_html

st.markdown('<div class="chat-wrapper">', unsafe_allow_html=True)
st.markdown(render_messages(), unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ─── INPUT AREA ───────────────────────────────────────────────────────────────
st.markdown('<div class="input-area">', unsafe_allow_html=True)

col_input, col_send = st.columns([5, 1])

with col_input:
    placeholder = {
        "angry": "Type something... if you dare. 😤",
        "funny": "Ask me anything, I'll make it funny 😂",
        "sad":   "Share your thoughts, I feel you 😢",
        None:    "Select a mode to start chatting...",
    }.get(st.session_state.mode_name)

    user_input = st.text_input("msg", placeholder=placeholder, label_visibility="hidden", 
                                key=f"user_input_{st.session_state.input_key}", 
                                disabled=(st.session_state.mode is None))

with col_send:
    send_clicked = st.button("SEND ➤", key="send_btn", disabled=(st.session_state.mode is None))

st.markdown('</div>', unsafe_allow_html=True)

# ─── CLEAR CHAT ───────────────────────────────────────────────────────────────
st.markdown('<div class="clear-area">', unsafe_allow_html=True)
if st.button("🗑 CLEAR CHAT", key="clear_btn"):
    st.session_state.messages = []
    st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# ─── CHAT LOGIC ───────────────────────────────────────────────────────────────
if send_clicked and user_input and user_input.strip() and st.session_state.mode:
    
    # Prevent duplicate sends
    if user_input.strip() != st.session_state.last_sent:
        st.session_state.last_sent = user_input.strip()

        # Build message history
        if not st.session_state.messages:
            st.session_state.messages.append(SystemMessage(content=st.session_state.mode))

        st.session_state.messages.append(HumanMessage(content=user_input.strip()))

        # Call Mistral
        try:
            model = ChatMistralAI(model="mistral-small-latest", temperature=0.9, max_tokens=300)
            response = model.invoke(st.session_state.messages)
            st.session_state.messages.append(AIMessage(content=response.content))
        except Exception as e:
            st.session_state.messages.append(AIMessage(content=f"⚠️ Error: {str(e)}"))

        # Clear input by changing key
        st.session_state.input_key += 1
        st.rerun()

# ─── AUTO SCROLL ──────────────────────────────────────────────────────────────
st.markdown("""
<script>
  const chatbox = document.getElementById('chatbox');
  if (chatbox) chatbox.scrollTop = chatbox.scrollHeight;
</script>
""", unsafe_allow_html=True)
