import streamlit as st
import csv
import pandas
#pandas was installed along with streamlit
# st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image('images/myphoto.jpg', width=250)
with col2:
    st.markdown("<br>",unsafe_allow_html=True) #linespacing
    st.title("Venkatesh Jajula")
    desc="""
    Hey! I am venkatesh_jajula from India. I graduated in 2022 in computer science from JNTU Kakinada.
    Basically I am a Python Developer as well as Azure Cloud Administrator.
    Also have server level administration experience. Currently looking for work in the role of Python Developer!...
    """
    st.info(desc)

content="""
Below you can find some of the apps I have built in python. Feel free to contact me!
"""
st.write(content)

#COMPONENTS FETCHING
# with open("data.csv",'r') as file:
#     data=list(csv.reader(file))
#
# for i in range(1,len(data),2):
#     tempcol1, tempcol2 = st.columns(2)
#     try:
#         with tempcol1:
#             title1=data[i][0]
#             description1=data[i][1]
#             currentimg1=data[i][3]
#             url1=data[i][2]
#             st.title(title1)
#             st.write(description1)
#             st.image(f"images/{currentimg1}",width=350)
#             st.write(f"<a href={url1}>Source Code</a>",unsafe_allow_html=True)
#         with tempcol2:
#             title2=data[i+1][0]
#             description2 = data[i+1][1]
#             currentimg2=data[i+1][3]
#             url2 = data[i][2]
#             st.title(title2)
#             st.write(description2)
#             st.image(f"images/{currentimg2}",width=350)
#             st.write(f"<a href={url2}>Source Code</a>", unsafe_allow_html=True)
#     except IndexError:
#         pass

#WORK AS SMART ASS- INSTEAD OF NORMAL CODE USING PANDAS
df = pandas.read_csv("data.csv", sep=',')
col3,empty, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, content in df[:10].iterrows():
        st.header(content["title"])
        st.write(content["description"])
        st.image("images/"+content['image'], width=350)
        st.write(f"[Source Code]({content['url']})")

with col4:
    for index, content in df[10:].iterrows():
        st.header(content["title"])
        st.write(content["description"])
        st.image("images/"+content['image'], width=350)
        st.write(f"[Source Code]({content['url']})")


