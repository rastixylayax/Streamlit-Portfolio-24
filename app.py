import streamlit as st
import base64

# SVG File
with open("./assets/whale.svg", "rb") as svg_file:
    svg_data = svg_file.read()
    svg_base64 = base64.b64encode(svg_data).decode("utf-8")

# Page w/ SVG Icon
st.set_page_config(
    page_title="itsArjii",
    page_icon=f"data:image/svg+xml;base64,{svg_base64}"
)

pages = {
    "🏠 Home": [
        st.Page("Home.py"),
    ],
    "🔨 Experience": [
        st.Page("Projects.py"),
    ],
    "🧑 About Me": [
        st.Page("About.py"),
    ],
}

pg = st.navigation(pages, position="sidebar")
pg.run()