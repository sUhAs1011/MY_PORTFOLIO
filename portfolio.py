import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import base64
from io import BytesIO
import os
import shutil

# Ensure directories are resolved relative to this script's directory (CWD agnostic)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Ensure static directory exists and contains the resume for static serving
static_dir = os.path.join(SCRIPT_DIR, "static")
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

resume_src = os.path.join(SCRIPT_DIR, "new_resume.pdf")
resume_dst = os.path.join(static_dir, "new_resume.pdf")
if os.path.exists(resume_src):
    try:
        shutil.copy(resume_src, resume_dst)
    except Exception:
        pass

# Ensure projects directory exists inside the project repository
projects_dir = os.path.join(SCRIPT_DIR, "projects")
if not os.path.exists(projects_dir):
    os.makedirs(projects_dir)

# Parent projects folder in case they are located in the parent directory
parent_dir = os.path.dirname(SCRIPT_DIR)
parent_projects_dir = os.path.join(parent_dir, "projects")

project_images = [
    "healthcare.jpg",
    "arduino.jpg",
    "chatbot.jpg",
    "udp.jpg",
    "kalpana.jpg",
    "career.jpg",
    "node_simulator.jpg",
    "cctv.jpg",
    "ai_personal_assistant.jpg",
    "traceops.jpg"
]

for img in project_images:
    dest_path = os.path.join(projects_dir, img)
    if not os.path.exists(dest_path):
        src_parent = os.path.join(parent_projects_dir, img)
        if os.path.exists(src_parent):
            try:
                shutil.move(src_parent, dest_path)
            except Exception:
                pass
        else:
            src_root = os.path.join(SCRIPT_DIR, img)
            if os.path.exists(src_root):
                try:
                    shutil.move(src_root, dest_path)
                except Exception:
                    pass

# --- PAGE CONFIG ---
favicon_path = os.path.join(SCRIPT_DIR, "suhas.jpg")
st.set_page_config(
    page_title="Suhas Venkata Karamalaputti · AI & Software Engineer", 
    page_icon=favicon_path if os.path.exists(favicon_path) else "⚡", 
    layout="wide"
)

# Viewport meta tag
st.markdown("""
<meta name="viewport" content="width=device-width, initial-scale=1.0">
""", unsafe_allow_html=True)

# Load consolidated CSS styles from static/style.css
css_path = os.path.join(SCRIPT_DIR, "static", "style.css")
if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- IMAGE & FILE HELPERS ---
@st.cache_data
def load_and_base64_image(file_path):
    try:
        img = Image.open(file_path)
        if "profile.jpg" in file_path:
            img = ImageEnhance.Sharpness(img).enhance(1.05)
            img = ImageEnhance.Contrast(img).enhance(1.03)
            img = ImageEnhance.Brightness(img).enhance(1.01)
            img = ImageEnhance.Color(img).enhance(1.02)
        elif "linked.jpeg" in file_path:
            img = ImageEnhance.Sharpness(img).enhance(1.08)
            img = ImageEnhance.Contrast(img).enhance(1.06)
            img = ImageEnhance.Brightness(img).enhance(1.03)
            img = ImageEnhance.Color(img).enhance(1.05)
            img = img.filter(ImageFilter.SMOOTH)
        
        buffered = BytesIO()
        img.save(buffered, format="PNG", quality=95)
        return base64.b64encode(buffered.getvalue()).decode()
    except FileNotFoundError:
        return None

@st.cache_data
def load_and_process_about_image(file_path):
    img = Image.open(file_path)
    img = ImageEnhance.Sharpness(img).enhance(1.8)
    img = ImageEnhance.Contrast(img).enhance(1.4)
    img = ImageEnhance.Color(img).enhance(1.2)
    img = img.filter(ImageFilter.SHARPEN)
    return img

@st.cache_data
def load_and_base64_pdf(file_path):
    try:
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                return base64.b64encode(f.read()).decode()
    except Exception:
        pass
    return ""

img_b64 = load_and_base64_image(os.path.join(SCRIPT_DIR, "profile.jpg"))
resume_pdf_path = os.path.join(SCRIPT_DIR, "new_resume.pdf")
resume_b64 = load_and_base64_pdf(resume_pdf_path)
resume_download_href = f"data:application/pdf;base64,{resume_b64}" if resume_b64 else "/app/static/new_resume.pdf"

# --- TOP NAVIGATION BAR ---
st.markdown("""<div class="navbar-custom">
<div class="navbar-top">
<a href="#home" class="navbar-brand">
<span class="navbar-brand-logo">SUHAS.AI</span>
<span class="navbar-brand-text">// INTELLIGENT SYSTEMS</span>
</a>
<div class="navbar-links" id="navbar-links">
<a href="#home">Home</a>
<a href="#about">Profile</a>
<a href="#skills">Stack</a>
<a href="#experience">Timeline</a>
<a href="#journey">Journey</a>
<a href="#achievements">Honors</a>
<a href="#projects">Work</a>
</div>
<a href="mailto:suhas.karamalaputti@gmail.com" class="navbar-talk-btn">GET IN TOUCH ⚡</a>
</div>
</div>""", unsafe_allow_html=True)

# --- HEADER TICKER SUB-BAR ---
st.markdown("""<div class="header-ticker-bar">
<div class="ticker-item">
<div class="ticker-pulse"></div>
<span>⚡ SPECIALIZING IN ML, NLP &amp; AGENTIC SYSTEMS</span>
</div>
<div class="ticker-item">
<span>PES UNIVERSITY · BENGALURU, INDIA</span>
</div>
</div>""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("<div id='home' class='content-section'>", unsafe_allow_html=True)

col_hero_left, col_hero_right = st.columns([1.25, 1])

with col_hero_left:
    st.markdown("""<div class="hero-container">
<div class="hero-tag">INITIALIZING SYSTEM // AI &amp; SOFTWARE ENGINEER</div>
<h1 class="hero-name">Suhas Venkata Karamalaputti<span class="hero-name-dot">.</span></h1>
<div class="hero-title">Machine Learning &amp; Software Engineer</div>
<p class="hero-bio">I engineer deep learning recommendation models, semantic vector search systems, and high-throughput enterprise platforms—bridging the gap between complex ML research and scalable production code.</p>
</div>""", unsafe_allow_html=True)
    
    # Action buttons row
    buttons_html = f"""<div class="button-row">
<a href="#projects" class="btn-primary-gradient">Explore Selected Work ⚡</a>
<a href="{resume_download_href}" download="Suhas_Resume.pdf" class="contact-button"><img src="https://img.icons8.com/?size=100&id=84020&format=png&color=FFFFFF" style="width:15px; height:15px; vertical-align:middle; margin-right:6px;" alt="Resume">Download résumé</a>
<a href="https://www.linkedin.com/in/suhas-venkata-karamalaputti/" target="_blank" class="contact-button"><img src="https://img.icons8.com/?size=100&id=8808&format=png&color=0077b5" style="width:15px; height:15px; vertical-align:middle; margin-right:6px;" alt="LinkedIn">LinkedIn</a>
<a href="https://github.com/sUhAs1011" target="_blank" class="contact-button"><img src="https://img.icons8.com/?size=100&id=SzgQDfObXUbA&format=png&color=FFFFFF" style="width:15px; height:15px; vertical-align:middle; margin-right:6px;" alt="GitHub">GitHub</a>
</div>"""
    st.markdown(buttons_html, unsafe_allow_html=True)
    
    # Currently Status pill
    if img_b64:
        status_html = f"""<div class="hero-status-bar">
<img src="data:image/png;base64,{img_b64}" class="status-avatar" alt="Avatar" />
<div class="status-text">
<div class="status-label">CURRENT ROLE</div>
<div class="status-company">Software Engineer Intern @ Epsilon</div>
</div>
</div>"""
        st.markdown(status_html, unsafe_allow_html=True)

with col_hero_right:
    # Custom SUHAS.CORE Intelligence Matrix HUD Widget
    hud_html = """<div class="core-hud-widget">
<div class="hud-header">
<div class="hud-title-tag">SUHAS.CORE // SYSTEM MATRIX</div>
<div class="hud-signal-badge"><span class="ticker-pulse"></span> LIVE SIGNAL 99.4%</div>
</div>
<div class="hud-matrix-grid">
<div class="hud-node-card">
<div class="node-index">[01] DOMAIN</div>
<div class="node-label">ML &amp; Deep Learning</div>
<div class="node-sub">PyTorch · DSSM · Annoy</div>
</div>
<div class="hud-node-card">
<div class="node-index">[02] DOMAIN</div>
<div class="node-label">NLP &amp; LLM Architecture</div>
<div class="node-sub">LangGraph · Transformers · Ollama</div>
</div>
<div class="hud-node-card">
<div class="node-index">[03] DOMAIN</div>
<div class="node-label">Agentic AI &amp; MCP</div>
<div class="node-sub">Multi-Agent · Vector Search</div>
</div>
<div class="hud-node-card">
<div class="node-index">[04] DOMAIN</div>
<div class="node-label">Full-Stack Enterprise</div>
<div class="node-sub">FastAPI · React · Streamlit</div>
</div>
</div>
<div class="hud-metrics-bar">
<div class="metric-box">
<div class="metric-value">10+</div>
<div class="metric-label">Projects Built</div>
</div>
<div class="metric-box">
<div class="metric-value">128D</div>
<div class="metric-label">Vector Space</div>
</div>
<div class="metric-box">
<div class="metric-value">&lt;100ms</div>
<div class="metric-label">Latency Speed</div>
</div>
</div>
</div>"""
    st.markdown(hud_html, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True) # End of Hero section

# --- ABOUT ME SECTION ---
img_about = load_and_process_about_image(os.path.join(SCRIPT_DIR, "linked.jpeg"))
buffered_about = BytesIO()
img_about.save(buffered_about, format="PNG", quality=95)
about_img_b64 = base64.b64encode(buffered_about.getvalue()).decode()

about_html = f"""<div id="about" class="content-section">
<h2 class="section-heading"><span class="section-tag" style="font-size: 0.9rem; padding: 5px 14px; letter-spacing: 1px;">[01] PROFILE</span></h2>
<div class="about-card">
<div class="about-image-wrapper">
<img src="data:image/png;base64,{about_img_b64}" class="about-image" alt="Suhas Venkata Karamalaputti" />
</div>
<div class="about-content">
<div class="about-paragraph">I’m <strong>Suhas Venkata Karamalaputti</strong>, a final-year Computer Science &amp; Engineering student at <span class="highlight-cyan">PES University</span>, currently working as a <span class="highlight-cyan">Software Engineer Intern at Epsilon</span>. I specialize in Machine Learning, Deep Learning, and Natural Language Processing, building intelligent systems that convert complex data into real-world impact.</div>
<div class="about-paragraph">Previously, I worked as a Software Engineering Intern at <span class="highlight-cyan">Elfonze Technologies</span>, where I developed AI-driven and full-stack enterprise platforms — including semantic document retrieval systems, travel expense platforms, and scalable ticketing workflows.</div>
<div class="about-paragraph">I thrive at the intersection of AI research and production engineering — building vector search engines, RAG pipelines, and multi-agent systems.</div>
<div class="about-meta-grid">
<div class="about-meta-item"><span class="meta-label">CURRENT ROLE</span><span class="meta-val">SWE Intern @ Epsilon</span></div>
<div class="about-meta-item"><span class="meta-label">EDUCATION</span><span class="meta-val">B.Tech CSE @ PES University</span></div>
<div class="about-meta-item"><span class="meta-label">LOCATION</span><span class="meta-val">Bengaluru, KA, India</span></div>
<div class="about-meta-item"><span class="meta-label">CORE FOCUS</span><span class="meta-val">Applied AI, NLP &amp; RAG</span></div>
</div>
</div>
</div>
</div>"""
st.markdown(about_html, unsafe_allow_html=True)

# --- SKILLS SECTION ---
st.markdown("<div id='skills' class='content-section'>", unsafe_allow_html=True)
st.markdown("""<h2 class="section-heading"><span class="section-tag" style="font-size: 0.9rem; padding: 5px 14px; letter-spacing: 1px;">[02] TECH STACK</span></h2>""", unsafe_allow_html=True)

# --- Programming Languages ---
st.markdown("<div class='skill-category-title'><img src='https://img.icons8.com/?size=100&id=20431&format=png&color=00d2ff' style='width:18px; height:18px;' alt='icon'>Programming Languages</div>", unsafe_allow_html=True)

icon_map = {
    "Python": "https://img.icons8.com/color/48/000000/python--v1.png",
    "C": "https://img.icons8.com/color/48/000000/c-programming.png",
    "C++": "https://img.icons8.com/color/48/000000/c-plus-plus-logo.png",
    "Java": "https://img.icons8.com/color/48/000000/java-coffee-cup-logo--v1.png",
    "Rust": "https://img.icons8.com/?size=100&id=haeAxVQEIg0F&format=png&color=000000",
    "R": "https://img.icons8.com/?size=100&id=CLvQeiwFpit4&format=png&color=000000"
}

prog_langs = ["Python", "C", "C++", "Java", "Rust", "R"]
prog_cols = st.columns(3)

for i, lang in enumerate(prog_langs):
    with prog_cols[i % 3]:
        icon_url = icon_map[lang]
        st.markdown(
            f"""
            <div class='skill-box'>
                <img src="{icon_url}" alt="{lang} icon" />
                <div class='skill-text'>{lang}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# --- Databases ---
st.markdown("<div class='skill-category-title'><img src='https://img.icons8.com/?size=100&id=11894&format=png&color=00d2ff' style='width:18px; height:18px;' alt='icon'>Databases &amp; Vector Stores</div>", unsafe_allow_html=True) 

db_icon_map = {
    "MySQL": "https://img.icons8.com/?size=100&id=9nLaR5KFGjN0&format=png&color=000000",
    "MongoDB": "https://img.icons8.com/?size=100&id=74402&format=png&color=000000",
    "ChromaDB": "https://miro.medium.com/v2/resize:fit:1044/1*d2XUNgrLw7687CDfXx9-Dw.png",
    "SQLite": "https://img.icons8.com/?size=100&id=yjSayFwWHyCo&format=png&color=000000",
    "PostgreSQL": "https://raw.githubusercontent.com/docker-library/docs/01c12653951b2fe592c1f93a13b4e289ada0e3a1/postgres/logo.png"
}

db_tools = ["MySQL", "MongoDB", "ChromaDB", "SQLite","PostgreSQL"]
db_cols = st.columns(3)

for i, tool in enumerate(db_tools):
    with db_cols[i % 3]:
        st.markdown(
            f"""
            <div class='skill-box'>
                <img src="{db_icon_map[tool]}" alt="{tool} icon" />
                <div class='skill-text'>{tool}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# --- AI/ML ---
st.markdown("<div class='skill-category-title'><img src='https://img.icons8.com/?size=100&id=59858&format=png&color=00d2ff' style='width:18px; height:18px;' alt='icon'>AI/ML Libraries</div>", unsafe_allow_html=True)

ml_icon_map = {
    "Scikit-learn": "https://quintagroup.com/cms/python/images/scikit-learn-logo.png",
    "Pandas":        "https://img.icons8.com/?size=100&id=xSkewUSqtErH&format=png&color=000000",
    "NumPy":         "https://img.icons8.com/?size=100&id=aR9CXyMagKIS&format=png&color=000000",
    "NLTK":          "https://miro.medium.com/v2/resize%3Afit%3A592/1%2AYM2HXc7f4v02pZBEO8h-qw.png",
    "Spacy":         "https://upload.wikimedia.org/wikipedia/commons/8/88/SpaCy_logo.svg",
    "PyTorch":       "https://img.icons8.com/?size=100&id=jH4BpkMnRrU5&format=png&color=000000",
    "Mathplotlib":   "https://img.icons8.com/?size=100&id=TkX1totjFmAD&format=png&color=000000",
    "Keras": "https://img.icons8.com/?size=100&id=XcSgtbIpgK6W&format=png&color=000000",
    "Seaborn": "https://cdn.worldvectorlogo.com/logos/seaborn-1.svg",
    "Selenium" : "https://img.icons8.com/?size=100&id=38553&format=png&color=000000",
    "OpenCV": "https://img.icons8.com/?size=100&id=bpip0gGiBLT1&format=png&color=000000"
}

ml_tools = ["Scikit-learn", "Pandas", "NumPy", "NLTK", "Spacy", "PyTorch", "Mathplotlib", "Keras", "Seaborn", "Selenium","OpenCV"]
ml_cols = st.columns(3)

for i, tool in enumerate(ml_tools):
    with ml_cols[i % 3]:
        icon_url = ml_icon_map.get(tool, "")
        st.markdown(
            f"""
            <div class='skill-box'>
                <img src="{icon_url}" alt="{tool} icon" />
                <div class='skill-text'>{tool}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# --- Tools ---
st.markdown("<div class='skill-category-title'><img src='https://img.icons8.com/?size=100&id=7859&format=png&color=00d2ff' style='width:18px; height:18px;' alt='icon'>Tools &amp; Platforms</div>", unsafe_allow_html=True)

tool_icon_map = {
    "Git": "https://img.icons8.com/?size=100&id=20906&format=png&color=000000",
    "Docker": "https://img.icons8.com/?size=100&id=22813&format=png&color=000000",
    "Kubernetes": "https://img.icons8.com/?size=100&id=cvzmaEA4kC0o&format=png&color=000000",
    "VSCode": "https://img.icons8.com/?size=100&id=0OQR1FYCuA9f&format=png&color=000000",
    "CursorAI": "https://img.icons8.com/?size=100&id=DiGZkjCzyZXn&format=png&color=000000",
    "Jupyter": "https://img.icons8.com/?size=100&id=J0SgMWzAxqFj&format=png&color=000000",
    "Google Colab": "https://img.icons8.com/?size=100&id=lOqoeP2Zy02f&format=png&color=000000",
    "Github": "https://img.icons8.com/?size=100&id=SzgQDfObXUbA&format=png&color=000000",
    "AntiGravity": "https://antigravity.google/assets/image/brand/antigravity-icon__full-color.png"
}

tools_list = list(tool_icon_map.keys())
tool_cols = st.columns(3)

for i, tool in enumerate(tools_list):
    with tool_cols[i % 3]:
        st.markdown(
            f"""
            <div class='skill-box'>
                <img src="{tool_icon_map[tool]}" alt="{tool} icon" />
                <div class='skill-text'>{tool}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# --- Operating Systems ---
st.markdown("<div class='skill-category-title'>🖥️ Operating Systems</div>", unsafe_allow_html=True)

os_icon_map = {
    "Windows": "https://img.icons8.com/?size=100&id=108792&format=png&color=000000",
    "Ubuntu": "https://img.icons8.com/?size=100&id=63208&format=png&color=000000",
    "Linux": "https://img.icons8.com/?size=100&id=m6O2bFdG70gw&format=png&color=000000"
}

os_list = list(os_icon_map.keys())
os_cols = st.columns(3)

for i, os_val in enumerate(os_list):
    with os_cols[i % 3]:
        st.markdown(
            f"""
            <div class='skill-box'>
                <img src="{os_icon_map[os_val]}" alt="{os_val} icon" />
                <div class='skill-text'>{os_val}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("</div>", unsafe_allow_html=True) # End of Skills section

# --- EXPERIENCE SECTION ---
st.markdown("<div id='experience' class='content-section'>", unsafe_allow_html=True)
st.markdown("""<h2 class="section-heading"><span class="section-tag" style="font-size: 0.9rem; padding: 5px 14px; letter-spacing: 1px;">[03] TIMELINE</span></h2>""", unsafe_allow_html=True)

experience_data = [
 {
  "role": "Software Engineering Intern",
  "company": "Elfonze Technologies Pvt. Ltd.",
  "date": "January 2026 - April 2026",
  "location": "Bengaluru, Karnataka",
  "description": [
    "Developed AI-driven and full-stack enterprise applications, including a semantic document retrieval system using vector embeddings, Annoy, FastAPI, and intelligent search workflows for efficient enterprise knowledge access.",
    "Built scalable business platforms including a travel expense management system and an enterprise ticketing workflow solution with role-based access control, SLA tracking, workflow automation, analytics dashboards, and real-time operational monitoring."
  ]
},
  {
    "role": "Summer Research Intern",
    "company": "Centre of Cognitive Computing and Computational Intelligence",
    "date": "June 2025 - August 2025",
    "location": "Bengaluru, Karnataka",
    "description": [
        "Engineered an end-to-end AI career advisory and recommendation system using Dual-Tower DSSM to align candidate profiles with real-time market demand, enabling high-precision skill gap identification across resumes, job descriptions, and courses.",
        "Architected a semantic search engine with PyTorch and ChromaDB to map resumes, jobs, and UN SDGs into a shared 128D latent space, integrating Ollama-powered XAI for reasoning and automating personalized reskilling roadmaps using Temporal Skill Decay and DAG-based learning pathways."
    ]
}
]

experience_html = ""
for exp in experience_data:
    experience_html += f"""
<div class="experience-card">
    <div class="exp-header">
        <div class="exp-row">
            <div class="exp-company">{exp['company']}</div>
            <div class="exp-date">{exp['date']}</div>
        </div>
        <div class="exp-row">
            <div class="exp-role">{exp['role']}</div>
            <div class="exp-loc">{exp['location']}</div>
        </div>
    </div>
    <ul class="exp-list">
"""
    for item in exp['description']:
        experience_html += f"<li>{item}</li>"
    
    experience_html += """
    </ul>
</div>
"""

st.markdown(experience_html, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- MY JOURNEY SECTION ---
st.markdown("<div id='journey' class='content-section'>", unsafe_allow_html=True)
st.markdown("""<h2 class="section-heading" style="justify-content:center;"><span class="section-tag" style="font-size: 0.9rem; padding: 5px 14px; letter-spacing: 1px;">[04] EDUCATION</span></h2>""", unsafe_allow_html=True)

st.markdown("""
<div class="timeline-container">

  <div class="timeline-item left">
    <div class="timeline-content">
      <h3>B.Tech CSE</h3>
      <p>PES University</p>
      <p>🗓️ 2022 - Present</p>
      <p>CGPA : 8.20</p>
    </div>
  </div>

  <div class="timeline-item right">
    <div class="timeline-content">
      <h3>12th CBSE</h3>
      <p>Geetanjali Olympiad School</p>
      <p>🗓️ 2020 - 2022</p>
      <p>12th Boards : 86%</p>
    </div>
  </div>

  <div class="timeline-item left">
    <div class="timeline-content">
      <h3>10th CBSE</h3>
      <p>Delhi Public School Bangalore East</p>
      <p>🗓️ 2007 - 2020</p>
      <p>10th Boards : 90%</p>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- ACHIEVEMENTS SECTION ---
st.markdown("<div id='achievements' class='content-section'>", unsafe_allow_html=True)
st.markdown("""<h2 class="section-heading"><span class="section-tag" style="font-size: 0.9rem; padding: 5px 14px; letter-spacing: 1px;">[05] HONORS</span></h2>""", unsafe_allow_html=True)

achievements = [
   {
    "title": "Praxis Hackathon",
    "icon": "📅",
    "desc": "Secured a <strong>Top 7 position</strong> among 50+ teams at <strong>Praxis Hackathon</strong> for building an AI-powered booking agent using <strong>LangGraph</strong>.",
    "tag": "Top 7 Finish",
    "id": "praxis",
    "cert_path": "certificates/praxis.jpg"
},
    {
        "title": "HealthHack Hackathon",
        "icon": "🧠",
        "desc": "Secured a <strong>Top 8 position</strong> among 80+ registered teams at <strong>HealthHack 4.0</strong> for building Kalpana AI, an AI-driven mental health peer support platform.",
        "tag": "Hackathon Achievement",
        "id": "healthhack",
        "cert_path": "certificates/healthhack.jpg"
    },
    {
        "title": "Encode-AI Agentathon",
        "icon": "🥈",
        "desc": "Achieved 2nd place for building a multi-agent Agentic AI incident investigation system using <strong>MCP</strong> and <strong>Ollama</strong>.",
        "tag": "Hackathon Runner-Up",
        "id": "encode",
        "cert_path": "certificates/encode.jpg"
    },
    {
        "title": "Heal-O-Code Hackathon",
        "icon": "🩺",
        "desc": "Top 6 out of 50+ teams. Built a healthcare decision support tool using <strong>Multi-Chain Blockchain</strong> and <strong>Ollama</strong> for better drug recommendation.",
        "tag": "Top 6 Finish",
        "id": "healocode",
        "cert_path": "certificates/healocode.jpg"
    },
    {
        "title": "Anveshana 2026",
        "icon": "🔍",
        "desc": "Ranked Top 11 out of 170 Capstone Teams for Detecting and Mitigating Replay Attacks in CCTV systems.",
        "tag": "Top 11 Finish",
        "id": "anveshana",
        "cert_path": "certificates/anveshana.jpg"
    },
    {
        "title": "MRD Scholarship",
        "icon": "🎓",
        "desc": "Awarded the prestigious <strong>MRD Scholarship</strong> in 1st Semester by <strong>PES University</strong>, receiving a 20% tuition fee reimbursement in recognition of academic excellence.",
        "tag": "Merit-Based Scholarship",
        "id": "mrd",
        "cert_path": "certificates/mrd.jpg"
    },
    {
        "title": "Distinction Scholarship",
        "icon": "🏅",
        "desc": "Received <strong>Distinction Scholarship</strong> of ₹ 2000 for achieving SGPA above <strong>7.75</strong> in <strong>Semesters 2–6</strong> at <strong>PES University</strong>.",
        "tag": "Consistent Academic Performance",
        "id": "distinction",
        "cert_path": "certificates/distinction.jpg"
    },
    {
        "title": "ICICT 2026",
        "icon": "📄",
        "desc": "Published a research paper titled <strong>“Detection and Mitigation of Replay Attacks in CCTV Systems”</strong> at 9th International Conference ICICT.",
        "tag": "International Research Presentation",
        "id": "icict",
        "cert_path": "certificates/ieee_icict.jpg"
    }
]

achievements_html = '<div class="achievements-grid">'
for item in achievements:
    achievements_html += f"""<label for="modal-{item['id']}" class="achievement-card">
<div class="achievement-header">
<div class="achievement-icon-wrapper">{item['icon']}</div>
<div class="achievement-title-text">{item['title']}</div>
</div>
<div class="achievement-description-text">{item['desc']}</div>
<div class="achievement-tag">{item['tag']}</div>
</label>"""
achievements_html += '</div>'

# Modals
achievements_html += '<div class="cert-modals-container">'
for item in achievements:
    cert_path = item.get("cert_path")
    if cert_path:
        full_cert_path = os.path.join(SCRIPT_DIR, cert_path)
        if os.path.exists(full_cert_path):
            cert_b64 = load_and_base64_image(full_cert_path)
            content_html = f'<img src="data:image/png;base64,{cert_b64}" class="cert-modal-img">'
        else:
            content_html = f"""<div class="cert-modal-fallback-card">
<div class="cert-modal-fallback-badge">{item['icon']}</div>
<h2 class="cert-modal-fallback-title">{item['title']}</h2>
<div class="cert-modal-fallback-desc">{item['desc']}</div>
<div class="cert-modal-fallback-tag">{item['tag']}</div>
<div class="cert-modal-fallback-status">✓ Verified Achievement</div>
</div>"""
    else:
        content_html = f"""<div class="cert-modal-fallback-card">
<div class="cert-modal-fallback-badge">{item['icon']}</div>
<h2 class="cert-modal-fallback-title">{item['title']}</h2>
<div class="cert-modal-fallback-desc">{item['desc']}</div>
<div class="cert-modal-fallback-tag">{item['tag']}</div>
<div class="cert-modal-fallback-status">✓ Verified Achievement</div>
</div>"""

    content_html_clean = "\n".join([line.strip() for line in content_html.split("\n")])

    achievements_html += f"""<input type="checkbox" id="modal-{item['id']}" class="cert-modal-toggle">
<div class="cert-modal-overlay">
<label for="modal-{item['id']}" class="cert-modal-backdrop-close"></label>
<div class="cert-modal-content">
{content_html_clean}
<label for="modal-{item['id']}" class="cert-modal-close-btn">Close Certificate</label>
</div>
</div>"""

achievements_html += '</div>'

st.markdown(achievements_html, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- PROJECTS SECTION ---
st.markdown("<div id='projects' class='content-section'>", unsafe_allow_html=True)
st.markdown("""<h2 class="section-heading"><span class="section-tag" style="font-size: 0.9rem; padding: 5px 14px; letter-spacing: 1px;">[06] FEATURED WORK</span></h2>""", unsafe_allow_html=True)

projects_list = [
    {
        "id": "proj-1",
        "title": "Blockchain-Powered AI Healthcare Insights",
        "icon": "https://img.icons8.com/?size=100&id=51845&format=png&color=000000",
        "url": "https://github.com/sUhAs1011/BLOCKCHAIN_POWERED_AI_HEALTHCARE_INSIGHTS",
        "image": "healthcare.jpg",
        "short_desc": "Designed and developed a secure, scalable system to extract actionable insights from Electronic Health Records (EHRs) using IPFS, multi-chain blockchain, and Gemini API OCR.",
        "pills": ["Python", "Flask", "Streamlit", "IPFS", "Blockchain", "Ollama", "Gemini API"],
        "bullets": """<ul>
<li>Integrated <strong>IPFS + multi-chain blockchain</strong> to store prescriptions with unique CIDs, ensuring data integrity, traceability, and decentralized access.</li>
<li>Built an OCR pipeline using <strong>Gemini API</strong> to extract drug names and dosages from prescriptions for structured analysis.</li>
<li>Implemented <strong>LLM-based drug interaction analysis</strong> to detect adverse drug-drug interactions and suggest safer alternatives.</li>
<li>Developed an end-to-end system with <strong>Flask backend + Streamlit UI</strong> enabling upload, analysis, and real-time clinical insights.</li>
</ul>"""
    },
    {
        "id": "proj-2",
        "title": "IoT-Enabled Arduino Intruder Detection & Alert System",
        "icon": "https://img.icons8.com/?size=100&id=8thlDCUHuqaK&format=png&color=000000",
        "url": "https://github.com/sUhAs1011/UE22CS251B-IOT_ENABLED_ARDUINO_BASED_INTRUDER_DETECTION_AND_ALERT_SYSTEM",
        "image": "arduino.jpg",
        "short_desc": "Engineered a real-time intrusion detection system using Arduino, designed to enhance home security through ultrasonic sensors, alarms, and automated GSM alert notifications.",
        "pills": ["C++", "Arduino", "Ultrasonic Sensor", "GSM Module", "SoftwareSerial.h"],
        "bullets": """<ul>
<li>Utilized an <strong>ultrasonic sensor</strong> to detect unauthorized entry, triggering a red LED, buzzer alarm, and <strong>GSM-based alert notifications</strong>.</li>
<li>Programmed using <strong>C++</strong> with SoftwareSerial.h to manage GSM module communication.</li>
<li>Configured the Arduino IDE and implemented serial communication to ensure seamless system performance and real-time responsiveness.</li>
<li>Achieved near-instant detection <strong>&lt; 100 ms</strong> with real-time serial communication, ensuring quick &amp; reliable security alerts.</li>
</ul>"""
    },
    {
        "id": "proj-3",
        "title": "LegalBot: AI-Powered Regulatory Mining Intelligence Bot",
        "icon": "https://img.icons8.com/?size=100&id=vkfmsvBD0PPO&format=png&color=000000",
        "url": "https://github.com/sUhAs1011/UE22CS342B_AI_POWERED_REGULATORY_MINING_INTELLIGENCE_BOT",
        "image": "chatbot.jpg",
        "short_desc": "Designed and developed an AI-powered regulatory intelligence bot to analyze mining laws, detect conflicts, and assist in compliance decision-making.",
        "pills": ["Python", "SentenceTransformers", "MongoDB", "NLP", "Streamlit"],
        "bullets": """<ul>
<li>Built an NLP pipeline to preprocess and store mining law documents in MongoDB for efficient retrieval and semantic search.</li>
<li>Implemented <strong>SentenceTransformer-based semantic search</strong> to fetch relevant legal sections based on user queries.</li>
<li>Developed a conflict detection system to identify contradictions across regulations and suggest alternative compliant actions.</li>
<li>Created an interactive chatbot interface using Streamlit for real-time querying, risk assessment, and regulatory insights.</li>
</ul>"""
    },
    {
        "id": "proj-4",
        "title": "Cloud File Transfer System using UDP",
        "icon": "https://img.icons8.com/?size=100&id=NIaxM8D5w6rv&format=png&color=FFFFFF",
        "url": "https://github.com/sUhAs1011/UE22CS252B_CLOUD_FILE_TRANSFER_SYSTEM_USING_UDP",
        "image": "udp.jpg",
        "short_desc": "Built a secure, network-based Cloud File Transfer System using Python and UDP, enabling efficient file transfer, SSL encryption, and command execution across systems.",
        "pills": ["Python", "UDP", "Socket Programming", "SSL", "File Handling"],
        "bullets": """<ul>
<li>Developed a <strong>client-server architecture</strong> using Python <strong>socket programming</strong> for file upload, download, and listing operations.</li>
<li>Integrated <strong>SSL certificates</strong> for secure communication between client and server.</li>
<li>Implemented <strong>dynamic IP handling</strong> to support both localhost and distributed multi-system deployments.</li>
<li>Enabled execution of remote shell commands and ensured seamless file transfers across networked devices.</li>
</ul>"""
    },
    {
        "id": "proj-5",
        "title": "Kalpana AI – Mental Health Peer Support Platform",
        "icon": "https://img.icons8.com/?size=100&id=2QfCaN1Zfmqf&format=png&color=000000",
        "url": "https://github.com/sUhAs1011",
        "image": "kalpana.jpg",
        "short_desc": "Developed Kalpana AI, an AI-powered platform designed to support individuals experiencing emotional distress through empathetic conversations, peer matchmaking, and crisis safety layers.",
        "pills": ["Python", "FastAPI", "React", "Ollama", "Pinecone"],
        "bullets": """<ul>
<li>Dual-agent architecture with a Listener AI for empathetic conversations and a Clinical Mapper for emotional risk analysis.</li>
<li>Voice-enabled interaction supporting multilingual speech-to-text and text-to-speech communication.</li>
<li>Peer matchmaking system using semantic embeddings and vector search to connect users with similar lived experiences.</li>
<li>Crisis safety layer that detects high-risk conversations and redirects users to emergency resources.</li>
</ul>"""
    },
    {
        "id": "proj-6",
        "title": "AI-Powered Career Skill Gap Analysis & Recommendation",
        "icon": "https://img.icons8.com/?size=100&id=fLrxgaxCrjaZ&format=png&color=FFFFFF",
        "url": "https://github.com/sUhAs1011/AI_POWERED_SKILL_GAP_ANALYSIS_RESKILLING_FOR_EMPLOYMENT_TRENDS",
        "image": "career.jpg",
        "short_desc": "Analyzing job trends, mapping skill gaps, and recommending targeted reskilling programs across employment sectors using PyTorch DSSM and ChromaDB embeddings.",
        "pills": ["Python", "PyTorch", "ChromaDB", "DSSM", "Streamlit", "Ollama", "Tesseract OCR"],
        "bullets": """<ul>
<li>Parsed resumes with <strong>Tesseract OCR</strong> and matched skills to job requirements using <strong>ChromaDB</strong> embeddings.</li>
<li>Engineered a <strong>PyTorch DSSM</strong> to map semantic relationships and prioritize high-demand missing skills.</li>
<li>Built an interactive <strong>Streamlit</strong> dashboard for skill gap analysis and learning-style-adapted course recommendations.</li>
<li>Integrated <strong>Ollama (LLaMA 3)</strong> to generate course rationales and mapped learning roadmaps via interactive graphs.</li>
</ul>"""
    },
    {
        "id": "proj-7",
        "title": "Distributed Systems Cluster Simulator Framework",
        "icon": "https://img.icons8.com/?size=100&id=7pFfikEfVGOV&format=png&color=000000",
        "url": "https://github.com/sUhAs1011/UE22CS351B_DISTRIBUTED_SYSTEMS_CLUSTER_SIMULATION_FRAMEWORK",
        "image": "node_simulator.jpg",
        "short_desc": "Designed a simulation framework modeling pod scheduling, node heartbeats, resource utilization constraints, and distributed heartbeat checks, fully dockerized.",
        "pills": ["Python", "Streamlit", "Docker", "Node.js", "RestAPI", "FastAPI", "JSON"],
        "bullets": """<ul>
<li>API Server: A centralized control unit for node management, pod scheduling, and health monitoring.</li>
<li>Cluster Nodes: Virtualized computing units that periodically send heartbeat signals to the <strong>API-Server</strong>.</li>
<li>Pods: Deployable units simulated on nodes, which require specific CPU resources.</li>
<li>Dockerized for portability and easy deployment and Real-time cluster health and pod scheduling visualization via Streamlit.</li>
</ul>"""
    },
    {
        "id": "proj-8",
        "title": "CCTV Replay Attack Detection And Mitigation",
        "icon": "https://img.icons8.com/?size=100&id=3wl52ZDVBgG0&format=png&color=000000",
        "url": "https://github.com/sUhAs1011/DETECTION_AND_MITIGATION_OF_REPLAY_ATTACK_IN_CCTV_SYSTEMS",
        "image": "cctv.jpg",
        "short_desc": "Built a temporal CCTV anomaly mitigation engine utilizing optical flow, Hierarchical Temporal Memory (HTM), and SHA-256 integrity hash verification.",
        "pills": ["Python", "HTM", "Optical Flow", "SDR", "SHA-256", "Streamlit", "FastAPI", "SQLite"],
        "bullets": """<ul>
<li><strong>Optical flow–based motion analysis</strong> with <strong>SDR</strong> encoding to capture temporal motion patterns in a compact and interpretable form.</li>
<li><strong>Hierarchical Temporal Memory (HTM)</strong> model for lightweight, real-time anomaly detection of unusual motion sequences.</li>
<li><strong>SHA‑256</strong> frame hashing and verification to ensure tamper-evident, forensic reliability of CCTV footage.</li>
<li>Decision engine with dashboard interface that fuses anomaly scores and integrity checks, providing real-time alerts, visualization, and forensic reporting.</li>
</ul>"""
    },
    {
        "id": "proj-9",
        "title": "Personal Booking Agent using LangGraph",
        "icon": "https://img.icons8.com/?size=100&id=nkGDoqzPxYM3&format=png&color=000000",
        "url": "https://github.com/sUhAs1011/AI_PERSONAL_ASSISTANT",
        "image": "ai_personal_assistant.jpg",
        "short_desc": "Built an LLM agent calendar workflow orchestrator utilizing LangGraph for reasoning loops, calendar API integrations, cache querying, and HITL overrides.",
        "pills": ["Python", "FastAPI", "LangGraph", "LangChain", "Groq", "React", "SQLite", "MCP"],
        "bullets": """<ul>
<li>Designed a LangGraph-based agent enabling dynamic tool-calling and multi-step reasoning for booking and queries.</li>
<li>Integrated MCP-based calendar services with conflict detection and Human-in-the-Loop (HITL) resolution.</li>
<li>Implemented cache-first queries for fast retrieval of event details like duration, location, and availability.</li>
<li>Developed a React + FastAPI system with real-time chat and robust backend validation.</li>
</ul>"""
    },
    {
        "id": "proj-10",
        "title": "TraceOps - AI Incident Response Agent",
        "icon": "https://img.icons8.com/?size=100&id=M16ic8QWK8x6&format=png&color=000000",
        "url": "https://github.com/sUhAs1011/TRACEOPS",
        "image": "traceops.jpg",
        "short_desc": "TraceOps is a multi-agent incident investigation system that automates root-cause analysis by correlating logs, configurations, and codebase context.",
        "pills": ["Python", "MCP", "LangGraph", "Ollama", "Streamlit"],
        "bullets": """<ul>
<li>Multi-agent reasoning pipeline for log ingestion, contextual analysis, and incident investigation.</li>
<li>Context-aware root-cause detection using configuration and codebase grounding.</li>
<li>Automated fix-plan generation with explainable, evidence-backed recommendations.</li>
<li>Decision dashboard providing incident summaries, traceability, and actionable alerts.</li>
</ul>"""
    }
]

# Generate 2-Column Compact Grid Cards
projects_html = '<div class="projects-grid">'
for item in projects_list:
    pills_html = "".join([f'<span class="tech-pill">{pill}</span>' for pill in item['pills']])
    projects_html += f"""<div class="project-compact-card">
<div class="project-header-row">
<div class="project-icon-box"><img src="{item['icon']}" alt="icon"></div>
<div class="project-title-text">{item['title']}</div>
</div>
<div class="project-short-desc">{item['short_desc']}</div>
<div class="project-pills-row">{pills_html}</div>
<div class="project-card-footer">
<label for="modal-{item['id']}" class="project-view-details-btn">View Details &rarr;</label>
<a href="{item['url']}" target="_blank" class="btn-github-repo-mini"><img src="https://img.icons8.com/?size=100&id=SzgQDfObXUbA&format=png&color=FFFFFF" style="width:14px; height:14px; vertical-align:middle; margin-right:4px;" alt="GitHub">GitHub &nearr;</a>
</div>
</div>"""
projects_html += '</div>'

# Generate Full-Screen Project Detail Modals
projects_html += '<div class="project-modals-container">'
for item in projects_list:
    img_path = os.path.join(projects_dir, item["image"])
    img_b64 = load_and_base64_image(img_path)
    img_src = f"data:image/png;base64,{img_b64}" if img_b64 else ""
    pills_html = "".join([f'<span class="tech-pill">{pill}</span>' for pill in item['pills']])
    bullets_clean = "\n".join([line.strip() for line in item['bullets'].split("\n")])

    projects_html += f"""<input type="checkbox" id="modal-{item['id']}" class="project-modal-toggle">
<div class="project-modal-overlay">
<label for="modal-{item['id']}" class="project-modal-backdrop-close"></label>
<div class="project-modal-card">
<label for="modal-{item['id']}" class="project-modal-close-icon">&times;</label>
<div class="project-modal-image-col">
<div class="project-modal-img-frame">
<img src="{img_src}" class="project-modal-img" alt="{item['title']}">
</div>
</div>
<div class="project-modal-content-col">
<div class="project-modal-header">
<div class="project-icon-box" style="width:44px; height:44px;"><img src="{item['icon']}" alt="icon" style="width:24px; height:24px;"></div>
<div class="project-modal-title">{item['title']}</div>
</div>
<div class="project-modal-bullets">
<p style="font-size: 1.02rem; line-height: 1.6; color: var(--text-main); margin-bottom: 14px;">{item['short_desc']}</p>
{bullets_clean}
</div>
<div class="project-pills-row" style="margin-bottom: 22px;">{pills_html}</div>
<div class="project-modal-actions">
<label for="modal-{item['id']}" class="btn-modal-close">Close</label>
</div>
</div>
</div>
</div>"""

projects_html += '</div>'

# Footer and closing div and back-to-top integrated into projects_html to avoid multiple Streamlit block wrappers
projects_html += """
<div style="text-align: center; padding: 15px 0 10px 0; font-family: var(--font-mono); font-size: 0.88rem; color: var(--text-dim); border-top: 1px dashed var(--bg-card-border); margin-top: 25px; margin-bottom: -15px;">
    Crafted by <strong style="color: var(--cyan-electric);">Suhas Venkata Karamalaputti</strong> with ⚡ using Python &amp; Streamlit
</div>
</div>
<a href="#home" class="back-to-top">&uarr;</a>
"""

st.markdown(projects_html, unsafe_allow_html=True)
