import streamlit as st
from streamlit_authenticator.utilities.hasher import Hasher

# logon form
with st.form(key="logon_form"):
    email = st.text_input("Email Address:")
    password = st.text_input("Password:")
    
    hashed_password = Hasher.hash(password)

    if st.form_submit_button("Login"):
        st.text(f'Email: {email}')
        st.text(f'Password: {hashed_password}')