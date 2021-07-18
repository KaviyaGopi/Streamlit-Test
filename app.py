from PIL import Image
import streamlit as st

# Text/Title
st.title("Hello Mounika")

# Header/Subheader
st.header("This is a header")
st.subheader("this is a subheader")

# Text
st.text("Hello Kaviya")

# Markdown
st.markdown("### This is a Markdown")

# Error/Colourful Text
st.success("Successful")

st.info("Information!")

st.warning("This is a warning")

st.error("This is an error Danger")

st.exception("NameError('name three not defined')")

# Get Help Info About Python
st.help(range)

# Writing Text/Super Fxn
st.write(range(10))

# Image
img = Image.open("images\cherry.jpg")
st.image(img, width=300, caption="Simple Image")
