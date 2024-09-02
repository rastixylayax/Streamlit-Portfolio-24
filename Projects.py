import streamlit as st
from PIL import Image
from pathlib import Path
import base64

# Path
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
profile_pic = current_dir / "assets" / "aboutArj.jpg"

# Profile Picture
profile_pic = Image.open(profile_pic)

# Hero Section
st.title("{ all about ARJI | experience}")
st.write('\n')
st.write(
        """
        My name is Rustico John Ylaya, a 4th-year Information Technology student at the Cebu Institute of Technology - University.
        I am an aspiring front-end developer and UI/UX designer. As a student, I am always eager to learn new things and improve my skills.
        I have a few projects that I have worked on and I am always looking for new opportunities to grow and learn.
        """
    )
st.write('\n')
# Container on columns for each skill
col1, col2, col3 = st.columns(3, gap = "medium")

with col1:
    container = st.container(border=True)
    container.write("💻 Frontend Development")
    container.progress(60)

with col2:
    container = st.container(border=True)
    container.write("🎨 UI/UX Design")
    container.progress(80)

with col3:
    container = st.container(border=True)
    container.write("📋 Project Management")
    container.progress(50)

st.divider()

def encode_svg_to_base64(svg_path):
    with open(svg_path, "rb") as svg_file:
        return base64.b64encode(svg_file.read()).decode("utf-8")
    
# SVG to Base64
logos_base64 = {
    "LinkedIn": encode_svg_to_base64("./assets/linkedin.svg"),
    "GitHub": encode_svg_to_base64("./assets//github.svg"),
    "Facebook": encode_svg_to_base64("./assets/facebook.svg"),
    "Instagram": encode_svg_to_base64("./assets/instagram.svg"),
    "Designs": encode_svg_to_base64("./assets/figma.svg"),
}

# Path
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

# Profile Information
NAME = "< Rustico John Ylaya />"
DESCRIPTION = "Information Technology Student | Frontend Developer | UI/UX Designer"
EMAIL = "ylayarusticojohn@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/rastixylaya",
    "GitHub": "https://github.com/rastixylayax",
    "Facebook": "https://www.facebook.com/rastixylaya",
    "Instagram": "https://twitter.com/rastixylaya",
    "Designs": "https://www.figma.com/design/mxrrmTIs9oeb1bfpLCoSpc/All-Figma-Projects?node-id=15-16392&t=WY1ECaYYUIZD8aPW-1",
}

# Socmed Links
cols = st.columns(len(SOCIAL_MEDIA))

# Column for each social media platform
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    if platform in logos_base64:
        logo_base64 = logos_base64[platform]
        cols[index].markdown(
            f"""
            <a href='{link}' target='_blank' style='text-decoration: none;'>
                <img src='data:image/svg+xml;base64,{logo_base64}' alt='{platform}' style='width:24px; height:24px; vertical-align:middle; margin-right:10px;'> {platform}
            </a>
            """,
            unsafe_allow_html=True
        )
    else:
        cols[index].write(f"[{platform}]({link})")

st.divider()

# Projects
tab1, tab2, tab3, tab4 = st.tabs(["Page 1", "Page 2", "Page 3", "Page 4"])

with tab1:
    st.image("./assets/first.png")
with tab2:
    st.image("./assets/second.png")
with tab3:
    st.image("./assets/third.png")
with tab4:
    st.image("./assets/fourth.png")
