
import streamlit as st
import pandas as pd 
import numpy as np
from ultralytics import YOLO
from PIL import Image
import pydeck as pdk
import time


st.set_page_config(layout="wide")
tab1, tab2, tab3, tab4, tab5= st.tabs(["Ozone Depletion", "Carbon Credits", "Implementation", "Effects IRL", "Understand the ML"])
with st.sidebar:
    st.title("To learn more and help the cause")
    st.link_button("Donate to the Environmental \n Defense Fund", "https://www.edf.org/")
    st.link_button("Read about how you can reduce your own \n carbon footprint ", "https://sustainability.georgetown.edu/community-engagement/things-you-can-do/")
    st.link_button("Watch this video to learn \n more about carbon credits", "https://www.youtube.com/watch?v=bYb7YLsXvzg")
# the stuff above this comment should not be touched since it serves as the backbone to the functions of the website

with tab1:
    st.title("Into the Stratosphere: Exploring Ozone Depletion and Atmospheric Dynamics")
    st.divider()
    st.subheader("What is stratopheric ozone?")
    st.markdown("""
                - The atmosphere is divided into several layers; The two we will discuss here are: **the Troposphere, and the Stratosphere**
                - Tropospheric ozone is primarily caused by car exhaust emissions during traffic, which produce nitrogen oxides. **The development of tropospheric ozone is hazardous to humans** 
                - Stratospheric ozone is naturally produced when solar radiation breaks down oxygen molecules in the atmosphere. **Stratospheric ozone protects us from UV radiation and makes the Earth habitable** 
                """                

)
    st.warning("Remember: Ozone itself isn't always harmful to us; It is only harmful when it develops within the troposphere. When it forms in the troposphere, ozone is also referred to as a 'secondary pollutant'", icon ="⚠️")
    st.divider()
    st.image('https://www.frontiersin.org/files/Articles/492681/fimmu-10-02518-HTML/image_m/fimmu-10-02518-g001.jpg')
    
    st.markdown("""
    ***Ozone can be formed in 2 primary ways:*** 
     - Volatile organic compounds react with nitrogen oxides, which form peroxyacetyl nitrates, or PAN's, which act as powerful respiratory and eye irritants and ozone
     - Nitrogen oxides are emitted from car exhaust pipes, which react with oxygen molecules to form ozone
    """)
    
    st.caption("The following are the chemical formulas for these reactions")
    
    st.latex(r'''
    NO + VOC + UV (sunlight) → Ozone (O3) 
    ''')
    
with tab2:
    st.title("Carbon Credits: A new way to combat climate change")
    st.divider()
    st.subheader("What are carbon credits?")
    st.markdown(
    """
    - Carbon credits are a new perspective on the methods we use to reduce greenhouse gas emissions
    - Today, many countries, like ***Canada, China, Japan, New Zealand, South Korea, Switzerland and the United States use this to combat the effects of climate change effectively*** 
    - While they have been controversial at times, they are generally seen as an effective tool for reducing carbon emissions and encouraging the adoption of cleaner, more sustainable forms of energy
    """
)
    st.divider() # metrics tables
    st.subheader("Emissions have changed exponentially over the past 4 decades")
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Average Surface Temperature", value = "70 °F", delta = "12% increase from 1980")
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
    st.divider() # video player for federal incentives for carbon credits
    st.subheader("Let's watch this video to learn more about federal incentives regarding carbon credits")
    VIDEO_URL = "https://www.youtube.com/watch?v=x_wzGPKIBp4"
    st.video(VIDEO_URL)


    
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
    
    st.subheader("These are map representations of the data")
    df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])
    
    st.map(df)
    
    chart_data = pd.DataFrame(
       np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
       columns=['lat', 'lon'])
    
    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
               'HexagonLayer',
               data=chart_data,
               get_position='[lon, lat]',
               radius=200,
               elevation_scale=4,
               elevation_range=[0, 1000],
               pickable=True,
               extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=chart_data,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
    ))
    st.warning('This data is not exact, and shows the typical behaviour of pollution levels in a qualitative, not quantitative manner', icon="⚠️")
    
    st.divider()
    st.subheader("Ozone depletion in the Antarctic stratosphere over the past 3 years")
    st.image('https://img.theweek.in/content/dam/week/news/2022/images/2022/12/21/Earth-ozone-hole-each-year-in-1979-(L)-and-in-2009.jpg')
    expander = st.expander("See what this means")
    expander.write('''
    Despite the Montreal Protocol's success in regulating ozone-depleting chemicals,
    the study raises concerns about the misperception that the ozone issue 
    has been resolved. While the protocol has improved the situation with CFCs,
    the ozone hole has reached record sizes in the past three years, 
    covering over 26 million square kilometres in 2023, nearly twice the area of Antarctica.
    The graph above shows an increase in the rate of ozone depletion in the past few years.
    ''')
    expander.write("On the other hand, various sources, notably NASA and 'The World Economic Forum', contrast this, showing that **the rate of ozone depletion has indeed continued to shrink since the introduction of the Montreal Protocol**")
    expander.write("""Several other protocols have also been put into place to combat climate emissions, notably: **The Kyoto Protocol (and the Doha amendment), the Clean Air Act,
                   and the Clean Water Act**
                   """)
    st.divider()
    
with tab5:
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
        progress_text = "Wait up! The classifier is doing its work"
        my_bar = st.progress(0, text=progress_text)
        
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        my_bar.empty()

        st.button("Want to try again? Click me!")
        x = res[0].names[pred] 
        st.write("Your image is classified as a ***{}***".format(res[0].names[pred]))

    st.subheader("This is the code for the project")
    st.code("""    
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
            """)
    
    st.warning("This, though a rudimentary model of large-scale image processing, which would use much more training data and computation power, displays how humans can use ML and satellite imaging to help improve our monitoring over areas rapdily changing due to global warming")
