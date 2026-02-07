"""
🎨 YEN NHI PORTFOLIO - FINAL VERSION
Clean, Simple, No HTML Rendering Issues
Proper Margins on Both Sides
"""

import streamlit as st

# ===== PAGE CONFIG =====
st.set_page_config(
    page_title="Yen Nhi - Graphic Designer Portfolio",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===== CUSTOM CSS =====
st.markdown("""
<style>
    /* Import Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;900&family=Lato:wght@300;400;700&display=swap');
    
    /* HIDE SIDEBAR */
    [data-testid="stSidebar"] {
        display: none !important;
    }
    
    /* Hide Streamlit Elements */
    #MainMenu, footer, .stDeployButton, header {
        visibility: hidden;
    }
    
    /* Smooth Scrolling */
    html {
        scroll-behavior: smooth;
    }
    
    /* Global Background with PROPER MARGINS */
    .main {
        background-color: #F5F1E8;
    }
    
    .block-container {
        padding: 2rem 8% !important;
        max-width: 1400px !important;
        margin: 0 auto !important;
    }
    
    /* Typography */
    h1, h2, h3 {
        font-family: 'Playfair Display', serif;
        color: #2B1E4B;
    }
    
    p, li {
        font-family: 'Lato', sans-serif;
        color: #666666;
        font-size: 1.05rem;
        line-height: 1.8;
    }
    
    /* Navigation */
    .nav-bar {
        background: #F5F1E8;
        padding: 1.5rem 0;
        text-align: center;
        border-bottom: 1px solid rgba(43, 30, 75, 0.1);
        position: sticky;
        top: 0;
        z-index: 1000;
        margin: 0 -8%;
        padding-left: 8%;
        padding-right: 8%;
    }
    
    .nav-bar a {
        font-family: 'Lato', sans-serif;
        color: #2B1E4B;
        text-decoration: none;
        margin: 0 1.5rem;
        font-size: 1rem;
        transition: color 0.3s;
    }
    
    .nav-bar a:hover {
        color: #FFB6C1;
    }
    
    /* Hero */
    .hero {
        text-align: center;
        padding: 8rem 2rem 6rem;
        margin: 0 -8%;
        background: #F5F1E8;
    }
    
    .hero-subtitle {
        font-family: 'Lato', sans-serif;
        font-size: 1rem;
        letter-spacing: 6px;
        color: #FFB6C1;
        margin-bottom: 1.5rem;
    }
    
    .hero-title {
        font-family: 'Playfair Display', serif;
        font-size: 7rem;
        font-weight: 900;
        color: #2B1E4B;
        margin: 1.5rem 0;
        line-height: 1;
    }
    
    .hero-role {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        color: #666666;
        font-style: italic;
        margin: 2rem 0 1rem;
    }
    
    .hero-location {
        font-family: 'Lato', sans-serif;
        font-size: 1.1rem;
        color: #666666;
        letter-spacing: 4px;
    }
    
    /* Section Title */
    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 4rem;
        font-weight: 700;
        color: #2B1E4B;
        margin: 3rem 0 2rem 0;
        position: relative;
        display: inline-block;
    }
    
    .section-title::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 0;
        width: 100px;
        height: 3px;
        background: #FFB6C1;
    }
    
    /* Content Box */
    .content-box {
        background: white;
        padding: 3rem;
        border-radius: 20px;
        margin: 2rem 0;
        box-shadow: 0 10px 40px rgba(0,0,0,0.05);
    }
    
    /* Vision Box */
    .vision-box {
        background: #2B1E4B;
        padding: 4rem;
        border-radius: 25px;
        margin: 3rem 0;
        color: white;
    }
    
    .vision-title {
        font-size: 3.5rem;
        color: #FFE5B4;
        margin-bottom: 2rem;
        position: relative;
        display: inline-block;
    }
    
    .vision-title::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 0;
        width: 80px;
        height: 3px;
        background: #FFB6C1;
    }
    
    /* Experience Card */
    .exp-card {
        background: white;
        padding: 3rem;
        border-radius: 20px;
        margin: 2rem 0;
        border-left: 5px solid #FFB6C1;
        box-shadow: 0 10px 40px rgba(0,0,0,0.05);
    }
    
    /* Image styling */
    .stImage {
        border-radius: 15px;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .block-container {
            padding: 1rem 4% !important;
        }
        .hero-title {
            font-size: 4rem;
        }
        .section-title {
            font-size: 2.5rem;
        }
        .nav-bar {
            margin: 0 -4%;
            padding-left: 4%;
            padding-right: 4%;
        }
        .hero {
            margin: 0 -4%;
        }
    }
</style>
""", unsafe_allow_html=True)

# ===== NAVIGATION =====
st.markdown("""
<div class='nav-bar'>
    <a href='#home'>Home</a>
    <a href='#about'>About</a>
    <a href='#vision'>Vision</a>
    <a href='#education'>Education</a>
    <a href='#skills'>Skills</a>
    <a href='#experience'>Experience</a>
    <a href='#projects'>Projects</a>
</div>
""", unsafe_allow_html=True)

# ===== HOME =====
st.markdown("""
<div id='home' class='hero'>
    <div class='hero-subtitle'>PORTFOLIO</div>
    <h1 class='hero-title'>YEN NHI</h1>
    <div class='hero-role'>Graphic Designer Intern</div>
    <div class='hero-location'>HA NOI</div>
</div>
""", unsafe_allow_html=True)

# ===== ABOUT =====
st.markdown("<div id='about'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>About Me</h2>", unsafe_allow_html=True)

col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("""
    <div class='content-box'>
        <p>Hello, I'm Yen Nhi, a passionate Graphic Design Intern candidate with a strong interest in visual communication and creative storytelling. I have hands-on experience in designing posters, banners, and digital content for student organizations and educational projects.</p>
        
        <p>With a background in Marketing and Communication activities, I understand not only how to design visually appealing products but also how to deliver messages effectively to target audiences. I enjoy transforming ideas into meaningful visuals and continuously improving my design skills through practice and real projects.</p>
        
        <p>I am currently seeking an internship opportunity where I can contribute my creativity, learn from professionals, and grow into a well-rounded graphic designer.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image("https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=800&h=1000&fit=crop", use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# ===== VISION =====
st.markdown("<div id='vision'>", unsafe_allow_html=True)

st.markdown("""
<div class='vision-box'>
    <h2 class='vision-title'>Vision</h2>
    <p style='font-size: 1.2rem; line-height: 2; margin: 2rem 0;'>
        My vision is to become a professional graphic designer who creates impactful visual experiences that connect brands with people.
    </p>
    <p style='font-size: 1.2rem; line-height: 2; margin: 2rem 0;'>
        I aim to develop strong design thinking, master industry-standard tools, and continuously explore new trends in digital design. In the long term, I hope to work in creative teams where collaboration, innovation, and storytelling play key roles in building meaningful products and campaigns.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ===== EDUCATION =====
st.markdown("<div id='education'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>Education</h2>", unsafe_allow_html=True)

st.markdown("""
<div class='content-box'>
    <h3 style='font-size: 2rem; margin-bottom: 0.5rem;'>Second-year student in Economics</h3>
    <p style='color: #FFB6C1; font-size: 1.1rem; margin-bottom: 2.5rem;'>Foreign Trade University (FTU)</p>
    
    <h4 style='font-size: 1.5rem; color: #2B1E4B; margin: 2rem 0 1rem 0;'>Relevant Coursework</h4>
</div>
""", unsafe_allow_html=True)

st.write("→ Marketing Fundamentals")
st.write("→ Digital Communication")
st.write("→ Consumer Behavior")
st.write("→ Branding Basics")

st.markdown("""
<div class='content-box'>
    <h4 style='font-size: 1.5rem; color: #2B1E4B; margin: 2rem 0 1rem 0;'>Additional Learning</h4>
</div>
""", unsafe_allow_html=True)

st.write("→ Self-study Graphic Design via online courses and practice projects")
st.write("→ Experience in club media teams and event communication")

st.markdown("</div>", unsafe_allow_html=True)

# ===== SKILLS =====
st.markdown("<div id='skills'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>Personal Skills</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='content-box'>
        <h3 style='font-size: 2rem; margin-bottom: 2rem;'>Hard Skills</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("• Graphic Design: Canva, Adobe Illustrator, Photoshop")
    st.write("• Layout Design for posters, banners, social media posts")
    st.write("• Basic UI/Visual thinking for web content")
    st.write("• Branding fundamentals")
    st.write("• Content visualization")
    st.write("• Basic HTML/CSS")

with col2:
    st.markdown("""
    <div class='content-box'>
        <h3 style='font-size: 2rem; margin-bottom: 2rem;'>Soft Skills</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("• Creativity and visual storytelling")
    st.write("• Strong sense of responsibility")
    st.write("• Time management and deadline awareness")
    st.write("• Teamwork and communication")
    st.write("• Willingness to learn and adapt")
    st.write("• Attention to detail")

st.markdown("<br>", unsafe_allow_html=True)

cols = st.columns(3)
images = [
    "https://images.unsplash.com/photo-1626785774573-4b799315345d?w=400&h=400&fit=crop",
    "https://images.unsplash.com/photo-1611224885990-ab7363d1f2a8?w=400&h=400&fit=crop",
    "https://images.unsplash.com/photo-1542744094-24638eff58bb?w=400&h=400&fit=crop"
]
for col, img in zip(cols, images):
    with col:
        st.image(img, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# ===== EXPERIENCE =====
st.markdown("<div id='experience'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>Experience</h2>", unsafe_allow_html=True)

st.markdown("""
<div class='exp-card'>
    <h3 style='font-size: 2rem; margin-bottom: 0.5rem;'>IPC Organizations</h3>
    <p style='color: #FFB6C1; font-size: 1.1rem; font-style: italic; margin: 0.5rem 0 1rem;'>Media & Marketing Member</p>
    <p style='color: #999999; font-size: 1rem; font-style: italic; margin-bottom: 2rem;'>[2024 – 2025]</p>
</div>
""", unsafe_allow_html=True)

st.write("• Designed posters, banners, and social media visuals for events and campaigns")
st.write("• Collaborated with marketing teams to develop creative concepts")
st.write("• Supported branding activities for workshops and seminars")
st.write("• Assisted in content planning and visual direction")
st.write("• Delivered designs under tight deadlines while maintaining quality")

st.markdown("<br>", unsafe_allow_html=True)

cols = st.columns(4)
exp_images = [
    "https://images.unsplash.com/photo-1557838923-2985c318be48?w=500&h=400&fit=crop",
    "https://images.unsplash.com/photo-1542744094-24638eff58bb?w=500&h=400&fit=crop",
    "https://images.unsplash.com/photo-1611224885990-ab7363d1f2a8?w=500&h=400&fit=crop",
    "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500&h=400&fit=crop"
]
for col, img in zip(cols, exp_images):
    with col:
        st.image(img, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# ===== PROJECTS =====
st.markdown("<div id='projects'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>Projects</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='content-box'>
        <h3 style='font-size: 1.8rem; margin-bottom: 1.5rem;'>Event Promotion Design – IP Day</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&h=500&fit=crop", use_container_width=True)
    
    st.write("Designed poster and digital banners for Intellectual Property Day. Created visual identity aligned with event theme and produced social media posts for promotion.")
    
    st.markdown("<p style='color: #2B1E4B; margin-top: 1rem;'><strong>Tools:</strong> Canva, Illustrator</p>", unsafe_allow_html=True)
    st.markdown("<p style='background: #FFF5F7; padding: 1rem; border-radius: 10px; border-left: 4px solid #FFB6C1;'><strong>Outcome:</strong> Increased event visibility and engagement</p>", unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='content-box'>
        <h3 style='font-size: 1.8rem; margin-bottom: 1.5rem;'>Community Project – Glowbies</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?w=800&h=500&fit=crop", use_container_width=True)
    
    st.write("Designed branding materials for children-focused community project. Created posters and fundraising visuals while supporting storytelling through warm color palettes and friendly layouts.")
    
    st.markdown("<p style='color: #2B1E4B; margin-top: 1rem;'><strong>Tools:</strong> Illustrator, Photoshop</p>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ===== FOOTER =====
st.markdown("""
<div style='text-align: center; padding: 3rem 2rem; margin-top: 4rem; border-top: 1px solid rgba(43, 30, 75, 0.1);'>
    <p style='font-family: Lato, sans-serif; color: #666666; margin: 0;'>
        © 2025 Yen Nhi - Graphic Designer Portfolio
    </p>
    <p style='font-family: Lato, sans-serif; color: #999999; margin: 0.5rem 0 0 0; font-size: 0.9rem;'>
        Designed with creativity and passion 🎨
    </p>
</div>
""", unsafe_allow_html=True)
