
import streamlit as st
import pandas as pd 
import numpy as np



st.set_page_config(layout="wide")
tab1, tab2, tab3, tab4 = st.tabs(["Introduction", "Implementation", "Pros VS Cons", "The ML"])
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


with tab2:
    st.title("The way we understand carbon credits has changed over the years")
    st.subheader("Carbon sequestration (per unit time by a average healthy tree) is not bound by a single formula, hence we"
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
    

with tab3:
    st.title("Global Ozone Depletion")
    st.subheader("This table shows the raze of ozone depletion")
    st.caption("The highlighted values show the pain in my soul")
    df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))


    st.dataframe(df.style.highlight_max(axis=0))

    df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.map(df)

