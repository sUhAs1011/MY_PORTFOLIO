import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import base64
from io import BytesIO

# --- PAGE CONFIG ---
st.set_page_config(page_title="Suhas Venkata · Portfolio", page_icon="suhas.jpg", layout="wide")

# Add viewport meta tag for mobile responsiveness
st.markdown("""
<meta name="viewport" content="width=device-width, initial-scale=1.0">
""", unsafe_allow_html=True)

# --- LOAD IMAGE ---
def load_and_base64_image(file_path):
    try:
        img = Image.open(file_path)
        
        # Enhance the profile image with better quality while keeping original size
        if "profile.jpg" in file_path:
            # Apply subtle image enhancements without resizing
            from PIL import ImageEnhance
            
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
            from PIL import ImageEnhance, ImageFilter
            
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

img_b64 = load_and_base64_image("profile.jpg")

# --- CUSTOM STYLES ---
st.markdown("""
<style>
/* Hide Streamlit default header */
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}

/* Hide Streamlit sidebar */
section[data-testid="stSidebar"] {visibility: hidden;}

/* Hide all Streamlit UI elements */
div[data-testid="stSidebar"] {visibility: hidden;}
div[data-testid="stSidebarNav"] {visibility: hidden;}
div[data-testid="stSidebarContent"] {visibility: hidden;}
div[data-testid="stSidebarUserContent"] {visibility: hidden;}
div[data-testid="stSidebarUserContent"] > div {visibility: hidden;}

html {
    scroll-behavior: smooth;
}

body {
    background-color: #0e1117;
    color: inherit; /* Ensure text is visible on dark background */
}

.gradient-text {
    font-size: 48px;
    font-weight: 800;
    /* Corrected: use linear-gradient for standard syntax and -webkit- for webkit browsers */
    background: linear-gradient(90deg, #005BEA, #00C6FB);
    -webkit-background-clip: text;
    -webkit-text-fill-color: inherit; /* Makes text transparent so gradient background shows through */
    color: inherit; /* Fallback for browsers that don't support -webkit-text-fill-color */
    margin-bottom: 5px;
    transition: all 0.3s ease;
    cursor: pointer;
}

.gradient-text:hover {
    transform: scale(1.05);
    text-shadow: 0 0 20px rgba(0, 198, 251, 0.5);
}

/* Individual letter hover effects */
.gradient-text span.letter {
    display: inline-block;
    cursor: pointer;
}

.gradient-text span.letter:hover {
    transform: translateY(-5px) scale(1.2);
    -webkit-text-fill-color: #00C6FB;
    text-shadow: 0 0 15px rgba(0, 198, 251, 0.8);
}

.gradient-text span {
    -webkit-text-fill-color: inherit; /* Span within gradient-text should also be transparent to inherit parent's gradient */
}

.subtitle {
    font-size: 20px;
    color: #ccc;
    margin-bottom: 25px;
}

.intro {
    font-size: 17px;
    line-height: 1.6;
    color: inherit;
    max-width: 550px;
}

.say-hello {
    border: 2px solid white;
    border-radius: 12px;
    padding: 10px 24px;
    background-color: transparent;
    color: inherit;
    font-size: 16px;
    margin-top: 25px;
    cursor: pointer;
    transition: 0.3s;
}

.say-hello:hover {
    background-color: inherit;
    color: black;
}

.profile-pic {
    border-radius: 50%;
    width: 300px;
    height: 300px;
    object-fit: cover;
    object-position: center;
    box-shadow: 0 0 25px rgba(0, 198, 251, 0.3), 0 0 15px rgba(255, 255, 255, 0.2);
    transform: translateX(150px);
    border: 4px solid rgba(0, 198, 251, 0.3);
    transition: all 0.3s ease;
    filter: brightness(1.0) contrast(1.0) saturate(1.0);
    overflow: hidden;
    display: block;
}

.profile-pic:hover {
    transform: translateX(150px) scale(1.02);
    box-shadow: 0 0 35px rgba(0, 198, 251, 0.5), 0 0 20px rgba(255, 255, 255, 0.3);
    border-color: rgba(0, 198, 251, 0.6);
}

.hero-container {
    padding: 40px 20px 20px 40px;
}

/* Mobile responsive styles for hero section */
@media screen and (max-width: 768px) {
    .profile-pic {
        width: 200px;
        height: 200px;
        transform: translateX(0);
        margin: 20px auto;
        display: block;
        object-fit: cover;
        object-position: center;
        border-radius: 50%;
        overflow: hidden;
    }
    
    .profile-pic:hover {
        transform: scale(1.02);
    }
    
    .hero-container {
        padding: 20px 15px;
        text-align: center;
    }
    
    .gradient-text {
        font-size: 32px;
        text-align: center;
    }
    
    .subtitle {
        font-size: 16px;
        text-align: center;
    }
    
    .intro {
        font-size: 16px;
        text-align: center;
        max-width: 100%;
    }
}

@media screen and (max-width: 480px) {
    .profile-pic {
        width: 150px;
        height: 150px;
        object-fit: cover;
        object-position: center;
        border-radius: 50%;
        overflow: hidden;
    }
    
    .gradient-text {
        font-size: 28px;
    }
    
    .subtitle {
        font-size: 14px;
    }
    
    .intro {
        font-size: 14px;
    }
}

/* Ensure content sections have padding to account for fixed navbar */
.content-section {
    padding-top: 5px; /* Adjust based on navbar height + desired spacing */
    margin-bottom: 40px; /* Add some space between sections */
}

/* Add extra padding for mobile navbar */
@media screen and (max-width: 768px) {
    .content-section {
        padding-top: 60px; /* Extra padding for mobile navbar */
    }
}

@media screen and (max-width: 480px) {
    .content-section {
        padding-top: 50px; /* Slightly less padding for smaller screens */
    }
}

/* Mobile responsive styles for content sections */
@media screen and (max-width: 768px) {
    .content-section {
        padding-left: 15px;
        padding-right: 15px;
    }
    
    /* Make project images stack vertically on mobile */
    .project-image {
        width: 100%;
        margin-bottom: 20px;
    }
    
    /* Adjust project text for mobile */
    .project-content {
        width: 100%;
    }
}

@media screen and (max-width: 480px) {
    .content-section {
        padding-left: 10px;
        padding-right: 10px;
    }
}

/* Timeline styling (for .timeline-wrapper, .timeline-col, etc. - these are generic and might not be used directly in the final timeline HTML, but good to keep if you have other timeline styles) */
.timeline-wrapper {
    display: flex;
    justify-content: space-between;
    margin-top: 50px;
}

.timeline-col {
    width: 45%;
}

.timeline-block {
    border-left: 2px solid #555;
    margin-left: 20px;
    padding-left: 20px;
    position: relative;
    margin-bottom: 50px;
}

.timeline-block::before {
    content: '';
    position: absolute;
    top: 0;
    left: -8px;
    width: 12px;
    height: 12px;
    background-color: #00C6FB;
    border-radius: 50%;
}

.timeline-title {
    font-weight: 700;
    font-size: 18px;
    color: #1da1f2;
}

.timeline-subtitle {
    color: #aaa;
    font-size: 15px;
}

.timeline-date {
    font-size: 14px;
    color: #888;
    margin-top: 5px;
}

/* Responsive Navigation Bar Styling */
.navbar-custom {
    overflow: visible;
    background-color: #0e1117;
    position: fixed;
    top: 0;
    width: 100%;
    left: 0;
    z-index: 1000;
    display: flex;
    flex-direction: column;
    padding: 12px 30px;
    box-sizing: border-box;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
}

.navbar-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
}

.navbar-name {
    color: inherit;
    font-size: 22px;
    font-weight: 700;
    text-decoration: none;
    transition: color 0.3s ease;
    position: relative;
    flex-shrink: 0;
    margin-left: 100px;
}

.navbar-name::before {
    content: '';
    position: absolute;
    left: -25px;
    top: 50%;
    transform: translateY(-50%);
    width: 10px;
    height: 10px;
    background-color: #00C6FB;
    border-radius: 50%;
    box-shadow: 0 0 8px rgba(0, 198, 251, 0.6);
}

.navbar-name:hover {
    color: #00C6FB;
    text-shadow: 0 0 10px rgba(0, 198, 251, 0.5);
}

/* Mobile hamburger menu */
.mobile-menu-toggle {
    display: none;
    background: none;
    border: none;
    color: inherit;
    font-size: 24px;
    cursor: pointer;
    padding: 8px;
    border-radius: 4px;
    transition: background-color 0.3s ease;
}

.mobile-menu-toggle:hover {
    background-color: rgba(255, 255, 255, 0.1);
}

.mobile-menu-toggle:active {
    background-color: rgba(255, 255, 255, 0.2);
}

.navbar-links {
    display: flex;
    gap: 5px;
    align-items: center;
    flex-wrap: wrap;
}

.navbar-custom a {
    color: #f2f2f2;
    text-align: center;
    padding: 8px 12px;
    text-decoration: none;
    font-size: 14px;
    transition: color 0.3s, background-color 0.3s;
    border-radius: 5px;
    white-space: nowrap;
}

.navbar-custom a:hover {
    color: #00C6FB;
    background-color: rgba(0, 198, 251, 0.1);
}

/* Desktop styles - hide mobile menu button */
@media screen and (min-width: 769px) {
    .mobile-menu-toggle {
        display: none;
    }
    
    .navbar-custom {
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
    }
    
    .navbar-top {
        display: contents;
    }
}

/* Mobile responsive styles */
@media screen and (max-width: 768px) {
    .navbar-custom {
        padding: 10px 20px;
    }
    
    .navbar-name {
        font-size: 18px;
        margin-left: 30px;
    }
    
    .navbar-name::before {
        left: -20px;
        width: 8px;
        height: 8px;
    }
    
    .mobile-menu-toggle {
        display: none;
    }
    
    .navbar-links {
        display: flex;
        position: static;
        width: 100%;
        background-color: transparent;
        flex-direction: row;
        padding: 0;
        box-shadow: none;
        gap: 2px;
        z-index: 1001;
        flex-wrap: wrap;
        justify-content: center;
        margin-top: 10px;
    }
    
    .navbar-links.active {
        display: flex;
    }
    
    .navbar-custom a {
        padding: 8px 12px;
        font-size: 12px;
        width: auto;
        text-align: center;
        border-bottom: none;
        border-radius: 4px;
        margin: 2px;
        flex: 1;
        min-width: 80px;
    }
    
    .navbar-custom a:last-child {
        border-bottom: none;
    }
}

@media screen and (max-width: 480px) {
    .navbar-custom {
        padding: 8px 15px;
    }
    
    .navbar-name {
        font-size: 16px;
        margin-left: 20px;
    }
    
    .navbar-name::before {
        left: -18px;
        width: 6px;
        height: 6px;
    }
    
    .navbar-custom a {
        font-size: 11px;
        padding: 6px 8px;
        min-width: 70px;
    }
}

/* Timeline CSS (alternating vertical style) - actual implementation style */
.timeline-container {
    position: relative;
    max-width: 800px;
    margin: 40px auto;
}

.timeline-item {
    padding: 20px 40px;
    position: relative;
    background-color: inherit;
    width: 100%;
}

.timeline-item::after {
    content: "";
    position: absolute;
    width: 6px;
    background-color: #1f77b4;
    top: 0;
    bottom: 0;
    left: 50%;
    margin-left: -3px;
}

.timeline-content {
    padding: 20px;
    background-color: #0e1117;
    position: relative;
    border-radius: 6px;
    width: 40%;
    color: inherit;
    box-shadow: 0 0 10px rgba(0, 198, 251, 0.2); /* Subtle glow from cyan */
    border: 2px solid rgba(0, 198, 251, 0.3);
    transition: all 0.3s ease;
    cursor: pointer;
}

.timeline-content:hover {
    transform: scale(1.02);
    box-shadow: 0 0 20px rgba(0, 198, 251, 0.4), 0 0 15px rgba(255, 255, 255, 0.2);
    border-color: rgba(0, 198, 251, 0.6);
    background-color: #111827;
}

.left {
    left: 0;
}

.right {
    left: 60%;
}

.timeline-content::before {
    content: " ";
    position: absolute;
    top: 20px;
    width: 25px;
    height: 25px;
    border-radius: 50%;
    background-color: #00C6FB;
    border: 4px solid white;
    z-index: 1;
    transition: all 0.3s ease;
}

.timeline-content:hover::before {
    background-color: #00E5FF;
    border-color: #00C6FB;
    transform: scale(1.1);
}

.left::before {
    left: 95%;
}

.right::before {
    left: -15px;
}

@media screen and (max-width: 768px) {
    .timeline-container {
        margin: 20px 15px;
        padding: 0 10px;
    }
    
    .timeline-item {
        padding: 20px 0;
    }
    
    .timeline-content {
        width: calc(100% - 60px);
        left: 60px !important;
        margin-left: 0;
        padding: 20px;
        position: relative;
    }
    
    .timeline-item::after {
        left: 30px;
        width: 4px;
    }
    
    .timeline-content::before {
        left: -15px;
        width: 20px;
        height: 20px;
        border: 3px solid white;
    }
    
    .left::before {
        left: -15px;
    }
    
    .right::before {
        left: -15px;
    }
}

@media screen and (max-width: 480px) {
    .timeline-container {
        margin: 15px 10px;
        padding: 0 5px;
    }
    
    .timeline-item {
        padding: 15px 0;
    }
    
    .timeline-content {
        width: calc(100% - 50px);
        left: 50px !important;
        padding: 15px;
    }
    
    .timeline-item::after {
        left: 25px;
        width: 3px;
    }
    
    .timeline-content::before {
        left: -12px;
        width: 18px;
        height: 18px;
        border: 2px solid white;
    }
    
    .left::before {
        left: -12px;
    }
    
    .right::before {
        left: -12px;
    }
}


</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
/* your .timeline-container, .timeline-item, .left/right CSS here */
</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>
/* ================= THEME-SAFE OVERRIDES (Light + Dark) ================= */
:root {
  --text-color: var(--color-text);
  --bg-color: var(--color-background);
}

/* Page background & base text */
body { background-color: var(--bg-color); color: var(--text-color) !important; }
p, div, .intro, .subtitle { color: var(--text-color) !important; }

/* Headings and nav */
h1, h2, h3, h4, h5, h6,
.navbar-name,
.navbar-custom a { color: var(--text-color) !important; }

/* Project links */
h3 a { color: var(--text-color) !important; font-weight: 700; }

/* Gradient name */
.gradient-text {
  background: linear-gradient(90deg, #005BEA, #00C6FB);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
}
.gradient-text span.letter { -webkit-text-fill-color: transparent !important; }
.gradient-text span.letter:hover { -webkit-text-fill-color: #00C6FB !important; }

/* Buttons */
.contact-button {
  background-color: transparent;
  border: 2px solid var(--text-color);
  color: var(--text-color) !important;
}
.contact-button:hover {
  background: linear-gradient(90deg, #005BEA, #00C6FB);
  border-color: #00C6FB;
  color: #fff !important;
}

/* Navbar background */
.navbar-custom { background: var(--bg-color) !important; border-bottom: 1px solid rgba(127,127,127,0.15); }

/* Profile pic glow tuned for both themes */
.profile-pic { box-shadow: 0 0 25px rgba(0, 198, 251, 0.35); }
.profile-pic:hover { box-shadow: 0 0 35px rgba(0, 198, 251, 0.55); }
</style>
""", unsafe_allow_html=True)

# --- NAVIGATION BAR ---
st.markdown("""
<div class="navbar-custom">
    <div class="navbar-top">
        <div class="navbar-name">Suhas Venkata</div>
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
    st.markdown("<div class='gradient-text'><span class='letter'>S</span><span class='letter'>u</span><span class='letter'>h</span><span class='letter'>a</span><span class='letter'>s</span> <span class='letter'>V</span><span class='letter'>e</span><span class='letter'>n</span><span class='letter'>k</span><span class='letter'>a</span><span class='letter'>t</span><span class='letter'>a</span> <span class='emoji'>👋</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>CSE Student at PES University</div>", unsafe_allow_html=True)
    st.markdown("""
<p style='font-size:18px; line-height:1.6;'>
Final-year Computer Science student at PES University, passionate about Machine Learning and Natural Language Processing. 
Recently interned at C3I, gaining hands-on experience in ML systems. 
Actively exploring software engineering and always open to new challenges and collaborations.
</p>
""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    if img_b64: 
        st.markdown(f"<img src='data:image/png;base64,{img_b64}' class='profile-pic'/>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True) # End of Home section

# --- STYLE FOR CONTACT BUTTONS ---
st.markdown("""
<style>
.button-row {
  display: flex;
  justify-content: flex-start;
  gap: 20px;
  margin-top: 20px;
  flex-wrap: wrap;
}

.contact-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  padding: 12px 20px;
  background-color: #111827;   /* Dark blue-gray background */
  border: 2px solid #1e3a8a;   /* Dark blue border */
  border-radius: 12px;
  text-decoration: none !important;
  color: white !important;
  font-weight: 600;
  width: 140px;
  height: 55px;
  transition: all 0.3s ease;
  cursor: pointer;
}

/* Hover effect = electric blue glow like the name */
.contact-button:hover {
  background: linear-gradient(90deg, #005BEA, #00C6FB); /* Same gradient as the name */
  border-color: #00C6FB;
  color: #fff;
  transform: translateY(-3px) scale(1.02);
  box-shadow: 0px 8px 20px rgba(0, 198, 251, 0.6), 0 0 15px rgba(0, 198, 251, 0.4);
  text-shadow: 0 0 10px rgba(0, 198, 251, 0.8);
}

.contact-icon {
  width: 24px;
  height: 24px;
}

/* Mobile responsive styles for contact buttons */
@media screen and (max-width: 768px) {
  .button-row {
    justify-content: center;
    gap: 15px;
    flex-wrap: wrap;
  }
  
  .contact-button {
    width: 120px;
    height: 50px;
    font-size: 14px;
    padding: 10px 15px;
  }
  
  .contact-icon {
    width: 20px;
    height: 20px;
  }
}

@media screen and (max-width: 480px) {
  .button-row {
    gap: 10px;
  }
  
  .contact-button {
    width: 100px;
    height: 45px;
    font-size: 12px;
    padding: 8px 12px;
  }
  
  .contact-icon {
    width: 18px;
    height: 18px;
  }
}
</style>
""", unsafe_allow_html=True)

import base64
buttons_html = """
<div class="button-row">
  <a href="data:application/pdf;base64,{resume_b64}" download="Suhas_Resume.pdf" class="contact-button">
    <img src="https://img.icons8.com/?size=100&id=32541&format=png&color=FFFFFF" class="contact-icon">Resume
  </a>
  <a href="mailto:suhas.karamalaputti@gmail.com" class="contact-button">
    <img src="https://img.icons8.com/?size=100&id=qyRpAggnV0zH&format=png&color=FFFFFF" class="contact-icon">Email
  </a>
  <a href="https://www.linkedin.com/in/suhas-venkata/" target="_blank" class="contact-button">
    <img src="https://img.icons8.com/?size=100&id=13930&format=png&color=FFFFFF" class="contact-icon">LinkedIn
  </a>
  <a href="https://github.com/sUhAs1011" target="_blank" class="contact-button">
    <img src="https://img.icons8.com/?size=100&id=SzgQDfObXUbA&format=png&color=000000" class="contact-icon">GitHub
  </a>
</div>
""".format(resume_b64=base64.b64encode(open("new_resume.pdf","rb").read()).decode())
st.markdown(buttons_html, unsafe_allow_html=True)



# --- ABOUT ME ---
st.markdown("<div id='about' class='content-section'>", unsafe_allow_html=True)
st.markdown("   ")

col1, col2 = st.columns([1, 2])

with col1:
    from PIL import Image
    img = Image.open("linked.jpg")
    img = ImageEnhance.Sharpness(img).enhance(1.8)
    img = ImageEnhance.Contrast(img).enhance(1.4)
    img = ImageEnhance.Color(img).enhance(1.2)
    img = img.filter(ImageFilter.SHARPEN)

    st.image(img, width=500)  # ensures correct rendering for local file

with col2:
    st.header("👨‍💼 About Me")
    st.markdown("""
    <div style="font-size:18px; line-height:1.6; text-align: left;">
        I’m <strong>Suhas Venkata</strong>, a Senior in Computer Science & Engineering at PES University. My passion lies in Machine learning and Deep learning, 
        and I thrive on solving real-world problems through cutting-edge technologies.
    </div>    
    """, unsafe_allow_html=True)
    st.markdown("    ")
    st.markdown("""
    <div style="font-size:18px; line-height:1.6; text-align: left;">
        During my internship at the Centre of Cognitive Computing and Computational Intelligence (C3I) in the Summer of 2025, I designed and deployed an end-to-end career advisory system using dual-tower Deep Structured Semantic Models and ChromaDB achieving highly accurate job–course matching.
    </div>    
    """, unsafe_allow_html=True)
    st.markdown("    ")
    st.markdown("""
    <div style="font-size:18px; line-height:1.6; text-align: left;">
        I’m always eager to take on new challenges, collaborate across disciplines, and keep learning. If you're working on Natural Language Processing, Machine Learning, or AI-driven projects, I’d love to connect and build something impactful together.
    </div>    
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- Skills Section ---
st.markdown("""
    <style>
    .skill-box {
        background-color: #111827;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 15px;
        transition: transform 0.2s ease-in-out;
    }
    .skill-box:hover {
        transform: scale(1.03);
    }
    .skill-text {
        font-size: 18px;
        font-weight: bold;
        color: #ffffff;
        transition: color 0.3s ease;
        cursor: pointer;
    }
    .skill-text:hover {
        color: #00BFFF;
    }
    
    /* Mobile responsive styles for skills */
    @media screen and (max-width: 768px) {
        .skill-box {
            padding: 15px;
            margin-bottom: 10px;
        }
        
        .skill-text {
            font-size: 16px;
        }
    }
    
    @media screen and (max-width: 480px) {
        .skill-box {
            padding: 12px;
            margin-bottom: 8px;
        }
        
        .skill-text {
            font-size: 14px;
        }
    }
    </style>
""", unsafe_allow_html=True)

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

# --- Web Development Sub-section ---
st.markdown("#### 🌐 Web Development")

# Icon URLs for Web Dev
webdev_icon_map = {
    "HTML": "https://img.icons8.com/?size=100&id=20909&format=png&color=000000",
    "CSS": "https://img.icons8.com/?size=100&id=21278&format=png&color=000000",
    "JavaScript": "https://static.vecteezy.com/system/resources/previews/027/127/463/non_2x/javascript-logo-javascript-icon-transparent-free-png.png",
    "Streamlit": "https://img.icons8.com/?size=100&id=Rffi8qeb2fK5&format=png&color=000000",
    "SpringBoot": "https://img.icons8.com/?size=100&id=90519&format=png&color=000000"
}

webdev_tools = ["HTML", "CSS", "JavaScript", "Streamlit","SpringBoot"]
webdev_cols = st.columns(3)

for i, tool in enumerate(webdev_tools):
    with webdev_cols[i % 3]:
        st.markdown(
            f"""
            <div class='skill-box' style="text-align:center; padding:10px;">
                <img src="{webdev_icon_map[tool]}" alt="{tool} icon" style="width:40px; height:40px; margin-bottom:10px;" />
                <div class='skill-text' style="font-weight:bold;">{tool}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# --- Databases Sub-section ---
st.markdown("#### 🗄️ Databases") 

db_icon_map = {
    "MySQL": "https://img.icons8.com/?size=100&id=9nLaR5KFGjN0&format=png&color=000000",
    "MongoDB": "https://img.icons8.com/?size=100&id=74402&format=png&color=000000",
    "ChromaDB": "https://miro.medium.com/v2/resize:fit:1044/1*d2XUNgrLw7687CDfXx9-Dw.png"  
}

db_tools = ["MySQL", "MongoDB", "ChromaDB"]
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
    "LLM": "https://img.icons8.com/?size=100&id=29a6ubG1s7cw&format=png&color=000000"
}

ml_tools = ["Scikit-learn", "Pandas", "NumPy", "NLTK", "Spacy", "PyTorch", "Mathplotlib", "Keras", "Seaborn", "Selenium","LLM"]
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
    "Jenkins": "https://img.icons8.com/?size=100&id=39292&format=png&color=000000"
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

for i, os in enumerate(os_list):
    with os_cols[i % 3]:
        st.markdown(
            f"""
            <div class='skill-box' style="text-align:center; padding:10px;">
                <img src="{os_icon_map[os]}" alt="{os} icon" style="width:40px; height:40px; margin-bottom:10px;" />
                <div class='skill-text' style="font-weight:bold;">{os}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# --- EXPERIENCE SECTION ---
st.markdown("<div id='experience' class='content-section'>", unsafe_allow_html=True)
st.markdown("    ")
st.header("💼 Experience")

st.markdown("""
<div style="display: flex; justify-content: space-between; align-items: center;">
    <div>
        <h3>
            <a href="https://research.pes.edu/centre-of-cognitive-computing-and-computational-intelligence-c3i/" target="_blank" style="text-decoration: none; color: inherit;">
                Centre of Cognitive Computing and Computational Intelligence
            </a>
        </h3>
        <div class='subtitle'>Summer Research Intern | June 2025 - August 2025</div>
    </div>
    <div style="text-align: right; font-size: 1.5rem;">Bengaluru, Karnataka</div>
</div>
""", unsafe_allow_html=True)

#Experience Details
st.write("""
- Architected and deployed a comprehensive career advisory system using **Deep Structured Semantic Model (DSSM)** with dual-tower neural networks for intelligent job-course matching.

- Developed advanced NLP pipeline for multi-format resume processing using **Tesseract** with sophisticated skill extraction using regex patterns and custom normalization algorithms, successfully extracting relevant technical and business skills in a resume.
 
- Implemented vector database solution using **ChromaDB** for efficient storage and retrieval of **1,00,000+** job and course embeddings, enabling real-time semantic similarity searches across diverse datasets.

- Built interactive **Streamlit** application with real-time skill gap analysis, providing personalized course recommendations from Coursera and other platforms based on **Cosine-Similarity** scoring and semantic matching.

- Optimized system performance through memory-efficient negative sampling, batch processing, and embedding normalization, handling **30,000+** job-course pairs while maintaining sub-second response times.
""")



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
      <p>CGPA : 8.06</p>
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
      <p>DPS East</p>
      <p>🗓️ 2007 - 2020</p>
      <p>10th Boards : 90%</p>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)

# --- Custom CSS ---
st.markdown("""
<style>
.achievement-container {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 20px;
}
.achievement-left {
    font-size: 18px;
    font-weight: bold;
}
.achievement-description {
    font-size: 16px;
}
.achievement-date {
    font-size: 16px;
    color: #bbb;
}
</style>
""", unsafe_allow_html=True)

# --- ACHIEVEMENTS SECTION ---
st.markdown("<div id='achievements' class='content-section'>", unsafe_allow_html=True)
st.markdown("   ")
st.header("🏆 Achievements")


# MRD Scholarship
st.markdown("""
<div style="display: flex; justify-content: space-between; align-items: center;">
    <h3 style="margin: 0;">🎓 MRD Scholarship</h3>
</div>
""", unsafe_allow_html=True)
st.write("""
Awarded the prestigious **MRD Scholarship** in 1st Semester by **PES University**, receiving a 20% tuition fee reimbursement in recognition of academic excellence.
""")

# Distinction Scholarship
st.markdown("""
<div style="display: flex; justify-content: space-between; align-items: center;">
    <h3 style="margin: 0;">🏅 Distinction Scholarship</h3>
</div>
""", unsafe_allow_html=True)
st.write("""
Received **Distinction Scholarship** of ₹ 2000 for achieving SGPA above **7.75** in **Semesters 2–6** at **PES University**.
""")

# Google Agentic AI Day
st.markdown("""
<div style="display: flex; justify-content: space-between; align-items: center;">
    <div style="display: flex; align-items: center; gap: 8px;">
        <img src="https://img.icons8.com/?size=100&id=WHRLQdbEXQ16&format=png&color=000000" 
             alt="Google Cloud Icon" width="30" height="30">
        <h3 style="margin: 0;">Google Cloud Agentic AI Day</h3>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("""
Participated in **Google Cloud Agentic AI Day**, contributing an innovative idea to harness Agentic AI for real-world problem solving.

""")

# Heal-O-Code
st.markdown("""
<div style="display: flex; justify-content: space-between; align-items: center;">
    <h3 style="margin: 0;">🩺 Heal-O-Code Hackathon</h3>
</div>
""", unsafe_allow_html=True)
st.write("""
Top 6 out of 50+ teams in **Heal-O-Code Hackathon**. Built a healthcare decision support tool using **Multi-Chain Blockchain** and **Ollama** for better drug recommendation.
""")

# Kaggle Achievements
st.markdown("""
<div style="display: flex; justify-content: space-between; align-items: center;">
    <div style="display: flex; align-items: center; gap: 8px;">
        <img src="https://img.icons8.com/?size=100&id=s1rM4KTx2Huf&format=png&color=000000" 
             alt="Kaggle Icon" width="30" height="30">
        <h3 style="margin: 0;">Kaggle Hackathon</h3>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("""
Ranked in the top 30% on Hackerrank college hackathons for **Data Analytics** and **Machine Learning coursework**.

""")
st.markdown("</div>", unsafe_allow_html=True)

# --- PROJECTS SECTION ---
st.markdown("<div id='projects' class='content-section'>", unsafe_allow_html=True)
st.markdown("   ")
st.header("🚀 Projects")


# --- Blockchain Healthcare Project with Image ---
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(
        "<h3><a href='https://github.com/sUhAs1011/HoC2_PS9_Hash_Bros' target='_blank' style='text-decoration: none; color: inherit;'>⚕️ Blockchain-Powered AI Healthcare Insights</a></h3>",
        unsafe_allow_html=True
    )

    st.write("""
    Designed and developed a secure, scalable system to extract actionable insights from **Electronic Health Records (EHRs)**.

    Key features include:
    - Extracted insights from IPFS-stored EHR’s using unique blockchain ID’s to ensuring data integrity & traceability. 
    - Applied OCR & Ollama to patient histories leading to faster clinical decisions, predicting adverse drug-drug reactions & recommending treatments.
    - Recommend personalized treatment plans based on patient's history 

    **Tech Stack**: Python, Streamlit, IPFS, Multi-Chain Blockchain
    """)

with col2:
    st.image("healthcare.jpg", caption="Healthcare Blockchain System", use_container_width=True)


# Alarm Burglar System with image on the left and content on the right
st.markdown("---")
col_left, col_right = st.columns([1, 2])

with col_left:
    st.image("arduino.jpg", caption="Arduino-Based Security System", use_container_width=True)

with col_right:
    st.markdown(
        """
        <h3>
            <img src="https://img.icons8.com/?size=100&id=8thlDCUHuqaK&format=png&color=000000" 
                 width="35" style="vertical-align:middle; margin-right:10px;">
            <a href='https://github.com/sUhAs1011/UE22CS251B-IoT-Enabled-Arduino-Based-Intruder-Detection-and-Alert-System' 
               target='_blank' style='text-decoration: none; color: inherit;'>
               IoT-Enabled Arduino-Based Intruder Detection and Alert System
            </a>
        </h3>
        """,
        unsafe_allow_html=True
    )
    st.write("""
    Engineered a **Real-Time Intrusion Detection System** using Arduino, designed to enhance home security through automated alerts and physical deterrents.

    Key features include:
    - Utilized an **ultrasonic sensor** to detect unauthorized entry, triggering a red LED, buzzer alarm, and **GSM-based alert notifications**.
    - Programmed using **C++** with SoftwareSerial.h to manage GSM module communication.
    - Configured the Arduino IDE and implemented serial communication to ensure seamless system performance and real-time responsiveness.
    - Achieved near-instant detection **< 100 ms** with real-time serial communication, ensuring quick & reliable security alerts.

    **Tech Stack**: C++, Arduino, Ultrasonic Sensor, GSM Module, SoftwareSerial.h
    """)


# LegalBot with image on the right and content on the left
st.markdown("---")
col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown(
        "<h3><a href='https://github.com/sUhAs1011/UE22CS342B-NLP_Mini_Project-' target='_blank' style='text-decoration: none; color: inherit;'>⚖️ LegalBot: AI-Powered Regulatory Mining Intelligence Bot </a></h3>",
        unsafe_allow_html=True
    )
    st.write("""
    Developed an intelligent legal chatbot to respond to text-based queries related to **Acts, Rules, and Regulations** in the mining industry.

    Key features include:
    - Analyzed and interpreted mining laws to deliver precise legal responses based on user input.
    - Utilized **Sentence Transformer models** and **cosine similarity** to match user queries with the most relevant legal provisions.
    - Identified contradictions between overlapping laws and suggested alternative documents when conflicts were found.

    This solution streamlines legal compliance and enhances accessibility to complex regulatory frameworks.

    **Tech Stack**: Python, Sentence Transformers, MongoDB, Streamlit
    """)

with col_right:
    st.image("chatbot.jpg", caption="LegalBot - AI Chatbot for Mining Compliance", use_container_width=True)

# Cloud Storage with image on the left and content on the right
st.markdown("---")
col_left, col_right = st.columns([1, 2])

with col_left:
    st.image("udp.jpg", caption="Cloud File Transfer System using UDP", use_container_width=True)

with col_right:
    st.markdown(
        """
        <h3>
            <img src='https://img.icons8.com/?size=100&id=NIaxM8D5w6rv&format=png&color=FFFFFF' 
                 style='width:35px; height:35px; vertical-align:middle; margin-right:8px;'/>
            <a href='https://github.com/sUhAs1011/UE22CS252B-Cloud-File-Transfer-System-using-UDP-' 
               target='_blank' style='text-decoration: none; color: inherit;'>
               Cloud File Transfer System using UDP
            </a>
        </h3>
        """,
        unsafe_allow_html=True
    )
    st.write("""
    Built a secure, network-based **Cloud File Transfer System** using **Python** and **UDP** (User Datagram Protocol), 
    enabling efficient file transfer and command execution across systems.

    Key features include:
    - Developed a **client-server architecture** using Python **socket programming** for file upload, download, and listing operations.
    - Integrated **SSL certificates** for secure communication between client and server.
    - Implemented **dynamic IP handling** to support both localhost and distributed multi-system deployments.
    - Enabled execution of remote shell commands and ensured seamless file transfers across networked devices.

    **Tech Stack**: Python, UDP, Socket Programming, SSL, File Handling
    """)


# Portfolio Project with image on the right and content on the left
st.markdown("---")
col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown(
        """
        <h3>
        <img src='https://img.icons8.com/?size=100&id=ognMDWHTIaDL&format=png&color=000000' 
                 style='width:40px; height:40px; vertical-align:middle; margin-right:8px;'/>
         <a href='https://github.com/sUhAs1011/My_Portfolio' 
               target='_blank' style='text-decoration: none; color: inherit;'>
               Interactive Personal Portfolio Website using Streamlit
        </a>
        </h3>""",
        unsafe_allow_html=True
    )
    st.write("""
    Crafted a polished personal site in **Streamlit** as a single source of truth for my story, projects, and contact touchpoints.

    Key features include:
    - Cinematic hero section with animated typography, profile portrait, and quick stats.
    - Modular skills grid, project spotlight cards, and experience timeline for fast scanning.
    - Built-in resume download plus branded CTAs for GitHub, LinkedIn, and email.
    - Fully responsive layout with custom CSS that adapts to Streamlit light/dark themes.

    **Tech Stack**: Python · Streamlit · HTML/CSS · PIL
    """)

with col_right:
    st.image("portfolio.jpg", caption="Streamlit Portfolio", use_container_width=True)

# Analyzing job posting trends, skill gaps, and recommend reskilling programs in  employment sectors
st.markdown("---")
col_left, col_right = st.columns([1, 2])

with col_left:
    st.image("career.jpg", caption="Career Copilot", use_container_width=True)

with col_right:
    st.markdown(
        """
        <h3>
            <img src='https://img.icons8.com/?size=100&id=fLrxgaxCrjaZ&format=png&color=FFFFFF' 
                 style='width:35px; height:35px; vertical-align:middle; margin-right:8px;'/>
            <a href='https://github.com/sUhAs1011/AI-Powered-Skill-Gap-Analysis-Reskilling-for-Employment-Trends' 
               target='_blank' style='text-decoration: none; color: inherit;'>
               AI-Powered Career Skill Gap Analysis & Recommendation
            </a>
        </h3>
        """,
        unsafe_allow_html=True
    )
    st.write("""
    Analyzing job trends, mapping skill gaps, and recommending targeted reskilling programs across different employment sectors.

    Key features include:
    - Utilized **all-MiniLM-L6-v2** to generate and push refined job-course embeddings into **ChromaDB** for efficient semantic search.
    - Employed a **Deep Structured Semantic Model (DSSM)** for training to learn enhanced semantic relationships.
    - Developed a Streamlit web application as a user-friendly frontend interface, facilitating interactive skill gap analysis and course recommendations.
    - Provided intelligent course suggestions directly addressing identified skill gaps relevant to a specific job position, leveraging the pre-computed mappings.
    
    **Tech Stack**: Python, Sentence Transformers, ChromaDB, DSSM, Streamlit, Tesseract 
    """)

# Distributed Cluster Simulator
st.markdown("---")
col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown(
        """
        <h3>
        <img src='https://img.icons8.com/?size=100&id=7pFfikEfVGOV&format=png&color=000000' 
                 style='width:35px; height:35px; vertical-align:middle; margin-right:8px;'/>
         <a href='https://github.com/sUhAs1011/UE22CS351B-Distributed_Systems_Cluster_Simulation_Framework' 
               target='_blank' style='text-decoration: none; color: inherit;'>
               Distributed Systems Cluster Simulator Framework
        </a>
        </h3>""",
        unsafe_allow_html=True
    )
    st.write("""
    Designed and implemented a distributed systems simulation framework using **Docker** and **API-server**

    Key features include:
    - API Server: A centralized control unit for node management, pod scheduling, and health monitoring.
    - Cluster Nodes: Virtualized computing units that periodically send heartbeat signals to the **API-Server**.
    - Pods: Deployable units simulated on nodes, which require specific CPU resources.
    - Dockerized for portability and easy deployment and Real-time cluster health and pod scheduling visualization via Streamlit.


    **Tech Stack**: Python, Streamlit, Docker, Node.js, REST APIs, JSON
    """)

with col_right:
    st.image("node_simulator.jpg", caption="Distributed Systems Cluster Simulator", use_container_width=True)


# Detection And Mitigation Of Replay Attack in CCTV systems
st.markdown("---")
col_left, col_right = st.columns([1, 2])

with col_left:
    st.image("cctv.jpg", caption="Replay Attack Detection And Mitigation in CCTV Systems", use_container_width=True)

with col_right:
    st.markdown(
        """
        <h3>
            <img src='https://img.icons8.com/?size=100&id=3wl52ZDVBgG0&format=png&color=000000' 
                 style='width:28px; height:26px; vertical-align:middle; margin-right:8px;'/>
            <a href='https://github.com/sUhAs1011/Detection_And_Mitigation_of_Replay_Attack_in_CCTV_Systems' 
               target='_blank' style='text-decoration: none; color: inherit;'>
               Detection and Mitigation of Replay Attack in CCTV Systems
            </a>
        </h3>
        """,
        unsafe_allow_html=True
    )
    st.write("""
    Replay attacks on CCTV systems exploit vulnerabilities by retransmitting recorded footage to bypass live monitoring

    Key features include:
    - **Optical flow–based motion analysis** with **SDR** encoding to capture temporal motion patterns in a compact and interpretable form.
    - **Hierarchical Temporal Memory (HTM)** model for lightweight, real-time anomaly detection of unusual motion sequences.
    - **SHA‑256** frame hashing and verification to ensure tamper-evident, forensic reliability of CCTV footage.
    - Decision engine with dashboard interface that fuses anomaly scores and integrity checks, providing real-time alerts, visualization, and forensic reporting.
    
    Tech Stack: Python, HTM, SHA-256, SDR
    """)


# --- Custom Footer with Styling ---
st.markdown("""
    <div style='text-align: center; padding-top: 20px; font-size: 25px; font-weight: 500; color: #ffffff;'>
        Made by Suhas Venkata with ❤️
    </div>
    <div style='text-align: center; padding-top: 0px; font-size: 20px; font-weight: 500; color: #ffffff;'>
        Using Streamlit and Python
    </div>
""", unsafe_allow_html=True)



st.markdown("""
<style>
/* ===== Name should be white on dark, black on light, and emoji visible ===== */
:root { --text-color: var(--color-text); }

.gradient-text {
  background: none !important;
  -webkit-background-clip: initial !important;
  -webkit-text-fill-color: var(--text-color) !important;
  color: var(--text-color) !important;
  text-shadow: none;
}

.gradient-text .letter {
  -webkit-text-fill-color: var(--text-color) !important;
  color: var(--text-color) !important;
  transition: transform 0.25s ease, color 0.25s ease;
}

/* Hover tint only (optional) */
.gradient-text .letter:hover {
  color: #1d4ed8 !important;
  -webkit-text-fill-color: #1d4ed8 !important;
  transform: translateY(-4px) scale(1.15);
}

/* Make emoji follow theme text color and stay visible */
.gradient-text .emoji {
  background: none !important;
  -webkit-background-clip: initial !important;
  -webkit-text-fill-color: var(--text-color) !important;
  color: var(--text-color) !important;
}
</style>
""", unsafe_allow_html=True)



st.markdown("""
<style>
/* ============= FINAL OVERRIDE: fix dark-mode invisibility ============= */
/* Use Streamlit's built-in variables with safe fallbacks */
:root{
  --sv-text: var(--text-color, #e5e7eb);
  --sv-bg:   var(--background-color, #0e1117);
}

/* Base */
body{ background-color: var(--sv-bg) !important; color: var(--sv-text) !important; }
p, div, span, li, .intro, .subtitle { color: var(--sv-text) !important; }
h1, h2, h3, h4, h5, h6, .navbar-name, .navbar-custom a { color: var(--sv-text) !important; }
h3 a{ color: var(--sv-text) !important; }

/* Name + emoji follow theme color */
.gradient-text,
.gradient-text .letter,
.gradient-text .emoji{
  -webkit-text-fill-color: var(--sv-text) !important;
  color: var(--sv-text) !important;
  background: none !important;
}

/* Buttons */
.contact-button{ border-color: var(--sv-text) !important; color: var(--sv-text) !important; }
</style>
""", unsafe_allow_html=True)



st.markdown("""
<style>
/* ===== Fix light-mode unreadable text inside dark cards ===== */
.skill-box,
.timeline-content {
  background-color: #0f172a !important;   /* dark surface */
  color: #ffffff !important;              /* force light text */
}
.skill-box .skill-text,
.skill-box div,
.skill-box p,
.timeline-content h3,
.timeline-content p,
.timeline-content span,
.timeline-content div {
  color: #ffffff !important;
}

/* Remove any lingering glow/blur from the name */
.gradient-text,
.gradient-text .letter {
  text-shadow: none !important;
  filter: none !important;
}

/* Keep subtitle and paragraph readable across themes */
.subtitle, .intro, p { color: var(--text-color, var(--sv-text, #111)) !important; }
</style>
""", unsafe_allow_html=True)



st.markdown("""
<style>
/* ===== Ultimate theme fix using media queries (wins over all previous rules) ===== */
@media (prefers-color-scheme: light){
  body, p, li, div, span, .subtitle, .intro,
  h1, h2, h3, h4, h5, h6,
  .navbar-name, .navbar-custom a, h3 a {
    color: #111827 !important;   /* near-black on white */
  }
  .contact-button { border-color:#111827 !important; color:#111827 !important; }
  /* Make the hero name visible in light mode */
  body .gradient-text, body .gradient-text .letter, body .gradient-text .emoji {
    background:none !important;
    -webkit-background-clip: initial !important;
    -webkit-text-fill-color:#111827 !important;
    color:#111827 !important;
    text-shadow:none !important;
  }
  /* Keep dark cards readable */
  .skill-box, .timeline-content {
    background-color:#0f172a !important;
    color:#ffffff !important;
  }
  .skill-box *,
  .timeline-content * { color:#ffffff !important; }
}

@media (prefers-color-scheme: dark){
  body, p, li, div, span, .subtitle, .intro,
  h1, h2, h3, h4, h5, h6,
  .navbar-name, .navbar-custom a, h3 a {
    color:#e5e7eb !important;   /* light gray on dark */
  }
  .contact-button { border-color:#e5e7eb !important; color:#e5e7eb !important; }
  /* Make the hero name visible in dark mode */
  body .gradient-text, body .gradient-text .letter, body .gradient-text .emoji {
    background:none !important;
    -webkit-background-clip: initial !important;
    -webkit-text-fill-color:#e5e7eb !important;
    color:#e5e7eb !important;
    text-shadow:none !important;
  }
}

/* ===== FINAL FIX: Contact Buttons Visible in Light & Dark Mode ===== */
.button-row .contact-button {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 8px !important;
  font-weight: 600 !important;
  border-radius: 12px !important;
}

/* Light mode — dark pill + white text */
@media (prefers-color-scheme: light) {
  .button-row .contact-button {
    background-color: #0f172a !important;
    border: 2px solid #1e3a8a !important;
    color: #ffffff !important;
  }
  .button-row .contact-button * {
    color: #ffffff !important;
  }
}

/* Dark mode — slightly lighter pill + white text */
@media (prefers-color-scheme: dark) {
  .button-row .contact-button {
    background-color: #111827 !important;
    border: 2px solid #1e3a8a !important;
    color: #ffffff !important;
  }
  .button-row .contact-button * {
    color: #ffffff !important;
  }
}

/* ===== Keep content below the fixed navbar (works in light & dark) ===== */
:root { --nav-offset: calc(var(--nav-h-dyn, var(--nav-h, 64px)) + 40px);  } /* fallback if JS hasn't run yet */

.navbar-custom{
  position: fixed !important;
  top: 0; left: 0; right: 0;
  z-index: 1000 !important;
  background: var(--background-color, #0e1117) !important;
  border-bottom: 1px solid rgba(255,255,255,0.08);
  /* keep links from wrapping into multiple rows */
  display:flex; flex-direction: row; align-items: center; gap: 12px;
}
.navbar-links{
  white-space: nowrap !important;
  overflow-x: auto !important; overflow-y: hidden !important;
  -webkit-overflow-scrolling: touch;
}
.navbar-links::-webkit-scrollbar { display: none; }

/* use measured height if available, else fallback */
[data-testid="stAppViewContainer"], .main{
  padding-top: calc(var(--nav-h-dyn, var(--nav-h)) + 10px) !important;
}
.content-section{
  scroll-margin-top: calc(var(--nav-h-dyn, var(--nav-h)) + 1px) !important;
}

@media (max-width: 768px){
  .content-section{
    scroll-margin-top: calc(var(--nav-h-dyn, var(--nav-h)) + 40px) !important;
  }

/* ✅ Force navbar readable in both themes */
@media (prefers-color-scheme: light){
  .navbar-custom{
    background: #ffffff !important;
    border-bottom: 1px solid rgba(0,0,0,0.15);
  }
  .navbar-custom a,
  .navbar-name{
    color: #000000 !important;
  }
}

@media (prefers-color-scheme: dark){
  .navbar-custom{
    background: #0e1117 !important;
    border-bottom: 1px solid rgba(255,255,255,0.08);
  }
  .navbar-custom a,
  .navbar-name{
    color: #e5e7eb !important;
  }
}


</style>
""", unsafe_allow_html=True)
