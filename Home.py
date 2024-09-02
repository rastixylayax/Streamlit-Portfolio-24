import streamlit as st
from PIL import Image
import base64
from pathlib import Path

def encode_svg_to_base64(svg_path):
    with open(svg_path, "rb") as svg_file:
        return base64.b64encode(svg_file.read()).decode("utf-8")
    
# SVG to Base64
logos_base64 = {
    "LinkedIn": encode_svg_to_base64("./assets/linkedin.svg"),
    "GitHub": encode_svg_to_base64("./assets//github.svg"),
    "Facebook": encode_svg_to_base64("./assets/facebook.svg"),
    "Instagram": encode_svg_to_base64("./assets/instagram.svg"),
}

# Path
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resumeArj.docx"
profile_pic = current_dir / "assets" / "pfpArj.png"

# Profile Information
NAME = "< Rustico John Ylaya />"
DESCRIPTION = "Information Technology Student | Frontend Developer | UI/UX Designer"
EMAIL = "ylayarusticojohn@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/rastixylaya",
    "GitHub": "https://github.com/rastixylayax",
    "Facebook": "https://www.facebook.com/rastixylaya",
    "Instagram": "https://twitter.com/rastixylaya",
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

# Resume File + Profile Picture
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# Hero Section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=300)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
st.write('\n')

st.divider()

code = '''def hello():
    print("Hello, everyone!")
    print("To learn more about me, check out and explore my portfolio!")
    print("I hope you enjoy your stay here!")'''
st.code(code, language="python")
