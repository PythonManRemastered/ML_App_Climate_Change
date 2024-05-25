import streamlit as st
from ultralytics import YOLO
from PIL import Image

st.title("Image classifier 9000")

#decorator thing?
@st.cache_resource


def load_model():
    mod = YOLO("best.pt")
    return mod

img = st.file_uploader("Upload an image to classify", type=["jpg", "png", "jpeg"])

if img is not None:
    img = Image.open(img)
    st.image(img)
    mod1 = load_model()
    res = mod1.predict(img)
    pred = res[0].probes.top5
    for ind in pred:
        st.write(res[0].names[ind])