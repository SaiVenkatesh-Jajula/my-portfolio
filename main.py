import streamlit as st

# st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image('images/myphoto.jpg', width=250)
with col2:
    st.markdown("<br><br><br>",unsafe_allow_html=True) #linespacing
    st.title("Venkatesh Jajula")
    desc="""
    I am a python developer as well as Azure cloud administrator.
    Also have server level administration experience. Currently looking for work in the role of Python Developer!...
    """
    st.info(desc)
