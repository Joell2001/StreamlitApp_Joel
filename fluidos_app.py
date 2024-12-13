# Import Python Libraries
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.express as px
from PIL import Image
from collections import namedtuple
from math import radians, isclose, acos, asin, cos, sin, tan, atan, degrees, sqrt

# Insert an icon
icon = Image.open("Resources/lodo_perf.jpg")

# State the design of the app
st.set_page_config(page_title="Drill Fluids APP", page_icon=icon)

# Insert css codes to improve the design of the app
st.markdown(
    """
<style>
h1 {text-align: center;
}
body {background-color: #DCE3D5;
      width: 1400px;
      margin: 15px auto;
}
footer {
  display: none;
}
</style>""",
    unsafe_allow_html=True,
)

# Insert title for app
st.title("Drill Fluids APP")

st.write("---")

# Add information of the app
st.markdown(
    """
    El aplicativo Drill Fluids Hub está diseñado para brindar información clave sobre las actividades relacionadas con los fluidos de perforación en operaciones petroleras. 
    Proporciona herramientas para monitorear propiedades, optimizar el uso de recursos y garantizar la sostenibilidad ambiental en los procesos de perforación."""


)

# Add additional information
expander = st.expander("Information")
expander.write(
    "This is an open-source web app fully programmed in Python for analyzing and optimizing drilling fluid parameters."
)

# Insert subheader
st.subheader("**Qué son los fluidos de perforación?**")
# Insert Image
image = Image.open("Resources/1.jpg")
st.image(image, width=100, use_container_width=True)

# Insert subheader
st.subheader("**Tpos de fluidos de perforación**")
# Insert Image
image = Image.open("Resources/2.png")
st.image(image, width=100, use_container_width=True)

# Insert subheader
st.subheader("**Perforación con sistema de lodoo**")

# Insert video
video = open("Resources/Perforación con sistema de lodo.mp4", "rb")
st.video(video)


# Sidebar section
logo = Image.open("Resources/logo.png")
st.sidebar.image(logo)

# Add title to the sidebar section
st.sidebar.title("⬇ Navigation")

# Upload files
file = st.sidebar.file_uploader("Upload your csv file")

# Add sections of the app
with st.sidebar:
    options = option_menu(
        menu_title="Menu",
        options=["Propiedades y Clasificación:", "Monitoreo y Control:", "Impacto Ambiental:"],
        icons=["house", "tv-fill", "box"],
    )
