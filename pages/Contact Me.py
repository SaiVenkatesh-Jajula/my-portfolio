import streamlit as st
import mailing
#github deployed failed may be for pages folder name starts with lowercase

st.title("Contact Me")

with st.form(key='contactform'):
    mailid = st.text_input("Enter your Email address:",key='mailid')
    usermsg=st.text_area("Message:",key="message")
    message=f"""\
Subject: Mail from {mailid}

Message From: {mailid}
{usermsg}
    """
    submit=st.form_submit_button("Submit")
    if submit:
        mailing.mailing(message)
        st.info("Sent Successfully")