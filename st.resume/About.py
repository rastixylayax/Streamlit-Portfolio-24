import streamlit as st
from PIL import Image
from pathlib import Path

# Path
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
profile_pic = current_dir / "assets" / "aboutArj.jpg"

# Profile Picture
profile_pic = Image.open(profile_pic)

# Hero Section
st.title("{ all about ARJI }")
st.write(
        """
        My name is Rustico John Ylaya, a 4th-year Information Technology student at the Cebu Institute of Technology - University.
        I am a man with a lot of hobbies. When I am not programming or designing, I love to hit the gym, play volleyball, and play video games.
        It keeps me sane and helps me to be more productive. I am also a huge fan of anime and manga. 
        """
    )
st.write('\n')

# Container on columns for each hobby
col1, col2, col3 = st.columns(3, gap = "medium")

with col1:
    container = st.container(border=True)
    container.write("🏐 Volleyball")

with col2:
    container = st.container(border=True)
    container.write("🎮 Video Games")

with col3:
    container = st.container(border=True)
    container.write("🏋️‍♂️ Gym")
    
st.divider()


st.subheader("< AniManga Recommendations />")

# Expander
with st.expander("Click to see my top 3 anime recommendations!"):
    # Columns
    col1, col2, col3 = st.columns(3)
    
    # Content per column
    with col1:
        st.image("./assets/samchamp.gif", caption="Samurai Champloo")
    with col2:
        st.image("./assets/csm.gif", caption="Chainsaw Man")
    with col3:
        st.image("./assets/haikyu.gif", caption="Haikyuu Series")

st.divider()

st.subheader("< Game Highlights />")

# Expander
with st.expander("Click to see my top 3 game highlights!"):
    # Columns
    col1, col2, col3 = st.columns(3)
    
    # Content per column
    with col1:
        st.video("./assets/sovaclutch.mp4")
    with col2:
        st.video("./assets/razeace.mp4")
    with col3:
        st.video("./assets/reynawtf.mp4")

st.divider()