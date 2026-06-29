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

# Parent projects folder in case they are located in the parent directory (workspace root)
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
        # 1. Try to find in parent projects directory (if moved outside by mistake)
        src_parent = os.path.join(parent_projects_dir, img)
        if os.path.exists(src_parent):
            try:
                shutil.move(src_parent, dest_path)
            except Exception:
                pass
        else:
            # 2. Try to find in script directory
            src_root = os.path.join(SCRIPT_DIR, img)
            if os.path.exists(src_root):
                try:
                    shutil.move(src_root, dest_path)
                except Exception:
                    pass

# Wrap st.image to automatically resolve paths inside projects_dir (CWD agnostic)
_original_st_image = st.image
def robust_st_image(image, *args, **kwargs):
    if isinstance(image, str) and (image.startswith("projects/") or image.startswith("projects\\")):
        filename = os.path.basename(image)
        resolved_path = os.path.join(projects_dir, filename)
        if os.path.exists(resolved_path):
            image = resolved_path
    return _original_st_image(image, *args, **kwargs)
st.image = robust_st_image

# --- PAGE CONFIG ---
favicon_path = os.path.join(SCRIPT_DIR, "suhas.jpg")
st.set_page_config(page_title="Suhas Venkata Karamalaputti · Portfolio", page_icon=favicon_path if os.path.exists(favicon_path) else "suhas.jpg", layout="wide")

# Add viewport meta tag for mobile responsiveness
st.markdown("""
<meta name="viewport" content="width=device-width, initial-scale=1.0">
""", unsafe_allow_html=True)

# Load consolidated styling
css_path = os.path.join(SCRIPT_DIR, "static", "style.css")
if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- LOAD IMAGE ---
@st.cache_data
def load_and_base64_image(file_path):
    try:
        img = Image.open(file_path)
        
        # Enhance the profile image with better quality while keeping original size
        if "profile.jpg" in file_path:
            # Apply subtle image enhancements without resizing
            
            # Very subtle sharpness enhancement
            img = ImageEnhance.Sharpness(img).enhance(1.05)
            
            # Very subtle contrast enhancement
            img = ImageEnhance.Contrast(img).enhance(1.03)
            
            # Very subtle brightness enhancement
            img = ImageEnhance.Brightness(img).enhance(1.01)
            
            # Very subtle color enhancement
            img = ImageEnhance.Color(img).enhance(1.02)
        
        # Enhance the LinkedIn image with better quality while keeping original size
        elif "linked.jpg" in file_path:
            # Apply professional image enhancements without resizing
            
            # Enhance sharpness for professional look
            img = ImageEnhance.Sharpness(img).enhance(1.08)
            
            # Enhance contrast for better definition
            img = ImageEnhance.Contrast(img).enhance(1.06)
            
            # Slight brightness boost for professional appearance
            img = ImageEnhance.Brightness(img).enhance(1.03)
            
            # Enhance color vibrancy
            img = ImageEnhance.Color(img).enhance(1.05)
            
            # Apply very subtle smoothing for polished look
            img = img.filter(ImageFilter.SMOOTH)
        
        buffered = BytesIO()
        img.save(buffered, format="PNG", quality=95) # Use PNG for transparency if needed
        return base64.b64encode(buffered.getvalue()).decode()
    except FileNotFoundError:
        st.error(f"Error: {file_path} not found. Please ensure the image is in the correct directory.")
        return None # Return None if file is not found

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

# PDF generation/loading helpers
resume_pdf_path = os.path.join(SCRIPT_DIR, "new_resume.pdf")
resume_b64 = load_and_base64_pdf(resume_pdf_path)
resume_download_href = f"data:application/pdf;base64,{resume_b64}" if resume_b64 else "/app/static/new_resume.pdf"

# --- CUSTOM STYLES ---
# Styles loaded from static/style.css

# --- NAVIGATION BAR ---
st.markdown("""
<div class="navbar-custom">
    <div class="navbar-top">
        <div class="navbar-name">Suhas Venkata Karamalaputti</div>
    </div>
    <div class="navbar-links" id="navbar-links">
        <a href="#about">👨‍💼 About Me</a>
        <a href="#skills">🛠️ Skills</a>
        <a href="#experience">💼 Experience</a>
        <a href="#journey">🚶‍♂ My Journey</a>
        <a href="#achievements">🏆 Achievements</a>
        <a href="#projects">🚀 Projects</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("<div id='home' class='content-section'>", unsafe_allow_html=True)

# Use responsive columns that stack on mobile
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("<div class='hero-container'>", unsafe_allow_html=True)
    st.markdown(
    "<div class='gradient-text'>"
    "<span class='letter'>S</span><span class='letter'>u</span><span class='letter'>h</span><span class='letter'>a</span><span class='letter'>s</span> "
    "<span class='letter'>V</span><span class='letter'>e</span><span class='letter'>n</span><span class='letter'>k</span><span class='letter'>a</span><span class='letter'>t</span><span class='letter'>a</span> "
    "<span class='letter'>K</span><span class='letter'>a</span><span class='letter'>r</span><span class='letter'>a</span><span class='letter'>m</span><span class='letter'>a</span><span class='letter'>l</span><span class='letter'>a</span><span class='letter'>p</span><span class='letter'>u</span><span class='letter'>t</span><span class='letter'>t</span><span class='letter'>i</span> "
    "<span class='emoji'>👋</span>"
    "</div>",
    unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>CSE Senior at PES University | Software Engineer Intern at Epsilon</div>", unsafe_allow_html=True)
    st.markdown("""<p style='font-size:18px; line-height:1.6;'>
Final-year Computer Science & Engineering student at PES University, currently working as a Software Engineer Intern at Epsilon. Previously worked as a Software Engineering Intern at Elfonze Technologies and as a Summer Research Intern at C3I, contributing to end-to-end AI and software solutions. Passionate about Machine Learning, Natural Language Processing, and applied AI, with hands-on experience building ML systems and solving real-world problems through software engineering and research-driven projects.
</p>
""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    if img_b64: 
        st.markdown(f"<img src='data:image/png;base64,{img_b64}' class='profile-pic'/>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True) # End of Home section

# --- STYLE FOR CONTACT BUTTONS ---
# Styles loaded from static/style.css

buttons_html = f"""
<div class="button-row">
  <a href="{resume_download_href}" download="Suhas_Resume.pdf" class="contact-button">
    <img src="https://img.icons8.com/?size=100&id=32541&format=png&color=FFFFFF" class="contact-icon">Resume
  </a>
  <a href="mailto:suhas.karamalaputti@gmail.com" class="contact-button">
    <img src="https://img.icons8.com/?size=100&id=qyRpAggnV0zH&format=png&color=FFFFFF" class="contact-icon">Email
  </a>
  <a href="https://www.linkedin.com/in/suhas-venkata-karamalaputti/" target="_blank" class="contact-button">
    <img src="https://img.icons8.com/?size=100&id=13930&format=png&color=FFFFFF" class="contact-icon">LinkedIn
  </a>
  <a href="https://github.com/sUhAs1011" target="_blank" class="contact-button">
    <img src="https://img.icons8.com/?size=100&id=SzgQDfObXUbA&format=png&color=000000" class="contact-icon">GitHub
  </a>
</div>
"""
st.markdown(buttons_html, unsafe_allow_html=True)



# --- ABOUT ME ---
st.markdown("<div id='about' class='content-section'>", unsafe_allow_html=True)

# Inject custom CSS styles for the About Me section to match margins, rounded corners, and hover effects
# Styles loaded from static/style.css

col1, col2 = st.columns([1.25, 2])

with col1:
    img = load_and_process_about_image(os.path.join(SCRIPT_DIR, "linked.jpg"))

    st.image(img, use_container_width=True)  # ensures correct rendering for local file

with col2:
    st.markdown("""
    <h2 class="about-header">👨‍💼 About Me</h2>
    <div class="about-paragraph">
       I’m Suhas Venkata Karamalaputti, a final-year Computer Science & Engineering student at PES University, currently working as a Software Engineer Intern at Epsilon. I have a strong interest in Machine Learning, Deep Learning, and Natural Language Processing, and I enjoy building AI systems that solve real-world problems and create meaningful impact.
    </div>    
    <div class="about-paragraph">
        Previously, I worked as a Software Engineering Intern at Elfonze Technologies, where I developed AI-driven and full-stack enterprise applications, including a semantic document retrieval system, a travel expense management platform, and a scalable ticketing workflow system.
    </div>    
    <div class="about-paragraph">
       I’m always excited to explore new technologies, take on challenging problems, and collaborate across domains. If you're working on AI-driven or ML/NLP-focused projects, I’d love to connect and build something impactful together.
    </div>    
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- Skills Section ---
# Styles loaded from static/style.css

# --- Skills Section ---
st.markdown("<div id='skills' class='content-section'>", unsafe_allow_html=True)
st.markdown("   ")
st.markdown("## 🛠️ Skills")

# --- Programming Languages Sub-section ---
st.markdown("#### 👨‍💻 Programming Languages")

# Icon URLs (you can expand for other languages similarly)
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
            <div class='skill-box' style="text-align:center; padding:10px;">
                <img src="{icon_url}" alt="{lang} icon" style="width:40px; height:40px; margin-bottom:10px;" />
                <div class='skill-text' style="font-weight:bold;">{lang}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# --- Databases Sub-section ---
st.markdown("#### 🗄️ Databases") 

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
            <div class='skill-box' style="text-align:center; padding:10px;">
                <img src="{db_icon_map[tool]}" alt="{tool} icon" style="width:40px; height:40px; margin-bottom:10px;" />
                <div class='skill-text' style="font-weight:bold;">{tool}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# --- AI/ML Sub-section ---
st.markdown("#### 🤖 AI/ML Library")


# Icon and label
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
            <div class='skill-box' style="text-align:center; padding:10px;">
                <img src="{icon_url}" alt="{tool} icon" style="width:40px; height:40px; margin-bottom:10px;" />
                <div class='skill-text' style="font-weight:bold;">{tool}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# --- Tools Sub-section ---
st.markdown("#### 🧰 Tools & Platforms")

tool_icon_map = {
    "Git": "https://img.icons8.com/?size=100&id=20906&format=png&color=000000",
    "Docker": "https://img.icons8.com/?size=100&id=22813&format=png&color=000000",
    "Kubernetes": "https://img.icons8.com/?size=100&id=cvzmaEA4kC0o&format=png&color=000000",
    "VSCode": "https://img.icons8.com/?size=100&id=0OQR1FYCuA9f&format=png&color=000000",
    "CursorAI": "https://img.icons8.com/?size=100&id=DiGZkjCzyZXn&format=png&color=000000",
    "Jupyter": "https://img.icons8.com/?size=100&id=J0SgMWzAxqFj&format=png&color=000000",  # Using generic Jupyter icon
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
            <div class='skill-box' style="text-align:center; padding:10px;">
                <img src="{tool_icon_map[tool]}" alt="{tool} icon" style="width:40px; height:40px; margin-bottom:10px;" />
                <div class='skill-text' style="font-weight:bold;">{tool}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# --- Operating Systems Sub-section ---
st.markdown("#### 🖥️ Operating Systems")

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
            <div class='skill-box' style="text-align:center; padding:10px;">
                <img src="{os_icon_map[os_val]}" alt="{os_val} icon" style="width:40px; height:40px; margin-bottom:10px;" />
                <div class='skill-text' style="font-weight:bold;">{os_val}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# --- EXPERIENCE SECTION ---
st.markdown("<div id='experience' class='content-section'>", unsafe_allow_html=True)
st.markdown("    ")
st.header("💼 Experience")

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
st.markdown("    ")
st.markdown("<h2 style='text-align:center;'>🚶‍♂ My Journey</h2>", unsafe_allow_html=True)

st.markdown("""
<div class="timeline-container">

  <div class="timeline-item">
    <div class="timeline-content left">
      <h3>B.Tech CSE</h3>
      <p>PES University</p>
      <p>🗓️ 2022 - Present</p>
      <p>CGPA : 8.20</p>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-content right">
      <h3>12th CBSE</h3>
      <p>Geetanjali Olympiad School</p>
      <p>🗓️ 2020 - 2022</p>
      <p>12th Boards : 86%</p>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-content left">
      <h3>10th CBSE</h3>
      <p>Delhi Public School Bangalore East</p>
      <p>🗓️ 2007 - 2020</p>
      <p>10th Boards : 90%</p>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)

# --- Custom CSS ---
# --- Custom CSS ---
# Styles loaded from static/style.css

# --- ACHIEVEMENTS SECTION ---
st.markdown("<div id='achievements' class='content-section'>", unsafe_allow_html=True)
st.markdown("   ")
st.header("🏆 Achievements")

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

# Generate Grid HTML
achievements_html = '<div class="achievements-grid">'

for item in achievements:
    achievements_html += f"""
<label for="modal-{item['id']}" class="achievement-card">
    <div class="achievement-header">
        <div class="achievement-icon-wrapper">{item['icon']}</div>
        <div class="achievement-title-text">{item['title']}</div>
    </div>
    <div class="achievement-description-text">{item['desc']}</div>
    <div class="achievement-tag">{item['tag']}</div>
</label>
"""

achievements_html += '</div>'

# Append checkboxes and modals at the bottom wrapped in a container block to bypass markdown formatting
achievements_html += '<div class="cert-modals-container">'
for item in achievements:
    cert_path = item.get("cert_path")
    if cert_path:
        full_cert_path = os.path.join(SCRIPT_DIR, cert_path)
        if os.path.exists(full_cert_path):
            cert_b64 = load_and_base64_image(full_cert_path)
            content_html = f'<img src="data:image/png;base64,{cert_b64}" class="cert-modal-img">'
        else:
            # Fallback if path is set but file not found
            content_html = f"""
            <div class="cert-modal-fallback-card">
                <div class="cert-modal-fallback-badge">{item['icon']}</div>
                <h2 class="cert-modal-fallback-title">{item['title']}</h2>
                <div class="cert-modal-fallback-desc">{item['desc']}</div>
                <div class="cert-modal-fallback-tag">{item['tag']}</div>
                <div class="cert-modal-fallback-status">✓ Verified Achievement</div>
            </div>
            """
    else:
        # Fallback card for achievements without certificate images
        content_html = f"""
        <div class="cert-modal-fallback-card">
            <div class="cert-modal-fallback-badge">{item['icon']}</div>
            <h2 class="cert-modal-fallback-title">{item['title']}</h2>
            <div class="cert-modal-fallback-desc">{item['desc']}</div>
            <div class="cert-modal-fallback-tag">{item['tag']}</div>
            <div class="cert-modal-fallback-status">✓ Verified Achievement</div>
        </div>
        """

    achievements_html += f"""
<input type="checkbox" id="modal-{item['id']}" class="cert-modal-toggle">
<div class="cert-modal-overlay">
    <label for="modal-{item['id']}" class="cert-modal-backdrop-close"></label>
    <div class="cert-modal-content">
        {content_html}
        <label for="modal-{item['id']}" class="cert-modal-close-btn">Close Certificate</label>
    </div>
</div>
"""
achievements_html += '</div>'

st.markdown(achievements_html, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- PROJECTS SECTION ---
st.markdown("<div id='projects' class='content-section'>", unsafe_allow_html=True)
st.markdown("   ")
st.header("🚀 Projects")

projects_data = [
    {
        "id": "healthcare",
        "title": "Blockchain-Powered AI Healthcare Insights",
        "icon": "https://img.icons8.com/?size=100&id=51845&format=png&color=000000",
        "url": "https://github.com/sUhAs1011/BLOCKCHAIN_POWERED_AI_HEALTHCARE_INSIGHTS",
        "desc": "Designed and developed a secure, scalable system to extract actionable insights from Electronic Health Records (EHRs) using IPFS, multi-chain blockchain, and Gemini API OCR.",
        "image_path": "projects/healthcare.jpg",
        "tech": ["Python", "Flask", "Streamlit", "IPFS", "Blockchain", "Ollama", "Gemini API"],
        "features": [
            "Integrated <strong>IPFS + multi-chain blockchain</strong> to store prescriptions with unique CIDs, ensuring data integrity, traceability, and decentralized access.",
            "Built an OCR pipeline using <strong>Gemini API</strong> to extract drug names and dosages from prescriptions for structured analysis.",
            "Implemented <strong>LLM-based drug interaction analysis</strong> to detect adverse drug-drug interactions and suggest safer alternatives.",
            "Developed an end-to-end system with <strong>Flask backend + Streamlit UI</strong> enabling upload, analysis, and real-time clinical insights."
        ]
    },
    {
        "id": "arduino",
        "title": "IoT-Enabled Intruder Detection System",
        "icon": "https://img.icons8.com/?size=100&id=8thlDCUHuqaK&format=png&color=000000",
        "url": "https://github.com/sUhAs1011/UE22CS251B-IOT_ENABLED_ARDUINO_BASED_INTRUDER_DETECTION_AND_ALERT_SYSTEM",
        "desc": "Engineered a real-time intrusion detection and alert system using Arduino, GSM communication modules, buzzer deterrents, and ultrasonic sensors (<100ms latency).",
        "image_path": "projects/arduino.jpg",
        "tech": ["C++", "Arduino", "Ultrasonic Sensor", "GSM Module", "SoftwareSerial.h"],
        "features": [
            "Utilized an <strong>ultrasonic sensor</strong> to detect unauthorized entry, triggering a red LED, buzzer alarm, and <strong>GSM-based alert notifications</strong>.",
            "Programmed using <strong>C++</strong> with SoftwareSerial.h to manage GSM module communication.",
            "Configured the Arduino IDE and implemented serial communication to ensure seamless performance and real-time responsiveness.",
            "Achieved near-instant detection <strong>&lt; 100 ms</strong> with real-time serial communication, ensuring quick & reliable security alerts."
        ]
    },
    {
        "id": "chatbot",
        "title": "LegalBot: Mining Intelligence Bot",
        "icon": "https://img.icons8.com/?size=100&id=vkfmsvBD0PPO&format=png&color=000000",
        "url": "https://github.com/sUhAs1011/UE22CS342B_AI_POWERED_REGULATORY_MINING_INTELLIGENCE_BOT",
        "desc": "Developed an AI chatbot parsing regulatory documents into MongoDB, querying relevant laws using SentenceTransformer semantic search, and performing risk assessment.",
        "image_path": "projects/chatbot.jpg",
        "tech": ["Python", "SentenceTransformers", "MongoDB", "NLP", "Streamlit"],
        "features": [
            "Built an NLP pipeline to preprocess and store mining law documents in MongoDB for efficient retrieval and semantic search.",
            "Implemented <strong>SentenceTransformer-based semantic search</strong> to fetch relevant legal sections based on user queries.",
            "Developed a conflict detection system to identify contradictions across regulations and suggest alternative compliant actions.",
            "Created an interactive chatbot interface using Streamlit for real-time querying, risk assessment, and regulatory insights."
        ]
    },
    {
        "id": "udp",
        "title": "Cloud File Transfer System using UDP",
        "icon": "https://img.icons8.com/?size=100&id=NIaxM8D5w6rv&format=png&color=FFFFFF",
        "url": "https://github.com/sUhAs1011/UE22CS252B_CLOUD_FILE_TRANSFER_SYSTEM_USING_UDP",
        "desc": "Built a secure client-server socket programming architecture enabling directory actions, file upload/downloads, and remote command execution using UDP and SSL.",
        "image_path": "projects/udp.jpg",
        "tech": ["Python", "UDP", "Socket Programming", "SSL", "File Handling"],
        "features": [
            "Developed a <strong>client-server architecture</strong> using Python <strong>socket programming</strong> for file upload, download, and listing operations.",
            "Integrated <strong>SSL certificates</strong> for secure communication between client and server.",
            "Implemented <strong>dynamic IP handling</strong> to support both localhost and distributed multi-system deployments.",
            "Enabled execution of remote shell commands and ensured seamless file transfers across networked devices."
        ]
    },
    {
        "id": "kalpana",
        "title": "Kalpana AI – Peer Support Platform",
        "icon": "https://img.icons8.com/?size=100&id=2QfCaN1Zfmqf&format=png&color=000000",
        "url": "https://github.com/sUhAs1011",
        "desc": "Developed a voice-enabled peer support chat app leveraging a Listener AI for empathy, clinical mapping for risk analysis, and vector search matching for lived experiences.",
        "image_path": "projects/kalpana.jpg",
        "tech": ["Python", "FastAPI", "React", "Ollama", "Pinecone"],
        "features": [
            "Dual-agent architecture with a Listener AI for empathetic conversations and a Clinical Mapper for emotional risk analysis.",
            "Voice-enabled interaction supporting multilingual speech-to-text and text-to-speech communication.",
            "Peer matchmaking system using semantic embeddings and vector search to connect users with similar lived experiences.",
            "Crisis safety layer that detects high-risk conversations and redirects users to emergency resources."
        ]
    },
    {
        "id": "career",
        "title": "AI-Powered Career Skill Gap Copilot",
        "icon": "https://img.icons8.com/?size=100&id=fLrxgaxCrjaZ&format=png&color=FFFFFF",
        "url": "https://github.com/sUhAs1011/AI_POWERED_SKILL_GAP_ANALYSIS_RESKILLING_FOR_EMPLOYMENT_TRENDS",
        "desc": "Analyzed job trends, parsed resumes with OCR, and mapped missing skills using a PyTorch DSSM model to generate learning roadmaps grounded in Ollama LLaMA-3.",
        "image_path": "projects/career.jpg",
        "tech": ["Python", "PyTorch", "ChromaDB", "DSSM", "Streamlit", "Ollama", "Tesseract OCR"],
        "features": [
            "Parsed resumes with <strong>Tesseract OCR</strong> and matched skills to job requirements using <strong>ChromaDB</strong> embeddings.",
            "Engineered a <strong>PyTorch DSSM</strong> to map semantic relationships and prioritize high-demand missing skills.",
            "Built an interactive <strong>Streamlit</strong> dashboard for skill gap analysis and learning-style-adapted course recommendations.",
            "Integrated <strong>Ollama (LLaMA 3)</strong> to generate course rationales and mapped learning roadmaps via interactive graphs."
        ]
    },
    {
        "id": "node_simulator",
        "title": "Distributed Systems Cluster Simulator",
        "icon": "https://img.icons8.com/?size=100&id=7pFfikEfVGOV&format=png&color=000000",
        "url": "https://github.com/sUhAs1011/UE22CS351B_DISTRIBUTED_SYSTEMS_CLUSTER_SIMULATION_FRAMEWORK",
        "desc": "Designed a simulation framework modeling pod scheduling, node heartbeats, resource utilization constraints, and distributed heartbeat checks, fully dockerized.",
        "image_path": "projects/node_simulator.jpg",
        "tech": ["Python", "Streamlit", "Docker", "Node.js", "RestAPI", "FastAPI", "JSON"],
        "features": [
            "API Server: A centralized control unit for node management, pod scheduling, and health monitoring.",
            "Cluster Nodes: Virtualized computing units that periodically send heartbeat signals to the <strong>API-Server</strong>.",
            "Pods: Deployable units simulated on nodes, which require specific CPU resources.",
            "Dockerized for portability and easy deployment and Real-time cluster health and pod scheduling visualization via Streamlit."
        ]
    },
    {
        "id": "cctv",
        "title": "CCTV Replay Attack Detection And Mitigation",
        "icon": "https://img.icons8.com/?size=100&id=3wl52ZDVBgG0&format=png&color=000000",
        "url": "https://github.com/sUhAs1011/DETECTION_AND_MITIGATION_OF_REPLAY_ATTACK_IN_CCTV_SYSTEMS",
        "desc": "Built a temporal CCTV anomaly mitigation engine utilizing optical flow, Hierarchical Temporal Memory (HTM), and SHA-256 integrity hash verification.",
        "image_path": "projects/cctv.jpg",
        "tech": ["Python", "HTM", "Optical Flow", "SDR", "SHA-256", "Streamlit", "FastAPI", "SQLite"],
        "features": [
            "<strong>Optical flow–based motion analysis</strong> with <strong>SDR</strong> encoding to capture temporal motion patterns in a compact and interpretable form.",
            "<strong>Hierarchical Temporal Memory (HTM)</strong> model for lightweight, real-time anomaly detection of unusual motion sequences.",
            "<strong>SHA‑256</strong> frame hashing and verification to ensure tamper-evident, forensic reliability of CCTV footage.",
            "Decision engine with dashboard interface that fuses anomaly scores and integrity checks, providing real-time alerts, visualization, and forensic reporting."
        ]
    },
    {
        "id": "ai_personal_assistant",
        "title": "Personal Booking Agent using LangGraph",
        "icon": "https://img.icons8.com/?size=100&id=nkGDoqzPxYM3&format=png&color=000000",
        "url": "https://github.com/sUhAs1011/AI_PERSONAL_ASSISTANT",
        "desc": "Built an LLM agent calendar workflow orchestrator utilizing LangGraph for reasoning loops, calendar API integrations, cache querying, and HITL overrides.",
        "image_path": "projects/ai_personal_assistant.jpg",
        "tech": ["Python", "FastAPI", "LangGraph", "LangChain", "Groq", "React", "SQLite", "MCP"],
        "features": [
            "Designed a LangGraph-based agent enabling dynamic tool-calling and multi-step reasoning for booking and queries.",
            "Integrated MCP-based calendar services with conflict detection and Human-in-the-Loop (HITL) resolution.",
            "Implemented cache-first queries for fast retrieval of event details like duration, location, and availability.",
            "Developed a React + FastAPI system with real-time chat and robust backend validation."
        ]
    },
    {
        "id": "traceops",
        "title": "TraceOps - AI Incident Response Agent",
        "icon": "https://img.icons8.com/?size=100&id=M16ic8QWK8x6&format=png&color=000000",
        "url": "https://github.com/sUhAs1011/TRACEOPS",
        "desc": "TraceOps is a multi-agent incident investigation system that automates root-cause analysis by correlating logs, configurations, and codebase context.",
        "image_path": "projects/traceops.jpg",
        "tech": ["Python", "MCP", "LangGraph", "Ollama", "Streamlit"],
        "features": [
            "Multi-agent reasoning pipeline for log ingestion, contextual analysis, and incident investigation.",
            "Context-aware root-cause detection using configuration and codebase grounding.",
            "Automated fix-plan generation with explainable, evidence-backed recommendations.",
            "Decision dashboard providing incident summaries, traceability, and actionable alerts."
        ]
    }
]

# Generate Projects Grid HTML and Modals
projects_html = '<div class="projects-grid">'

for proj in projects_data:
    tag_pills = "".join([f'<span class="project-tag">{tech}</span>' for tech in proj["tech"]])
    # Project card is now a label that toggles the project modal checkbox
    projects_html += f'<label for="modal-project-{proj["id"]}" class="project-card">'
    projects_html += f'<div class="project-header">'
    projects_html += f'<div class="project-icon-wrapper">'
    projects_html += f'<img src="{proj["icon"]}" class="project-icon" alt="icon" />'
    projects_html += f'</div>'
    projects_html += f'<div class="project-title-text">{proj["title"]}</div>'
    projects_html += f'</div>'
    projects_html += f'<div class="project-description-text">{proj["desc"]}</div>'
    projects_html += f'<div class="project-tags">{tag_pills}</div>'
    projects_html += f'<div class="project-link">View Details &rarr;</div>'
    projects_html += f'</label>'

projects_html += '</div>'

# Append checkboxes and modal overlay wrappers for projects
projects_html += '<div class="cert-modals-container">'
for proj in projects_data:
    # Build list of feature bullets
    bullets_html = "".join([f'<li>{bullet}</li>' for bullet in proj["features"]])
    tag_pills_modal = "".join([f'<span class="project-tag">{tech}</span>' for tech in proj["tech"]])
    
    # Load project image as base64
    img_b64 = ""
    img_path = os.path.join(SCRIPT_DIR, proj["image_path"])
    if os.path.exists(img_path):
        img_b64 = load_and_base64_image(img_path)
    
    img_src = f"data:image/png;base64,{img_b64}" if img_b64 else proj["image_path"]
    
    projects_html += f'<input type="checkbox" id="modal-project-{proj["id"]}" class="project-modal-toggle" />'
    projects_html += f'<div class="project-modal-overlay">'
    projects_html += f'<label for="modal-project-{proj["id"]}" class="project-modal-backdrop-close"></label>'
    projects_html += f'<div class="project-modal-content">'
    
    # Left column: Image
    projects_html += f'<div class="project-modal-left">'
    projects_html += f'<label for="modal-project-img-{proj["id"]}">'
    projects_html += f'<img src="{img_src}" class="project-modal-img" alt="{proj["title"]}" />'
    projects_html += f'</label>'
    projects_html += f'</div>'
    
    # Right column: Details and Actions
    projects_html += f'<div class="project-modal-right">'
    projects_html += f'<div class="project-modal-title">'
    projects_html += f'<img src="{proj["icon"]}" style="width:30px; height:30px; vertical-align:middle;" /> '
    projects_html += f'{proj["title"]}'
    projects_html += f'</div>'
    projects_html += f'<div class="project-modal-desc">'
    projects_html += f'{proj["desc"]}'
    projects_html += f'<ul>{bullets_html}</ul>'
    projects_html += f'</div>'
    projects_html += f'<div class="project-modal-tech">{tag_pills_modal}</div>'
    projects_html += f'<div class="project-modal-actions">'
    projects_html += f'<a href="{proj["url"]}" target="_blank" class="project-modal-btn project-modal-btn-primary">View GitHub Repo</a>'
    projects_html += f'<label for="modal-project-{proj["id"]}" class="project-modal-btn project-modal-btn-secondary">Close</label>'
    projects_html += f'</div>'
    projects_html += f'</div>' # End project-modal-right
    
    projects_html += f'</div>' # End project-modal-content
    projects_html += f'</div>' # End project-modal-overlay
    
    # Zoom Modal for Project Image (uses cert-modal classes for design/behavior)
    projects_html += f'<input type="checkbox" id="modal-project-img-{proj["id"]}" class="cert-modal-toggle" />'
    projects_html += f'<div class="cert-modal-overlay">'
    projects_html += f'<label for="modal-project-img-{proj["id"]}" class="cert-modal-backdrop-close"></label>'
    projects_html += f'<div class="cert-modal-content">'
    projects_html += f'<img src="{img_src}" class="cert-modal-img" alt="{proj["title"]} Zoomed" />'
    projects_html += f'<label for="modal-project-img-{proj["id"]}" class="cert-modal-close-btn">Close Image</label>'
    projects_html += f'</div>'
    projects_html += f'</div>'
    
projects_html += '</div>' # End cert-modals-container

st.markdown(projects_html, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- Custom Footer, Back-to-Top, and Scroll Progress Bar (Merged to minimize DOM wrappers) ---
st.markdown("""
    <div style='text-align: center; padding-top: 20px; font-size: 25px; font-weight: 500; color: #ffffff;'>
        Made by Suhas Venkata Karamalaputti with ❤️
    </div>
    <div style='text-align: center; padding-top: 5px; font-size: 20px; font-weight: 500; color: #ffffff; margin-bottom: 10px;'>
        Using Streamlit and Python
    </div>
    
    <a href="#home" class="back-to-top">↑</a>
    
    <div id="scroll-progress-bar" style="
        position: fixed;
        top: 0;
        left: 0;
        width: 0%;
        height: 4px;
        background: linear-gradient(90deg, #005BEA, #00C6FB);
        z-index: 10001;
        box-shadow: 0 0 10px rgba(0, 198, 251, 0.8), 0 0 5px rgba(0, 91, 234, 0.5);
        transition: width 0.08s ease-out;
    "></div>

    <script>
    (function() {
        function initProgressBar() {
            const progressBar = document.getElementById('scroll-progress-bar');
            const scrollContainer = document.querySelector('[data-testid="stAppViewContainer"]') || window;
            
            if (!scrollContainer) {
                setTimeout(initProgressBar, 200);
                return;
            }

            const target = scrollContainer === window ? document.documentElement : scrollContainer;

            scrollContainer.addEventListener('scroll', () => {
                const scrollTop = target.scrollTop !== undefined ? target.scrollTop : window.pageYOffset;
                const scrollHeight = target.scrollHeight !== undefined ? target.scrollHeight : document.documentElement.scrollHeight;
                const clientHeight = target.clientHeight !== undefined ? target.clientHeight : window.innerHeight;
                
                const totalScroll = scrollHeight - clientHeight;
                const scrollPercentage = totalScroll > 0 ? (scrollTop / totalScroll) * 100 : 0;
                
                progressBar.style.width = scrollPercentage + '%';
            });
        }

        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', initProgressBar);
        } else {
            initProgressBar();
        }
    })();
    </script>
""", unsafe_allow_html=True)
