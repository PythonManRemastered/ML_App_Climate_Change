
import streamlit as st
import pandas as pd 
import numpy as np
from ultralytics import YOLO
from PIL import Image


st.set_page_config(layout="wide")
tab1, tab2, tab3, tab4, tab5, tab6= st.tabs(["Carbon Credits", "Ozone Depletion", "Implementation", "Effects IRL", "Government Protocols", "Understand the ML"])
with st.sidebar:
    st.title("To learn more and help the cause")
    st.link_button("Donate to the Environmental \n Defense Fund", "https://www.edf.org/")
    st.link_button("Read about how you can reduce your own \n carbon footprint ", "https://sustainability.georgetown.edu/community-engagement/things-you-can-do/")
    st.link_button("Watch this video to learn \n more about carbon credits", "https://www.youtube.com/watch?v=bYb7YLsXvzg")
# the stuff above this comment should not be touched since it serves as the backbone to the functions of the website
with tab1:
    st.title("Carbon Credits: A new way to combat climate change")
    st.divider()
    st.subheader("What are carbon credits?")
    st.markdown(
    """
    - Carbon credits are a new perspective on the methods we use to reduce greenhouse gas emmisions
    - Today, many countries, like: Canada, China, Japan, New Zealand, South Korea, Switzerland and the United States use this to effectively combat the effects of climate change 
    - While they have been controversial at times, they are generally seen as an effective tool for reducing carbon emissions and encouraging the adoption of cleaner, more sustainable forms of energy
    """
)
    st.subheader("This is how carbon credits are employed considering C02 emmisions ppm")

    chart_data = pd.DataFrame(
   {"col1": list(range(20)), "col2": np.random.randn(20), "col3": np.random.randn(20)}
    )

    st.bar_chart(
    chart_data, x="col1", y=["col2", "col3"], color=["#FF0000", "#0000FF"]
    )
    st.divider()
    st.subheader("Emmisions have changed exponentially over the past 4 decades")
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Average Sufrace Temperature", value = "70 °F", delta = "12% increase from 1980")
    col2.metric(label="Sea Level", value = "10 cm", delta = "3cm increase from 1980")
    col3.metric(label="Use of Fossil Fuels", value = "178 billion gallons", delta = "7.8% increase from 1980 ")
    st.divider()
    page_bg_img = '''
    <style>
    .stApp {
    background-image: URL("https://images.rawpixel.com/image_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvdjEwMTYtYy0wOF8xLWtzaDZtemEzLmpwZw.jpg");
    background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

with tab2:
    st.title("Into the Stratosphere: Exploring Ozone Depletion and Atmospheric Dynamics")
    st.divider()
    st.subheader("What is stratopheric ozone?")
    st.markdown("""
                - The atmosphere is divided into several layers; The two we will discuss here are: **the Troposphere, and the Stratosphere**
                - Tropospheric ozone is primarily caused by car exhaust emissions during traffic, which produce nitrogen oxides. **The development of tropospheric ozone is hazardous to humans** 
                - Stratospheric ozone is naturally produced when solar radiation breaks down oxygen molecules in the atmosphere. **Stratospheric ozone protects us from UV radiation, and makes the Earth habitable** 
                """                

)


with tab3:
    st.title("The way we understand carbon credits has changed over the years")
    st.subheader("Carbon sequestration (per unit time by an average healthy tree) is not bound by a single formula, hence we"
                 "have to follow various steps to find this value")
    st.divider()
    st.caption("First, we have to calculate the below-ground-biomass, or 'BGB', "
                 "using the above-ground biomass, or 'AGB', to find"
                 "the total biomass, or 'TB'")
    st.latex(r'''
    BGB = 0.2 * AGB      
    ''')
    st.latex(r'''
    TB = AGB + BGB = AGB + 0.2*AGB = 1.2 * AGB    
    ''')
    st.image('https://carbonneutral.com.au/wp-content/uploads/2022/04/sequestration-age-graph-1024x939.png')
    st.divider()
    

with tab4:
    st.title("Some real examples behind Ozone Depletion")
    st.subheader("This table shows the rate of ozone depletion by sector in San Francisco")
    st.caption("The highlighted values demonstrate the areas of highest stratospheric ozone effect")
    
    df = pd.DataFrame(np.random.randn(10, 20), columns=("Sector %d" % i for i in range(20)))
    st.dataframe(df.style.highlight_max(axis=0))
    st.divider()
    st.subheader("This is the map representation of the data")
    df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])
    
    st.map(df)

    st.divider()
    st.subheader("Ozone depletion in the Antarctic stratosphere over the past 3 years")
    st.image('https://img.theweek.in/content/dam/week/news/2022/images/2022/12/21/Earth-ozone-hole-each-year-in-1979-(L)-and-in-2009.jpg')
    expander = st.expander("See what this means")
    expander.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')
    expander.image("https://static.streamlit.io/examples/dice.jpg")
    


with tab5:
    st.title("Hola!")
    

with tab6:
    st.title("Understand how AI sees the world around us")
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
        pred = res[0].probs.top1
        st.write(res[0].names[pred])

